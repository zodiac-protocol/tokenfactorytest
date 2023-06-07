use cosmwasm_std::{to_vec, from_binary, Empty, Uint128, Coin, Binary, StdResult, StdError, Deps, SystemResult, ContractResult, CosmosMsg};
use cosmwasm_schema::cw_serde;
use cw_asset::Asset;
use crate::osmo_bal_lockup_vault::KeeperTokenAction;
use crate::utils::compose_stargate_query;
use osmosis_std::types::osmosis::gamm::v1beta1 as gamm;
use osmosis_std::types::osmosis::poolmanager::v1beta1 as poolmanager;
use osmosis_std::types::cosmos::base::v1beta1::Coin as ProtoCoin;
use prost::Message as ProstMessage;
use std::str::FromStr;

// TODO: explore borsh serde
#[cw_serde]
pub struct InitOptions {
    pub pool_id: u64,
    pub ptoken_l: Uint128,
    pub flash_loan_address: String,
    pub redeem_fee: u64,
    pub claim_yield_fee: u64,
    pub fee_collector: String,
    pub pool_readable_name: String, //ex: atomosmo
}

#[cw_serde]
pub enum ExecuteMsg {
    //owner functionality
    UpdateConfig {
        owner: Option<String>,
        maturity_timestamp: Option<u64>,
        collateral_token: Option<String>,
        flash_loan_address: Option<String>,
        fee_collector: Option<String>,
        yield_token_hook_contract: Option<String>,
    },
    ToggleFlashLoanFeature{},
    OwnerAction{
      msgs: Vec<CosmosMsg>,
    },

    //core user-facing functionality
    ClaimYield {},
    Combine {
        amount: Uint128,
    },
    DepositCollateral{},
    RedeemPrincipal{
        amount: Uint128,
    },

    /// functionality for white-listed intermediary contracts
    //borrow capability for yield vaults (initally osmo lockup vaults)
    CreateYieldVault{
        code_id: u64,
        maturity_timestamp: u64,
        vault_keeper_logic: Vec<KeeperTokenAction>,
        init_options: Binary,
    },
    Borrow{
        yield_tokens_locked: Uint128, // child vault will lock yield tokens, and then request to custody underlying LP tokens
    },
    Repay{
        yield_tokens_unlocked: Uint128,
    }, 

    //flash loan capability for flash loan contract
    FlashLoan{
        loan_asset: Asset,
    },
    PostFlashLoan{},
}

#[cw_serde]
pub enum QueryMsg {
    Config {},
    State {},
    Holder { address: String },
    YieldVaults {},

    //yield tokens not staked in a child yield vault are eligible for zodiac incentives
    YieldTokensEarningIncentives{},
}

#[cw_serde]
pub enum SudoMsg {
    BlockBeforeSend{
        to: String,
        from: String,
        amount: Coin,
    },
    TrackBeforeSend{
        to: String,
        from: String,
        amount: Coin,
    },
}

#[cw_serde]
pub struct ConfigResponse {
    pub owner: String,
    pub collateral_token: String,
    pub maturity_timestamp: u64,
    pub principal_token: String,
    pub yield_token: String,
    pub pool_id: u64,
    pub ptoken_l: Uint128,
    pub flash_loan_address: String,
    pub fee_collector: String,

    pub redeem_fee: u64,
    pub claim_yield_fee: u64,

    pub display_name: String,
    pub yield_token_hook_contract: String,
}

#[cw_serde]
pub struct MigrateMsg {
}

#[cw_serde]
pub struct RedeemResponse {
    pub amount: Uint128,
}

#[cw_serde]
pub struct DepositCollateralResponse {
    pub mint_amount: Uint128,
}

#[cw_serde]
pub struct BorrowResponse {
    pub borrowed_lp: Coin,
}

pub fn query_pool_state(
    deps: &Deps, 
    gamm_pool_id: u64,
    a_token_denom: Option<&String>, 
  ) -> StdResult<(Uint128, Uint128, ProtoCoin, gamm::Pool)>{

    let pool_query = compose_stargate_query::<Empty>(
      &poolmanager::PoolRequest{
          pool_id: gamm_pool_id
      },
      String::from("/osmosis.poolmanager.v1beta1.Query/Pool"),
    )?;

    let raw = to_vec(&pool_query).map_err(|serialize_err| StdError::generic_err(format!("Serializing QueryRequest: {}", serialize_err)))?;

    let pool_query_resp: StdResult<Binary> = match deps.querier.raw_query(&raw) {
        SystemResult::Err(system_err) => Err(StdError::generic_err(format!(
            "Querier system error: {}",
            system_err
        ))),
        SystemResult::Ok(ContractResult::Err(contract_err)) => Err(StdError::generic_err(format!(
            "Querier contract error: {}",
            contract_err
        ))),
        SystemResult::Ok(ContractResult::Ok(value)) => Ok(value),
    };

    let pool_query_resp: Binary = pool_query_resp.map_err(|err| StdError::generic_err(format!("{:?}", err)))?;
    let pool_query_resp: poolmanager::PoolResponse = from_binary::<poolmanager::PoolResponse>(&pool_query_resp)?;

    if let Some(pool_state) = pool_query_resp.pool{
  
      //decode the binary value field of the Any-type pool field of the response
      let pool_state: gamm::Pool = ProstMessage::decode(pool_state.value.as_slice()).map_err(|_| StdError::parse_err("gamm::Pool", "Unable to decode"))?;
  
      //quality-of-life logic to designate which asset is the pt/lp denom
      let token_a: ProtoCoin = pool_state.pool_assets[0].token.clone().ok_or_else(||StdError::generic_err("Pool is somehow missing a Coin constituent"))?;
  
      let token_b: ProtoCoin = pool_state.pool_assets[1].token.clone().ok_or_else(||StdError::generic_err("Pool is somehow missing a Coin constituent"))?;
  
      let (a_token_amount, b_token_amount): (Uint128, Uint128) = if a_token_denom.is_none() || Some(&token_a.denom) == a_token_denom {
        (Uint128::from_str(&token_a.amount)?, Uint128::from_str(&token_b.amount)?)
      } else {
        (Uint128::from_str(&token_b.amount)?, Uint128::from_str(&token_a.amount)?)
      };
  
      //more quality-of-life logic to unwrap fields that should never be none
      let shares: ProtoCoin = pool_state.total_shares.clone().ok_or_else(||StdError::generic_err("Pool is somehow missing the total_share field"))?;
  
      Ok((a_token_amount, b_token_amount, shares, pool_state))
    } else {
      Err(StdError::generic_err("Pool information is missing for this pool_id"))
    }
  
  
  }



  #[cfg(test)]
  mod tests {
      use super::*;
      use osmosis_std::shim::Any;
      use testing::mocks as zodiac_mock_shit;
  
      #[test]
      fn test_query_pool_state() {
        let mut mock_deps = zodiac_mock_shit::mock_dependencies(&vec![]);
        mock_deps.querier.set_query_pool_response(69u64, None);
        let mock_pool: Any = mock_deps.querier.osmosis_querier.pools.clone().get(&69u64).unwrap().pool.clone().unwrap();
        let mock_pool: gamm::Pool = ProstMessage::decode(mock_pool.value.clone().as_slice()).unwrap();

        let (token_a_amount, token_b_amount, shares, pool) = query_pool_state(&mock_deps.as_ref(), 69u64, None).unwrap();

        assert_eq!(token_a_amount, Uint128::from(143000000u32));
        assert_eq!(token_b_amount, Uint128::from(143000000u32));
        assert_eq!(shares, ProtoCoin{
          denom: "gamm/69".to_string(),
          amount: "14299999999999999993135".to_string(),
        });

        assert_eq!(pool, mock_pool);
      }

}
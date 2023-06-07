use cosmwasm_std::{Coin, CosmosMsg};
use cosmwasm_schema::cw_serde;

#[cw_serde]
pub struct InstantiateMsg {
    pub owner: String,
    pub token_actions: Vec<KeeperTokenAction>,
}

#[cw_serde]
pub enum ExecuteMsg {
    UpdateConfig{
        owner: Option<String>,
    },
    UpsertTokenAction{
        token_action: KeeperTokenAction,
    },
    RemoveTokenAction{
        denom: String,
    },

    //token actions
    SwapDenoms{
        denom_in: String, 
        denom_out: String, 
        pool_id: u64,
        max_price_impact_bps: u64,
    }, // perform GAMM swap with all available denom_in tokens

    WithdrawLP{
        pool_id: u64,
        denom: String,
        token_out_mins: Vec<Coin>,
    }, // withdraw liquidity; note LP tokens will be a popular fee denom 

    SwapToPool{
        denom_in: String,
        pool_id: u64,
        max_price_impact_bps: u64,
    }, // 

    Execute{
        msg: CosmosMsg,
    }, //call anything

    Keep{},
}

#[cw_serde]
pub enum QueryMsg {
    Config{},
}

#[cw_serde]
pub struct ConfigResponse {
    pub owner: String,
    pub token_actions: Vec<KeeperTokenAction>,
}

#[cw_serde]
pub struct KeeperTokenAction {
    pub denom: String,
    pub order: u8,
    pub actions: Vec<ExecuteMsg>,
}

use cosmwasm_schema::cw_serde;
use cosmwasm_std::{Coin, Uint128, Binary};
use schemars::JsonSchema;
use serde::{Deserialize, Serialize};

#[cw_serde]
pub struct InstantiateMsg {
}

#[cw_serde]
pub enum ExecuteMsg {

    MintTo{
        address: String,
        amount: Uint128,
    },

    BurnFrom{
        address: String,
        amount: Uint128,
    },

    Mint{
        amount: Uint128,
    },
    Burn{
        amount: Uint128,
    },
    Stake{
    },
    Unstake{
        amount: Uint128,
    },
}

#[cw_serde]
pub enum QueryMsg {
    HookActivationHistory{},
    Denom{},
    StargateQuery{
        path: String,
        msg: Binary, //should be protobuf bytes
    },
    ModuleAccounts{},
}

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, Eq, JsonSchema)]
#[serde(rename_all = "snake_case")]
pub enum SudoMsg {
    BlockBeforeSend{
      from: String,
      to: String,
      amount: Coin,
    },
    TrackBeforeSend{
      from: String,
      to: String,
      amount: Coin,
    },
    
}


#[cw_serde]
pub struct MigrateMsg {
}
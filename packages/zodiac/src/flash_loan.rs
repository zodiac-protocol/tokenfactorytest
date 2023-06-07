use cosmwasm_std::{Binary, CosmosMsg};
use cw_asset::Asset;
use cosmwasm_schema::cw_serde;

#[cw_serde]
pub struct InstantiateMsg {
    pub owner: String,
    pub fee_collector: String, 
    pub fee: u64, //in bps
}

#[cw_serde]
pub enum ExecuteMsg {
    UpdateConfig{
        owner: Option<String>,
        fee_collector: Option<String>,
        fee: Option<u64>,
    },

    FlashLoan{ 
        vault_address: String,
        loan_asset: Asset, 
        callback: Binary
    },

    FlashLoanV{
        vault_address: String,
        loan_asset: Asset,
        callbacks: Vec<CosmosMsg>,
    },
}

#[cw_serde]
pub enum QueryMsg {
    Config{},
    State{},
    PreLoanSnapshot{},
}

#[cw_serde]
pub struct ConfigResponse {
    pub owner: String,
    pub fee_collector: String,
    pub fee: u64,
}

#[cw_serde]
pub struct StateResponse {
    pub flash_loan_in_flight: bool,
}

#[cw_serde]
pub struct PreLoanSnapshotResponse {
    pub borrower_address: String,
    pub loan_asset: Asset,
    pub vault_address: String,
}

#[cw_serde]
pub struct MigrateMsg {
}
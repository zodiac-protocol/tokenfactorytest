use cosmwasm_schema::cw_serde;
use cosmwasm_std::Uint128;

#[cw_serde]
pub struct InstantiateMsg {
    pub owner: String,
    pub flash_loan_address: String,
}

#[cw_serde]
pub enum ExecuteMsg {
    UpdateConfig{
        owner: Option<String>,
    },

    ToYLPFlashLoanLogic{
        swapper_address: String,
        loan_amount: Uint128,
    },

    ToPLPFlashLoanLogic{
        swapper_address: String,
        loan_amount: Uint128,
    },

    ToYLP{
        vault_address: String,
        pool_id: u64,
        token_out_lower_bound: Option<Uint128>,
    },
    ToPLP{
        vault_address: String,
        pool_id: u64,
        token_out_lower_bound: Option<Uint128>,
    },
}

#[cw_serde]
pub enum QueryMsg {
    Config{},
}

#[cw_serde]
pub struct MigrateMsg {
}
use cosmwasm_std::Uint128;
use cosmwasm_schema::cw_serde;

#[cw_serde]
pub enum ExecuteMsg {
    //hooks
    IncreaseBalanceYt{
        sender: String,
        amount: Uint128,
    },
    DecreaseBalanceYt{
        sender: String,
        amount: Uint128,
    },

}

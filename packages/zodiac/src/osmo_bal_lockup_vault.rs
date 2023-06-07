use cosmwasm_std::{Binary, Uint128};
use cosmwasm_schema::cw_serde;
use crate::osmo_bal_vault::ConfigResponse as VaultConfigResponse;

#[cw_serde]
pub struct InitOptions {
    pub lockup_duration: u64, //in seconds
    pub unlock_time_buffer: u64, //in seconds
    pub closing_penalty_bps: u64, //if yt holder does not withdraw assets before maturity, others may permissionlessly close their accounts
    pub min_yt_deposit: Uint128,
}

#[cw_serde]
pub struct InstantiateMsg {
    pub owner: String,
    pub child_vault_maturity_timestamp: u64,
    pub keep_cooldown_seconds: u64,
    pub token_actions: Vec<KeeperTokenAction>, //the yield vault has sovereignty of its strat
    pub init_options: Binary,
}

#[cw_serde]
#[allow(clippy::large_enum_variant)]
pub enum ExecuteMsg {
    // owner only
    UpdateConfig {
        owner: Option<String>,
        parent_vault_config: Option<VaultConfigResponse>,
        maturity_timestamp: Option<u64>,
    },
    UpsertTokenAction {token_action: KeeperTokenAction},

    // yt holders 
    Deposit{}, //deposit ytoken, request collateral borrow from vault, and lockup for config'd duration
    Unlock{
        yt_amount: Uint128,
    }, //request unlock, collateral repaid to vault
    Withdraw{}, //withdraw yt and repay unlocked collateral to zodiac vault
    ClaimYield {}, // extract yield in terms of target_denom; two sources, incent farming and natural collateral swap fees

    // keeper/croncat
    SwapDenoms{
        denom_in: String, 
        denom_out: String, 
        pool_id: u64
    }, // perform GAMM swap with all available denom_in tokens
    SwapToPool{
        denom_in: String,
        pool_id: u64,
    }, //convert all available denom_in tokens into LP share tokens

    Keep{}, //fetch rewards from collateral vault, swap to target_denom

    CloseVaultStageOne{}, //unlock everything; shut off Deposit{}, Unlock{}; store how much LP is getting unlocked

    CloseVaultStageTwo{}, //send pt-designated portion of collateral back to zodiac vault
    //fetch amount of LP getting unlocked from stage one, and create a final yield payment

    //TODO: a "liquidate" type message likely needed to forcibly call Withdraw{} on behalf of holder; must ensure parent vault's borrowed LP is returned 
    //  actually, does the math work if we just decrement the global index?
    CloseHolder{
        address: String,
    },
}

#[cw_serde]
pub enum QueryMsg {
    Config {},
    State {},
    Holder { address: String },
    Holders {start_after: Option<String>, limit: Option<u32>},
}

#[cw_serde]
pub struct ConfigResponse {
    pub owner: String,
    pub parent_vault_address: String,
    pub parent_vault_config: VaultConfigResponse,
    pub token_actions: Vec<KeeperTokenAction>,
    pub maturity_timestamp: u64,
    pub lockup_duration: u64,
    pub keep_cooldown_seconds: u64,
    pub unlock_time_buffer: u64,
    pub closing_penalty_bps: u64,
    pub min_yt_deposit: Uint128,
}

#[cw_serde]
pub struct KeeperTokenAction {
    pub denom: String,
    pub order: u8,
    pub actions: Vec<ExecuteMsg>,
}

#[cw_serde]
pub struct MigrateMsg {
}
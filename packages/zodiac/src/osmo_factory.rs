use cosmwasm_std::Binary;
use cosmwasm_schema::cw_serde;

#[cw_serde]
pub struct InstantiateMsg {
    pub vault_types: Vec<String>,
}

#[cw_serde]
pub struct VaultInstantiateMsg {
    pub collateral_token: String,
    pub vault_name: String,
    pub maturity_timestamp: u64,
    pub owner: String,
    pub options: Option<Binary>,
}

#[cw_serde]
pub enum ExecuteMsg {
    UpdateConfig {
        owner: Option<String>,
        vault_types: Option<Vec<String>>,
    },
    UpdateVaultConfig {
        config: VaultConfig,
    },
    CreateVault {
        vault_type: String,
        collateral_token: String,
        maturity_month: u64,
        maturity_year: i64,
        options: Option<Binary>,
        name: Option<String>,
        owner: String,
    },
}

#[cw_serde]
pub enum QueryMsg {
    Config {},
    Vaults {
        start_after: Option<VaultInfo>,
        limit: Option<u32>,
    },
}

#[cw_serde]
pub struct ConfigResponse {
    pub owner: String,
    pub vault_types: Vec<String>,
}

#[cw_serde]
pub struct VaultConfig {
    pub code_id: u64,
    pub vault_type: String,
}

#[cw_serde]
pub struct VaultsResponse {
    pub vaults: Vec<VaultFullInfo>,
}

#[cw_serde]
pub struct VaultInfo {
    pub collateral_token: String,
    pub vault_type: String,
    pub maturity_month: u64,
    pub maturity_year: i64,
}

#[cw_serde]
pub struct VaultFullInfo {
    pub vault_address: String,
    pub principal_token: String,
    pub yield_token: String,
    pub maturity_month: u64,
    pub maturity_year: i64,
    pub collateral_token: String,
    pub vault_type: String,
    pub display_name: String,
}

#[cw_serde]
pub struct MigrateMsg {
}
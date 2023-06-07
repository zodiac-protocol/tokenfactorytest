use schemars::JsonSchema;
use serde::{Deserialize, Serialize};
use cw_storage_plus::Item;

pub const HISTORY: Item<Vec<HistoryItem>> = Item::new("\u{0}\u{7}history");
pub const DENOM: Item<String> = Item::new("denom");

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, Eq, JsonSchema)]
#[serde(rename_all = "snake_case")]
pub struct HistoryItem{
    pub block: u64,
    pub hook_msg: String,
}

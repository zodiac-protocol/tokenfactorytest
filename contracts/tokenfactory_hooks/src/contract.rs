#[cfg(not(feature = "library"))]
use cosmwasm_std::entry_point;
use cosmwasm_std::{
    to_binary, Binary, CosmosMsg, Deps, DepsMut, Env,
    MessageInfo, Reply, Response, StdError, StdResult, SubMsg, Uint128,
    WasmMsg, Decimal256, Uint256, Coin, Event, QueryRequest, SystemResult,
    ContractResult, Empty, to_vec
};

use zodiac::utils::{compose_stargate_msg, parse_reply_data};
use zodiac::tokenfactory_hooks::{InstantiateMsg, ExecuteMsg, QueryMsg, SudoMsg, MigrateMsg};
use osmosis_std::types::osmosis::tokenfactory::v1beta1::{MsgCreateDenom, MsgCreateDenomResponse, MsgMint, MsgBurn, MsgSetBeforeSendHook,};
use osmosis_std::types::cosmos::base::v1beta1::Coin as ProtoCoin;
use osmosis_std::types::cosmos::auth::v1beta1::{QueryModuleAccountsRequest, QueryModuleAccountsResponse};
use prost::Message as ProstMessage;

use crate::state::{HISTORY, HistoryItem, DENOM};

#[entry_point]
pub fn migrate(_deps: DepsMut, _env: Env, _msg: MigrateMsg) -> StdResult<Response> {
    // No state migrations performed, just returned a Response
    Ok(Response::default())
}


#[cfg_attr(not(feature = "library"), entry_point)]
pub fn instantiate(
    deps: DepsMut,
    env: Env,
    _info: MessageInfo,
    _msg: InstantiateMsg,
) -> StdResult<Response> {

    HISTORY.save(deps.storage, &vec![])?;

    let create_msg: CosmosMsg = compose_stargate_msg(
        &MsgCreateDenom{
            sender: env.contract.address.to_string(),
            subdenom: String::from("test"),
        },
        String::from("/osmosis.tokenfactory.v1beta1.MsgCreateDenom"),
    )?;

    let create_msg: SubMsg = SubMsg::reply_on_success(create_msg, 1u64);

    Ok(Response::new().add_submessage(create_msg))
}

#[entry_point]
pub fn reply(deps: DepsMut, env: Env, reply: Reply) -> StdResult<Response> {

    let data = parse_reply_data(reply)?;
    let response: MsgCreateDenomResponse = ProstMessage::decode(data.as_slice()).map_err(|_| StdError::parse_err("MsgCreateDenomResponse", "failed to parse data"))?;

    DENOM.save(deps.storage, &response.new_token_denom)?;

    let register_hook_msg: CosmosMsg = compose_stargate_msg(
        &MsgSetBeforeSendHook{
            sender: env.contract.address.to_string(),
            denom: response.new_token_denom,
            cosmwasm_address: env.contract.address.to_string(),
        },
        String::from("/osmosis.tokenfactory.v1beta1.MsgSetBeforeSendHook"),
    )?;

    Ok(Response::new().add_message(register_hook_msg))
}

#[cfg_attr(not(feature = "library"), entry_point)]
pub fn execute(deps: DepsMut, env: Env, _info: MessageInfo, msg: ExecuteMsg) -> StdResult<Response> {
    match msg {
        ExecuteMsg::MintTo {
            address,
            amount,
        } => {
            let mint_msg: CosmosMsg = compose_stargate_msg(
                &MsgMint{
                    sender: env.contract.address.to_string(),
                    amount: Some(ProtoCoin{
                        denom: DENOM.load(deps.storage)?,
                        amount: amount.into(),
                    }),
                    mint_to_address: address.to_string(),
                },
                String::from("/osmosis.tokenfactory.v1beta1.MsgMint"),
            )?;

            Ok(Response::new().add_message(mint_msg))
        },

        ExecuteMsg::BurnFrom{
            address,
            amount
        } => {
            let burn_msg: CosmosMsg = compose_stargate_msg(
                &MsgBurn{
                    sender: env.contract.address.to_string(),
                    amount: Some(ProtoCoin{
                        denom: DENOM.load(deps.storage)?,
                        amount: amount.into(),
                    }),
                    burn_from_address: address.to_string(),
                },
                String::from("/osmosis.tokenfactory.v1beta1.MsgBurn"),
            )?;

            Ok(Response::new().add_message(burn_msg))
        },

        ExecuteMsg::Mint{
            amount
        } => {
            let mint_msg: CosmosMsg = compose_stargate_msg(
                &MsgMint{
                    sender: env.contract.address.to_string(),
                    amount: Some(ProtoCoin{
                        denom: DENOM.load(deps.storage)?,
                        amount: amount.into(),
                    }),
                    mint_to_address: String::from(""),
                },
                String::from("/osmosis.tokenfactory.v1beta1.MsgMint"),
            )?;

            Ok(Response::new().add_message(mint_msg))
        },

        ExecuteMsg::Burn{
            amount
        } => {
            let burn_msg: CosmosMsg = compose_stargate_msg(
                &MsgBurn{
                    sender: env.contract.address.to_string(),
                    amount: Some(ProtoCoin{
                        denom: DENOM.load(deps.storage)?,
                        amount: amount.into(),
                    }),
                    burn_from_address: String::from(""),
                },
                String::from("/osmosis.tokenfactory.v1beta1.MsgBurn"),
            )?;

            Ok(Response::new().add_message(burn_msg))
        },
    }
}


#[entry_point]
pub fn sudo(deps: DepsMut, env: Env, msg: SudoMsg) ->  StdResult<Response> {

    match &msg{
        SudoMsg::BlockBeforeSend { from, to, amount} => {
            let mut history: Vec<HistoryItem> = HISTORY.load(deps.storage)?;
            history.push(HistoryItem{
                block: env.block.height,
                hook_msg: format!("{:?}", msg.clone()),
            });
            HISTORY.save(deps.storage, &history)?;
            Ok(Response::new().add_attributes(vec![
                ("hook", "block"),
                ("from", from),
                ("to", to),
                ("amount", &amount.to_string())
            ]))
        },
        SudoMsg::TrackBeforeSend { from, to, amount} => {
            let mut history: Vec<HistoryItem> = HISTORY.load(deps.storage)?;
            history.push(HistoryItem{
                block: env.block.height,
                hook_msg: format!("{:?}", msg.clone()),
            });
            HISTORY.save(deps.storage, &history)?;
            Ok(Response::new().add_attributes(vec![
                ("hook", "track"),
                ("from", from),
                ("to", to),
                ("amount", &amount.to_string())
            ]))
        }
    }
}

#[cfg_attr(not(feature = "library"), entry_point)]
pub fn query(deps: Deps, _env: Env, msg: QueryMsg) -> StdResult<Binary> {
    match msg {
        QueryMsg::HookActivationHistory {} => Ok(to_binary(&HISTORY.load(deps.storage)?)?),
        QueryMsg::Denom {} => Ok(to_binary(&DENOM.load(deps.storage)?)?),
        QueryMsg::StargateQuery{ path, msg } => {

            let qr = QueryRequest::<Empty>::Stargate{
                path: path,
                data: msg.into(),
            };

            let raw = to_vec(&qr).map_err(|serialize_err| StdError::generic_err(format!("Serializing QueryRequest: {}", serialize_err)))?;

            let resp: StdResult<Binary> = match deps.querier.raw_query(&raw) {
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
        
            resp
        },
        QueryMsg::ModuleAccounts{ } => {
            let resp = perform_stargate_query::<Empty>(
                &deps,
                &QueryModuleAccountsRequest{
                },
                String::from("/cosmos.auth.v1beta1.Query/ModuleAccounts")
            );

            resp

        }
    }
}

use prost::Message;
use serde::{Deserialize, Serialize};

#[allow(clippy::redundant_field_names)]
pub fn compose_stargate_query<C>(msg: &impl Message, path: String) -> StdResult<QueryRequest<C>>{
    let mut msg_bytes: Vec<u8> = vec![];
    Message::encode(msg, &mut msg_bytes).map_err(|_| StdError::generic_err("Cannot encode proto to bytes"))?;

    Ok(QueryRequest::<C>::Stargate{
        path: path,
        data: msg_bytes.into(),
    })
}

pub fn perform_stargate_query<C>(deps: &Deps, msg: &impl Message, path: String) -> StdResult<Binary> 
where 
    C: Serialize
{
    let query = compose_stargate_query::<C>(msg, path)?;
    let raw = to_vec(&query).map_err(|serialize_err| StdError::generic_err(format!("Serializing QueryRequest: {}", serialize_err)))?;

    let resp: StdResult<Binary> = match deps.querier.raw_query(&raw) {
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

    resp
}
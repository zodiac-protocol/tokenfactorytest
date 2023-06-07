use cosmwasm_std::{StdError, StdResult, Uint128, CosmosMsg, Reply, Binary, Coin, QueryRequest, SubMsgResult, SystemResult, ContractResult, to_vec, Deps, BankMsg, Addr, coins};
use prost::Message;
use serde::Serialize;

#[allow(clippy::redundant_field_names)]
pub fn compose_stargate_msg(msg: &impl Message, type_url: String) -> StdResult<CosmosMsg>{
    let mut msg_bytes: Vec<u8> = vec![];
    Message::encode(msg, &mut msg_bytes).map_err(|_| StdError::generic_err("Cannot encode proto to bytes"))?;

    Ok(CosmosMsg::Stargate{
        type_url: type_url,
        value: msg_bytes.into(),
    })
}

#[allow(clippy::redundant_field_names)]
pub fn compose_stargate_query<C>(msg: &impl Message, path: String) -> StdResult<QueryRequest<C>>{
    let mut msg_bytes: Vec<u8> = vec![];
    Message::encode(msg, &mut msg_bytes).map_err(|_| StdError::generic_err("Cannot encode proto to bytes"))?;

    Ok(QueryRequest::<C>::Stargate{
        path: path,
        data: msg_bytes.into(),
    })
}

/**

Errors if a reply's data is missing.

**/
pub fn parse_reply_data(reply: Reply) -> StdResult<Binary> {
    match reply.result {
        SubMsgResult::Ok(resp) => {
            match resp.data{
                Some(bin) => {
                    Ok(bin)
                },
                None => {
                    Err(StdError::generic_err("The submsg's reply is missing required data"))
                }
            }
        },  
        SubMsgResult::Err(err) => {
            Err(StdError::generic_err(format!("{:?}", err)))
        }
    }
}

pub fn extract_target_denom(target_denom: String, funds: &Vec<Coin>, fail_if_multiple_sent: bool) -> StdResult<Coin> {
    if fail_if_multiple_sent && funds.len() != 1{
        return Err(StdError::generic_err(format!("Received {:?}, expected only {:?}", funds.clone(), target_denom)));
    }

    let coin: &Coin = funds
      .iter()
      .find(|x| x.denom == target_denom && x.amount > Uint128::zero())
      .ok_or_else(|| {
          StdError::generic_err(format!("No {} tokens sent", target_denom))
      })?;
  
    Ok(coin.clone())
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

pub fn build_send_asset_msg(recipient_addr: &Addr, denom: &str, amount: Uint128) -> CosmosMsg {
    CosmosMsg::Bank(BankMsg::Send {
        to_address: recipient_addr.into(),
        amount: coins(amount.u128(), denom),
    })
}



#[cfg(test)]
mod tests {
    use super::*;
    use cosmwasm_std::{Empty, Reply, SubMsgResponse, SubMsgResult, to_binary};
    use osmosis_std::types::osmosis::tokenfactory::v1beta1 as tokenfactory;
    use osmosis_std::types::osmosis::poolmanager::v1beta1 as poolmanager;

    //TODO test bounds
    #[test]
    fn test_extract_target_denom() {

        let target_denom: String =  "uosmo".to_string();
        let funds: Vec<Coin> = vec![
            Coin{
                denom: "uosmo".to_string(),
                amount: Uint128::from(69u32),
            },
        ];
        let fail_if_multiple_sent: bool = false;

        let extracted_coins = extract_target_denom(target_denom.clone(), &funds, fail_if_multiple_sent);

        assert_eq!(extracted_coins, Ok(Coin{
            denom: target_denom,
            amount: Uint128::from(69u32)
        }));
    }

    #[test]
    fn test_compose_stargate_msg() {

        let msg = tokenfactory::MsgCreateDenom{
            sender: "zodiac".to_string(),
            subdenom: "factory/zodiac/OSMO-ZDC/2030-10/p".to_string(),
        };
        let type_url: String = String::from("/osmosis.tokenfactory.v1beta1.MsgCreateDenom");

        let stargate_msg = compose_stargate_msg(&msg, type_url.clone());

        let mut msg_bytes: Vec<u8> = vec![];
        Message::encode(&msg, &mut msg_bytes).map_err(|_| StdError::generic_err("Cannot encode proto to bytes")).unwrap();

        assert_eq!(stargate_msg, Ok(CosmosMsg::Stargate{
            type_url: type_url,
            value: msg_bytes.into(),
        }));
    }

    #[test]
    fn test_compose_stargate_query() {

        let msg = poolmanager::PoolRequest{
            pool_id: 69u64,
        };
        let type_url: String = String::from("/osmosis.poolmanager.v1beta1.Query/Pool");

        let stargate_query = compose_stargate_query::<Empty>(&msg, type_url.clone());

        let mut msg_bytes: Vec<u8> = vec![];
        Message::encode(&msg, &mut msg_bytes).map_err(|_| StdError::generic_err("Cannot encode proto to bytes")).unwrap();

        assert_eq!(stargate_query, Ok(QueryRequest::<Empty>::Stargate{
            path: type_url,
            data: msg_bytes.into(),
        }));
    }

    #[test]
    fn test_parse_reply_data() {

        let reply: Reply = Reply{
            id: 69,
            result: SubMsgResult::Ok(SubMsgResponse{
                events: vec![],
                data: Some(to_binary(&Uint128::from(696969u32)).unwrap()),
            }),
        };

        let parsed_reply = parse_reply_data(reply.clone());

        assert_eq!(parsed_reply, Ok(to_binary(&Uint128::from(696969u32)).unwrap()));
    }

    #[test]
    fn test_build_send_asset_msg(){

        let recipient: Addr = Addr::unchecked("recipient");
        let asset = "factory/recipient/523rwer3".to_string();
        let amount: Uint128 = Uint128::from(123455432u32);

        let msg: CosmosMsg = build_send_asset_msg(&recipient, &asset, amount);

        assert_eq!(msg, CosmosMsg::Bank(BankMsg::Send{
            to_address: recipient.to_string(),
            amount: vec![
                Coin{
                    denom: asset,
                    amount: amount,
                }
            ]
        }));
    }
}

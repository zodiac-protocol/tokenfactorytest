################################################
# imports
################################################

from lib2to3.pgen2 import token
from unittest import runner
import pandas as pd
import json
import os
import argparse
from terra_sdk.client.lcd import LCDClient
from terra_sdk.core.wasm import MsgStoreCode, MsgInstantiateContract, MsgExecuteContract
from terra_sdk.core.bank import MsgSend
from terra_sdk.core.fee import Fee
from terra_sdk.key.mnemonic import MnemonicKey
from terra_sdk.core.bech32 import get_bech
from terra_sdk.core import AccAddress, Coin, Coins
from terra_sdk.client.lcd.api.tx import CreateTxOptions, SignerOptions
from terra_sdk.client.localterra import LocalTerra
import base64
import requests
from terra_sdk.core.wasm.data import AccessConfig
from terra_proto.cosmwasm.wasm.v1 import AccessType
import subprocess
from bech32 import bech32_decode, bech32_encode, convertbits
from terra_sdk.client.lcd.api._base import BaseAsyncAPI, sync_bind

from terra_proto.cosmos.tx.v1beta1 import Tx, TxBody, AuthInfo, SignDoc, SignerInfo, ModeInfo, ModeInfoSingle, BroadcastTxResponse
from terra_proto.cosmos.base.abci.v1beta1 import TxResponse
from terra_proto.cosmos.tx.signing.v1beta1 import SignMode
from betterproto.lib.google.protobuf import Any

from ecdsa import SECP256k1, SigningKey
from ecdsa.util import sigencode_string_canonize
import hashlib

from google.protobuf.json_format import Parse, ParseDict

import sys
sys.path.append(os.path.join(os.path.dirname(__name__), '.'))

from helpers import proto_to_binary, timestamp_string_to_proto, stargate_msg, create_ibc_client, fetch_chain_objects, bech32_to_hexstring, hexstring_to_bytes, bech32_to_b64, b64_to_bytes, fabricate_update_client, fetch_proofs, deploy_local_wasm, init_contract, execute_msg, fetch_channel_proof, bank_msg_send, to_binary, migrate_msg, fetch_packet_proof, fetch_ack_proof, OsmoKey, bytes_to_hexstring, b64_to_hexstring, cleanup_wallet


parser = argparse.ArgumentParser(description="provide lcd url")
#parser.add_argument("--url", help="lcd url with port", type=str, required=False, default="http://127.0.0.1:1317")
parser.add_argument("--url", help="lcd url with port", type=str)
args = parser.parse_args(args=[])
lcd_url = args.url

################################################
# chain objects
################################################

if lcd_url is None:
  (osmo, osmo_wallet, osmo_rpc_url, osmo_rpc_header) = fetch_chain_objects("localosmosis")
else:
  (osmo, osmo_wallet, osmo_rpc_url, osmo_rpc_header) = create_osmo_chain_objects(lcd_url, "localosmosis")

#various wallets from localnet genesis file

wallet1 = osmo.wallet(OsmoKey(mnemonic="notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius", coin_type=118))

wallet2 = osmo.wallet(OsmoKey(mnemonic="quality vacuum heart guard buzz spike sight swarm shove special gym robust assume sudden deposit grid alcohol choice devote leader tilt noodle tide penalty", coin_type=118))

wallet3 = osmo.wallet(OsmoKey(mnemonic='symbol force gallery make bulk round subway violin worry mixture penalty kingdom boring survey tool fringe patrol sausage hard admit remember broken alien absorb', coin_type=118))

wallet4 = osmo.wallet(OsmoKey(mnemonic='bounce success option birth apple portion aunt rural episode solution hockey pencil lend session cause hedgehog slender journey system canvas decorate razor catch empty', coin_type=118))

wallet_10 = osmo.wallet(OsmoKey(mnemonic="prefer forget visit mistake mixture feel eyebrow autumn shop pair address airport diesel street pass vague innocent poem method awful require hurry unhappy shoulder", coin_type=118))

################################################
# deploy local wasms
################################################

tf_code_id = deploy_local_wasm("/repos/zodiac/tokenfactorytest/artifacts/tokenfactory_hooks.wasm", osmo_wallet, osmo)

cleanup_wallet(wallet1, wallet_10, osmo)
cleanup_wallet(wallet2, wallet_10, osmo)
cleanup_wallet(wallet3, wallet_10, osmo)
cleanup_wallet(osmo_wallet, wallet_10, osmo)

################################################
# setup test contract
################################################

init_result = init_contract(tf_code_id, {}, osmo_wallet, osmo, "test", fee_in=Fee(42000000, "11000000uosmo"))
tf_test_address = init_result.logs[0].events_by_type["instantiate"]["_contract_address"][0]
tf_denom = osmo.wasm.contract_query(tf_test_address, {"denom":{}})

execute_msg(tf_test_address, {"mint_to": {"address": osmo_wallet.key.acc_address, "amount": "69"}}, osmo_wallet, osmo)
execute_msg(tf_test_address, {"burn_from": {"address": osmo_wallet.key.acc_address, "amount": "69"}}, osmo_wallet, osmo)

print(osmo.wasm.contract_query(tf_test_address, {"hook_activation_history":{}}))

execute_msg(tf_test_address, {"mint_to": {"address": osmo_wallet.key.acc_address, "amount": "69"}}, osmo_wallet, osmo)
execute_msg(tf_test_address, {"mint_to": {"address": wallet2.key.acc_address, "amount": "69"}}, osmo_wallet, osmo)

print(osmo.wasm.contract_query(tf_test_address, {"hook_activation_history":{}}))

execute_msg(tf_test_address, {"mint": {"amount": "69"}}, osmo_wallet, osmo)
execute_msg(tf_test_address, {"burn": {"amount": "69"}}, osmo_wallet, osmo)

print(osmo.wasm.contract_query(tf_test_address, {"hook_activation_history":{}}))

bank_msg_send(wallet2.key.acc_address, Coins([Coin(denom=tf_denom, amount="69")]), osmo_wallet, osmo)

print(osmo.wasm.contract_query(tf_test_address, {"hook_activation_history":{}}))
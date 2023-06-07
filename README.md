# tokenfactorytest

## localosmosis environment

initial state of repo
```
ubuntu@ip-172-31-21-69:~/repos/osmosis$ sudo rm -rf ~/.osmosisd-local
ubuntu@ip-172-31-21-69:~/repos/osmosis$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

update max gas per tx from 25M to 120M
```
ubuntu@ip-172-31-21-69:~/repos/osmosis$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   cmd/osmosisd/cmd/root.go

no changes added to commit (use "git add" and/or "git commit -a")
ubuntu@ip-172-31-21-69:~/repos/osmosis$ git diff cmd/osmosisd/cmd/root.go
diff --git a/cmd/osmosisd/cmd/root.go b/cmd/osmosisd/cmd/root.go
index 641f027e1..c1d98cb2f 100644
--- a/cmd/osmosisd/cmd/root.go
+++ b/cmd/osmosisd/cmd/root.go
@@ -148,7 +148,7 @@ func initAppConfig() (string, interface{}) {
 [osmosis-mempool]
 # This is the max allowed gas any tx. 
 # This is only for local mempool purposes, and thus    is only ran on check tx.
-max-gas-wanted-per-tx = "25000000"
+max-gas-wanted-per-tx = "120000000"
 
 # This is the minimum gas fee any arbitrage tx should have, denominated in uosmo per gas
 # Default value of ".005" then means that a tx with 1 million gas costs (.005 uosmo/gas) * 1_000_000 gas = .005 osmo
 ```

build docker image
```
ubuntu@ip-172-31-21-69:~/repos/osmosis$ DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 docker-compose -f tests/localosmosis/docker-compose.yml build
```

spin-up localosmosis
```
ubuntu@ip-172-31-21-69:~/repos/osmosis$ STATE="" docker-compose -f tests/localosmosis/docker-compose.yml up -d
ubuntu@ip-172-31-21-69:~/repos/osmosis$ docker ps
CONTAINER ID   IMAGE           COMMAND                CREATED              STATUS          PORTS                                                                                                                                                                                                           NAMES
1722f1aa28be   local:osmosis   "/osmosis/setup.sh "   About a minute ago   Up 44 seconds   0.0.0.0:1317->1317/tcp, :::1317->1317/tcp, 0.0.0.0:6060->6060/tcp, :::6060->6060/tcp, 0.0.0.0:9090-9091->9090-9091/tcp, :::9090-9091->9090-9091/tcp, 0.0.0.0:26657->26657/tcp, :::26657->26657/tcp, 26656/tcp   localosmosis_osmosisd_1

```

## overview of tokenfactory test contract

The tokenfactorytest contract creates a tokenfactory denom on instantiate, and then persists all blockbeforesend and trackbeforesend msgs in state.

The sudo contract entry_point is implemented here: https://github.com/zodiac-protocol/tokenfactorytest/blob/9238f29dc2039514f1aa229db913202bd7661bf6/contracts/tokenfactory_hooks/src/contract.rs#L149

Any permutation of mint/burn with the target address set/unset does not get picked up by the contract's sudo hook
```
In [15]: %cpaste
Pasting code; enter '--' alone on the line to stop or use Ctrl-D.
:execute_msg(tf_test_address, {"burn_from": {"address": osmo_wallet.key.acc_address, "amount": "69"}}, osmo_wallet, osmo)

execute_msg(tf_test_address, {"mint_to": {"address": osmo_wallet.key.acc_address, "amount": "69"}}, osmo_wallet, osmo)
execute_msg(tf_test_address, {"mint_to": {"address": wallet2.key.acc_address, "amount": "69"}}, osmo_wallet, osmo)

execute_msg(tf_test_address, {"mint": {"amount": "69"}}, osmo_wallet, osmo)
execute_msg(tf_test_address, {"burn": {"amount": "69"}}, osmo_wallet, osmo)::::::
:<EOF>
Out[15]: BlockTxBroadcastResult(height=92, txhash='AFE6A8AA1EF6D64BF59440C8C782F85CCDD0E82EEEF718DBDBF0DFC6311AD08C', raw_log='[{"events":[{"type":"burn","attributes":[{"key":"burner","value":"osmo19ejy8n9qsectrf4semdp9cpknflld0j64mwamn"},{"key":"amount","value":"69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test"}]},{"type":"coin_received","attributes":[{"key":"receiver","value":"osmo19ejy8n9qsectrf4semdp9cpknflld0j64mwamn"},{"key":"amount","value":"69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test"}]},{"type":"coin_spent","attributes":[{"key":"spender","value":"osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670"},{"key":"amount","value":"69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test"},{"key":"spender","value":"osmo19ejy8n9qsectrf4semdp9cpknflld0j64mwamn"},{"key":"amount","value":"69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test"}]},{"type":"execute","attributes":[{"key":"_contract_address","value":"osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670"}]},{"type":"message","attributes":[{"key":"action","value":"/cosmwasm.wasm.v1.MsgExecuteContract"},{"key":"module","value":"wasm"},{"key":"sender","value":"osmo14hcxlnwlqtq75ttaxf674vk6mafspg8xwgnn53"}]},{"type":"tf_burn","attributes":[{"key":"burn_from_address","value":"osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670"},{"key":"amount","value":"69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test"}]},{"type":"transfer","attributes":[{"key":"recipient","value":"osmo19ejy8n9qsectrf4semdp9cpknflld0j64mwamn"},{"key":"sender","value":"osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670"},{"key":"amount","value":"69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test"}]}]}]', gas_wanted=4000000, gas_used=162068, logs=[TxLog(msg_index=0, log='', events=[{'type': 'burn', 'attributes': [{'key': 'burner', 'value': 'osmo19ejy8n9qsectrf4semdp9cpknflld0j64mwamn'}, {'key': 'amount', 'value': '69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test'}]}, {'type': 'coin_received', 'attributes': [{'key': 'receiver', 'value': 'osmo19ejy8n9qsectrf4semdp9cpknflld0j64mwamn'}, {'key': 'amount', 'value': '69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test'}]}, {'type': 'coin_spent', 'attributes': [{'key': 'spender', 'value': 'osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670'}, {'key': 'amount', 'value': '69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test'}, {'key': 'spender', 'value': 'osmo19ejy8n9qsectrf4semdp9cpknflld0j64mwamn'}, {'key': 'amount', 'value': '69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test'}]}, {'type': 'execute', 'attributes': [{'key': '_contract_address', 'value': 'osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670'}]}, {'type': 'message', 'attributes': [{'key': 'action', 'value': '/cosmwasm.wasm.v1.MsgExecuteContract'}, {'key': 'module', 'value': 'wasm'}, {'key': 'sender', 'value': 'osmo14hcxlnwlqtq75ttaxf674vk6mafspg8xwgnn53'}]}, {'type': 'tf_burn', 'attributes': [{'key': 'burn_from_address', 'value': 'osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670'}, {'key': 'amount', 'value': '69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test'}]}, {'type': 'transfer', 'attributes': [{'key': 'recipient', 'value': 'osmo19ejy8n9qsectrf4semdp9cpknflld0j64mwamn'}, {'key': 'sender', 'value': 'osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670'}, {'key': 'amount', 'value': '69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test'}]}], events_by_type={'burn': {'burner': ['osmo19ejy8n9qsectrf4semdp9cpknflld0j64mwamn'], 'amount': ['69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test']}, 'coin_received': {'receiver': ['osmo19ejy8n9qsectrf4semdp9cpknflld0j64mwamn'], 'amount': ['69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test']}, 'coin_spent': {'spender': ['osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670', 'osmo19ejy8n9qsectrf4semdp9cpknflld0j64mwamn'], 'amount': ['69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test', '69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test']}, 'execute': {'_contract_address': ['osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670']}, 'message': {'action': ['/cosmwasm.wasm.v1.MsgExecuteContract'], 'module': ['wasm'], 'sender': ['osmo14hcxlnwlqtq75ttaxf674vk6mafspg8xwgnn53']}, 'tf_burn': {'burn_from_address': ['osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670'], 'amount': ['69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test']}, 'transfer': {'recipient': ['osmo19ejy8n9qsectrf4semdp9cpknflld0j64mwamn'], 'sender': ['osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670'], 'amount': ['69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test']}})], code=0, codespace='', info=None, data=None, timestamp=None)

In [16]: osmo.wasm.contract_query(tf_test_address, {"hook_activation_history":{}})
Out[16]: []
```

Only a bank send of the tokenfactory denom triggers the hook
```
In [17]: bank_msg_send(wallet2.key.acc_address, Coins([Coin(denom=tf_denom, amount="69")]), osmo_wallet, osmo)
Out[17]: BlockTxBroadcastResult(height=94, txhash='48E406659773182513A21998F67A2BFF4369871EDC9181B18424D8E5463D779D', raw_log='[{"events":[{"type":"coin_received","attributes":[{"key":"receiver","value":"osmo18s5lynnmx37hq4wlrw9gdn68sg2uxp5rgk26vv"},{"key":"amount","value":"69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test"}]},{"type":"coin_spent","attributes":[{"key":"spender","value":"osmo14hcxlnwlqtq75ttaxf674vk6mafspg8xwgnn53"},{"key":"amount","value":"69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test"}]},{"type":"message","attributes":[{"key":"action","value":"/cosmos.bank.v1beta1.MsgSend"},{"key":"sender","value":"osmo14hcxlnwlqtq75ttaxf674vk6mafspg8xwgnn53"},{"key":"module","value":"bank"}]},{"type":"transfer","attributes":[{"key":"recipient","value":"osmo18s5lynnmx37hq4wlrw9gdn68sg2uxp5rgk26vv"},{"key":"sender","value":"osmo14hcxlnwlqtq75ttaxf674vk6mafspg8xwgnn53"},{"key":"amount","value":"69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test"}]}]}]', gas_wanted=4000000, gas_used=250740, logs=[TxLog(msg_index=0, log='', events=[{'type': 'coin_received', 'attributes': [{'key': 'receiver', 'value': 'osmo18s5lynnmx37hq4wlrw9gdn68sg2uxp5rgk26vv'}, {'key': 'amount', 'value': '69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test'}]}, {'type': 'coin_spent', 'attributes': [{'key': 'spender', 'value': 'osmo14hcxlnwlqtq75ttaxf674vk6mafspg8xwgnn53'}, {'key': 'amount', 'value': '69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test'}]}, {'type': 'message', 'attributes': [{'key': 'action', 'value': '/cosmos.bank.v1beta1.MsgSend'}, {'key': 'sender', 'value': 'osmo14hcxlnwlqtq75ttaxf674vk6mafspg8xwgnn53'}, {'key': 'module', 'value': 'bank'}]}, {'type': 'transfer', 'attributes': [{'key': 'recipient', 'value': 'osmo18s5lynnmx37hq4wlrw9gdn68sg2uxp5rgk26vv'}, {'key': 'sender', 'value': 'osmo14hcxlnwlqtq75ttaxf674vk6mafspg8xwgnn53'}, {'key': 'amount', 'value': '69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test'}]}], events_by_type={'coin_received': {'receiver': ['osmo18s5lynnmx37hq4wlrw9gdn68sg2uxp5rgk26vv'], 'amount': ['69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test']}, 'coin_spent': {'spender': ['osmo14hcxlnwlqtq75ttaxf674vk6mafspg8xwgnn53'], 'amount': ['69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test']}, 'message': {'action': ['/cosmos.bank.v1beta1.MsgSend'], 'sender': ['osmo14hcxlnwlqtq75ttaxf674vk6mafspg8xwgnn53'], 'module': ['bank']}, 'transfer': {'recipient': ['osmo18s5lynnmx37hq4wlrw9gdn68sg2uxp5rgk26vv'], 'sender': ['osmo14hcxlnwlqtq75ttaxf674vk6mafspg8xwgnn53'], 'amount': ['69factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test']}})], code=0, codespace='', info=None, data=None, timestamp=None)

In [18]: osmo.wasm.contract_query(tf_test_address, {"hook_activation_history":{}})
Out[18]: 
[{'block': 94,
  'hook_msg': 'BlockBeforeSend { from: "osmo14hcxlnwlqtq75ttaxf674vk6mafspg8xwgnn53", to: "osmo18s5lynnmx37hq4wlrw9gdn68sg2uxp5rgk26vv", amount: Coin { denom: "factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test", amount: Uint128(69) } }'},
 {'block': 94,
  'hook_msg': 'TrackBeforeSend { from: "osmo14hcxlnwlqtq75ttaxf674vk6mafspg8xwgnn53", to: "osmo18s5lynnmx37hq4wlrw9gdn68sg2uxp5rgk26vv", amount: Coin { denom: "factory/osmo1wug8sewp6cedgkmrmvhl3lf3tulagm9hnvy8p0rppz9yjw0g4wtqcm3670/test", amount: Uint128(69) } }'}]
```


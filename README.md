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


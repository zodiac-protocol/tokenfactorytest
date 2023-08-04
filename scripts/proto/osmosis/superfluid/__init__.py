# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: osmosis/superfluid/genesis.proto, osmosis/superfluid/params.proto, osmosis/superfluid/query.proto, osmosis/superfluid/superfluid.proto, osmosis/superfluid/tx.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List, Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


class SuperfluidAssetType(betterproto.Enum):
    SuperfluidAssetTypeNative = 0
    SuperfluidAssetTypeLPShare = 1


@dataclass(eq=False, repr=False)
class SuperfluidAsset(betterproto.Message):
    """
    SuperfluidAsset stores the pair of superfluid asset type and denom pair
    """

    denom: str = betterproto.string_field(1)
    asset_type: "SuperfluidAssetType" = betterproto.enum_field(2)


@dataclass(eq=False, repr=False)
class SuperfluidIntermediaryAccount(betterproto.Message):
    """
    SuperfluidIntermediaryAccount takes the role of intermediary between LP
    token and OSMO tokens for superfluid staking
    """

    denom: str = betterproto.string_field(1)
    val_addr: str = betterproto.string_field(2)
    # perpetual gauge for rewards distribution
    gauge_id: int = betterproto.uint64_field(3)


@dataclass(eq=False, repr=False)
class OsmoEquivalentMultiplierRecord(betterproto.Message):
    """
    The Osmo-Equivalent-Multiplier Record for epoch N refers to the osmo worth
    we treat an LP share as having, for all of epoch N. Eventually this is
    intended to be set as the Time-weighted-average-osmo-backing for the entire
    duration of epoch N-1. (Thereby locking whats in use for epoch N as based
    on the prior epochs rewards) However for now, this is not the TWAP but
    instead the spot price at the boundary.  For different types of assets in
    the future, it could change.
    """

    epoch_number: int = betterproto.int64_field(1)
    # superfluid asset denom, can be LP token or native token
    denom: str = betterproto.string_field(2)
    multiplier: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class SuperfluidDelegationRecord(betterproto.Message):
    """
    SuperfluidDelegationRecord takes the role of intermediary between LP token
    and OSMO tokens for superfluid staking
    """

    delegator_address: str = betterproto.string_field(1)
    validator_address: str = betterproto.string_field(2)
    delegation_amount: "__cosmos_base_v1_beta1__.Coin" = betterproto.message_field(3)
    equivalent_staked_amount: "__cosmos_base_v1_beta1__.Coin" = (
        betterproto.message_field(4)
    )


@dataclass(eq=False, repr=False)
class LockIdIntermediaryAccountConnection(betterproto.Message):
    lock_id: int = betterproto.uint64_field(1)
    intermediary_account: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class UnpoolWhitelistedPools(betterproto.Message):
    ids: List[int] = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params holds parameters for the superfluid module"""

    # the risk_factor is to be cut on OSMO equivalent value of lp tokens for
    # superfluid staking, default: 5%
    minimum_risk_factor: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the module's genesis state."""

    params: "Params" = betterproto.message_field(1)
    superfluid_assets: List["SuperfluidAsset"] = betterproto.message_field(2)
    osmo_equivalent_multipliers: List[
        "OsmoEquivalentMultiplierRecord"
    ] = betterproto.message_field(3)
    intermediary_accounts: List[
        "SuperfluidIntermediaryAccount"
    ] = betterproto.message_field(4)
    intemediary_account_connections: List[
        "LockIdIntermediaryAccountConnection"
    ] = betterproto.message_field(5)


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    # params defines the parameters of the module.
    params: "Params" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class AssetTypeRequest(betterproto.Message):
    denom: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class AssetTypeResponse(betterproto.Message):
    asset_type: "SuperfluidAssetType" = betterproto.enum_field(1)


@dataclass(eq=False, repr=False)
class AllAssetsRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class AllAssetsResponse(betterproto.Message):
    assets: List["SuperfluidAsset"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class AssetMultiplierRequest(betterproto.Message):
    denom: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class AssetMultiplierResponse(betterproto.Message):
    osmo_equivalent_multiplier: "OsmoEquivalentMultiplierRecord" = (
        betterproto.message_field(1)
    )


@dataclass(eq=False, repr=False)
class SuperfluidIntermediaryAccountInfo(betterproto.Message):
    denom: str = betterproto.string_field(1)
    val_addr: str = betterproto.string_field(2)
    gauge_id: int = betterproto.uint64_field(3)
    address: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class AllIntermediaryAccountsRequest(betterproto.Message):
    pagination: "__cosmos_base_query_v1_beta1__.PageRequest" = (
        betterproto.message_field(1)
    )


@dataclass(eq=False, repr=False)
class AllIntermediaryAccountsResponse(betterproto.Message):
    accounts: List["SuperfluidIntermediaryAccountInfo"] = betterproto.message_field(1)
    pagination: "__cosmos_base_query_v1_beta1__.PageResponse" = (
        betterproto.message_field(2)
    )


@dataclass(eq=False, repr=False)
class ConnectedIntermediaryAccountRequest(betterproto.Message):
    lock_id: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class ConnectedIntermediaryAccountResponse(betterproto.Message):
    account: "SuperfluidIntermediaryAccountInfo" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class TotalSuperfluidDelegationsRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class TotalSuperfluidDelegationsResponse(betterproto.Message):
    total_delegations: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class SuperfluidDelegationAmountRequest(betterproto.Message):
    delegator_address: str = betterproto.string_field(1)
    validator_address: str = betterproto.string_field(2)
    denom: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class SuperfluidDelegationAmountResponse(betterproto.Message):
    amount: List["__cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class SuperfluidDelegationsByDelegatorRequest(betterproto.Message):
    delegator_address: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class SuperfluidDelegationsByDelegatorResponse(betterproto.Message):
    superfluid_delegation_records: List[
        "SuperfluidDelegationRecord"
    ] = betterproto.message_field(1)
    total_delegated_coins: List[
        "__cosmos_base_v1_beta1__.Coin"
    ] = betterproto.message_field(2)
    total_equivalent_staked_amount: "__cosmos_base_v1_beta1__.Coin" = (
        betterproto.message_field(3)
    )


@dataclass(eq=False, repr=False)
class SuperfluidUndelegationsByDelegatorRequest(betterproto.Message):
    delegator_address: str = betterproto.string_field(1)
    denom: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class SuperfluidUndelegationsByDelegatorResponse(betterproto.Message):
    superfluid_delegation_records: List[
        "SuperfluidDelegationRecord"
    ] = betterproto.message_field(1)
    total_undelegated_coins: List[
        "__cosmos_base_v1_beta1__.Coin"
    ] = betterproto.message_field(2)
    synthetic_locks: List["_lockup__.SyntheticLock"] = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class SuperfluidDelegationsByValidatorDenomRequest(betterproto.Message):
    validator_address: str = betterproto.string_field(1)
    denom: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class SuperfluidDelegationsByValidatorDenomResponse(betterproto.Message):
    superfluid_delegation_records: List[
        "SuperfluidDelegationRecord"
    ] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class EstimateSuperfluidDelegatedAmountByValidatorDenomRequest(betterproto.Message):
    validator_address: str = betterproto.string_field(1)
    denom: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class EstimateSuperfluidDelegatedAmountByValidatorDenomResponse(betterproto.Message):
    total_delegated_coins: List[
        "__cosmos_base_v1_beta1__.Coin"
    ] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class MsgSuperfluidDelegate(betterproto.Message):
    sender: str = betterproto.string_field(1)
    lock_id: int = betterproto.uint64_field(2)
    val_addr: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class MsgSuperfluidDelegateResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class MsgSuperfluidUndelegate(betterproto.Message):
    sender: str = betterproto.string_field(1)
    lock_id: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class MsgSuperfluidUndelegateResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class MsgSuperfluidUnbondLock(betterproto.Message):
    sender: str = betterproto.string_field(1)
    lock_id: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class MsgSuperfluidUnbondLockResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class MsgLockAndSuperfluidDelegate(betterproto.Message):
    """
    MsgLockAndSuperfluidDelegate locks coins with the unbonding period
    duration, and then does a superfluid lock from the newly created lockup, to
    the specified validator addr.
    """

    sender: str = betterproto.string_field(1)
    coins: List["__cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(2)
    val_addr: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class MsgLockAndSuperfluidDelegateResponse(betterproto.Message):
    id: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class MsgUnPoolWhitelistedPool(betterproto.Message):
    """
    MsgUnPoolWhitelistedPool Unpools every lock the sender has, that is
    associated with pool pool_id. If pool_id is not approved for unpooling by
    governance, this is a no-op. Unpooling takes the locked gamm shares, and
    runs "ExitPool" on it, to get the constituent tokens. e.g. z gamm/pool/1
    tokens ExitPools into constituent tokens x uatom, y uosmo. Then it creates
    a new lock for every constituent token, with the duration associated with
    the lock. If the lock was unbonding, the new lockup durations should be the
    time left until unbond completion.
    """

    sender: str = betterproto.string_field(1)
    pool_id: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class MsgUnPoolWhitelistedPoolResponse(betterproto.Message):
    exited_lock_ids: List[int] = betterproto.uint64_field(1)


class QueryStub(betterproto.ServiceStub):
    async def params(self) -> "QueryParamsResponse":

        request = QueryParamsRequest()

        return await self._unary_unary(
            "/osmosis.superfluid.Query/Params", request, QueryParamsResponse
        )

    async def asset_type(self, *, denom: str = "") -> "AssetTypeResponse":

        request = AssetTypeRequest()
        request.denom = denom

        return await self._unary_unary(
            "/osmosis.superfluid.Query/AssetType", request, AssetTypeResponse
        )

    async def all_assets(self) -> "AllAssetsResponse":

        request = AllAssetsRequest()

        return await self._unary_unary(
            "/osmosis.superfluid.Query/AllAssets", request, AllAssetsResponse
        )

    async def asset_multiplier(self, *, denom: str = "") -> "AssetMultiplierResponse":

        request = AssetMultiplierRequest()
        request.denom = denom

        return await self._unary_unary(
            "/osmosis.superfluid.Query/AssetMultiplier",
            request,
            AssetMultiplierResponse,
        )

    async def all_intermediary_accounts(
        self, *, pagination: "__cosmos_base_query_v1_beta1__.PageRequest" = None
    ) -> "AllIntermediaryAccountsResponse":

        request = AllIntermediaryAccountsRequest()
        if pagination is not None:
            request.pagination = pagination

        return await self._unary_unary(
            "/osmosis.superfluid.Query/AllIntermediaryAccounts",
            request,
            AllIntermediaryAccountsResponse,
        )

    async def connected_intermediary_account(
        self, *, lock_id: int = 0
    ) -> "ConnectedIntermediaryAccountResponse":

        request = ConnectedIntermediaryAccountRequest()
        request.lock_id = lock_id

        return await self._unary_unary(
            "/osmosis.superfluid.Query/ConnectedIntermediaryAccount",
            request,
            ConnectedIntermediaryAccountResponse,
        )

    async def total_superfluid_delegations(
        self,
    ) -> "TotalSuperfluidDelegationsResponse":

        request = TotalSuperfluidDelegationsRequest()

        return await self._unary_unary(
            "/osmosis.superfluid.Query/TotalSuperfluidDelegations",
            request,
            TotalSuperfluidDelegationsResponse,
        )

    async def superfluid_delegation_amount(
        self,
        *,
        delegator_address: str = "",
        validator_address: str = "",
        denom: str = ""
    ) -> "SuperfluidDelegationAmountResponse":

        request = SuperfluidDelegationAmountRequest()
        request.delegator_address = delegator_address
        request.validator_address = validator_address
        request.denom = denom

        return await self._unary_unary(
            "/osmosis.superfluid.Query/SuperfluidDelegationAmount",
            request,
            SuperfluidDelegationAmountResponse,
        )

    async def superfluid_delegations_by_delegator(
        self, *, delegator_address: str = ""
    ) -> "SuperfluidDelegationsByDelegatorResponse":

        request = SuperfluidDelegationsByDelegatorRequest()
        request.delegator_address = delegator_address

        return await self._unary_unary(
            "/osmosis.superfluid.Query/SuperfluidDelegationsByDelegator",
            request,
            SuperfluidDelegationsByDelegatorResponse,
        )

    async def superfluid_undelegations_by_delegator(
        self, *, delegator_address: str = "", denom: str = ""
    ) -> "SuperfluidUndelegationsByDelegatorResponse":

        request = SuperfluidUndelegationsByDelegatorRequest()
        request.delegator_address = delegator_address
        request.denom = denom

        return await self._unary_unary(
            "/osmosis.superfluid.Query/SuperfluidUndelegationsByDelegator",
            request,
            SuperfluidUndelegationsByDelegatorResponse,
        )

    async def superfluid_delegations_by_validator_denom(
        self, *, validator_address: str = "", denom: str = ""
    ) -> "SuperfluidDelegationsByValidatorDenomResponse":

        request = SuperfluidDelegationsByValidatorDenomRequest()
        request.validator_address = validator_address
        request.denom = denom

        return await self._unary_unary(
            "/osmosis.superfluid.Query/SuperfluidDelegationsByValidatorDenom",
            request,
            SuperfluidDelegationsByValidatorDenomResponse,
        )

    async def estimate_superfluid_delegated_amount_by_validator_denom(
        self, *, validator_address: str = "", denom: str = ""
    ) -> "EstimateSuperfluidDelegatedAmountByValidatorDenomResponse":

        request = EstimateSuperfluidDelegatedAmountByValidatorDenomRequest()
        request.validator_address = validator_address
        request.denom = denom

        return await self._unary_unary(
            "/osmosis.superfluid.Query/EstimateSuperfluidDelegatedAmountByValidatorDenom",
            request,
            EstimateSuperfluidDelegatedAmountByValidatorDenomResponse,
        )


class MsgStub(betterproto.ServiceStub):
    async def superfluid_delegate(
        self, *, sender: str = "", lock_id: int = 0, val_addr: str = ""
    ) -> "MsgSuperfluidDelegateResponse":

        request = MsgSuperfluidDelegate()
        request.sender = sender
        request.lock_id = lock_id
        request.val_addr = val_addr

        return await self._unary_unary(
            "/osmosis.superfluid.Msg/SuperfluidDelegate",
            request,
            MsgSuperfluidDelegateResponse,
        )

    async def superfluid_undelegate(
        self, *, sender: str = "", lock_id: int = 0
    ) -> "MsgSuperfluidUndelegateResponse":

        request = MsgSuperfluidUndelegate()
        request.sender = sender
        request.lock_id = lock_id

        return await self._unary_unary(
            "/osmosis.superfluid.Msg/SuperfluidUndelegate",
            request,
            MsgSuperfluidUndelegateResponse,
        )

    async def superfluid_unbond_lock(
        self, *, sender: str = "", lock_id: int = 0
    ) -> "MsgSuperfluidUnbondLockResponse":

        request = MsgSuperfluidUnbondLock()
        request.sender = sender
        request.lock_id = lock_id

        return await self._unary_unary(
            "/osmosis.superfluid.Msg/SuperfluidUnbondLock",
            request,
            MsgSuperfluidUnbondLockResponse,
        )

    async def lock_and_superfluid_delegate(
        self,
        *,
        sender: str = "",
        coins: Optional[List["__cosmos_base_v1_beta1__.Coin"]] = None,
        val_addr: str = ""
    ) -> "MsgLockAndSuperfluidDelegateResponse":
        coins = coins or []

        request = MsgLockAndSuperfluidDelegate()
        request.sender = sender
        if coins is not None:
            request.coins = coins
        request.val_addr = val_addr

        return await self._unary_unary(
            "/osmosis.superfluid.Msg/LockAndSuperfluidDelegate",
            request,
            MsgLockAndSuperfluidDelegateResponse,
        )

    async def un_pool_whitelisted_pool(
        self, *, sender: str = "", pool_id: int = 0
    ) -> "MsgUnPoolWhitelistedPoolResponse":

        request = MsgUnPoolWhitelistedPool()
        request.sender = sender
        request.pool_id = pool_id

        return await self._unary_unary(
            "/osmosis.superfluid.Msg/UnPoolWhitelistedPool",
            request,
            MsgUnPoolWhitelistedPoolResponse,
        )


class QueryBase(ServiceBase):
    async def params(self) -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def asset_type(self, denom: str) -> "AssetTypeResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def all_assets(self) -> "AllAssetsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def asset_multiplier(self, denom: str) -> "AssetMultiplierResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def all_intermediary_accounts(
        self, pagination: "__cosmos_base_query_v1_beta1__.PageRequest"
    ) -> "AllIntermediaryAccountsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def connected_intermediary_account(
        self, lock_id: int
    ) -> "ConnectedIntermediaryAccountResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def total_superfluid_delegations(
        self,
    ) -> "TotalSuperfluidDelegationsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def superfluid_delegation_amount(
        self, delegator_address: str, validator_address: str, denom: str
    ) -> "SuperfluidDelegationAmountResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def superfluid_delegations_by_delegator(
        self, delegator_address: str
    ) -> "SuperfluidDelegationsByDelegatorResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def superfluid_undelegations_by_delegator(
        self, delegator_address: str, denom: str
    ) -> "SuperfluidUndelegationsByDelegatorResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def superfluid_delegations_by_validator_denom(
        self, validator_address: str, denom: str
    ) -> "SuperfluidDelegationsByValidatorDenomResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def estimate_superfluid_delegated_amount_by_validator_denom(
        self, validator_address: str, denom: str
    ) -> "EstimateSuperfluidDelegatedAmountByValidatorDenomResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_params(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.params(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_asset_type(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "denom": request.denom,
        }

        response = await self.asset_type(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_all_assets(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.all_assets(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_asset_multiplier(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "denom": request.denom,
        }

        response = await self.asset_multiplier(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_all_intermediary_accounts(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "pagination": request.pagination,
        }

        response = await self.all_intermediary_accounts(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_connected_intermediary_account(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "lock_id": request.lock_id,
        }

        response = await self.connected_intermediary_account(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_total_superfluid_delegations(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.total_superfluid_delegations(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_superfluid_delegation_amount(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "delegator_address": request.delegator_address,
            "validator_address": request.validator_address,
            "denom": request.denom,
        }

        response = await self.superfluid_delegation_amount(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_superfluid_delegations_by_delegator(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "delegator_address": request.delegator_address,
        }

        response = await self.superfluid_delegations_by_delegator(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_superfluid_undelegations_by_delegator(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "delegator_address": request.delegator_address,
            "denom": request.denom,
        }

        response = await self.superfluid_undelegations_by_delegator(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_superfluid_delegations_by_validator_denom(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "validator_address": request.validator_address,
            "denom": request.denom,
        }

        response = await self.superfluid_delegations_by_validator_denom(
            **request_kwargs
        )
        await stream.send_message(response)

    async def __rpc_estimate_superfluid_delegated_amount_by_validator_denom(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "validator_address": request.validator_address,
            "denom": request.denom,
        }

        response = await self.estimate_superfluid_delegated_amount_by_validator_denom(
            **request_kwargs
        )
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/osmosis.superfluid.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
            "/osmosis.superfluid.Query/AssetType": grpclib.const.Handler(
                self.__rpc_asset_type,
                grpclib.const.Cardinality.UNARY_UNARY,
                AssetTypeRequest,
                AssetTypeResponse,
            ),
            "/osmosis.superfluid.Query/AllAssets": grpclib.const.Handler(
                self.__rpc_all_assets,
                grpclib.const.Cardinality.UNARY_UNARY,
                AllAssetsRequest,
                AllAssetsResponse,
            ),
            "/osmosis.superfluid.Query/AssetMultiplier": grpclib.const.Handler(
                self.__rpc_asset_multiplier,
                grpclib.const.Cardinality.UNARY_UNARY,
                AssetMultiplierRequest,
                AssetMultiplierResponse,
            ),
            "/osmosis.superfluid.Query/AllIntermediaryAccounts": grpclib.const.Handler(
                self.__rpc_all_intermediary_accounts,
                grpclib.const.Cardinality.UNARY_UNARY,
                AllIntermediaryAccountsRequest,
                AllIntermediaryAccountsResponse,
            ),
            "/osmosis.superfluid.Query/ConnectedIntermediaryAccount": grpclib.const.Handler(
                self.__rpc_connected_intermediary_account,
                grpclib.const.Cardinality.UNARY_UNARY,
                ConnectedIntermediaryAccountRequest,
                ConnectedIntermediaryAccountResponse,
            ),
            "/osmosis.superfluid.Query/TotalSuperfluidDelegations": grpclib.const.Handler(
                self.__rpc_total_superfluid_delegations,
                grpclib.const.Cardinality.UNARY_UNARY,
                TotalSuperfluidDelegationsRequest,
                TotalSuperfluidDelegationsResponse,
            ),
            "/osmosis.superfluid.Query/SuperfluidDelegationAmount": grpclib.const.Handler(
                self.__rpc_superfluid_delegation_amount,
                grpclib.const.Cardinality.UNARY_UNARY,
                SuperfluidDelegationAmountRequest,
                SuperfluidDelegationAmountResponse,
            ),
            "/osmosis.superfluid.Query/SuperfluidDelegationsByDelegator": grpclib.const.Handler(
                self.__rpc_superfluid_delegations_by_delegator,
                grpclib.const.Cardinality.UNARY_UNARY,
                SuperfluidDelegationsByDelegatorRequest,
                SuperfluidDelegationsByDelegatorResponse,
            ),
            "/osmosis.superfluid.Query/SuperfluidUndelegationsByDelegator": grpclib.const.Handler(
                self.__rpc_superfluid_undelegations_by_delegator,
                grpclib.const.Cardinality.UNARY_UNARY,
                SuperfluidUndelegationsByDelegatorRequest,
                SuperfluidUndelegationsByDelegatorResponse,
            ),
            "/osmosis.superfluid.Query/SuperfluidDelegationsByValidatorDenom": grpclib.const.Handler(
                self.__rpc_superfluid_delegations_by_validator_denom,
                grpclib.const.Cardinality.UNARY_UNARY,
                SuperfluidDelegationsByValidatorDenomRequest,
                SuperfluidDelegationsByValidatorDenomResponse,
            ),
            "/osmosis.superfluid.Query/EstimateSuperfluidDelegatedAmountByValidatorDenom": grpclib.const.Handler(
                self.__rpc_estimate_superfluid_delegated_amount_by_validator_denom,
                grpclib.const.Cardinality.UNARY_UNARY,
                EstimateSuperfluidDelegatedAmountByValidatorDenomRequest,
                EstimateSuperfluidDelegatedAmountByValidatorDenomResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def superfluid_delegate(
        self, sender: str, lock_id: int, val_addr: str
    ) -> "MsgSuperfluidDelegateResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def superfluid_undelegate(
        self, sender: str, lock_id: int
    ) -> "MsgSuperfluidUndelegateResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def superfluid_unbond_lock(
        self, sender: str, lock_id: int
    ) -> "MsgSuperfluidUnbondLockResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def lock_and_superfluid_delegate(
        self,
        sender: str,
        coins: Optional[List["__cosmos_base_v1_beta1__.Coin"]],
        val_addr: str,
    ) -> "MsgLockAndSuperfluidDelegateResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def un_pool_whitelisted_pool(
        self, sender: str, pool_id: int
    ) -> "MsgUnPoolWhitelistedPoolResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_superfluid_delegate(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "sender": request.sender,
            "lock_id": request.lock_id,
            "val_addr": request.val_addr,
        }

        response = await self.superfluid_delegate(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_superfluid_undelegate(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "sender": request.sender,
            "lock_id": request.lock_id,
        }

        response = await self.superfluid_undelegate(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_superfluid_unbond_lock(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "sender": request.sender,
            "lock_id": request.lock_id,
        }

        response = await self.superfluid_unbond_lock(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_lock_and_superfluid_delegate(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "sender": request.sender,
            "coins": request.coins,
            "val_addr": request.val_addr,
        }

        response = await self.lock_and_superfluid_delegate(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_un_pool_whitelisted_pool(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "sender": request.sender,
            "pool_id": request.pool_id,
        }

        response = await self.un_pool_whitelisted_pool(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/osmosis.superfluid.Msg/SuperfluidDelegate": grpclib.const.Handler(
                self.__rpc_superfluid_delegate,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgSuperfluidDelegate,
                MsgSuperfluidDelegateResponse,
            ),
            "/osmosis.superfluid.Msg/SuperfluidUndelegate": grpclib.const.Handler(
                self.__rpc_superfluid_undelegate,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgSuperfluidUndelegate,
                MsgSuperfluidUndelegateResponse,
            ),
            "/osmosis.superfluid.Msg/SuperfluidUnbondLock": grpclib.const.Handler(
                self.__rpc_superfluid_unbond_lock,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgSuperfluidUnbondLock,
                MsgSuperfluidUnbondLockResponse,
            ),
            "/osmosis.superfluid.Msg/LockAndSuperfluidDelegate": grpclib.const.Handler(
                self.__rpc_lock_and_superfluid_delegate,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgLockAndSuperfluidDelegate,
                MsgLockAndSuperfluidDelegateResponse,
            ),
            "/osmosis.superfluid.Msg/UnPoolWhitelistedPool": grpclib.const.Handler(
                self.__rpc_un_pool_whitelisted_pool,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgUnPoolWhitelistedPool,
                MsgUnPoolWhitelistedPoolResponse,
            ),
        }


from .. import lockup as _lockup__
from ...cosmos.base import v1beta1 as __cosmos_base_v1_beta1__
from ...cosmos.base.query import v1beta1 as __cosmos_base_query_v1_beta1__

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: osmosis/gamm/pool-models/stableswap/stableswap_pool.proto, osmosis/gamm/pool-models/stableswap/tx.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List, Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class PoolParams(betterproto.Message):
    """
    PoolParams defined the parameters that will be managed by the pool
    governance in the future. This params are not managed by the chain
    governance. Instead they will be managed by the token holders of the pool.
    The pool's token holders are specified in future_pool_governor.
    """

    swap_fee: str = betterproto.string_field(1)
    exit_fee: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class Pool(betterproto.Message):
    """Pool is the stableswap Pool struct"""

    address: str = betterproto.string_field(1)
    id: int = betterproto.uint64_field(2)
    pool_params: "PoolParams" = betterproto.message_field(3)
    # This string specifies who will govern the pool in the future. Valid forms
    # of this are: {token name},{duration} {duration} where {token name} if
    # specified is the token which determines the governor, and if not specified
    # is the LP token for this pool.duration is a time specified as 0w,1w,2w,
    # etc. which specifies how long the token would need to be locked up to count
    # in governance. 0w means no lockup.
    future_pool_governor: str = betterproto.string_field(4)
    # sum of all LP shares
    total_shares: "_____cosmos_base_v1_beta1__.Coin" = betterproto.message_field(5)
    # assets in the pool
    pool_liquidity: List[
        "_____cosmos_base_v1_beta1__.Coin"
    ] = betterproto.message_field(6)
    # for calculation amognst assets with different precisions
    scaling_factor: List[int] = betterproto.uint64_field(7)
    # scaling_factor_governor is the address can adjust pool scaling factors
    scaling_factor_governor: str = betterproto.string_field(8)


@dataclass(eq=False, repr=False)
class MsgCreateStableswapPool(betterproto.Message):
    sender: str = betterproto.string_field(1)
    pool_params: "PoolParams" = betterproto.message_field(2)
    initial_pool_liquidity: List[
        "_____cosmos_base_v1_beta1__.Coin"
    ] = betterproto.message_field(3)
    future_pool_governor: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class MsgCreateStableswapPoolResponse(betterproto.Message):
    pool_id: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class MsgStableSwapAdjustScalingFactors(betterproto.Message):
    # Sender must be the pool's scaling_factor_governor in order for the tx to
    # succeed
    sender: str = betterproto.string_field(1)
    pool_id: int = betterproto.uint64_field(2)
    scaling_factors: List[int] = betterproto.uint64_field(3)


@dataclass(eq=False, repr=False)
class MsgStableSwapAdjustScalingFactorsResponse(betterproto.Message):
    pass


class MsgStub(betterproto.ServiceStub):
    async def create_stableswap_pool(
        self,
        *,
        sender: str = "",
        pool_params: "PoolParams" = None,
        initial_pool_liquidity: Optional[
            List["_____cosmos_base_v1_beta1__.Coin"]
        ] = None,
        future_pool_governor: str = ""
    ) -> "MsgCreateStableswapPoolResponse":
        initial_pool_liquidity = initial_pool_liquidity or []

        request = MsgCreateStableswapPool()
        request.sender = sender
        if pool_params is not None:
            request.pool_params = pool_params
        if initial_pool_liquidity is not None:
            request.initial_pool_liquidity = initial_pool_liquidity
        request.future_pool_governor = future_pool_governor

        return await self._unary_unary(
            "/osmosis.gamm.poolmodels.stableswap.v1beta1.Msg/CreateStableswapPool",
            request,
            MsgCreateStableswapPoolResponse,
        )

    async def stable_swap_adjust_scaling_factors(
        self,
        *,
        sender: str = "",
        pool_id: int = 0,
        scaling_factors: Optional[List[int]] = None
    ) -> "MsgStableSwapAdjustScalingFactorsResponse":
        scaling_factors = scaling_factors or []

        request = MsgStableSwapAdjustScalingFactors()
        request.sender = sender
        request.pool_id = pool_id
        request.scaling_factors = scaling_factors

        return await self._unary_unary(
            "/osmosis.gamm.poolmodels.stableswap.v1beta1.Msg/StableSwapAdjustScalingFactors",
            request,
            MsgStableSwapAdjustScalingFactorsResponse,
        )


class MsgBase(ServiceBase):
    async def create_stableswap_pool(
        self,
        sender: str,
        pool_params: "PoolParams",
        initial_pool_liquidity: Optional[List["_____cosmos_base_v1_beta1__.Coin"]],
        future_pool_governor: str,
    ) -> "MsgCreateStableswapPoolResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def stable_swap_adjust_scaling_factors(
        self, sender: str, pool_id: int, scaling_factors: Optional[List[int]]
    ) -> "MsgStableSwapAdjustScalingFactorsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_create_stableswap_pool(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "sender": request.sender,
            "pool_params": request.pool_params,
            "initial_pool_liquidity": request.initial_pool_liquidity,
            "future_pool_governor": request.future_pool_governor,
        }

        response = await self.create_stableswap_pool(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_stable_swap_adjust_scaling_factors(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "sender": request.sender,
            "pool_id": request.pool_id,
            "scaling_factors": request.scaling_factors,
        }

        response = await self.stable_swap_adjust_scaling_factors(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/osmosis.gamm.poolmodels.stableswap.v1beta1.Msg/CreateStableswapPool": grpclib.const.Handler(
                self.__rpc_create_stableswap_pool,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgCreateStableswapPool,
                MsgCreateStableswapPoolResponse,
            ),
            "/osmosis.gamm.poolmodels.stableswap.v1beta1.Msg/StableSwapAdjustScalingFactors": grpclib.const.Handler(
                self.__rpc_stable_swap_adjust_scaling_factors,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgStableSwapAdjustScalingFactors,
                MsgStableSwapAdjustScalingFactorsResponse,
            ),
        }


from ......cosmos.base import v1beta1 as _____cosmos_base_v1_beta1__
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: osmosis/incentives/gauge.proto, osmosis/incentives/genesis.proto, osmosis/incentives/params.proto, osmosis/incentives/query.proto, osmosis/incentives/tx.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import (
    datetime,
    timedelta,
)
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from ...cosmos.base import v1beta1 as __cosmos_base_v1_beta1__
from ...cosmos.base.query import v1beta1 as __cosmos_base_query_v1_beta1__
from .. import lockup as _lockup__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class Gauge(betterproto.Message):
    """
    Gauge is an object that stores and distributes yields to recipients who
    satisfy certain conditions. Currently gauges support conditions around the
    duration for which a given denom is locked.
    """

    id: int = betterproto.uint64_field(1)
    """id is the unique ID of a Gauge"""

    is_perpetual: bool = betterproto.bool_field(2)
    """
    is_perpetual is a flag to show if it's a perpetual or non-perpetual gauge
    Non-perpetual gauges distribute their tokens equally per epoch while the
    gauge is in the active period. Perpetual gauges distribute all their tokens
    at a single time and only distribute their tokens again once the gauge is
    refilled, Intended for use with incentives that get refilled daily.
    """

    distribute_to: "_lockup__.QueryCondition" = betterproto.message_field(3)
    """
    distribute_to is where the gauge rewards are distributed to. This is
    queried via lock duration or by timestamp
    """

    coins: List["__cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(4)
    """
    coins is the total amount of coins that have been in the gauge Can
    distribute multiple coin denoms
    """

    start_time: datetime = betterproto.message_field(5)
    """start_time is the distribution start time"""

    num_epochs_paid_over: int = betterproto.uint64_field(6)
    """
    num_epochs_paid_over is the number of total epochs distribution will be
    completed over
    """

    filled_epochs: int = betterproto.uint64_field(7)
    """
    filled_epochs is the number of epochs distribution has been completed on
    already
    """

    distributed_coins: List[
        "__cosmos_base_v1_beta1__.Coin"
    ] = betterproto.message_field(8)
    """distributed_coins are coins that have been distributed already"""


@dataclass(eq=False, repr=False)
class LockableDurationsInfo(betterproto.Message):
    lockable_durations: List[timedelta] = betterproto.message_field(1)
    """List of incentivised durations that gauges will pay out to"""


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params holds parameters for the incentives module"""

    distr_epoch_identifier: str = betterproto.string_field(1)
    """
    distr_epoch_identifier is what epoch type distribution will be triggered by
    (day, week, etc.)
    """


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """
    GenesisState defines the incentives module's various parameters when first
    initialized
    """

    params: "Params" = betterproto.message_field(1)
    """params are all the parameters of the module"""

    gauges: List["Gauge"] = betterproto.message_field(2)
    """gauges are all gauges that should exist at genesis"""

    lockable_durations: List[timedelta] = betterproto.message_field(3)
    """
    lockable_durations are all lockup durations that gauges can be locked for
    in order to recieve incentives
    """

    last_gauge_id: int = betterproto.uint64_field(4)
    """
    last_gauge_id is what the gauge number will increment from when creating
    the next gauge after genesis
    """


@dataclass(eq=False, repr=False)
class ModuleToDistributeCoinsRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class ModuleToDistributeCoinsResponse(betterproto.Message):
    coins: List["__cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(1)
    """Coins that have yet to be distributed"""


@dataclass(eq=False, repr=False)
class GaugeByIdRequest(betterproto.Message):
    id: int = betterproto.uint64_field(1)
    """Gague ID being queried"""


@dataclass(eq=False, repr=False)
class GaugeByIdResponse(betterproto.Message):
    gauge: "Gauge" = betterproto.message_field(1)
    """Gauge that corresponds to provided gague ID"""


@dataclass(eq=False, repr=False)
class GaugesRequest(betterproto.Message):
    pagination: "__cosmos_base_query_v1_beta1__.PageRequest" = (
        betterproto.message_field(1)
    )
    """Pagination defines pagination for the request"""


@dataclass(eq=False, repr=False)
class GaugesResponse(betterproto.Message):
    data: List["Gauge"] = betterproto.message_field(1)
    """Upcoming and active gauges"""

    pagination: "__cosmos_base_query_v1_beta1__.PageResponse" = (
        betterproto.message_field(2)
    )
    """Pagination defines pagination for the response"""


@dataclass(eq=False, repr=False)
class ActiveGaugesRequest(betterproto.Message):
    pagination: "__cosmos_base_query_v1_beta1__.PageRequest" = (
        betterproto.message_field(1)
    )
    """Pagination defines pagination for the request"""


@dataclass(eq=False, repr=False)
class ActiveGaugesResponse(betterproto.Message):
    data: List["Gauge"] = betterproto.message_field(1)
    """Active gagues only"""

    pagination: "__cosmos_base_query_v1_beta1__.PageResponse" = (
        betterproto.message_field(2)
    )
    """Pagination defines pagination for the response"""


@dataclass(eq=False, repr=False)
class ActiveGaugesPerDenomRequest(betterproto.Message):
    denom: str = betterproto.string_field(1)
    """Desired denom when querying active gagues"""

    pagination: "__cosmos_base_query_v1_beta1__.PageRequest" = (
        betterproto.message_field(2)
    )
    """Pagination defines pagination for the request"""


@dataclass(eq=False, repr=False)
class ActiveGaugesPerDenomResponse(betterproto.Message):
    data: List["Gauge"] = betterproto.message_field(1)
    """Active gagues that match denom in query"""

    pagination: "__cosmos_base_query_v1_beta1__.PageResponse" = (
        betterproto.message_field(2)
    )
    """Pagination defines pagination for the response"""


@dataclass(eq=False, repr=False)
class UpcomingGaugesRequest(betterproto.Message):
    pagination: "__cosmos_base_query_v1_beta1__.PageRequest" = (
        betterproto.message_field(1)
    )
    """Pagination defines pagination for the request"""


@dataclass(eq=False, repr=False)
class UpcomingGaugesResponse(betterproto.Message):
    data: List["Gauge"] = betterproto.message_field(1)
    """Gauges whose distribution is upcoming"""

    pagination: "__cosmos_base_query_v1_beta1__.PageResponse" = (
        betterproto.message_field(2)
    )
    """Pagination defines pagination for the response"""


@dataclass(eq=False, repr=False)
class UpcomingGaugesPerDenomRequest(betterproto.Message):
    denom: str = betterproto.string_field(1)
    """Filter for upcoming gagues that match specific denom"""

    pagination: "__cosmos_base_query_v1_beta1__.PageRequest" = (
        betterproto.message_field(2)
    )
    """Pagination defines pagination for the request"""


@dataclass(eq=False, repr=False)
class UpcomingGaugesPerDenomResponse(betterproto.Message):
    upcoming_gauges: List["Gauge"] = betterproto.message_field(1)
    """Upcoming gagues that match denom in query"""

    pagination: "__cosmos_base_query_v1_beta1__.PageResponse" = (
        betterproto.message_field(2)
    )
    """Pagination defines pagination for the response"""


@dataclass(eq=False, repr=False)
class RewardsEstRequest(betterproto.Message):
    owner: str = betterproto.string_field(1)
    """Address that is being queried for future estimated rewards"""

    lock_ids: List[int] = betterproto.uint64_field(2)
    """Lock IDs included in future reward estimation"""

    end_epoch: int = betterproto.int64_field(3)
    """Upper time limit of reward estimation Lower limit is current epoch"""


@dataclass(eq=False, repr=False)
class RewardsEstResponse(betterproto.Message):
    coins: List["__cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(1)
    """
    Estimated coin rewards that will be recieved at provided address from
    specified locks between current time and end epoch
    """


@dataclass(eq=False, repr=False)
class QueryLockableDurationsRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class QueryLockableDurationsResponse(betterproto.Message):
    lockable_durations: List[timedelta] = betterproto.message_field(1)
    """
    Time durations that users can lock coins for in order to recieve rewards
    """


@dataclass(eq=False, repr=False)
class MsgCreateGauge(betterproto.Message):
    """MsgCreateGauge creates a gague to distribute rewards to users"""

    is_perpetual: bool = betterproto.bool_field(1)
    """
    is_perpetual shows if it's a perpetual or non-perpetual gauge Non-perpetual
    gauges distribute their tokens equally per epoch while the gauge is in the
    active period. Perpetual gauges distribute all their tokens at a single
    time and only distribute their tokens again once the gauge is refilled
    """

    owner: str = betterproto.string_field(2)
    """owner is the address of gauge creator"""

    distribute_to: "_lockup__.QueryCondition" = betterproto.message_field(3)
    """
    distribute_to show which lock the gauge should distribute to by time
    duration or by timestamp
    """

    coins: List["__cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(4)
    """coins are coin(s) to be distributed by the gauge"""

    start_time: datetime = betterproto.message_field(5)
    """start_time is the distribution start time"""

    num_epochs_paid_over: int = betterproto.uint64_field(6)
    """
    num_epochs_paid_over is the number of epochs distribution will be completed
    over
    """


@dataclass(eq=False, repr=False)
class MsgCreateGaugeResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class MsgAddToGauge(betterproto.Message):
    """MsgAddToGauge adds coins to a previously created gauge"""

    owner: str = betterproto.string_field(1)
    """owner is the gauge owner's address"""

    gauge_id: int = betterproto.uint64_field(2)
    """gauge_id is the ID of gauge that rewards are getting added to"""

    rewards: List["__cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(3)
    """rewards are the coin(s) to add to gauge"""


@dataclass(eq=False, repr=False)
class MsgAddToGaugeResponse(betterproto.Message):
    pass


class QueryStub(betterproto.ServiceStub):
    async def module_to_distribute_coins(
        self,
        module_to_distribute_coins_request: "ModuleToDistributeCoinsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "ModuleToDistributeCoinsResponse":
        return await self._unary_unary(
            "/osmosis.incentives.Query/ModuleToDistributeCoins",
            module_to_distribute_coins_request,
            ModuleToDistributeCoinsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def gauge_by_id(
        self,
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "GaugeByIdResponse":
        return await self._unary_unary(
            "/osmosis.incentives.Query/GaugeByID",
            gauge_by_id_request,
            GaugeByIdResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def gauges(
        self,
        gauges_request: "GaugesRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "GaugesResponse":
        return await self._unary_unary(
            "/osmosis.incentives.Query/Gauges",
            gauges_request,
            GaugesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def active_gauges(
        self,
        active_gauges_request: "ActiveGaugesRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "ActiveGaugesResponse":
        return await self._unary_unary(
            "/osmosis.incentives.Query/ActiveGauges",
            active_gauges_request,
            ActiveGaugesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def active_gauges_per_denom(
        self,
        active_gauges_per_denom_request: "ActiveGaugesPerDenomRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "ActiveGaugesPerDenomResponse":
        return await self._unary_unary(
            "/osmosis.incentives.Query/ActiveGaugesPerDenom",
            active_gauges_per_denom_request,
            ActiveGaugesPerDenomResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def upcoming_gauges(
        self,
        upcoming_gauges_request: "UpcomingGaugesRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "UpcomingGaugesResponse":
        return await self._unary_unary(
            "/osmosis.incentives.Query/UpcomingGauges",
            upcoming_gauges_request,
            UpcomingGaugesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def upcoming_gauges_per_denom(
        self,
        upcoming_gauges_per_denom_request: "UpcomingGaugesPerDenomRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "UpcomingGaugesPerDenomResponse":
        return await self._unary_unary(
            "/osmosis.incentives.Query/UpcomingGaugesPerDenom",
            upcoming_gauges_per_denom_request,
            UpcomingGaugesPerDenomResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def rewards_est(
        self,
        rewards_est_request: "RewardsEstRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "RewardsEstResponse":
        return await self._unary_unary(
            "/osmosis.incentives.Query/RewardsEst",
            rewards_est_request,
            RewardsEstResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def lockable_durations(
        self,
        query_lockable_durations_request: "QueryLockableDurationsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryLockableDurationsResponse":
        return await self._unary_unary(
            "/osmosis.incentives.Query/LockableDurations",
            query_lockable_durations_request,
            QueryLockableDurationsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgStub(betterproto.ServiceStub):
    async def create_gauge(
        self,
        msg_create_gauge: "MsgCreateGauge",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgCreateGaugeResponse":
        return await self._unary_unary(
            "/osmosis.incentives.Msg/CreateGauge",
            msg_create_gauge,
            MsgCreateGaugeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def add_to_gauge(
        self,
        msg_add_to_gauge: "MsgAddToGauge",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgAddToGaugeResponse":
        return await self._unary_unary(
            "/osmosis.incentives.Msg/AddToGauge",
            msg_add_to_gauge,
            MsgAddToGaugeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def module_to_distribute_coins(
        self, module_to_distribute_coins_request: "ModuleToDistributeCoinsRequest"
    ) -> "ModuleToDistributeCoinsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def gauge_by_id(self) -> "GaugeByIdResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def gauges(self, gauges_request: "GaugesRequest") -> "GaugesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def active_gauges(
        self, active_gauges_request: "ActiveGaugesRequest"
    ) -> "ActiveGaugesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def active_gauges_per_denom(
        self, active_gauges_per_denom_request: "ActiveGaugesPerDenomRequest"
    ) -> "ActiveGaugesPerDenomResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def upcoming_gauges(
        self, upcoming_gauges_request: "UpcomingGaugesRequest"
    ) -> "UpcomingGaugesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def upcoming_gauges_per_denom(
        self, upcoming_gauges_per_denom_request: "UpcomingGaugesPerDenomRequest"
    ) -> "UpcomingGaugesPerDenomResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def rewards_est(
        self, rewards_est_request: "RewardsEstRequest"
    ) -> "RewardsEstResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def lockable_durations(
        self, query_lockable_durations_request: "QueryLockableDurationsRequest"
    ) -> "QueryLockableDurationsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_module_to_distribute_coins(
        self,
        stream: "grpclib.server.Stream[ModuleToDistributeCoinsRequest, ModuleToDistributeCoinsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.module_to_distribute_coins(request)
        await stream.send_message(response)

    async def __rpc_gauge_by_id(
        self, stream: "grpclib.server.Stream[GaugeByIdRequest, GaugeByIdResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.gauge_by_id(request)
        await stream.send_message(response)

    async def __rpc_gauges(
        self, stream: "grpclib.server.Stream[GaugesRequest, GaugesResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.gauges(request)
        await stream.send_message(response)

    async def __rpc_active_gauges(
        self, stream: "grpclib.server.Stream[ActiveGaugesRequest, ActiveGaugesResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.active_gauges(request)
        await stream.send_message(response)

    async def __rpc_active_gauges_per_denom(
        self,
        stream: "grpclib.server.Stream[ActiveGaugesPerDenomRequest, ActiveGaugesPerDenomResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.active_gauges_per_denom(request)
        await stream.send_message(response)

    async def __rpc_upcoming_gauges(
        self,
        stream: "grpclib.server.Stream[UpcomingGaugesRequest, UpcomingGaugesResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.upcoming_gauges(request)
        await stream.send_message(response)

    async def __rpc_upcoming_gauges_per_denom(
        self,
        stream: "grpclib.server.Stream[UpcomingGaugesPerDenomRequest, UpcomingGaugesPerDenomResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.upcoming_gauges_per_denom(request)
        await stream.send_message(response)

    async def __rpc_rewards_est(
        self, stream: "grpclib.server.Stream[RewardsEstRequest, RewardsEstResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.rewards_est(request)
        await stream.send_message(response)

    async def __rpc_lockable_durations(
        self,
        stream: "grpclib.server.Stream[QueryLockableDurationsRequest, QueryLockableDurationsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.lockable_durations(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/osmosis.incentives.Query/ModuleToDistributeCoins": grpclib.const.Handler(
                self.__rpc_module_to_distribute_coins,
                grpclib.const.Cardinality.UNARY_UNARY,
                ModuleToDistributeCoinsRequest,
                ModuleToDistributeCoinsResponse,
            ),
            "/osmosis.incentives.Query/GaugeByID": grpclib.const.Handler(
                self.__rpc_gauge_by_id,
                grpclib.const.Cardinality.UNARY_UNARY,
                GaugeByIdRequest,
                GaugeByIdResponse,
            ),
            "/osmosis.incentives.Query/Gauges": grpclib.const.Handler(
                self.__rpc_gauges,
                grpclib.const.Cardinality.UNARY_UNARY,
                GaugesRequest,
                GaugesResponse,
            ),
            "/osmosis.incentives.Query/ActiveGauges": grpclib.const.Handler(
                self.__rpc_active_gauges,
                grpclib.const.Cardinality.UNARY_UNARY,
                ActiveGaugesRequest,
                ActiveGaugesResponse,
            ),
            "/osmosis.incentives.Query/ActiveGaugesPerDenom": grpclib.const.Handler(
                self.__rpc_active_gauges_per_denom,
                grpclib.const.Cardinality.UNARY_UNARY,
                ActiveGaugesPerDenomRequest,
                ActiveGaugesPerDenomResponse,
            ),
            "/osmosis.incentives.Query/UpcomingGauges": grpclib.const.Handler(
                self.__rpc_upcoming_gauges,
                grpclib.const.Cardinality.UNARY_UNARY,
                UpcomingGaugesRequest,
                UpcomingGaugesResponse,
            ),
            "/osmosis.incentives.Query/UpcomingGaugesPerDenom": grpclib.const.Handler(
                self.__rpc_upcoming_gauges_per_denom,
                grpclib.const.Cardinality.UNARY_UNARY,
                UpcomingGaugesPerDenomRequest,
                UpcomingGaugesPerDenomResponse,
            ),
            "/osmosis.incentives.Query/RewardsEst": grpclib.const.Handler(
                self.__rpc_rewards_est,
                grpclib.const.Cardinality.UNARY_UNARY,
                RewardsEstRequest,
                RewardsEstResponse,
            ),
            "/osmosis.incentives.Query/LockableDurations": grpclib.const.Handler(
                self.__rpc_lockable_durations,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryLockableDurationsRequest,
                QueryLockableDurationsResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def create_gauge(
        self, msg_create_gauge: "MsgCreateGauge"
    ) -> "MsgCreateGaugeResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def add_to_gauge(
        self, msg_add_to_gauge: "MsgAddToGauge"
    ) -> "MsgAddToGaugeResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_create_gauge(
        self, stream: "grpclib.server.Stream[MsgCreateGauge, MsgCreateGaugeResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.create_gauge(request)
        await stream.send_message(response)

    async def __rpc_add_to_gauge(
        self, stream: "grpclib.server.Stream[MsgAddToGauge, MsgAddToGaugeResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.add_to_gauge(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/osmosis.incentives.Msg/CreateGauge": grpclib.const.Handler(
                self.__rpc_create_gauge,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgCreateGauge,
                MsgCreateGaugeResponse,
            ),
            "/osmosis.incentives.Msg/AddToGauge": grpclib.const.Handler(
                self.__rpc_add_to_gauge,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgAddToGauge,
                MsgAddToGaugeResponse,
            ),
        }

// @generated
/// Gauge is an object that stores and distributes yields to recipients who
/// satisfy certain conditions. Currently gauges support conditions around the
/// duration for which a given denom is locked.
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Gauge {
    /// id is the unique ID of a Gauge
    #[prost(uint64, tag="1")]
    pub id: u64,
    /// is_perpetual is a flag to show if it's a perpetual or non-perpetual gauge
    /// Non-perpetual gauges distribute their tokens equally per epoch while the
    /// gauge is in the active period. Perpetual gauges distribute all their tokens
    /// at a single time and only distribute their tokens again once the gauge is
    /// refilled, Intended for use with incentives that get refilled daily.
    #[prost(bool, tag="2")]
    pub is_perpetual: bool,
    /// distribute_to is where the gauge rewards are distributed to.
    /// This is queried via lock duration or by timestamp
    #[prost(message, optional, tag="3")]
    pub distribute_to: ::core::option::Option<super::lockup::QueryCondition>,
    /// coins is the total amount of coins that have been in the gauge
    /// Can distribute multiple coin denoms
    #[prost(message, repeated, tag="4")]
    pub coins: ::prost::alloc::vec::Vec<super::super::cosmos::base::v1beta1::Coin>,
    /// start_time is the distribution start time
    #[prost(message, optional, tag="5")]
    pub start_time: ::core::option::Option<::prost_types::Timestamp>,
    /// num_epochs_paid_over is the number of total epochs distribution will be
    /// completed over
    #[prost(uint64, tag="6")]
    pub num_epochs_paid_over: u64,
    /// filled_epochs is the number of epochs distribution has been completed on
    /// already
    #[prost(uint64, tag="7")]
    pub filled_epochs: u64,
    /// distributed_coins are coins that have been distributed already
    #[prost(message, repeated, tag="8")]
    pub distributed_coins: ::prost::alloc::vec::Vec<super::super::cosmos::base::v1beta1::Coin>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct LockableDurationsInfo {
    /// List of incentivised durations that gauges will pay out to
    #[prost(message, repeated, tag="1")]
    pub lockable_durations: ::prost::alloc::vec::Vec<::prost_types::Duration>,
}
/// Params holds parameters for the incentives module
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Params {
    /// distr_epoch_identifier is what epoch type distribution will be triggered by
    /// (day, week, etc.)
    #[prost(string, tag="1")]
    pub distr_epoch_identifier: ::prost::alloc::string::String,
}
/// GenesisState defines the incentives module's various parameters when first
/// initialized
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct GenesisState {
    /// params are all the parameters of the module
    #[prost(message, optional, tag="1")]
    pub params: ::core::option::Option<Params>,
    /// gauges are all gauges that should exist at genesis
    #[prost(message, repeated, tag="2")]
    pub gauges: ::prost::alloc::vec::Vec<Gauge>,
    /// lockable_durations are all lockup durations that gauges can be locked for
    /// in order to recieve incentives
    #[prost(message, repeated, tag="3")]
    pub lockable_durations: ::prost::alloc::vec::Vec<::prost_types::Duration>,
    /// last_gauge_id is what the gauge number will increment from when creating
    /// the next gauge after genesis
    #[prost(uint64, tag="4")]
    pub last_gauge_id: u64,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ModuleToDistributeCoinsRequest {
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ModuleToDistributeCoinsResponse {
    /// Coins that have yet to be distributed
    #[prost(message, repeated, tag="1")]
    pub coins: ::prost::alloc::vec::Vec<super::super::cosmos::base::v1beta1::Coin>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct GaugeByIdRequest {
    /// Gague ID being queried
    #[prost(uint64, tag="1")]
    pub id: u64,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct GaugeByIdResponse {
    /// Gauge that corresponds to provided gague ID
    #[prost(message, optional, tag="1")]
    pub gauge: ::core::option::Option<Gauge>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct GaugesRequest {
    /// Pagination defines pagination for the request
    #[prost(message, optional, tag="1")]
    pub pagination: ::core::option::Option<super::super::cosmos::base::query::v1beta1::PageRequest>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct GaugesResponse {
    /// Upcoming and active gauges
    #[prost(message, repeated, tag="1")]
    pub data: ::prost::alloc::vec::Vec<Gauge>,
    /// Pagination defines pagination for the response
    #[prost(message, optional, tag="2")]
    pub pagination: ::core::option::Option<super::super::cosmos::base::query::v1beta1::PageResponse>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ActiveGaugesRequest {
    /// Pagination defines pagination for the request
    #[prost(message, optional, tag="1")]
    pub pagination: ::core::option::Option<super::super::cosmos::base::query::v1beta1::PageRequest>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ActiveGaugesResponse {
    /// Active gagues only
    #[prost(message, repeated, tag="1")]
    pub data: ::prost::alloc::vec::Vec<Gauge>,
    /// Pagination defines pagination for the response
    #[prost(message, optional, tag="2")]
    pub pagination: ::core::option::Option<super::super::cosmos::base::query::v1beta1::PageResponse>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ActiveGaugesPerDenomRequest {
    /// Desired denom when querying active gagues
    #[prost(string, tag="1")]
    pub denom: ::prost::alloc::string::String,
    /// Pagination defines pagination for the request
    #[prost(message, optional, tag="2")]
    pub pagination: ::core::option::Option<super::super::cosmos::base::query::v1beta1::PageRequest>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ActiveGaugesPerDenomResponse {
    /// Active gagues that match denom in query
    #[prost(message, repeated, tag="1")]
    pub data: ::prost::alloc::vec::Vec<Gauge>,
    /// Pagination defines pagination for the response
    #[prost(message, optional, tag="2")]
    pub pagination: ::core::option::Option<super::super::cosmos::base::query::v1beta1::PageResponse>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct UpcomingGaugesRequest {
    /// Pagination defines pagination for the request
    #[prost(message, optional, tag="1")]
    pub pagination: ::core::option::Option<super::super::cosmos::base::query::v1beta1::PageRequest>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct UpcomingGaugesResponse {
    /// Gauges whose distribution is upcoming
    #[prost(message, repeated, tag="1")]
    pub data: ::prost::alloc::vec::Vec<Gauge>,
    /// Pagination defines pagination for the response
    #[prost(message, optional, tag="2")]
    pub pagination: ::core::option::Option<super::super::cosmos::base::query::v1beta1::PageResponse>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct UpcomingGaugesPerDenomRequest {
    /// Filter for upcoming gagues that match specific denom
    #[prost(string, tag="1")]
    pub denom: ::prost::alloc::string::String,
    /// Pagination defines pagination for the request
    #[prost(message, optional, tag="2")]
    pub pagination: ::core::option::Option<super::super::cosmos::base::query::v1beta1::PageRequest>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct UpcomingGaugesPerDenomResponse {
    /// Upcoming gagues that match denom in query
    #[prost(message, repeated, tag="1")]
    pub upcoming_gauges: ::prost::alloc::vec::Vec<Gauge>,
    /// Pagination defines pagination for the response
    #[prost(message, optional, tag="2")]
    pub pagination: ::core::option::Option<super::super::cosmos::base::query::v1beta1::PageResponse>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RewardsEstRequest {
    /// Address that is being queried for future estimated rewards
    #[prost(string, tag="1")]
    pub owner: ::prost::alloc::string::String,
    /// Lock IDs included in future reward estimation
    #[prost(uint64, repeated, tag="2")]
    pub lock_ids: ::prost::alloc::vec::Vec<u64>,
    /// Upper time limit of reward estimation
    /// Lower limit is current epoch
    #[prost(int64, tag="3")]
    pub end_epoch: i64,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RewardsEstResponse {
    /// Estimated coin rewards that will be recieved at provided address
    /// from specified locks between current time and end epoch
    #[prost(message, repeated, tag="1")]
    pub coins: ::prost::alloc::vec::Vec<super::super::cosmos::base::v1beta1::Coin>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct QueryLockableDurationsRequest {
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct QueryLockableDurationsResponse {
    /// Time durations that users can lock coins for in order to recieve rewards
    #[prost(message, repeated, tag="1")]
    pub lockable_durations: ::prost::alloc::vec::Vec<::prost_types::Duration>,
}
/// MsgCreateGauge creates a gague to distribute rewards to users
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct MsgCreateGauge {
    /// is_perpetual shows if it's a perpetual or non-perpetual gauge
    /// Non-perpetual gauges distribute their tokens equally per epoch while the
    /// gauge is in the active period. Perpetual gauges distribute all their tokens
    /// at a single time and only distribute their tokens again once the gauge is
    /// refilled
    #[prost(bool, tag="1")]
    pub is_perpetual: bool,
    /// owner is the address of gauge creator
    #[prost(string, tag="2")]
    pub owner: ::prost::alloc::string::String,
    /// distribute_to show which lock the gauge should distribute to by time
    /// duration or by timestamp
    #[prost(message, optional, tag="3")]
    pub distribute_to: ::core::option::Option<super::lockup::QueryCondition>,
    /// coins are coin(s) to be distributed by the gauge
    #[prost(message, repeated, tag="4")]
    pub coins: ::prost::alloc::vec::Vec<super::super::cosmos::base::v1beta1::Coin>,
    /// start_time is the distribution start time
    #[prost(message, optional, tag="5")]
    pub start_time: ::core::option::Option<::prost_types::Timestamp>,
    /// num_epochs_paid_over is the number of epochs distribution will be completed
    /// over
    #[prost(uint64, tag="6")]
    pub num_epochs_paid_over: u64,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct MsgCreateGaugeResponse {
}
/// MsgAddToGauge adds coins to a previously created gauge
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct MsgAddToGauge {
    /// owner is the gauge owner's address
    #[prost(string, tag="1")]
    pub owner: ::prost::alloc::string::String,
    /// gauge_id is the ID of gauge that rewards are getting added to
    #[prost(uint64, tag="2")]
    pub gauge_id: u64,
    /// rewards are the coin(s) to add to gauge
    #[prost(message, repeated, tag="3")]
    pub rewards: ::prost::alloc::vec::Vec<super::super::cosmos::base::v1beta1::Coin>,
}
#[allow(clippy::derive_partial_eq_without_eq)]
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct MsgAddToGaugeResponse {
}
// @@protoc_insertion_point(module)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: osmosis/tokenfactory/v1beta1/authorityMetadata.proto, osmosis/tokenfactory/v1beta1/genesis.proto, osmosis/tokenfactory/v1beta1/params.proto, osmosis/tokenfactory/v1beta1/query.proto, osmosis/tokenfactory/v1beta1/tx.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class DenomAuthorityMetadata(betterproto.Message):
    """
    DenomAuthorityMetadata specifies metadata for addresses that have specific
    capabilities over a token factory denom. Right now there is only one Admin
    permission, but is planned to be extended to the future.
    """

    # Can be empty for no admin, or a valid osmosis address
    admin: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params defines the parameters for the tokenfactory module."""

    denom_creation_fee: List[
        "___cosmos_base_v1_beta1__.Coin"
    ] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the tokenfactory module's genesis state."""

    # params defines the paramaters of the module.
    params: "Params" = betterproto.message_field(1)
    factory_denoms: List["GenesisDenom"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class GenesisDenom(betterproto.Message):
    """
    GenesisDenom defines a tokenfactory denom that is defined within genesis
    state. The structure contains DenomAuthorityMetadata which defines the
    denom's admin.
    """

    denom: str = betterproto.string_field(1)
    authority_metadata: "DenomAuthorityMetadata" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """
    QueryParamsRequest is the request type for the Query/Params RPC method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """
    QueryParamsResponse is the response type for the Query/Params RPC method.
    """

    # params defines the parameters of the module.
    params: "Params" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryDenomAuthorityMetadataRequest(betterproto.Message):
    """
    QueryDenomAuthorityMetadataRequest defines the request structure for the
    DenomAuthorityMetadata gRPC query.
    """

    denom: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryDenomAuthorityMetadataResponse(betterproto.Message):
    """
    QueryDenomAuthorityMetadataResponse defines the response structure for the
    DenomAuthorityMetadata gRPC query.
    """

    authority_metadata: "DenomAuthorityMetadata" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryDenomsFromCreatorRequest(betterproto.Message):
    """
    QueryDenomsFromCreatorRequest defines the request structure for the
    DenomsFromCreator gRPC query.
    """

    creator: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryDenomsFromCreatorResponse(betterproto.Message):
    """
    QueryDenomsFromCreatorRequest defines the response structure for the
    DenomsFromCreator gRPC query.
    """

    denoms: List[str] = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryBeforeSendHookAddressRequest(betterproto.Message):
    denom: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryBeforeSendHookAddressResponse(betterproto.Message):
    """
    QueryBeforeSendHookAddressResponse defines the response structure for the
    DenomBeforeSendHook gRPC query.
    """

    cosmwasm_address: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class MsgCreateDenom(betterproto.Message):
    """
    MsgCreateDenom defines the message structure for the CreateDenom gRPC
    service method. It allows an account to create a new denom. It requires a
    sender address and a sub denomination. The (sender_address,
    sub_denomination) tuple must be unique and cannot be re-used. The resulting
    denom created is defined as <factory/{creatorAddress}/{subdenom}>. The
    resulting denom's admin is originally set to be the creator, but this can
    be changed later. The token denom does not indicate the current admin.
    """

    sender: str = betterproto.string_field(1)
    # subdenom can be up to 44 "alphanumeric" characters long.
    subdenom: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class MsgCreateDenomResponse(betterproto.Message):
    """
    MsgCreateDenomResponse is the return value of MsgCreateDenom It returns the
    full string of the newly created denom
    """

    new_token_denom: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class MsgMint(betterproto.Message):
    """
    MsgMint is the sdk.Msg type for allowing an admin account to mint more of a
    token.  For now, we only support minting to the sender account
    """

    sender: str = betterproto.string_field(1)
    amount: "___cosmos_base_v1_beta1__.Coin" = betterproto.message_field(2)
    mint_to_address: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class MsgMintResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class MsgBurn(betterproto.Message):
    """
    MsgBurn is the sdk.Msg type for allowing an admin account to burn a token.
    For now, we only support burning from the sender account.
    """

    sender: str = betterproto.string_field(1)
    amount: "___cosmos_base_v1_beta1__.Coin" = betterproto.message_field(2)
    burn_from_address: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class MsgBurnResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class MsgChangeAdmin(betterproto.Message):
    """
    MsgChangeAdmin is the sdk.Msg type for allowing an admin account to
    reassign adminship of a denom to a new account
    """

    sender: str = betterproto.string_field(1)
    denom: str = betterproto.string_field(2)
    new_admin: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class MsgChangeAdminResponse(betterproto.Message):
    """
    MsgChangeAdminResponse defines the response structure for an executed
    MsgChangeAdmin message.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgSetBeforeSendHook(betterproto.Message):
    """
    MsgSetBeforeSendHook is the sdk.Msg type for allowing an admin account to
    assign a CosmWasm contract to call with a BeforeSend hook
    """

    sender: str = betterproto.string_field(1)
    denom: str = betterproto.string_field(2)
    cosmwasm_address: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class MsgSetBeforeSendHookResponse(betterproto.Message):
    """
    MsgSetBeforeSendHookResponse defines the response structure for an executed
    MsgSetBeforeSendHook message.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgSetDenomMetadata(betterproto.Message):
    """
    MsgSetDenomMetadata is the sdk.Msg type for allowing an admin account to
    set the denom's bank metadata
    """

    sender: str = betterproto.string_field(1)
    metadata: "___cosmos_bank_v1_beta1__.Metadata" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class MsgSetDenomMetadataResponse(betterproto.Message):
    """
    MsgSetDenomMetadataResponse defines the response structure for an executed
    MsgSetDenomMetadata message.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgForceTransfer(betterproto.Message):
    sender: str = betterproto.string_field(1)
    amount: "___cosmos_base_v1_beta1__.Coin" = betterproto.message_field(2)
    transfer_from_address: str = betterproto.string_field(3)
    transfer_to_address: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class MsgForceTransferResponse(betterproto.Message):
    pass


class QueryStub(betterproto.ServiceStub):
    async def params(self) -> "QueryParamsResponse":
        request = QueryParamsRequest()

        return await self._unary_unary(
            "/osmosis.tokenfactory.v1beta1.Query/Params", request, QueryParamsResponse
        )

    async def denom_authority_metadata(
        self, *, denom: str = ""
    ) -> "QueryDenomAuthorityMetadataResponse":
        request = QueryDenomAuthorityMetadataRequest()
        request.denom = denom

        return await self._unary_unary(
            "/osmosis.tokenfactory.v1beta1.Query/DenomAuthorityMetadata",
            request,
            QueryDenomAuthorityMetadataResponse,
        )

    async def denoms_from_creator(
        self, *, creator: str = ""
    ) -> "QueryDenomsFromCreatorResponse":
        request = QueryDenomsFromCreatorRequest()
        request.creator = creator

        return await self._unary_unary(
            "/osmosis.tokenfactory.v1beta1.Query/DenomsFromCreator",
            request,
            QueryDenomsFromCreatorResponse,
        )

    async def before_send_hook_address(
        self, *, denom: str = ""
    ) -> "QueryBeforeSendHookAddressResponse":
        request = QueryBeforeSendHookAddressRequest()
        request.denom = denom

        return await self._unary_unary(
            "/osmosis.tokenfactory.v1beta1.Query/BeforeSendHookAddress",
            request,
            QueryBeforeSendHookAddressResponse,
        )


class MsgStub(betterproto.ServiceStub):
    async def create_denom(
        self, *, sender: str = "", subdenom: str = ""
    ) -> "MsgCreateDenomResponse":
        request = MsgCreateDenom()
        request.sender = sender
        request.subdenom = subdenom

        return await self._unary_unary(
            "/osmosis.tokenfactory.v1beta1.Msg/CreateDenom",
            request,
            MsgCreateDenomResponse,
        )

    async def mint(
        self,
        *,
        sender: str = "",
        amount: "___cosmos_base_v1_beta1__.Coin" = None,
        mint_to_address: str = ""
    ) -> "MsgMintResponse":
        request = MsgMint()
        request.sender = sender
        if amount is not None:
            request.amount = amount
        request.mint_to_address = mint_to_address

        return await self._unary_unary(
            "/osmosis.tokenfactory.v1beta1.Msg/Mint", request, MsgMintResponse
        )

    async def burn(
        self,
        *,
        sender: str = "",
        amount: "___cosmos_base_v1_beta1__.Coin" = None,
        burn_from_address: str = ""
    ) -> "MsgBurnResponse":
        request = MsgBurn()
        request.sender = sender
        if amount is not None:
            request.amount = amount
        request.burn_from_address = burn_from_address

        return await self._unary_unary(
            "/osmosis.tokenfactory.v1beta1.Msg/Burn", request, MsgBurnResponse
        )

    async def change_admin(
        self, *, sender: str = "", denom: str = "", new_admin: str = ""
    ) -> "MsgChangeAdminResponse":
        request = MsgChangeAdmin()
        request.sender = sender
        request.denom = denom
        request.new_admin = new_admin

        return await self._unary_unary(
            "/osmosis.tokenfactory.v1beta1.Msg/ChangeAdmin",
            request,
            MsgChangeAdminResponse,
        )

    async def set_denom_metadata(
        self, *, sender: str = "", metadata: "___cosmos_bank_v1_beta1__.Metadata" = None
    ) -> "MsgSetDenomMetadataResponse":
        request = MsgSetDenomMetadata()
        request.sender = sender
        if metadata is not None:
            request.metadata = metadata

        return await self._unary_unary(
            "/osmosis.tokenfactory.v1beta1.Msg/SetDenomMetadata",
            request,
            MsgSetDenomMetadataResponse,
        )

    async def set_before_send_hook(
        self, *, sender: str = "", denom: str = "", cosmwasm_address: str = ""
    ) -> "MsgSetBeforeSendHookResponse":
        request = MsgSetBeforeSendHook()
        request.sender = sender
        request.denom = denom
        request.cosmwasm_address = cosmwasm_address

        return await self._unary_unary(
            "/osmosis.tokenfactory.v1beta1.Msg/SetBeforeSendHook",
            request,
            MsgSetBeforeSendHookResponse,
        )

    async def force_transfer(
        self,
        *,
        sender: str = "",
        amount: "___cosmos_base_v1_beta1__.Coin" = None,
        transfer_from_address: str = "",
        transfer_to_address: str = ""
    ) -> "MsgForceTransferResponse":
        request = MsgForceTransfer()
        request.sender = sender
        if amount is not None:
            request.amount = amount
        request.transfer_from_address = transfer_from_address
        request.transfer_to_address = transfer_to_address

        return await self._unary_unary(
            "/osmosis.tokenfactory.v1beta1.Msg/ForceTransfer",
            request,
            MsgForceTransferResponse,
        )


class QueryBase(ServiceBase):
    async def params(self) -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def denom_authority_metadata(
        self, denom: str
    ) -> "QueryDenomAuthorityMetadataResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def denoms_from_creator(
        self, creator: str
    ) -> "QueryDenomsFromCreatorResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def before_send_hook_address(
        self, denom: str
    ) -> "QueryBeforeSendHookAddressResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_params(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.params(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_denom_authority_metadata(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "denom": request.denom,
        }

        response = await self.denom_authority_metadata(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_denoms_from_creator(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "creator": request.creator,
        }

        response = await self.denoms_from_creator(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_before_send_hook_address(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "denom": request.denom,
        }

        response = await self.before_send_hook_address(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/osmosis.tokenfactory.v1beta1.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
            "/osmosis.tokenfactory.v1beta1.Query/DenomAuthorityMetadata": grpclib.const.Handler(
                self.__rpc_denom_authority_metadata,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryDenomAuthorityMetadataRequest,
                QueryDenomAuthorityMetadataResponse,
            ),
            "/osmosis.tokenfactory.v1beta1.Query/DenomsFromCreator": grpclib.const.Handler(
                self.__rpc_denoms_from_creator,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryDenomsFromCreatorRequest,
                QueryDenomsFromCreatorResponse,
            ),
            "/osmosis.tokenfactory.v1beta1.Query/BeforeSendHookAddress": grpclib.const.Handler(
                self.__rpc_before_send_hook_address,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryBeforeSendHookAddressRequest,
                QueryBeforeSendHookAddressResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def create_denom(
        self, sender: str, subdenom: str
    ) -> "MsgCreateDenomResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def mint(
        self,
        sender: str,
        amount: "___cosmos_base_v1_beta1__.Coin",
        mint_to_address: str,
    ) -> "MsgMintResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def burn(
        self,
        sender: str,
        amount: "___cosmos_base_v1_beta1__.Coin",
        burn_from_address: str,
    ) -> "MsgBurnResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def change_admin(
        self, sender: str, denom: str, new_admin: str
    ) -> "MsgChangeAdminResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def set_denom_metadata(
        self, sender: str, metadata: "___cosmos_bank_v1_beta1__.Metadata"
    ) -> "MsgSetDenomMetadataResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def set_before_send_hook(
        self, sender: str, denom: str, cosmwasm_address: str
    ) -> "MsgSetBeforeSendHookResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def force_transfer(
        self,
        sender: str,
        amount: "___cosmos_base_v1_beta1__.Coin",
        transfer_from_address: str,
        transfer_to_address: str,
    ) -> "MsgForceTransferResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_create_denom(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "sender": request.sender,
            "subdenom": request.subdenom,
        }

        response = await self.create_denom(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_mint(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "sender": request.sender,
            "amount": request.amount,
            "mint_to_address": request.mint_to_address,
        }

        response = await self.mint(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_burn(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "sender": request.sender,
            "amount": request.amount,
            "burn_from_address": request.burn_from_address,
        }

        response = await self.burn(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_change_admin(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "sender": request.sender,
            "denom": request.denom,
            "new_admin": request.new_admin,
        }

        response = await self.change_admin(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_set_denom_metadata(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "sender": request.sender,
            "metadata": request.metadata,
        }

        response = await self.set_denom_metadata(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_set_before_send_hook(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "sender": request.sender,
            "denom": request.denom,
            "cosmwasm_address": request.cosmwasm_address,
        }

        response = await self.set_before_send_hook(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_force_transfer(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "sender": request.sender,
            "amount": request.amount,
            "transfer_from_address": request.transfer_from_address,
            "transfer_to_address": request.transfer_to_address,
        }

        response = await self.force_transfer(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/osmosis.tokenfactory.v1beta1.Msg/CreateDenom": grpclib.const.Handler(
                self.__rpc_create_denom,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgCreateDenom,
                MsgCreateDenomResponse,
            ),
            "/osmosis.tokenfactory.v1beta1.Msg/Mint": grpclib.const.Handler(
                self.__rpc_mint,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgMint,
                MsgMintResponse,
            ),
            "/osmosis.tokenfactory.v1beta1.Msg/Burn": grpclib.const.Handler(
                self.__rpc_burn,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgBurn,
                MsgBurnResponse,
            ),
            "/osmosis.tokenfactory.v1beta1.Msg/ChangeAdmin": grpclib.const.Handler(
                self.__rpc_change_admin,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgChangeAdmin,
                MsgChangeAdminResponse,
            ),
            "/osmosis.tokenfactory.v1beta1.Msg/SetDenomMetadata": grpclib.const.Handler(
                self.__rpc_set_denom_metadata,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgSetDenomMetadata,
                MsgSetDenomMetadataResponse,
            ),
            "/osmosis.tokenfactory.v1beta1.Msg/SetBeforeSendHook": grpclib.const.Handler(
                self.__rpc_set_before_send_hook,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgSetBeforeSendHook,
                MsgSetBeforeSendHookResponse,
            ),
            "/osmosis.tokenfactory.v1beta1.Msg/ForceTransfer": grpclib.const.Handler(
                self.__rpc_force_transfer,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgForceTransfer,
                MsgForceTransferResponse,
            ),
        }


from ....cosmos.bank import v1beta1 as ___cosmos_bank_v1_beta1__
from ....cosmos.base import v1beta1 as ___cosmos_base_v1_beta1__

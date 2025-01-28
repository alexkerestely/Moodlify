# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import idm_pb2 as idm__pb2

GRPC_GENERATED_VERSION = '1.69.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in idm_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class AuthServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterUser = channel.unary_unary(
                '/com.POSproject.grpc.AuthService/RegisterUser',
                request_serializer=idm__pb2.RegisterRequest.SerializeToString,
                response_deserializer=idm__pb2.RegisterResponse.FromString,
                _registered_method=True)
        self.LoginUser = channel.unary_unary(
                '/com.POSproject.grpc.AuthService/LoginUser',
                request_serializer=idm__pb2.LoginRequest.SerializeToString,
                response_deserializer=idm__pb2.LoginResponse.FromString,
                _registered_method=True)
        self.CheckToken = channel.unary_unary(
                '/com.POSproject.grpc.AuthService/CheckToken',
                request_serializer=idm__pb2.CheckTokenRequest.SerializeToString,
                response_deserializer=idm__pb2.CheckTokenResponse.FromString,
                _registered_method=True)
        self.DestroyToken = channel.unary_unary(
                '/com.POSproject.grpc.AuthService/DestroyToken',
                request_serializer=idm__pb2.DestroyTokenRequest.SerializeToString,
                response_deserializer=idm__pb2.DestroyTokenResponse.FromString,
                _registered_method=True)


class AuthServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoginUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DestroyToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterUser': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterUser,
                    request_deserializer=idm__pb2.RegisterRequest.FromString,
                    response_serializer=idm__pb2.RegisterResponse.SerializeToString,
            ),
            'LoginUser': grpc.unary_unary_rpc_method_handler(
                    servicer.LoginUser,
                    request_deserializer=idm__pb2.LoginRequest.FromString,
                    response_serializer=idm__pb2.LoginResponse.SerializeToString,
            ),
            'CheckToken': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckToken,
                    request_deserializer=idm__pb2.CheckTokenRequest.FromString,
                    response_serializer=idm__pb2.CheckTokenResponse.SerializeToString,
            ),
            'DestroyToken': grpc.unary_unary_rpc_method_handler(
                    servicer.DestroyToken,
                    request_deserializer=idm__pb2.DestroyTokenRequest.FromString,
                    response_serializer=idm__pb2.DestroyTokenResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.POSproject.grpc.AuthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('com.POSproject.grpc.AuthService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AuthService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.POSproject.grpc.AuthService/RegisterUser',
            idm__pb2.RegisterRequest.SerializeToString,
            idm__pb2.RegisterResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def LoginUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.POSproject.grpc.AuthService/LoginUser',
            idm__pb2.LoginRequest.SerializeToString,
            idm__pb2.LoginResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CheckToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.POSproject.grpc.AuthService/CheckToken',
            idm__pb2.CheckTokenRequest.SerializeToString,
            idm__pb2.CheckTokenResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DestroyToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.POSproject.grpc.AuthService/DestroyToken',
            idm__pb2.DestroyTokenRequest.SerializeToString,
            idm__pb2.DestroyTokenResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

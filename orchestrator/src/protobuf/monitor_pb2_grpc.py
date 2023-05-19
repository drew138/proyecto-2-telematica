# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import monitor_pb2 as monitor__pb2


class MonitorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
                '/MonitorService/Ping',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=monitor__pb2.PingResponse.FromString,
                )
        self.GetMetrics = channel.unary_unary(
                '/MonitorService/GetMetrics',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=monitor__pb2.MetricResponse.FromString,
                )


class MonitorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMetrics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MonitorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=monitor__pb2.PingResponse.SerializeToString,
            ),
            'GetMetrics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMetrics,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=monitor__pb2.MetricResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MonitorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MonitorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MonitorService/Ping',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            monitor__pb2.PingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMetrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MonitorService/GetMetrics',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            monitor__pb2.MetricResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ssigmaapi.markethub.v1 import markethub_pb2 as ssigmaapi_dot_markethub_dot_v1_dot_markethub__pb2


class MarketHubServiceV1Stub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetTrades = channel.unary_stream(
        '/ssigmaapi.markethub.v1.MarketHubServiceV1/GetTrades',
        request_serializer=ssigmaapi_dot_markethub_dot_v1_dot_markethub__pb2.GetTradesRequest.SerializeToString,
        response_deserializer=ssigmaapi_dot_markethub_dot_v1_dot_markethub__pb2.GetTradesResponse.FromString,
        )
    self.GetOrderBooks = channel.unary_stream(
        '/ssigmaapi.markethub.v1.MarketHubServiceV1/GetOrderBooks',
        request_serializer=ssigmaapi_dot_markethub_dot_v1_dot_markethub__pb2.GetOrderBooksRequest.SerializeToString,
        response_deserializer=ssigmaapi_dot_markethub_dot_v1_dot_markethub__pb2.GetOrderBooksResponse.FromString,
        )
    self.GetTradesAndOrderBooks = channel.unary_stream(
        '/ssigmaapi.markethub.v1.MarketHubServiceV1/GetTradesAndOrderBooks',
        request_serializer=ssigmaapi_dot_markethub_dot_v1_dot_markethub__pb2.GetTradesAndOrderBooksRequest.SerializeToString,
        response_deserializer=ssigmaapi_dot_markethub_dot_v1_dot_markethub__pb2.GetTradesAndOrderBooksResponse.FromString,
        )


class MarketHubServiceV1Servicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetTrades(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetOrderBooks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTradesAndOrderBooks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MarketHubServiceV1Servicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetTrades': grpc.unary_stream_rpc_method_handler(
          servicer.GetTrades,
          request_deserializer=ssigmaapi_dot_markethub_dot_v1_dot_markethub__pb2.GetTradesRequest.FromString,
          response_serializer=ssigmaapi_dot_markethub_dot_v1_dot_markethub__pb2.GetTradesResponse.SerializeToString,
      ),
      'GetOrderBooks': grpc.unary_stream_rpc_method_handler(
          servicer.GetOrderBooks,
          request_deserializer=ssigmaapi_dot_markethub_dot_v1_dot_markethub__pb2.GetOrderBooksRequest.FromString,
          response_serializer=ssigmaapi_dot_markethub_dot_v1_dot_markethub__pb2.GetOrderBooksResponse.SerializeToString,
      ),
      'GetTradesAndOrderBooks': grpc.unary_stream_rpc_method_handler(
          servicer.GetTradesAndOrderBooks,
          request_deserializer=ssigmaapi_dot_markethub_dot_v1_dot_markethub__pb2.GetTradesAndOrderBooksRequest.FromString,
          response_serializer=ssigmaapi_dot_markethub_dot_v1_dot_markethub__pb2.GetTradesAndOrderBooksResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ssigmaapi.markethub.v1.MarketHubServiceV1', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

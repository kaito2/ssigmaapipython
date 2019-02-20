# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ssigmaapi/pashirirest/v1/pashirirest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ssigmaapi.type import market_pb2 as ssigmaapi_dot_type_dot_market__pb2
from ssigmaapi.type import orderbook_pb2 as ssigmaapi_dot_type_dot_orderbook__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ssigmaapi/pashirirest/v1/pashirirest.proto',
  package='ssigmaapi.pashirirest.v1',
  syntax='proto3',
  serialized_options=_b('Z8github.com/kaito2/ssigmaapigo/pashirirest/v1;pashirirest'),
  serialized_pb=_b('\n*ssigmaapi/pashirirest/v1/pashirirest.proto\x12\x18ssigmaapi.pashirirest.v1\x1a\x1bssigmaapi/type/market.proto\x1a\x1essigmaapi/type/orderbook.proto2]\n\x14PashiriRestServiceV1\x12\x45\n\x0cGetOrderBook\x12\x16.ssigmaapi.type.Market\x1a\x19.ssigmaapi.type.OrderBook\"\x00\x30\x01\x42:Z8github.com/kaito2/ssigmaapigo/pashirirest/v1;pashirirestb\x06proto3')
  ,
  dependencies=[ssigmaapi_dot_type_dot_market__pb2.DESCRIPTOR,ssigmaapi_dot_type_dot_orderbook__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_PASHIRIRESTSERVICEV1 = _descriptor.ServiceDescriptor(
  name='PashiriRestServiceV1',
  full_name='ssigmaapi.pashirirest.v1.PashiriRestServiceV1',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=133,
  serialized_end=226,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetOrderBook',
    full_name='ssigmaapi.pashirirest.v1.PashiriRestServiceV1.GetOrderBook',
    index=0,
    containing_service=None,
    input_type=ssigmaapi_dot_type_dot_market__pb2._MARKET,
    output_type=ssigmaapi_dot_type_dot_orderbook__pb2._ORDERBOOK,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PASHIRIRESTSERVICEV1)

DESCRIPTOR.services_by_name['PashiriRestServiceV1'] = _PASHIRIRESTSERVICEV1

# @@protoc_insertion_point(module_scope)
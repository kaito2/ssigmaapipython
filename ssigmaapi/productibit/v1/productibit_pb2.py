# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ssigmaapi/productibit/v1/productibit.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ssigmaapi.type import useractivity_pb2 as ssigmaapi_dot_type_dot_useractivity__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ssigmaapi/productibit/v1/productibit.proto',
  package='ssigmaapi.productibit.v1',
  syntax='proto3',
  serialized_options=_b('Z8github.com/kaito2/ssigmaapigo/productibit/v1;productibit'),
  serialized_pb=_b('\n*ssigmaapi/productibit/v1/productibit.proto\x12\x18ssigmaapi.productibit.v1\x1a!ssigmaapi/type/useractivity.proto\x1a\x1bgoogle/protobuf/empty.proto\"N\n\rSensorMessage\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x30\n\nactivities\x18\x02 \x03(\x0b\x32\x1c.ssigmaapi.type.UserActivity2i\n\x14ProductibitServiceV1\x12Q\n\x0cUploadSensor\x12\'.ssigmaapi.productibit.v1.SensorMessage\x1a\x16.google.protobuf.Empty\"\x00\x42:Z8github.com/kaito2/ssigmaapigo/productibit/v1;productibitb\x06proto3')
  ,
  dependencies=[ssigmaapi_dot_type_dot_useractivity__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_SENSORMESSAGE = _descriptor.Descriptor(
  name='SensorMessage',
  full_name='ssigmaapi.productibit.v1.SensorMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='ssigmaapi.productibit.v1.SensorMessage.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activities', full_name='ssigmaapi.productibit.v1.SensorMessage.activities', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=214,
)

_SENSORMESSAGE.fields_by_name['activities'].message_type = ssigmaapi_dot_type_dot_useractivity__pb2._USERACTIVITY
DESCRIPTOR.message_types_by_name['SensorMessage'] = _SENSORMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SensorMessage = _reflection.GeneratedProtocolMessageType('SensorMessage', (_message.Message,), dict(
  DESCRIPTOR = _SENSORMESSAGE,
  __module__ = 'ssigmaapi.productibit.v1.productibit_pb2'
  # @@protoc_insertion_point(class_scope:ssigmaapi.productibit.v1.SensorMessage)
  ))
_sym_db.RegisterMessage(SensorMessage)


DESCRIPTOR._options = None

_PRODUCTIBITSERVICEV1 = _descriptor.ServiceDescriptor(
  name='ProductibitServiceV1',
  full_name='ssigmaapi.productibit.v1.ProductibitServiceV1',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=216,
  serialized_end=321,
  methods=[
  _descriptor.MethodDescriptor(
    name='UploadSensor',
    full_name='ssigmaapi.productibit.v1.ProductibitServiceV1.UploadSensor',
    index=0,
    containing_service=None,
    input_type=_SENSORMESSAGE,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRODUCTIBITSERVICEV1)

DESCRIPTOR.services_by_name['ProductibitServiceV1'] = _PRODUCTIBITSERVICEV1

# @@protoc_insertion_point(module_scope)

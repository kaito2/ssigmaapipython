# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ssigmaapi/type/useractivity.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ssigmaapi/type/useractivity.proto',
  package='ssigmaapi.type',
  syntax='proto3',
  serialized_options=_b('Z<github.com/kaito2/ssigmaapigo/type/useractivity;useractivity'),
  serialized_pb=_b('\n!ssigmaapi/type/useractivity.proto\x12\x0essigmaapi.type\"\x8d\x02\n\x0cUserActivity\x12\x17\n\x0fstart_timestamp\x18\x01 \x01(\x03\x12\x15\n\rend_timestamp\x18\x02 \x01(\x03\x12\x35\n\x0ekeyboard_input\x18\x03 \x01(\x0b\x32\x1d.ssigmaapi.type.KeyboardInput\x12\x36\n\x0bwindow_list\x18\x04 \x03(\x0b\x32!.ssigmaapi.type.ApplicationWindow\x12:\n\nuser_state\x18\x05 \x01(\x0e\x32&.ssigmaapi.type.UserActivity.UserState\"\"\n\tUserState\x12\x0b\n\x07WORKING\x10\x00\x12\x08\n\x04\x41WAY\x10\x01\"%\n\rKeyboardInput\x12\x14\n\x0cstroke_count\x18\x01 \x01(\x03\"\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x03\x12\t\n\x01y\x18\x02 \x01(\x03\"\xcd\x02\n\x11\x41pplicationWindow\x12&\n\x07lefttop\x18\x01 \x01(\x0b\x32\x15.ssigmaapi.type.Point\x12\x0e\n\x06height\x18\x02 \x01(\x03\x12\r\n\x05width\x18\x03 \x01(\x03\x12\r\n\x05title\x18\x04 \x01(\t\x12\x14\n\x0cprogram_name\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x0f\n\x07\x63ompany\x18\x07 \x01(\t\x12\x15\n\ris_foreground\x18\x08 \x01(\x08\x12\x43\n\x0cwindow_state\x18\t \x01(\x0e\x32-.ssigmaapi.type.ApplicationWindow.WindowState\x12\x11\n\ttimestamp\x18\n \x01(\x03\"7\n\x0bWindowState\x12\n\n\x06NORMAL\x10\x00\x12\r\n\tMAXIMIZED\x10\x01\x12\r\n\tMINIMIZED\x10\x02\x42>Z<github.com/kaito2/ssigmaapigo/type/useractivity;useractivityb\x06proto3')
)



_USERACTIVITY_USERSTATE = _descriptor.EnumDescriptor(
  name='UserState',
  full_name='ssigmaapi.type.UserActivity.UserState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WORKING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AWAY', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=289,
  serialized_end=323,
)
_sym_db.RegisterEnumDescriptor(_USERACTIVITY_USERSTATE)

_APPLICATIONWINDOW_WINDOWSTATE = _descriptor.EnumDescriptor(
  name='WindowState',
  full_name='ssigmaapi.type.ApplicationWindow.WindowState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAXIMIZED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MINIMIZED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=674,
  serialized_end=729,
)
_sym_db.RegisterEnumDescriptor(_APPLICATIONWINDOW_WINDOWSTATE)


_USERACTIVITY = _descriptor.Descriptor(
  name='UserActivity',
  full_name='ssigmaapi.type.UserActivity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='ssigmaapi.type.UserActivity.start_timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_timestamp', full_name='ssigmaapi.type.UserActivity.end_timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyboard_input', full_name='ssigmaapi.type.UserActivity.keyboard_input', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='window_list', full_name='ssigmaapi.type.UserActivity.window_list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_state', full_name='ssigmaapi.type.UserActivity.user_state', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USERACTIVITY_USERSTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=323,
)


_KEYBOARDINPUT = _descriptor.Descriptor(
  name='KeyboardInput',
  full_name='ssigmaapi.type.KeyboardInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stroke_count', full_name='ssigmaapi.type.KeyboardInput.stroke_count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=325,
  serialized_end=362,
)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='ssigmaapi.type.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='ssigmaapi.type.Point.x', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='ssigmaapi.type.Point.y', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=364,
  serialized_end=393,
)


_APPLICATIONWINDOW = _descriptor.Descriptor(
  name='ApplicationWindow',
  full_name='ssigmaapi.type.ApplicationWindow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lefttop', full_name='ssigmaapi.type.ApplicationWindow.lefttop', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='ssigmaapi.type.ApplicationWindow.height', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='ssigmaapi.type.ApplicationWindow.width', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='ssigmaapi.type.ApplicationWindow.title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='program_name', full_name='ssigmaapi.type.ApplicationWindow.program_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='ssigmaapi.type.ApplicationWindow.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='company', full_name='ssigmaapi.type.ApplicationWindow.company', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_foreground', full_name='ssigmaapi.type.ApplicationWindow.is_foreground', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='window_state', full_name='ssigmaapi.type.ApplicationWindow.window_state', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ssigmaapi.type.ApplicationWindow.timestamp', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _APPLICATIONWINDOW_WINDOWSTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=396,
  serialized_end=729,
)

_USERACTIVITY.fields_by_name['keyboard_input'].message_type = _KEYBOARDINPUT
_USERACTIVITY.fields_by_name['window_list'].message_type = _APPLICATIONWINDOW
_USERACTIVITY.fields_by_name['user_state'].enum_type = _USERACTIVITY_USERSTATE
_USERACTIVITY_USERSTATE.containing_type = _USERACTIVITY
_APPLICATIONWINDOW.fields_by_name['lefttop'].message_type = _POINT
_APPLICATIONWINDOW.fields_by_name['window_state'].enum_type = _APPLICATIONWINDOW_WINDOWSTATE
_APPLICATIONWINDOW_WINDOWSTATE.containing_type = _APPLICATIONWINDOW
DESCRIPTOR.message_types_by_name['UserActivity'] = _USERACTIVITY
DESCRIPTOR.message_types_by_name['KeyboardInput'] = _KEYBOARDINPUT
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['ApplicationWindow'] = _APPLICATIONWINDOW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserActivity = _reflection.GeneratedProtocolMessageType('UserActivity', (_message.Message,), dict(
  DESCRIPTOR = _USERACTIVITY,
  __module__ = 'ssigmaapi.type.useractivity_pb2'
  # @@protoc_insertion_point(class_scope:ssigmaapi.type.UserActivity)
  ))
_sym_db.RegisterMessage(UserActivity)

KeyboardInput = _reflection.GeneratedProtocolMessageType('KeyboardInput', (_message.Message,), dict(
  DESCRIPTOR = _KEYBOARDINPUT,
  __module__ = 'ssigmaapi.type.useractivity_pb2'
  # @@protoc_insertion_point(class_scope:ssigmaapi.type.KeyboardInput)
  ))
_sym_db.RegisterMessage(KeyboardInput)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), dict(
  DESCRIPTOR = _POINT,
  __module__ = 'ssigmaapi.type.useractivity_pb2'
  # @@protoc_insertion_point(class_scope:ssigmaapi.type.Point)
  ))
_sym_db.RegisterMessage(Point)

ApplicationWindow = _reflection.GeneratedProtocolMessageType('ApplicationWindow', (_message.Message,), dict(
  DESCRIPTOR = _APPLICATIONWINDOW,
  __module__ = 'ssigmaapi.type.useractivity_pb2'
  # @@protoc_insertion_point(class_scope:ssigmaapi.type.ApplicationWindow)
  ))
_sym_db.RegisterMessage(ApplicationWindow)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

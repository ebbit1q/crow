# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: serverinfo_arrow.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import color_pb2 as color__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='serverinfo_arrow.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16serverinfo_arrow.proto\x1a\x0b\x63olor.proto\"\xc6\x01\n\x10ServerInfo_Arrow\x12\n\n\x02id\x18\x01 \x01(\x11\x12\x17\n\x0fstart_player_id\x18\x02 \x01(\x11\x12\x12\n\nstart_zone\x18\x03 \x01(\t\x12\x15\n\rstart_card_id\x18\x04 \x01(\x11\x12\x18\n\x10target_player_id\x18\x05 \x01(\x11\x12\x13\n\x0btarget_zone\x18\x06 \x01(\t\x12\x16\n\x0etarget_card_id\x18\x07 \x01(\x11\x12\x1b\n\x0b\x61rrow_color\x18\x08 \x01(\x0b\x32\x06.color'
  ,
  dependencies=[color__pb2.DESCRIPTOR,])




_SERVERINFO_ARROW = _descriptor.Descriptor(
  name='ServerInfo_Arrow',
  full_name='ServerInfo_Arrow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ServerInfo_Arrow.id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_player_id', full_name='ServerInfo_Arrow.start_player_id', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_zone', full_name='ServerInfo_Arrow.start_zone', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_card_id', full_name='ServerInfo_Arrow.start_card_id', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_player_id', full_name='ServerInfo_Arrow.target_player_id', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_zone', full_name='ServerInfo_Arrow.target_zone', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_card_id', full_name='ServerInfo_Arrow.target_card_id', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='arrow_color', full_name='ServerInfo_Arrow.arrow_color', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=238,
)

_SERVERINFO_ARROW.fields_by_name['arrow_color'].message_type = color__pb2._COLOR
DESCRIPTOR.message_types_by_name['ServerInfo_Arrow'] = _SERVERINFO_ARROW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerInfo_Arrow = _reflection.GeneratedProtocolMessageType('ServerInfo_Arrow', (_message.Message,), {
  'DESCRIPTOR' : _SERVERINFO_ARROW,
  '__module__' : 'serverinfo_arrow_pb2'
  # @@protoc_insertion_point(class_scope:ServerInfo_Arrow)
  })
_sym_db.RegisterMessage(ServerInfo_Arrow)


# @@protoc_insertion_point(module_scope)

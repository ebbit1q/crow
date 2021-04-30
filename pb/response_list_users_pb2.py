# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_list_users.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import response_pb2 as response__pb2
import serverinfo_user_pb2 as serverinfo__user__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_list_users.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19response_list_users.proto\x1a\x0eresponse.proto\x1a\x15serverinfo_user.proto\"g\n\x12Response_ListUsers\x12#\n\tuser_list\x18\x01 \x03(\x0b\x32\x10.ServerInfo_User2,\n\x03\x65xt\x12\t.Response\x18\xe9\x07 \x01(\x0b\x32\x13.Response_ListUsers'
  ,
  dependencies=[response__pb2.DESCRIPTOR,serverinfo__user__pb2.DESCRIPTOR,])




_RESPONSE_LISTUSERS = _descriptor.Descriptor(
  name='Response_ListUsers',
  full_name='Response_ListUsers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_list', full_name='Response_ListUsers.user_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Response_ListUsers.ext', index=0,
      number=1001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=68,
  serialized_end=171,
)

_RESPONSE_LISTUSERS.fields_by_name['user_list'].message_type = serverinfo__user__pb2._SERVERINFO_USER
DESCRIPTOR.message_types_by_name['Response_ListUsers'] = _RESPONSE_LISTUSERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Response_ListUsers = _reflection.GeneratedProtocolMessageType('Response_ListUsers', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE_LISTUSERS,
  '__module__' : 'response_list_users_pb2'
  # @@protoc_insertion_point(class_scope:Response_ListUsers)
  })
_sym_db.RegisterMessage(Response_ListUsers)

_RESPONSE_LISTUSERS.extensions_by_name['ext'].message_type = _RESPONSE_LISTUSERS
response__pb2.Response.RegisterExtension(_RESPONSE_LISTUSERS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
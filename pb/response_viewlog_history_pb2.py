# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_viewlog_history.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import response_pb2 as response__pb2
import serverinfo_chat_message_pb2 as serverinfo__chat__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_viewlog_history.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1eresponse_viewlog_history.proto\x1a\x0eresponse.proto\x1a\x1dserverinfo_chat_message.proto\"z\n\x17Response_ViewLogHistory\x12,\n\x0blog_message\x18\x01 \x03(\x0b\x32\x17.ServerInfo_ChatMessage21\n\x03\x65xt\x12\t.Response\x18\xf7\x07 \x01(\x0b\x32\x18.Response_ViewLogHistory'
  ,
  dependencies=[response__pb2.DESCRIPTOR,serverinfo__chat__message__pb2.DESCRIPTOR,])




_RESPONSE_VIEWLOGHISTORY = _descriptor.Descriptor(
  name='Response_ViewLogHistory',
  full_name='Response_ViewLogHistory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_message', full_name='Response_ViewLogHistory.log_message', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Response_ViewLogHistory.ext', index=0,
      number=1015, type=11, cpp_type=10, label=1,
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
  serialized_start=81,
  serialized_end=203,
)

_RESPONSE_VIEWLOGHISTORY.fields_by_name['log_message'].message_type = serverinfo__chat__message__pb2._SERVERINFO_CHATMESSAGE
DESCRIPTOR.message_types_by_name['Response_ViewLogHistory'] = _RESPONSE_VIEWLOGHISTORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Response_ViewLogHistory = _reflection.GeneratedProtocolMessageType('Response_ViewLogHistory', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE_VIEWLOGHISTORY,
  '__module__' : 'response_viewlog_history_pb2'
  # @@protoc_insertion_point(class_scope:Response_ViewLogHistory)
  })
_sym_db.RegisterMessage(Response_ViewLogHistory)

_RESPONSE_VIEWLOGHISTORY.extensions_by_name['ext'].message_type = _RESPONSE_VIEWLOGHISTORY
response__pb2.Response.RegisterExtension(_RESPONSE_VIEWLOGHISTORY.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
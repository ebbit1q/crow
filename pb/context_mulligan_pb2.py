# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: context_mulligan.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_event_context_pb2 as game__event__context__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='context_mulligan.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16\x63ontext_mulligan.proto\x1a\x18game_event_context.proto\"V\n\x10\x43ontext_Mulligan\x12\x0e\n\x06number\x18\x01 \x01(\r22\n\x03\x65xt\x12\x11.GameEventContext\x18\xed\x07 \x01(\x0b\x32\x11.Context_Mulligan'
  ,
  dependencies=[game__event__context__pb2.DESCRIPTOR,])




_CONTEXT_MULLIGAN = _descriptor.Descriptor(
  name='Context_Mulligan',
  full_name='Context_Mulligan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='Context_Mulligan.number', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Context_Mulligan.ext', index=0,
      number=1005, type=11, cpp_type=10, label=1,
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
  serialized_start=52,
  serialized_end=138,
)

DESCRIPTOR.message_types_by_name['Context_Mulligan'] = _CONTEXT_MULLIGAN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Context_Mulligan = _reflection.GeneratedProtocolMessageType('Context_Mulligan', (_message.Message,), {
  'DESCRIPTOR' : _CONTEXT_MULLIGAN,
  '__module__' : 'context_mulligan_pb2'
  # @@protoc_insertion_point(class_scope:Context_Mulligan)
  })
_sym_db.RegisterMessage(Context_Mulligan)

_CONTEXT_MULLIGAN.extensions_by_name['ext'].message_type = _CONTEXT_MULLIGAN
game__event__context__pb2.GameEventContext.RegisterExtension(_CONTEXT_MULLIGAN.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: context_concede.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_event_context_pb2 as game__event__context__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x63ontext_concede.proto\x1a\x18game_event_context.proto\"D\n\x0f\x43ontext_Concede21\n\x03\x65xt\x12\x11.GameEventContext\x18\xe9\x07 \x01(\x0b\x32\x10.Context_Concede\"H\n\x11\x43ontext_Unconcede23\n\x03\x65xt\x12\x11.GameEventContext\x18\xf1\x07 \x01(\x0b\x32\x12.Context_Unconcede')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'context_concede_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  game__event__context__pb2.GameEventContext.RegisterExtension(_CONTEXT_CONCEDE.extensions_by_name['ext'])
  game__event__context__pb2.GameEventContext.RegisterExtension(_CONTEXT_UNCONCEDE.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _CONTEXT_CONCEDE._serialized_start=51
  _CONTEXT_CONCEDE._serialized_end=119
  _CONTEXT_UNCONCEDE._serialized_start=121
  _CONTEXT_UNCONCEDE._serialized_end=193
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: event_destroy_card.proto
# Protobuf Python Version: 5.29.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    2,
    '',
    'event_destroy_card.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_event_pb2 as game__event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x65vent_destroy_card.proto\x1a\x10game_event.proto\"e\n\x11\x45vent_DestroyCard\x12\x11\n\tzone_name\x18\x01 \x01(\t\x12\x0f\n\x07\x63\x61rd_id\x18\x02 \x01(\r2,\n\x03\x65xt\x12\n.GameEvent\x18\xdb\x0f \x01(\x0b\x32\x12.Event_DestroyCard')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_destroy_card_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EVENT_DESTROYCARD']._serialized_start=46
  _globals['_EVENT_DESTROYCARD']._serialized_end=147
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: event_set_counter.proto
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
    'event_set_counter.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_event_pb2 as game__event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x65vent_set_counter.proto\x1a\x10game_event.proto\"b\n\x10\x45vent_SetCounter\x12\x12\n\ncounter_id\x18\x01 \x01(\x11\x12\r\n\x05value\x18\x02 \x01(\x11\x32+\n\x03\x65xt\x12\n.GameEvent\x18\xd3\x0f \x01(\x0b\x32\x11.Event_SetCounter')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_set_counter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EVENT_SETCOUNTER']._serialized_start=45
  _globals['_EVENT_SETCOUNTER']._serialized_end=143
# @@protoc_insertion_point(module_scope)

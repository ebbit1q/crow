# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: event_server_identification.proto
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
    'event_server_identification.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import session_event_pb2 as session__event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!event_server_identification.proto\x1a\x13session_event.proto\"\xa5\x02\n\x1a\x45vent_ServerIdentification\x12\x13\n\x0bserver_name\x18\x01 \x01(\t\x12\x16\n\x0eserver_version\x18\x02 \x01(\t\x12\x18\n\x10protocol_version\x18\x03 \x01(\r\x12L\n\x0eserver_options\x18\x04 \x01(\x0e\x32).Event_ServerIdentification.ServerOptions:\tNoOptions\"8\n\rServerOptions\x12\r\n\tNoOptions\x10\x00\x12\x18\n\x14SupportsPasswordHash\x10\x01\x32\x38\n\x03\x65xt\x12\r.SessionEvent\x18\xf4\x03 \x01(\x0b\x32\x1b.Event_ServerIdentification')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_server_identification_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EVENT_SERVERIDENTIFICATION']._serialized_start=59
  _globals['_EVENT_SERVERIDENTIFICATION']._serialized_end=352
  _globals['_EVENT_SERVERIDENTIFICATION_SERVEROPTIONS']._serialized_start=238
  _globals['_EVENT_SERVERIDENTIFICATION_SERVEROPTIONS']._serialized_end=294
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_server_shutdown.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import session_event_pb2 as session__event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x65vent_server_shutdown.proto\x1a\x13session_event.proto\"k\n\x14\x45vent_ServerShutdown\x12\x0e\n\x06reason\x18\x01 \x01(\t\x12\x0f\n\x07minutes\x18\x02 \x01(\r22\n\x03\x65xt\x12\r.SessionEvent\x18\xe9\x07 \x01(\x0b\x32\x15.Event_ServerShutdown')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_server_shutdown_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  session__event__pb2.SessionEvent.RegisterExtension(_EVENT_SERVERSHUTDOWN.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _EVENT_SERVERSHUTDOWN._serialized_start=52
  _EVENT_SERVERSHUTDOWN._serialized_end=159
# @@protoc_insertion_point(module_scope)

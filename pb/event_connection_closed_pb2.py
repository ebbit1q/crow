# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: event_connection_closed.proto
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
    'event_connection_closed.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import session_event_pb2 as session__event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x65vent_connection_closed.proto\x1a\x13session_event.proto\"\xcf\x02\n\x16\x45vent_ConnectionClosed\x12\x33\n\x06reason\x18\x01 \x01(\x0e\x32#.Event_ConnectionClosed.CloseReason\x12\x12\n\nreason_str\x18\x02 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\r\"\xa3\x01\n\x0b\x43loseReason\x12\t\n\x05OTHER\x10\x01\x12\x13\n\x0fSERVER_SHUTDOWN\x10\x02\x12\x18\n\x14TOO_MANY_CONNECTIONS\x10\x03\x12\n\n\x06\x42\x41NNED\x10\x04\x12\x13\n\x0fUSERNAMEINVALID\x10\x05\x12\x16\n\x12USER_LIMIT_REACHED\x10\x06\x12\x0b\n\x07\x44\x45MOTED\x10\x07\x12\x14\n\x10LOGGEDINELSEWERE\x10\x08\x32\x34\n\x03\x65xt\x12\r.SessionEvent\x18\xea\x07 \x01(\x0b\x32\x17.Event_ConnectionClosed')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_connection_closed_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EVENT_CONNECTIONCLOSED']._serialized_start=55
  _globals['_EVENT_CONNECTIONCLOSED']._serialized_end=390
  _globals['_EVENT_CONNECTIONCLOSED_CLOSEREASON']._serialized_start=173
  _globals['_EVENT_CONNECTIONCLOSED_CLOSEREASON']._serialized_end=336
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: event_notify_user.proto
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
    'event_notify_user.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import session_event_pb2 as session__event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x65vent_notify_user.proto\x1a\x13session_event.proto\"\x93\x02\n\x10\x45vent_NotifyUser\x12\x30\n\x04type\x18\x01 \x01(\x0e\x32\".Event_NotifyUser.NotificationType\x12\x16\n\x0ewarning_reason\x18\x02 \x01(\t\x12\x14\n\x0c\x63ustom_title\x18\x03 \x01(\t\x12\x16\n\x0e\x63ustom_content\x18\x04 \x01(\t\"W\n\x10NotificationType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08PROMOTED\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\x0f\n\x0bIDLEWARNING\x10\x03\x12\n\n\x06\x43USTOM\x10\x04\x32.\n\x03\x65xt\x12\r.SessionEvent\x18\xf2\x07 \x01(\x0b\x32\x11.Event_NotifyUser')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_notify_user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EVENT_NOTIFYUSER']._serialized_start=49
  _globals['_EVENT_NOTIFYUSER']._serialized_end=324
  _globals['_EVENT_NOTIFYUSER_NOTIFICATIONTYPE']._serialized_start=189
  _globals['_EVENT_NOTIFYUSER_NOTIFICATIONTYPE']._serialized_end=276
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: event_server_complete_list.proto
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
    'event_server_complete_list.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import session_event_pb2 as session__event__pb2
import serverinfo_user_pb2 as serverinfo__user__pb2
import serverinfo_room_pb2 as serverinfo__room__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n event_server_complete_list.proto\x1a\x13session_event.proto\x1a\x15serverinfo_user.proto\x1a\x15serverinfo_room.proto\"\xaf\x01\n\x18\x45vent_ServerCompleteList\x12\x11\n\tserver_id\x18\x01 \x01(\r\x12#\n\tuser_list\x18\x02 \x03(\x0b\x32\x10.ServerInfo_User\x12#\n\troom_list\x18\x03 \x03(\x0b\x32\x10.ServerInfo_Room26\n\x03\x65xt\x12\r.SessionEvent\x18\xd8\x04 \x01(\x0b\x32\x19.Event_ServerCompleteList')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_server_complete_list_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EVENT_SERVERCOMPLETELIST']._serialized_start=104
  _globals['_EVENT_SERVERCOMPLETELIST']._serialized_end=279
# @@protoc_insertion_point(module_scope)

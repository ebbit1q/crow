# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: serverinfo_playerproperties.proto
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
    'serverinfo_playerproperties.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import serverinfo_user_pb2 as serverinfo__user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!serverinfo_playerproperties.proto\x1a\x15serverinfo_user.proto\"\xe1\x01\n\x1bServerInfo_PlayerProperties\x12\x11\n\tplayer_id\x18\x01 \x01(\x11\x12#\n\tuser_info\x18\x02 \x01(\x0b\x32\x10.ServerInfo_User\x12\x11\n\tspectator\x18\x03 \x01(\x08\x12\x10\n\x08\x63onceded\x18\x04 \x01(\x08\x12\x13\n\x0bready_start\x18\x05 \x01(\x08\x12\x11\n\tdeck_hash\x18\x06 \x01(\t\x12\x14\n\x0cping_seconds\x18\x07 \x01(\x11\x12\x18\n\x10sideboard_locked\x18\x08 \x01(\x08\x12\r\n\x05judge\x18\t \x01(\x08')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'serverinfo_playerproperties_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SERVERINFO_PLAYERPROPERTIES']._serialized_start=61
  _globals['_SERVERINFO_PLAYERPROPERTIES']._serialized_end=286
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: serverinfo_player.proto
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
    'serverinfo_player.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import serverinfo_zone_pb2 as serverinfo__zone__pb2
import serverinfo_counter_pb2 as serverinfo__counter__pb2
import serverinfo_arrow_pb2 as serverinfo__arrow__pb2
import serverinfo_playerproperties_pb2 as serverinfo__playerproperties__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17serverinfo_player.proto\x1a\x15serverinfo_zone.proto\x1a\x18serverinfo_counter.proto\x1a\x16serverinfo_arrow.proto\x1a!serverinfo_playerproperties.proto\"\xcf\x01\n\x11ServerInfo_Player\x12\x30\n\nproperties\x18\x01 \x01(\x0b\x32\x1c.ServerInfo_PlayerProperties\x12\x11\n\tdeck_list\x18\x02 \x01(\t\x12#\n\tzone_list\x18\x03 \x03(\x0b\x32\x10.ServerInfo_Zone\x12)\n\x0c\x63ounter_list\x18\x04 \x03(\x0b\x32\x13.ServerInfo_Counter\x12%\n\narrow_list\x18\x05 \x03(\x0b\x32\x11.ServerInfo_Arrow')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'serverinfo_player_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SERVERINFO_PLAYER']._serialized_start=136
  _globals['_SERVERINFO_PLAYER']._serialized_end=343
# @@protoc_insertion_point(module_scope)

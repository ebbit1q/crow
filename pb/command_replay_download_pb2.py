# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: command_replay_download.proto
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
    'command_replay_download.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import session_commands_pb2 as session__commands__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63ommand_replay_download.proto\x1a\x16session_commands.proto\"g\n\x16\x43ommand_ReplayDownload\x12\x15\n\treplay_id\x18\x01 \x01(\x11:\x02-126\n\x03\x65xt\x12\x0f.SessionCommand\x18\xcd\x08 \x01(\x0b\x32\x17.Command_ReplayDownload')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'command_replay_download_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_COMMAND_REPLAYDOWNLOAD']._serialized_start=57
  _globals['_COMMAND_REPLAYDOWNLOAD']._serialized_end=160
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_replay_list.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import session_commands_pb2 as session__commands__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x63ommand_replay_list.proto\x1a\x16session_commands.proto\"H\n\x12\x43ommand_ReplayList22\n\x03\x65xt\x12\x0f.SessionCommand\x18\xcc\x08 \x01(\x0b\x32\x13.Command_ReplayList')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'command_replay_list_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  session__commands__pb2.SessionCommand.RegisterExtension(_COMMAND_REPLAYLIST.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _COMMAND_REPLAYLIST._serialized_start=53
  _COMMAND_REPLAYLIST._serialized_end=125
# @@protoc_insertion_point(module_scope)

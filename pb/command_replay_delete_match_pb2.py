# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_replay_delete_match.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import session_commands_pb2 as session__commands__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!command_replay_delete_match.proto\x1a\x16session_commands.proto\"k\n\x19\x43ommand_ReplayDeleteMatch\x12\x13\n\x07game_id\x18\x01 \x01(\x11:\x02-129\n\x03\x65xt\x12\x0f.SessionCommand\x18\xcf\x08 \x01(\x0b\x32\x1a.Command_ReplayDeleteMatch')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'command_replay_delete_match_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  session__commands__pb2.SessionCommand.RegisterExtension(_COMMAND_REPLAYDELETEMATCH.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _COMMAND_REPLAYDELETEMATCH._serialized_start=61
  _COMMAND_REPLAYDELETEMATCH._serialized_end=168
# @@protoc_insertion_point(module_scope)

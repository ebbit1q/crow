# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: command_kick_from_game.proto
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
    'command_kick_from_game.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_commands_pb2 as game__commands__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63ommand_kick_from_game.proto\x1a\x13game_commands.proto\"`\n\x14\x43ommand_KickFromGame\x12\x15\n\tplayer_id\x18\x01 \x01(\x11:\x02-121\n\x03\x65xt\x12\x0c.GameCommand\x18\xe8\x07 \x01(\x0b\x32\x15.Command_KickFromGame')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'command_kick_from_game_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_COMMAND_KICKFROMGAME']._serialized_start=53
  _globals['_COMMAND_KICKFROMGAME']._serialized_end=149
# @@protoc_insertion_point(module_scope)

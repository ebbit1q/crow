# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_roll_die.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_commands_pb2 as game__commands__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x63ommand_roll_die.proto\x1a\x13game_commands.proto\"]\n\x0f\x43ommand_RollDie\x12\r\n\x05sides\x18\x01 \x01(\r\x12\r\n\x05\x63ount\x18\x02 \x01(\r2,\n\x03\x65xt\x12\x0c.GameCommand\x18\xed\x07 \x01(\x0b\x32\x10.Command_RollDie')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'command_roll_die_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  game__commands__pb2.GameCommand.RegisterExtension(_COMMAND_ROLLDIE.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _COMMAND_ROLLDIE._serialized_start=47
  _COMMAND_ROLLDIE._serialized_end=140
# @@protoc_insertion_point(module_scope)

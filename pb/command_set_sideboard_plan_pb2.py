# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_set_sideboard_plan.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_commands_pb2 as game__commands__pb2
import move_card_to_zone_pb2 as move__card__to__zone__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n command_set_sideboard_plan.proto\x1a\x13game_commands.proto\x1a\x17move_card_to_zone.proto\"v\n\x18\x43ommand_SetSideboardPlan\x12#\n\tmove_list\x18\x01 \x03(\x0b\x32\x10.MoveCard_ToZone25\n\x03\x65xt\x12\x0c.GameCommand\x18\x84\x08 \x01(\x0b\x32\x19.Command_SetSideboardPlan')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'command_set_sideboard_plan_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  game__commands__pb2.GameCommand.RegisterExtension(_COMMAND_SETSIDEBOARDPLAN.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _COMMAND_SETSIDEBOARDPLAN._serialized_start=82
  _COMMAND_SETSIDEBOARDPLAN._serialized_end=200
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_deck_select.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_commands_pb2 as game__commands__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x63ommand_deck_select.proto\x1a\x13game_commands.proto\"h\n\x12\x43ommand_DeckSelect\x12\x0c\n\x04\x64\x65\x63k\x18\x01 \x01(\t\x12\x13\n\x07\x64\x65\x63k_id\x18\x02 \x01(\x11:\x02-12/\n\x03\x65xt\x12\x0c.GameCommand\x18\x85\x08 \x01(\x0b\x32\x13.Command_DeckSelect')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'command_deck_select_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  game__commands__pb2.GameCommand.RegisterExtension(_COMMAND_DECKSELECT.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _COMMAND_DECKSELECT._serialized_start=50
  _COMMAND_DECKSELECT._serialized_end=154
# @@protoc_insertion_point(module_scope)

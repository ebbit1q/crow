# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_reveal_cards.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_commands_pb2 as game__commands__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63ommand_reveal_cards.proto\x1a\x13game_commands.proto\"\xb9\x01\n\x13\x43ommand_RevealCards\x12\x11\n\tzone_name\x18\x01 \x01(\t\x12\x13\n\x07\x63\x61rd_id\x18\x02 \x03(\x11\x42\x02\x10\x00\x12\x15\n\tplayer_id\x18\x03 \x01(\x11:\x02-1\x12\x1a\n\x12grant_write_access\x18\x04 \x01(\x08\x12\x15\n\ttop_cards\x18\x05 \x01(\x11:\x02-120\n\x03\x65xt\x12\x0c.GameCommand\x18\x82\x08 \x01(\x0b\x32\x14.Command_RevealCards')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'command_reveal_cards_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  game__commands__pb2.GameCommand.RegisterExtension(_COMMAND_REVEALCARDS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _COMMAND_REVEALCARDS.fields_by_name['card_id']._options = None
  _COMMAND_REVEALCARDS.fields_by_name['card_id']._serialized_options = b'\020\000'
  _COMMAND_REVEALCARDS._serialized_start=52
  _COMMAND_REVEALCARDS._serialized_end=237
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_deck_download.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import session_commands_pb2 as session__commands__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x63ommand_deck_download.proto\x1a\x16session_commands.proto\"a\n\x14\x43ommand_DeckDownload\x12\x13\n\x07\x64\x65\x63k_id\x18\x01 \x01(\x11:\x02-124\n\x03\x65xt\x12\x0f.SessionCommand\x18\xf4\x07 \x01(\x0b\x32\x15.Command_DeckDownload')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'command_deck_download_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  session__commands__pb2.SessionCommand.RegisterExtension(_COMMAND_DECKDOWNLOAD.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _COMMAND_DECKDOWNLOAD._serialized_start=55
  _COMMAND_DECKDOWNLOAD._serialized_end=152
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: command_draw_cards.proto
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
    'command_draw_cards.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_commands_pb2 as game__commands__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x63ommand_draw_cards.proto\x1a\x13game_commands.proto\"S\n\x11\x43ommand_DrawCards\x12\x0e\n\x06number\x18\x01 \x01(\r2.\n\x03\x65xt\x12\x0c.GameCommand\x18\xee\x07 \x01(\x0b\x32\x12.Command_DrawCards')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'command_draw_cards_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_COMMAND_DRAWCARDS']._serialized_start=49
  _globals['_COMMAND_DRAWCARDS']._serialized_end=132
# @@protoc_insertion_point(module_scope)

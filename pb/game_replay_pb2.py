# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game_replay.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import serverinfo_game_pb2 as serverinfo__game__pb2
import game_event_container_pb2 as game__event__container__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11game_replay.proto\x1a\x15serverinfo_game.proto\x1a\x1agame_event_container.proto\"\x87\x01\n\nGameReplay\x12\x11\n\treplay_id\x18\x01 \x01(\x04\x12#\n\tgame_info\x18\x02 \x01(\x0b\x32\x10.ServerInfo_Game\x12\'\n\nevent_list\x18\x03 \x03(\x0b\x32\x13.GameEventContainer\x12\x18\n\x10\x64uration_seconds\x18\x04 \x01(\r')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'game_replay_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GAMEREPLAY._serialized_start=73
  _GAMEREPLAY._serialized_end=208
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_game_state_changed.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_event_pb2 as game__event__pb2
import serverinfo_player_pb2 as serverinfo__player__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x65vent_game_state_changed.proto\x1a\x10game_event.proto\x1a\x17serverinfo_player.proto\"\xd3\x01\n\x16\x45vent_GameStateChanged\x12\'\n\x0bplayer_list\x18\x01 \x03(\x0b\x32\x12.ServerInfo_Player\x12\x14\n\x0cgame_started\x18\x02 \x01(\x08\x12\x18\n\x10\x61\x63tive_player_id\x18\x03 \x01(\x11\x12\x14\n\x0c\x61\x63tive_phase\x18\x04 \x01(\x11\x12\x17\n\x0fseconds_elapsed\x18\x05 \x01(\r21\n\x03\x65xt\x12\n.GameEvent\x18\xed\x07 \x01(\x0b\x32\x17.Event_GameStateChanged')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_game_state_changed_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  game__event__pb2.GameEvent.RegisterExtension(_EVENT_GAMESTATECHANGED.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _EVENT_GAMESTATECHANGED._serialized_start=78
  _EVENT_GAMESTATECHANGED._serialized_end=289
# @@protoc_insertion_point(module_scope)

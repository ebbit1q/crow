# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_player_properties_changed.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_event_pb2 as game__event__pb2
import serverinfo_playerproperties_pb2 as serverinfo__playerproperties__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%event_player_properties_changed.proto\x1a\x10game_event.proto\x1a!serverinfo_playerproperties.proto\"\x92\x01\n\x1d\x45vent_PlayerPropertiesChanged\x12\x37\n\x11player_properties\x18\x01 \x01(\x0b\x32\x1c.ServerInfo_PlayerProperties28\n\x03\x65xt\x12\n.GameEvent\x18\xef\x07 \x01(\x0b\x32\x1e.Event_PlayerPropertiesChanged')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_player_properties_changed_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  game__event__pb2.GameEvent.RegisterExtension(_EVENT_PLAYERPROPERTIESCHANGED.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _EVENT_PLAYERPROPERTIESCHANGED._serialized_start=95
  _EVENT_PLAYERPROPERTIESCHANGED._serialized_end=241
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_join_room.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import room_event_pb2 as room__event__pb2
import serverinfo_user_pb2 as serverinfo__user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x65vent_join_room.proto\x1a\x10room_event.proto\x1a\x15serverinfo_user.proto\"`\n\x0e\x45vent_JoinRoom\x12#\n\tuser_info\x18\x01 \x01(\x0b\x32\x10.ServerInfo_User2)\n\x03\x65xt\x12\n.RoomEvent\x18\xe9\x07 \x01(\x0b\x32\x0f.Event_JoinRoom')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_join_room_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  room__event__pb2.RoomEvent.RegisterExtension(_EVENT_JOINROOM.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _EVENT_JOINROOM._serialized_start=66
  _EVENT_JOINROOM._serialized_end=162
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_roll_die.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_event_pb2 as game__event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x65vent_roll_die.proto\x1a\x10game_event.proto\"g\n\rEvent_RollDie\x12\r\n\x05sides\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r\x12\x0e\n\x06values\x18\x03 \x03(\r2(\n\x03\x65xt\x12\n.GameEvent\x18\xd8\x0f \x01(\x0b\x32\x0e.Event_RollDie')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_roll_die_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  game__event__pb2.GameEvent.RegisterExtension(_EVENT_ROLLDIE.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _EVENT_ROLLDIE._serialized_start=42
  _EVENT_ROLLDIE._serialized_end=145
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_flip_card.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_event_pb2 as game__event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x65vent_flip_card.proto\x1a\x10game_event.proto\"\x85\x01\n\x0e\x45vent_FlipCard\x12\x11\n\tzone_name\x18\x01 \x01(\t\x12\x0f\n\x07\x63\x61rd_id\x18\x02 \x01(\x11\x12\x11\n\tcard_name\x18\x03 \x01(\t\x12\x11\n\tface_down\x18\x04 \x01(\x08\x32)\n\x03\x65xt\x12\n.GameEvent\x18\xda\x0f \x01(\x0b\x32\x0f.Event_FlipCard')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_flip_card_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  game__event__pb2.GameEvent.RegisterExtension(_EVENT_FLIPCARD.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _EVENT_FLIPCARD._serialized_start=44
  _EVENT_FLIPCARD._serialized_end=177
# @@protoc_insertion_point(module_scope)

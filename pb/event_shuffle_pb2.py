# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_shuffle.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_event_pb2 as game__event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x65vent_shuffle.proto\x1a\x10game_event.proto\"o\n\rEvent_Shuffle\x12\x11\n\tzone_name\x18\x01 \x01(\t\x12\x10\n\x05start\x18\x02 \x01(\x11:\x01\x30\x12\x0f\n\x03\x65nd\x18\x03 \x01(\x11:\x02-12(\n\x03\x65xt\x12\n.GameEvent\x18\xd7\x0f \x01(\x0b\x32\x0e.Event_Shuffle')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_shuffle_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  game__event__pb2.GameEvent.RegisterExtension(_EVENT_SHUFFLE.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _EVENT_SHUFFLE._serialized_start=41
  _EVENT_SHUFFLE._serialized_end=152
# @@protoc_insertion_point(module_scope)

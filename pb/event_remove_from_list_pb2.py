# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_remove_from_list.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import session_event_pb2 as session__event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x65vent_remove_from_list.proto\x1a\x13session_event.proto\"p\n\x14\x45vent_RemoveFromList\x12\x11\n\tlist_name\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t22\n\x03\x65xt\x12\r.SessionEvent\x18\xee\x07 \x01(\x0b\x32\x15.Event_RemoveFromList')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_remove_from_list_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  session__event__pb2.SessionEvent.RegisterExtension(_EVENT_REMOVEFROMLIST.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _EVENT_REMOVEFROMLIST._serialized_start=53
  _EVENT_REMOVEFROMLIST._serialized_end=165
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_add_to_list.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import session_event_pb2 as session__event__pb2
import serverinfo_user_pb2 as serverinfo__user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x65vent_add_to_list.proto\x1a\x13session_event.proto\x1a\x15serverinfo_user.proto\"x\n\x0f\x45vent_AddToList\x12\x11\n\tlist_name\x18\x01 \x01(\t\x12#\n\tuser_info\x18\x02 \x01(\x0b\x32\x10.ServerInfo_User2-\n\x03\x65xt\x12\r.SessionEvent\x18\xed\x07 \x01(\x0b\x32\x10.Event_AddToList')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_add_to_list_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  session__event__pb2.SessionEvent.RegisterExtension(_EVENT_ADDTOLIST.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _EVENT_ADDTOLIST._serialized_start=71
  _EVENT_ADDTOLIST._serialized_end=191
# @@protoc_insertion_point(module_scope)

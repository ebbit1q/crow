# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_user_joined.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import session_event_pb2 as session__event__pb2
import serverinfo_user_pb2 as serverinfo__user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x65vent_user_joined.proto\x1a\x13session_event.proto\x1a\x15serverinfo_user.proto\"g\n\x10\x45vent_UserJoined\x12#\n\tuser_info\x18\x01 \x01(\x0b\x32\x10.ServerInfo_User2.\n\x03\x65xt\x12\r.SessionEvent\x18\xef\x07 \x01(\x0b\x32\x11.Event_UserJoined')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_user_joined_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  session__event__pb2.SessionEvent.RegisterExtension(_EVENT_USERJOINED.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _EVENT_USERJOINED._serialized_start=71
  _EVENT_USERJOINED._serialized_end=174
# @@protoc_insertion_point(module_scope)

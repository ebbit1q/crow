# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_leave.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_event_pb2 as game__event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x65vent_leave.proto\x1a\x10game_event.proto\"\xb0\x01\n\x0b\x45vent_Leave\x12(\n\x06reason\x18\x01 \x01(\x0e\x32\x18.Event_Leave.LeaveReason\"O\n\x0bLeaveReason\x12\t\n\x05OTHER\x10\x01\x12\x0f\n\x0bUSER_KICKED\x10\x02\x12\r\n\tUSER_LEFT\x10\x03\x12\x15\n\x11USER_DISCONNECTED\x10\x04\x32&\n\x03\x65xt\x12\n.GameEvent\x18\xe9\x07 \x01(\x0b\x32\x0c.Event_Leave')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_leave_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  game__event__pb2.GameEvent.RegisterExtension(_EVENT_LEAVE.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _EVENT_LEAVE._serialized_start=40
  _EVENT_LEAVE._serialized_end=216
  _EVENT_LEAVE_LEAVEREASON._serialized_start=97
  _EVENT_LEAVE_LEAVEREASON._serialized_end=176
# @@protoc_insertion_point(module_scope)

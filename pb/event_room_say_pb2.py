# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: event_room_say.proto
# Protobuf Python Version: 5.29.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    2,
    '',
    'event_room_say.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import room_event_pb2 as room__event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x65vent_room_say.proto\x1a\x10room_event.proto\"\xe1\x01\n\rEvent_RoomSay\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x34\n\x0cmessage_type\x18\x03 \x01(\x0e\x32\x1e.Event_RoomSay.RoomMessageType\x12\x0f\n\x07time_of\x18\x04 \x01(\x04\"@\n\x0fRoomMessageType\x12\x0f\n\x0bUserMessage\x10\x00\x12\x0b\n\x07Welcome\x10\x01\x12\x0f\n\x0b\x43hatHistory\x10\x02\x32(\n\x03\x65xt\x12\n.RoomEvent\x18\xea\x07 \x01(\x0b\x32\x0e.Event_RoomSay')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_room_say_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EVENT_ROOMSAY']._serialized_start=43
  _globals['_EVENT_ROOMSAY']._serialized_end=268
  _globals['_EVENT_ROOMSAY_ROOMMESSAGETYPE']._serialized_start=162
  _globals['_EVENT_ROOMSAY_ROOMMESSAGETYPE']._serialized_end=226
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: isl_message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import response_pb2 as response__pb2
import session_event_pb2 as session__event__pb2
import commands_pb2 as commands__pb2
import game_event_container_pb2 as game__event__container__pb2
import room_event_pb2 as room__event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11isl_message.proto\x1a\x0eresponse.proto\x1a\x13session_event.proto\x1a\x0e\x63ommands.proto\x1a\x1agame_event_container.proto\x1a\x10room_event.proto\"\xe5\x03\n\nIslMessage\x12-\n\x0cmessage_type\x18\x01 \x01(\x0e\x32\x17.IslMessage.MessageType\x12\x12\n\nsession_id\x18\t \x01(\x04\x12\x15\n\tplayer_id\x18\n \x01(\x11:\x02-1\x12\'\n\x0cgame_command\x18\x64 \x01(\x0b\x32\x11.CommandContainer\x12\'\n\x0croom_command\x18\x65 \x01(\x0b\x32\x11.CommandContainer\x12\x1c\n\x08response\x18\xc8\x01 \x01(\x0b\x32\t.Response\x12%\n\rsession_event\x18\xc9\x01 \x01(\x0b\x32\r.SessionEvent\x12\x32\n\x14game_event_container\x18\xca\x01 \x01(\x0b\x32\x13.GameEventContainer\x12\x1f\n\nroom_event\x18\xcb\x01 \x01(\x0b\x32\n.RoomEvent\"\x90\x01\n\x0bMessageType\x12\x1a\n\x16GAME_COMMAND_CONTAINER\x10\x00\x12\x1a\n\x16ROOM_COMMAND_CONTAINER\x10\x01\x12\x0c\n\x08RESPONSE\x10\n\x12\x11\n\rSESSION_EVENT\x10\x0b\x12\x18\n\x14GAME_EVENT_CONTAINER\x10\x0c\x12\x0e\n\nROOM_EVENT\x10\r')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'isl_message_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ISLMESSAGE._serialized_start=121
  _ISLMESSAGE._serialized_end=606
  _ISLMESSAGE_MESSAGETYPE._serialized_start=462
  _ISLMESSAGE_MESSAGETYPE._serialized_end=606
# @@protoc_insertion_point(module_scope)

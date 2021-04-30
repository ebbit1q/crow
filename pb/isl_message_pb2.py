# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: isl_message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import response_pb2 as response__pb2
import session_event_pb2 as session__event__pb2
import commands_pb2 as commands__pb2
import game_event_container_pb2 as game__event__container__pb2
import room_event_pb2 as room__event__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='isl_message.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11isl_message.proto\x1a\x0eresponse.proto\x1a\x13session_event.proto\x1a\x0e\x63ommands.proto\x1a\x1agame_event_container.proto\x1a\x10room_event.proto\"\xe5\x03\n\nIslMessage\x12-\n\x0cmessage_type\x18\x01 \x01(\x0e\x32\x17.IslMessage.MessageType\x12\x12\n\nsession_id\x18\t \x01(\x04\x12\x15\n\tplayer_id\x18\n \x01(\x11:\x02-1\x12\'\n\x0cgame_command\x18\x64 \x01(\x0b\x32\x11.CommandContainer\x12\'\n\x0croom_command\x18\x65 \x01(\x0b\x32\x11.CommandContainer\x12\x1c\n\x08response\x18\xc8\x01 \x01(\x0b\x32\t.Response\x12%\n\rsession_event\x18\xc9\x01 \x01(\x0b\x32\r.SessionEvent\x12\x32\n\x14game_event_container\x18\xca\x01 \x01(\x0b\x32\x13.GameEventContainer\x12\x1f\n\nroom_event\x18\xcb\x01 \x01(\x0b\x32\n.RoomEvent\"\x90\x01\n\x0bMessageType\x12\x1a\n\x16GAME_COMMAND_CONTAINER\x10\x00\x12\x1a\n\x16ROOM_COMMAND_CONTAINER\x10\x01\x12\x0c\n\x08RESPONSE\x10\n\x12\x11\n\rSESSION_EVENT\x10\x0b\x12\x18\n\x14GAME_EVENT_CONTAINER\x10\x0c\x12\x0e\n\nROOM_EVENT\x10\r'
  ,
  dependencies=[response__pb2.DESCRIPTOR,session__event__pb2.DESCRIPTOR,commands__pb2.DESCRIPTOR,game__event__container__pb2.DESCRIPTOR,room__event__pb2.DESCRIPTOR,])



_ISLMESSAGE_MESSAGETYPE = _descriptor.EnumDescriptor(
  name='MessageType',
  full_name='IslMessage.MessageType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GAME_COMMAND_CONTAINER', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOM_COMMAND_CONTAINER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESPONSE', index=2, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SESSION_EVENT', index=3, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GAME_EVENT_CONTAINER', index=4, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOM_EVENT', index=5, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=462,
  serialized_end=606,
)
_sym_db.RegisterEnumDescriptor(_ISLMESSAGE_MESSAGETYPE)


_ISLMESSAGE = _descriptor.Descriptor(
  name='IslMessage',
  full_name='IslMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_type', full_name='IslMessage.message_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='IslMessage.session_id', index=1,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='IslMessage.player_id', index=2,
      number=10, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='game_command', full_name='IslMessage.game_command', index=3,
      number=100, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='room_command', full_name='IslMessage.room_command', index=4,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response', full_name='IslMessage.response', index=5,
      number=200, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_event', full_name='IslMessage.session_event', index=6,
      number=201, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='game_event_container', full_name='IslMessage.game_event_container', index=7,
      number=202, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='room_event', full_name='IslMessage.room_event', index=8,
      number=203, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ISLMESSAGE_MESSAGETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=606,
)

_ISLMESSAGE.fields_by_name['message_type'].enum_type = _ISLMESSAGE_MESSAGETYPE
_ISLMESSAGE.fields_by_name['game_command'].message_type = commands__pb2._COMMANDCONTAINER
_ISLMESSAGE.fields_by_name['room_command'].message_type = commands__pb2._COMMANDCONTAINER
_ISLMESSAGE.fields_by_name['response'].message_type = response__pb2._RESPONSE
_ISLMESSAGE.fields_by_name['session_event'].message_type = session__event__pb2._SESSIONEVENT
_ISLMESSAGE.fields_by_name['game_event_container'].message_type = game__event__container__pb2._GAMEEVENTCONTAINER
_ISLMESSAGE.fields_by_name['room_event'].message_type = room__event__pb2._ROOMEVENT
_ISLMESSAGE_MESSAGETYPE.containing_type = _ISLMESSAGE
DESCRIPTOR.message_types_by_name['IslMessage'] = _ISLMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IslMessage = _reflection.GeneratedProtocolMessageType('IslMessage', (_message.Message,), {
  'DESCRIPTOR' : _ISLMESSAGE,
  '__module__' : 'isl_message_pb2'
  # @@protoc_insertion_point(class_scope:IslMessage)
  })
_sym_db.RegisterMessage(IslMessage)


# @@protoc_insertion_point(module_scope)

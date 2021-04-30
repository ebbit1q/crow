# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_get_games_of_user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import response_pb2 as response__pb2
import serverinfo_game_pb2 as serverinfo__game__pb2
import serverinfo_room_pb2 as serverinfo__room__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_get_games_of_user.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n response_get_games_of_user.proto\x1a\x0eresponse.proto\x1a\x15serverinfo_game.proto\x1a\x15serverinfo_room.proto\"\x96\x01\n\x17Response_GetGamesOfUser\x12#\n\troom_list\x18\x01 \x03(\x0b\x32\x10.ServerInfo_Room\x12#\n\tgame_list\x18\x02 \x03(\x0b\x32\x10.ServerInfo_Game21\n\x03\x65xt\x12\t.Response\x18\xea\x07 \x01(\x0b\x32\x18.Response_GetGamesOfUser'
  ,
  dependencies=[response__pb2.DESCRIPTOR,serverinfo__game__pb2.DESCRIPTOR,serverinfo__room__pb2.DESCRIPTOR,])




_RESPONSE_GETGAMESOFUSER = _descriptor.Descriptor(
  name='Response_GetGamesOfUser',
  full_name='Response_GetGamesOfUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='room_list', full_name='Response_GetGamesOfUser.room_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='game_list', full_name='Response_GetGamesOfUser.game_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Response_GetGamesOfUser.ext', index=0,
      number=1002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=249,
)

_RESPONSE_GETGAMESOFUSER.fields_by_name['room_list'].message_type = serverinfo__room__pb2._SERVERINFO_ROOM
_RESPONSE_GETGAMESOFUSER.fields_by_name['game_list'].message_type = serverinfo__game__pb2._SERVERINFO_GAME
DESCRIPTOR.message_types_by_name['Response_GetGamesOfUser'] = _RESPONSE_GETGAMESOFUSER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Response_GetGamesOfUser = _reflection.GeneratedProtocolMessageType('Response_GetGamesOfUser', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE_GETGAMESOFUSER,
  '__module__' : 'response_get_games_of_user_pb2'
  # @@protoc_insertion_point(class_scope:Response_GetGamesOfUser)
  })
_sym_db.RegisterMessage(Response_GetGamesOfUser)

_RESPONSE_GETGAMESOFUSER.extensions_by_name['ext'].message_type = _RESPONSE_GETGAMESOFUSER
response__pb2.Response.RegisterExtension(_RESPONSE_GETGAMESOFUSER.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)

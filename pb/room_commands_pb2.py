# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: room_commands.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13room_commands.proto\"l\n\x0bRoomCommand\"S\n\x0fRoomCommandType\x12\x0f\n\nLEAVE_ROOM\x10\xe8\x07\x12\r\n\x08ROOM_SAY\x10\xe9\x07\x12\x10\n\x0b\x43REATE_GAME\x10\xea\x07\x12\x0e\n\tJOIN_GAME\x10\xeb\x07*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"C\n\x11\x43ommand_LeaveRoom2.\n\x03\x65xt\x12\x0c.RoomCommand\x18\xe8\x07 \x01(\x0b\x32\x12.Command_LeaveRoom\"P\n\x0f\x43ommand_RoomSay\x12\x0f\n\x07message\x18\x01 \x01(\t2,\n\x03\x65xt\x12\x0c.RoomCommand\x18\xe9\x07 \x01(\x0b\x32\x10.Command_RoomSay\"\x94\x03\n\x12\x43ommand_CreateGame\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x13\n\x0bmax_players\x18\x03 \x01(\r\x12\x14\n\x0conly_buddies\x18\x04 \x01(\x08\x12\x17\n\x0fonly_registered\x18\x05 \x01(\x08\x12\x1a\n\x12spectators_allowed\x18\x06 \x01(\x08\x12 \n\x18spectators_need_password\x18\x07 \x01(\x08\x12\x1b\n\x13spectators_can_talk\x18\x08 \x01(\x08\x12!\n\x19spectators_see_everything\x18\t \x01(\x08\x12\x15\n\rgame_type_ids\x18\n \x03(\r\x12\x15\n\rjoin_as_judge\x18\x0b \x01(\x08\x12\x19\n\x11join_as_spectator\x18\x0c \x01(\x08\x12\x1b\n\x13starting_life_total\x18\r \x01(\r2/\n\x03\x65xt\x12\x0c.RoomCommand\x18\xea\x07 \x01(\x0b\x32\x13.Command_CreateGame\"\xb1\x01\n\x10\x43ommand_JoinGame\x12\x13\n\x07game_id\x18\x01 \x01(\x11:\x02-1\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x11\n\tspectator\x18\x03 \x01(\x08\x12\x1d\n\x15override_restrictions\x18\x04 \x01(\x08\x12\x15\n\rjoin_as_judge\x18\x05 \x01(\x08\x32-\n\x03\x65xt\x12\x0c.RoomCommand\x18\xeb\x07 \x01(\x0b\x32\x11.Command_JoinGame')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'room_commands_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  RoomCommand.RegisterExtension(_COMMAND_LEAVEROOM.extensions_by_name['ext'])
  RoomCommand.RegisterExtension(_COMMAND_ROOMSAY.extensions_by_name['ext'])
  RoomCommand.RegisterExtension(_COMMAND_CREATEGAME.extensions_by_name['ext'])
  RoomCommand.RegisterExtension(_COMMAND_JOINGAME.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _ROOMCOMMAND._serialized_start=23
  _ROOMCOMMAND._serialized_end=131
  _ROOMCOMMAND_ROOMCOMMANDTYPE._serialized_start=38
  _ROOMCOMMAND_ROOMCOMMANDTYPE._serialized_end=121
  _COMMAND_LEAVEROOM._serialized_start=133
  _COMMAND_LEAVEROOM._serialized_end=200
  _COMMAND_ROOMSAY._serialized_start=202
  _COMMAND_ROOMSAY._serialized_end=282
  _COMMAND_CREATEGAME._serialized_start=285
  _COMMAND_CREATEGAME._serialized_end=689
  _COMMAND_JOINGAME._serialized_start=692
  _COMMAND_JOINGAME._serialized_end=869
# @@protoc_insertion_point(module_scope)

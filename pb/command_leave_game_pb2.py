# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_leave_game.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_commands_pb2 as game__commands__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='command_leave_game.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18\x63ommand_leave_game.proto\x1a\x13game_commands.proto\"C\n\x11\x43ommand_LeaveGame2.\n\x03\x65xt\x12\x0c.GameCommand\x18\xe9\x07 \x01(\x0b\x32\x12.Command_LeaveGame'
  ,
  dependencies=[game__commands__pb2.DESCRIPTOR,])




_COMMAND_LEAVEGAME = _descriptor.Descriptor(
  name='Command_LeaveGame',
  full_name='Command_LeaveGame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_LeaveGame.ext', index=0,
      number=1001, type=11, cpp_type=10, label=1,
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
  serialized_start=49,
  serialized_end=116,
)

DESCRIPTOR.message_types_by_name['Command_LeaveGame'] = _COMMAND_LEAVEGAME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command_LeaveGame = _reflection.GeneratedProtocolMessageType('Command_LeaveGame', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND_LEAVEGAME,
  '__module__' : 'command_leave_game_pb2'
  # @@protoc_insertion_point(class_scope:Command_LeaveGame)
  })
_sym_db.RegisterMessage(Command_LeaveGame)

_COMMAND_LEAVEGAME.extensions_by_name['ext'].message_type = _COMMAND_LEAVEGAME
game__commands__pb2.GameCommand.RegisterExtension(_COMMAND_LEAVEGAME.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_reverse_turn.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_commands_pb2 as game__commands__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='command_reverse_turn.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1a\x63ommand_reverse_turn.proto\x1a\x13game_commands.proto\"G\n\x13\x43ommand_ReverseTurn20\n\x03\x65xt\x12\x0c.GameCommand\x18\x8a\x08 \x01(\x0b\x32\x14.Command_ReverseTurn'
  ,
  dependencies=[game__commands__pb2.DESCRIPTOR,])




_COMMAND_REVERSETURN = _descriptor.Descriptor(
  name='Command_ReverseTurn',
  full_name='Command_ReverseTurn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_ReverseTurn.ext', index=0,
      number=1034, type=11, cpp_type=10, label=1,
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
  serialized_start=51,
  serialized_end=122,
)

DESCRIPTOR.message_types_by_name['Command_ReverseTurn'] = _COMMAND_REVERSETURN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command_ReverseTurn = _reflection.GeneratedProtocolMessageType('Command_ReverseTurn', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND_REVERSETURN,
  '__module__' : 'command_reverse_turn_pb2'
  # @@protoc_insertion_point(class_scope:Command_ReverseTurn)
  })
_sym_db.RegisterMessage(Command_ReverseTurn)

_COMMAND_REVERSETURN.extensions_by_name['ext'].message_type = _COMMAND_REVERSETURN
game__commands__pb2.GameCommand.RegisterExtension(_COMMAND_REVERSETURN.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_set_active_phase.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_commands_pb2 as game__commands__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='command_set_active_phase.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1e\x63ommand_set_active_phase.proto\x1a\x13game_commands.proto\"\\\n\x16\x43ommand_SetActivePhase\x12\r\n\x05phase\x18\x01 \x01(\r23\n\x03\x65xt\x12\x0c.GameCommand\x18\xff\x07 \x01(\x0b\x32\x17.Command_SetActivePhase'
  ,
  dependencies=[game__commands__pb2.DESCRIPTOR,])




_COMMAND_SETACTIVEPHASE = _descriptor.Descriptor(
  name='Command_SetActivePhase',
  full_name='Command_SetActivePhase',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='phase', full_name='Command_SetActivePhase.phase', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_SetActivePhase.ext', index=0,
      number=1023, type=11, cpp_type=10, label=1,
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
  serialized_start=55,
  serialized_end=147,
)

DESCRIPTOR.message_types_by_name['Command_SetActivePhase'] = _COMMAND_SETACTIVEPHASE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command_SetActivePhase = _reflection.GeneratedProtocolMessageType('Command_SetActivePhase', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND_SETACTIVEPHASE,
  '__module__' : 'command_set_active_phase_pb2'
  # @@protoc_insertion_point(class_scope:Command_SetActivePhase)
  })
_sym_db.RegisterMessage(Command_SetActivePhase)

_COMMAND_SETACTIVEPHASE.extensions_by_name['ext'].message_type = _COMMAND_SETACTIVEPHASE
game__commands__pb2.GameCommand.RegisterExtension(_COMMAND_SETACTIVEPHASE.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)

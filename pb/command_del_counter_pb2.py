# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_del_counter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_commands_pb2 as game__commands__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='command_del_counter.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19\x63ommand_del_counter.proto\x1a\x13game_commands.proto\"]\n\x12\x43ommand_DelCounter\x12\x16\n\ncounter_id\x18\x01 \x01(\x11:\x02-12/\n\x03\x65xt\x12\x0c.GameCommand\x18\xfd\x07 \x01(\x0b\x32\x13.Command_DelCounter'
  ,
  dependencies=[game__commands__pb2.DESCRIPTOR,])




_COMMAND_DELCOUNTER = _descriptor.Descriptor(
  name='Command_DelCounter',
  full_name='Command_DelCounter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='counter_id', full_name='Command_DelCounter.counter_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_DelCounter.ext', index=0,
      number=1021, type=11, cpp_type=10, label=1,
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
  serialized_start=50,
  serialized_end=143,
)

DESCRIPTOR.message_types_by_name['Command_DelCounter'] = _COMMAND_DELCOUNTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command_DelCounter = _reflection.GeneratedProtocolMessageType('Command_DelCounter', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND_DELCOUNTER,
  '__module__' : 'command_del_counter_pb2'
  # @@protoc_insertion_point(class_scope:Command_DelCounter)
  })
_sym_db.RegisterMessage(Command_DelCounter)

_COMMAND_DELCOUNTER.extensions_by_name['ext'].message_type = _COMMAND_DELCOUNTER
game__commands__pb2.GameCommand.RegisterExtension(_COMMAND_DELCOUNTER.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)

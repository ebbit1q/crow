# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_delete_arrow.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_commands_pb2 as game__commands__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='command_delete_arrow.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1a\x63ommand_delete_arrow.proto\x1a\x13game_commands.proto\"]\n\x13\x43ommand_DeleteArrow\x12\x14\n\x08\x61rrow_id\x18\x01 \x01(\x11:\x02-120\n\x03\x65xt\x12\x0c.GameCommand\x18\xf4\x07 \x01(\x0b\x32\x14.Command_DeleteArrow'
  ,
  dependencies=[game__commands__pb2.DESCRIPTOR,])




_COMMAND_DELETEARROW = _descriptor.Descriptor(
  name='Command_DeleteArrow',
  full_name='Command_DeleteArrow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='arrow_id', full_name='Command_DeleteArrow.arrow_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_DeleteArrow.ext', index=0,
      number=1012, type=11, cpp_type=10, label=1,
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
  serialized_end=144,
)

DESCRIPTOR.message_types_by_name['Command_DeleteArrow'] = _COMMAND_DELETEARROW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command_DeleteArrow = _reflection.GeneratedProtocolMessageType('Command_DeleteArrow', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND_DELETEARROW,
  '__module__' : 'command_delete_arrow_pb2'
  # @@protoc_insertion_point(class_scope:Command_DeleteArrow)
  })
_sym_db.RegisterMessage(Command_DeleteArrow)

_COMMAND_DELETEARROW.extensions_by_name['ext'].message_type = _COMMAND_DELETEARROW
game__commands__pb2.GameCommand.RegisterExtension(_COMMAND_DELETEARROW.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)

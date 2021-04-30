# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_change_zone_properties.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_commands_pb2 as game__commands__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='command_change_zone_properties.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$command_change_zone_properties.proto\x1a\x13game_commands.proto\"\xad\x01\n\x1c\x43ommand_ChangeZoneProperties\x12\x11\n\tzone_name\x18\x01 \x01(\t\x12\x1e\n\x16\x61lways_reveal_top_card\x18\n \x01(\x08\x12\x1f\n\x17\x61lways_look_at_top_card\x18\x0b \x01(\x08\x32\x39\n\x03\x65xt\x12\x0c.GameCommand\x18\x87\x08 \x01(\x0b\x32\x1d.Command_ChangeZoneProperties'
  ,
  dependencies=[game__commands__pb2.DESCRIPTOR,])




_COMMAND_CHANGEZONEPROPERTIES = _descriptor.Descriptor(
  name='Command_ChangeZoneProperties',
  full_name='Command_ChangeZoneProperties',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='zone_name', full_name='Command_ChangeZoneProperties.zone_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='always_reveal_top_card', full_name='Command_ChangeZoneProperties.always_reveal_top_card', index=1,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='always_look_at_top_card', full_name='Command_ChangeZoneProperties.always_look_at_top_card', index=2,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_ChangeZoneProperties.ext', index=0,
      number=1031, type=11, cpp_type=10, label=1,
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
  serialized_start=62,
  serialized_end=235,
)

DESCRIPTOR.message_types_by_name['Command_ChangeZoneProperties'] = _COMMAND_CHANGEZONEPROPERTIES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command_ChangeZoneProperties = _reflection.GeneratedProtocolMessageType('Command_ChangeZoneProperties', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND_CHANGEZONEPROPERTIES,
  '__module__' : 'command_change_zone_properties_pb2'
  # @@protoc_insertion_point(class_scope:Command_ChangeZoneProperties)
  })
_sym_db.RegisterMessage(Command_ChangeZoneProperties)

_COMMAND_CHANGEZONEPROPERTIES.extensions_by_name['ext'].message_type = _COMMAND_CHANGEZONEPROPERTIES
game__commands__pb2.GameCommand.RegisterExtension(_COMMAND_CHANGEZONEPROPERTIES.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
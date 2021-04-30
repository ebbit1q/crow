# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_reveal_cards.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_commands_pb2 as game__commands__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='command_reveal_cards.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1a\x63ommand_reveal_cards.proto\x1a\x13game_commands.proto\"\xb9\x01\n\x13\x43ommand_RevealCards\x12\x11\n\tzone_name\x18\x01 \x01(\t\x12\x13\n\x07\x63\x61rd_id\x18\x02 \x01(\x11:\x02-1\x12\x15\n\tplayer_id\x18\x03 \x01(\x11:\x02-1\x12\x1a\n\x12grant_write_access\x18\x04 \x01(\x08\x12\x15\n\ttop_cards\x18\x05 \x01(\x11:\x02-120\n\x03\x65xt\x12\x0c.GameCommand\x18\x82\x08 \x01(\x0b\x32\x14.Command_RevealCards'
  ,
  dependencies=[game__commands__pb2.DESCRIPTOR,])




_COMMAND_REVEALCARDS = _descriptor.Descriptor(
  name='Command_RevealCards',
  full_name='Command_RevealCards',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='zone_name', full_name='Command_RevealCards.zone_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='card_id', full_name='Command_RevealCards.card_id', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='Command_RevealCards.player_id', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grant_write_access', full_name='Command_RevealCards.grant_write_access', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='top_cards', full_name='Command_RevealCards.top_cards', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_RevealCards.ext', index=0,
      number=1026, type=11, cpp_type=10, label=1,
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
  serialized_start=52,
  serialized_end=237,
)

DESCRIPTOR.message_types_by_name['Command_RevealCards'] = _COMMAND_REVEALCARDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command_RevealCards = _reflection.GeneratedProtocolMessageType('Command_RevealCards', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND_REVEALCARDS,
  '__module__' : 'command_reveal_cards_pb2'
  # @@protoc_insertion_point(class_scope:Command_RevealCards)
  })
_sym_db.RegisterMessage(Command_RevealCards)

_COMMAND_REVEALCARDS.extensions_by_name['ext'].message_type = _COMMAND_REVEALCARDS
game__commands__pb2.GameCommand.RegisterExtension(_COMMAND_REVEALCARDS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)

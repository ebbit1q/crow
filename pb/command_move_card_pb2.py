# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_move_card.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_commands_pb2 as game__commands__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='command_move_card.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17\x63ommand_move_card.proto\x1a\x13game_commands.proto\"P\n\nCardToMove\x12\x13\n\x07\x63\x61rd_id\x18\x01 \x01(\x11:\x02-1\x12\x11\n\tface_down\x18\x02 \x01(\x08\x12\n\n\x02pt\x18\x03 \x01(\t\x12\x0e\n\x06tapped\x18\x04 \x01(\x08\".\n\x11ListOfCardsToMove\x12\x19\n\x04\x63\x61rd\x18\x01 \x03(\x0b\x32\x0b.CardToMove\"\xee\x01\n\x10\x43ommand_MoveCard\x12\x1b\n\x0fstart_player_id\x18\x01 \x01(\x11:\x02-1\x12\x12\n\nstart_zone\x18\x02 \x01(\t\x12)\n\rcards_to_move\x18\x03 \x01(\x0b\x32\x12.ListOfCardsToMove\x12\x1c\n\x10target_player_id\x18\x04 \x01(\x11:\x02-1\x12\x13\n\x0btarget_zone\x18\x05 \x01(\t\x12\r\n\x01x\x18\x06 \x01(\x11:\x02-1\x12\r\n\x01y\x18\x07 \x01(\x11:\x02-12-\n\x03\x65xt\x12\x0c.GameCommand\x18\x83\x08 \x01(\x0b\x32\x11.Command_MoveCard'
  ,
  dependencies=[game__commands__pb2.DESCRIPTOR,])




_CARDTOMOVE = _descriptor.Descriptor(
  name='CardToMove',
  full_name='CardToMove',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='card_id', full_name='CardToMove.card_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='face_down', full_name='CardToMove.face_down', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pt', full_name='CardToMove.pt', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tapped', full_name='CardToMove.tapped', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
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
  serialized_start=48,
  serialized_end=128,
)


_LISTOFCARDSTOMOVE = _descriptor.Descriptor(
  name='ListOfCardsToMove',
  full_name='ListOfCardsToMove',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='card', full_name='ListOfCardsToMove.card', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
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
  serialized_start=130,
  serialized_end=176,
)


_COMMAND_MOVECARD = _descriptor.Descriptor(
  name='Command_MoveCard',
  full_name='Command_MoveCard',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_player_id', full_name='Command_MoveCard.start_player_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_zone', full_name='Command_MoveCard.start_zone', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cards_to_move', full_name='Command_MoveCard.cards_to_move', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_player_id', full_name='Command_MoveCard.target_player_id', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_zone', full_name='Command_MoveCard.target_zone', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x', full_name='Command_MoveCard.x', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='Command_MoveCard.y', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_MoveCard.ext', index=0,
      number=1027, type=11, cpp_type=10, label=1,
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
  serialized_start=179,
  serialized_end=417,
)

_LISTOFCARDSTOMOVE.fields_by_name['card'].message_type = _CARDTOMOVE
_COMMAND_MOVECARD.fields_by_name['cards_to_move'].message_type = _LISTOFCARDSTOMOVE
DESCRIPTOR.message_types_by_name['CardToMove'] = _CARDTOMOVE
DESCRIPTOR.message_types_by_name['ListOfCardsToMove'] = _LISTOFCARDSTOMOVE
DESCRIPTOR.message_types_by_name['Command_MoveCard'] = _COMMAND_MOVECARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CardToMove = _reflection.GeneratedProtocolMessageType('CardToMove', (_message.Message,), {
  'DESCRIPTOR' : _CARDTOMOVE,
  '__module__' : 'command_move_card_pb2'
  # @@protoc_insertion_point(class_scope:CardToMove)
  })
_sym_db.RegisterMessage(CardToMove)

ListOfCardsToMove = _reflection.GeneratedProtocolMessageType('ListOfCardsToMove', (_message.Message,), {
  'DESCRIPTOR' : _LISTOFCARDSTOMOVE,
  '__module__' : 'command_move_card_pb2'
  # @@protoc_insertion_point(class_scope:ListOfCardsToMove)
  })
_sym_db.RegisterMessage(ListOfCardsToMove)

Command_MoveCard = _reflection.GeneratedProtocolMessageType('Command_MoveCard', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND_MOVECARD,
  '__module__' : 'command_move_card_pb2'
  # @@protoc_insertion_point(class_scope:Command_MoveCard)
  })
_sym_db.RegisterMessage(Command_MoveCard)

_COMMAND_MOVECARD.extensions_by_name['ext'].message_type = _COMMAND_MOVECARD
game__commands__pb2.GameCommand.RegisterExtension(_COMMAND_MOVECARD.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
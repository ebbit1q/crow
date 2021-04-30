# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_draw_cards.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_event_pb2 as game__event__pb2
import serverinfo_card_pb2 as serverinfo__card__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='event_draw_cards.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16\x65vent_draw_cards.proto\x1a\x10game_event.proto\x1a\x15serverinfo_card.proto\"n\n\x0f\x45vent_DrawCards\x12\x0e\n\x06number\x18\x01 \x01(\x11\x12\x1f\n\x05\x63\x61rds\x18\x02 \x03(\x0b\x32\x10.ServerInfo_Card2*\n\x03\x65xt\x12\n.GameEvent\x18\xd5\x0f \x01(\x0b\x32\x10.Event_DrawCards'
  ,
  dependencies=[game__event__pb2.DESCRIPTOR,serverinfo__card__pb2.DESCRIPTOR,])




_EVENT_DRAWCARDS = _descriptor.Descriptor(
  name='Event_DrawCards',
  full_name='Event_DrawCards',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='Event_DrawCards.number', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cards', full_name='Event_DrawCards.cards', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Event_DrawCards.ext', index=0,
      number=2005, type=11, cpp_type=10, label=1,
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
  serialized_start=67,
  serialized_end=177,
)

_EVENT_DRAWCARDS.fields_by_name['cards'].message_type = serverinfo__card__pb2._SERVERINFO_CARD
DESCRIPTOR.message_types_by_name['Event_DrawCards'] = _EVENT_DRAWCARDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event_DrawCards = _reflection.GeneratedProtocolMessageType('Event_DrawCards', (_message.Message,), {
  'DESCRIPTOR' : _EVENT_DRAWCARDS,
  '__module__' : 'event_draw_cards_pb2'
  # @@protoc_insertion_point(class_scope:Event_DrawCards)
  })
_sym_db.RegisterMessage(Event_DrawCards)

_EVENT_DRAWCARDS.extensions_by_name['ext'].message_type = _EVENT_DRAWCARDS
game__event__pb2.GameEvent.RegisterExtension(_EVENT_DRAWCARDS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)

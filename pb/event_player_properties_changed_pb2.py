# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_player_properties_changed.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_event_pb2 as game__event__pb2
import serverinfo_playerproperties_pb2 as serverinfo__playerproperties__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='event_player_properties_changed.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%event_player_properties_changed.proto\x1a\x10game_event.proto\x1a!serverinfo_playerproperties.proto\"\x92\x01\n\x1d\x45vent_PlayerPropertiesChanged\x12\x37\n\x11player_properties\x18\x01 \x01(\x0b\x32\x1c.ServerInfo_PlayerProperties28\n\x03\x65xt\x12\n.GameEvent\x18\xef\x07 \x01(\x0b\x32\x1e.Event_PlayerPropertiesChanged'
  ,
  dependencies=[game__event__pb2.DESCRIPTOR,serverinfo__playerproperties__pb2.DESCRIPTOR,])




_EVENT_PLAYERPROPERTIESCHANGED = _descriptor.Descriptor(
  name='Event_PlayerPropertiesChanged',
  full_name='Event_PlayerPropertiesChanged',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_properties', full_name='Event_PlayerPropertiesChanged.player_properties', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Event_PlayerPropertiesChanged.ext', index=0,
      number=1007, type=11, cpp_type=10, label=1,
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
  serialized_start=95,
  serialized_end=241,
)

_EVENT_PLAYERPROPERTIESCHANGED.fields_by_name['player_properties'].message_type = serverinfo__playerproperties__pb2._SERVERINFO_PLAYERPROPERTIES
DESCRIPTOR.message_types_by_name['Event_PlayerPropertiesChanged'] = _EVENT_PLAYERPROPERTIESCHANGED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event_PlayerPropertiesChanged = _reflection.GeneratedProtocolMessageType('Event_PlayerPropertiesChanged', (_message.Message,), {
  'DESCRIPTOR' : _EVENT_PLAYERPROPERTIESCHANGED,
  '__module__' : 'event_player_properties_changed_pb2'
  # @@protoc_insertion_point(class_scope:Event_PlayerPropertiesChanged)
  })
_sym_db.RegisterMessage(Event_PlayerPropertiesChanged)

_EVENT_PLAYERPROPERTIESCHANGED.extensions_by_name['ext'].message_type = _EVENT_PLAYERPROPERTIESCHANGED
game__event__pb2.GameEvent.RegisterExtension(_EVENT_PLAYERPROPERTIESCHANGED.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)

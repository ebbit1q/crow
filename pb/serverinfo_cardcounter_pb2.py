# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: serverinfo_cardcounter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='serverinfo_cardcounter.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cserverinfo_cardcounter.proto\"3\n\x16ServerInfo_CardCounter\x12\n\n\x02id\x18\x01 \x01(\x11\x12\r\n\x05value\x18\x02 \x01(\x11'
)




_SERVERINFO_CARDCOUNTER = _descriptor.Descriptor(
  name='ServerInfo_CardCounter',
  full_name='ServerInfo_CardCounter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ServerInfo_CardCounter.id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='ServerInfo_CardCounter.value', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=32,
  serialized_end=83,
)

DESCRIPTOR.message_types_by_name['ServerInfo_CardCounter'] = _SERVERINFO_CARDCOUNTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerInfo_CardCounter = _reflection.GeneratedProtocolMessageType('ServerInfo_CardCounter', (_message.Message,), {
  'DESCRIPTOR' : _SERVERINFO_CARDCOUNTER,
  '__module__' : 'serverinfo_cardcounter_pb2'
  # @@protoc_insertion_point(class_scope:ServerInfo_CardCounter)
  })
_sym_db.RegisterMessage(ServerInfo_CardCounter)


# @@protoc_insertion_point(module_scope)

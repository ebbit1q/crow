# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: event_set_card_attr.proto
# Protobuf Python Version: 5.29.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    2,
    '',
    'event_set_card_attr.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_event_pb2 as game__event__pb2
import card_attributes_pb2 as card__attributes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x65vent_set_card_attr.proto\x1a\x10game_event.proto\x1a\x15\x63\x61rd_attributes.proto\"\x9c\x01\n\x11\x45vent_SetCardAttr\x12\x11\n\tzone_name\x18\x01 \x01(\t\x12\x0f\n\x07\x63\x61rd_id\x18\x02 \x01(\x11\x12!\n\tattribute\x18\x03 \x01(\x0e\x32\x0e.CardAttribute\x12\x12\n\nattr_value\x18\x04 \x01(\t2,\n\x03\x65xt\x12\n.GameEvent\x18\xde\x0f \x01(\x0b\x32\x12.Event_SetCardAttr')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_set_card_attr_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EVENT_SETCARDATTR']._serialized_start=71
  _globals['_EVENT_SETCARDATTR']._serialized_end=227
# @@protoc_insertion_point(module_scope)

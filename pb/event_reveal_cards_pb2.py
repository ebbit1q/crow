# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: event_reveal_cards.proto
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
    'event_reveal_cards.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_event_pb2 as game__event__pb2
import serverinfo_card_pb2 as serverinfo__card__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x65vent_reveal_cards.proto\x1a\x10game_event.proto\x1a\x15serverinfo_card.proto\"\xdc\x01\n\x11\x45vent_RevealCards\x12\x11\n\tzone_name\x18\x01 \x01(\t\x12\x13\n\x07\x63\x61rd_id\x18\x02 \x03(\x11\x42\x02\x10\x00\x12\x1b\n\x0fother_player_id\x18\x03 \x01(\x11:\x02-1\x12\x1f\n\x05\x63\x61rds\x18\x04 \x03(\x0b\x32\x10.ServerInfo_Card\x12\x1a\n\x12grant_write_access\x18\x05 \x01(\x08\x12\x17\n\x0fnumber_of_cards\x18\x06 \x01(\r2,\n\x03\x65xt\x12\n.GameEvent\x18\xd6\x0f \x01(\x0b\x32\x12.Event_RevealCards')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_reveal_cards_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EVENT_REVEALCARDS'].fields_by_name['card_id']._loaded_options = None
  _globals['_EVENT_REVEALCARDS'].fields_by_name['card_id']._serialized_options = b'\020\000'
  _globals['_EVENT_REVEALCARDS']._serialized_start=70
  _globals['_EVENT_REVEALCARDS']._serialized_end=290
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: serverinfo_user.proto
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
    'serverinfo_user.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15serverinfo_user.proto\"\xe4\x03\n\x0fServerInfo_User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nuser_level\x18\x02 \x01(\r\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x11\n\treal_name\x18\x04 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x06 \x01(\t\x12\x12\n\navatar_bmp\x18\x07 \x01(\x0c\x12\x0e\n\x02id\x18\x08 \x01(\x11:\x02-1\x12\x15\n\tserver_id\x18\t \x01(\x11:\x02-1\x12\x12\n\nsession_id\x18\n \x01(\x04\x12\x17\n\x0f\x61\x63\x63ountage_secs\x18\x0b \x01(\x04\x12\r\n\x05\x65mail\x18\x0c \x01(\t\x12\x10\n\x08\x63lientid\x18\r \x01(\t\x12\x11\n\tprivlevel\x18\x0e \x01(\t\x12\x38\n\x0bpawn_colors\x18\x0f \x01(\x0b\x32#.ServerInfo_User.PawnColorsOverride\x1a;\n\x12PawnColorsOverride\x12\x11\n\tleft_side\x18\x01 \x01(\t\x12\x12\n\nright_side\x18\x02 \x01(\t\"g\n\rUserLevelFlag\x12\r\n\tIsNothing\x10\x00\x12\n\n\x06IsUser\x10\x01\x12\x10\n\x0cIsRegistered\x10\x02\x12\x0f\n\x0bIsModerator\x10\x04\x12\x0b\n\x07IsAdmin\x10\x08\x12\x0b\n\x07IsJudge\x10\x10')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'serverinfo_user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SERVERINFO_USER']._serialized_start=26
  _globals['_SERVERINFO_USER']._serialized_end=510
  _globals['_SERVERINFO_USER_PAWNCOLORSOVERRIDE']._serialized_start=346
  _globals['_SERVERINFO_USER_PAWNCOLORSOVERRIDE']._serialized_end=405
  _globals['_SERVERINFO_USER_USERLEVELFLAG']._serialized_start=407
  _globals['_SERVERINFO_USER_USERLEVELFLAG']._serialized_end=510
# @@protoc_insertion_point(module_scope)

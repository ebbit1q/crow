# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_login.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import response_pb2 as response__pb2
import serverinfo_user_pb2 as serverinfo__user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14response_login.proto\x1a\x0eresponse.proto\x1a\x15serverinfo_user.proto\"\xfa\x01\n\x0eResponse_Login\x12#\n\tuser_info\x18\x01 \x01(\x0b\x32\x10.ServerInfo_User\x12$\n\nbuddy_list\x18\x02 \x03(\x0b\x32\x10.ServerInfo_User\x12%\n\x0bignore_list\x18\x03 \x03(\x0b\x32\x10.ServerInfo_User\x12\x19\n\x11\x64\x65nied_reason_str\x18\x04 \x01(\t\x12\x17\n\x0f\x64\x65nied_end_time\x18\x05 \x01(\x04\x12\x18\n\x10missing_features\x18\x06 \x03(\t2(\n\x03\x65xt\x12\t.Response\x18\xed\x07 \x01(\x0b\x32\x0f.Response_Login')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'response_login_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  response__pb2.Response.RegisterExtension(_RESPONSE_LOGIN.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _RESPONSE_LOGIN._serialized_start=64
  _RESPONSE_LOGIN._serialized_end=314
# @@protoc_insertion_point(module_scope)

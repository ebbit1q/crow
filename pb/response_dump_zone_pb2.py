# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_dump_zone.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import response_pb2 as response__pb2
import serverinfo_zone_pb2 as serverinfo__zone__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18response_dump_zone.proto\x1a\x0eresponse.proto\x1a\x15serverinfo_zone.proto\"e\n\x11Response_DumpZone\x12#\n\tzone_info\x18\x01 \x01(\x0b\x32\x10.ServerInfo_Zone2+\n\x03\x65xt\x12\t.Response\x18\xec\x07 \x01(\x0b\x32\x12.Response_DumpZone')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'response_dump_zone_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  response__pb2.Response.RegisterExtension(_RESPONSE_DUMPZONE.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _RESPONSE_DUMPZONE._serialized_start=67
  _RESPONSE_DUMPZONE._serialized_end=168
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admin_commands.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61\x64min_commands.proto\"\x83\x01\n\x0c\x41\x64minCommand\"i\n\x10\x41\x64minCommandType\x12\x1a\n\x15UPDATE_SERVER_MESSAGE\x10\xe8\x07\x12\x14\n\x0fSHUTDOWN_SERVER\x10\xe9\x07\x12\x12\n\rRELOAD_CONFIG\x10\xea\x07\x12\x0f\n\nADJUST_MOD\x10\xeb\x07*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"X\n\x1b\x43ommand_UpdateServerMessage29\n\x03\x65xt\x12\r.AdminCommand\x18\xe8\x07 \x01(\x0b\x32\x1c.Command_UpdateServerMessage\"o\n\x16\x43ommand_ShutdownServer\x12\x0e\n\x06reason\x18\x01 \x01(\t\x12\x0f\n\x07minutes\x18\x02 \x01(\r24\n\x03\x65xt\x12\r.AdminCommand\x18\xe9\x07 \x01(\x0b\x32\x17.Command_ShutdownServer\"J\n\x14\x43ommand_ReloadConfig22\n\x03\x65xt\x12\r.AdminCommand\x18\xea\x07 \x01(\x0b\x32\x15.Command_ReloadConfig\"\x87\x01\n\x11\x43ommand_AdjustMod\x12\x11\n\tuser_name\x18\x01 \x02(\t\x12\x15\n\rshould_be_mod\x18\x02 \x01(\x08\x12\x17\n\x0fshould_be_judge\x18\x03 \x01(\x08\x32/\n\x03\x65xt\x12\r.AdminCommand\x18\xeb\x07 \x01(\x0b\x32\x12.Command_AdjustMod')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'admin_commands_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  AdminCommand.RegisterExtension(_COMMAND_UPDATESERVERMESSAGE.extensions_by_name['ext'])
  AdminCommand.RegisterExtension(_COMMAND_SHUTDOWNSERVER.extensions_by_name['ext'])
  AdminCommand.RegisterExtension(_COMMAND_RELOADCONFIG.extensions_by_name['ext'])
  AdminCommand.RegisterExtension(_COMMAND_ADJUSTMOD.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _ADMINCOMMAND._serialized_start=25
  _ADMINCOMMAND._serialized_end=156
  _ADMINCOMMAND_ADMINCOMMANDTYPE._serialized_start=41
  _ADMINCOMMAND_ADMINCOMMANDTYPE._serialized_end=146
  _COMMAND_UPDATESERVERMESSAGE._serialized_start=158
  _COMMAND_UPDATESERVERMESSAGE._serialized_end=246
  _COMMAND_SHUTDOWNSERVER._serialized_start=248
  _COMMAND_SHUTDOWNSERVER._serialized_end=359
  _COMMAND_RELOADCONFIG._serialized_start=361
  _COMMAND_RELOADCONFIG._serialized_end=435
  _COMMAND_ADJUSTMOD._serialized_start=438
  _COMMAND_ADJUSTMOD._serialized_end=573
# @@protoc_insertion_point(module_scope)

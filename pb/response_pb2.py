# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: response.proto
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
    'response.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eresponse.proto\"\xcf\x0b\n\x08Response\x12\x0e\n\x06\x63md_id\x18\x01 \x02(\x04\x12-\n\rresponse_code\x18\x02 \x01(\x0e\x32\x16.Response.ResponseCode\"\xe6\x07\n\x0cResponseCode\x12\x1d\n\x10RespNotConnected\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x0f\n\x0bRespNothing\x10\x00\x12\n\n\x06RespOk\x10\x01\x12\x11\n\rRespNotInRoom\x10\x02\x12\x15\n\x11RespInternalError\x10\x03\x12\x16\n\x12RespInvalidCommand\x10\x04\x12\x13\n\x0fRespInvalidData\x10\x05\x12\x14\n\x10RespNameNotFound\x10\x06\x12\x13\n\x0fRespLoginNeeded\x10\x07\x12\x1a\n\x16RespFunctionNotAllowed\x10\x08\x12\x16\n\x12RespGameNotStarted\x10\t\x12\x10\n\x0cRespGameFull\x10\n\x12\x14\n\x10RespContextError\x10\x0b\x12\x15\n\x11RespWrongPassword\x10\x0c\x12\x1c\n\x18RespSpectatorsNotAllowed\x10\r\x12\x13\n\x0fRespOnlyBuddies\x10\x0e\x12\x17\n\x13RespUserLevelTooLow\x10\x0f\x12\x14\n\x10RespInIgnoreList\x10\x10\x12 \n\x1cRespWouldOverwriteOldSession\x10\x11\x12\x11\n\rRespChatFlood\x10\x12\x12\x14\n\x10RespUserIsBanned\x10\x13\x12\x14\n\x10RespAccessDenied\x10\x14\x12\x17\n\x13RespUsernameInvalid\x10\x15\x12\x1c\n\x18RespRegistrationRequired\x10\x16\x12\x1c\n\x18RespRegistrationAccepted\x10\x17\x12\x19\n\x15RespUserAlreadyExists\x10\x18\x12\x1f\n\x1bRespEmailRequiredToRegister\x10\x19\x12\x17\n\x13RespTooManyRequests\x10\x1a\x12\x18\n\x14RespPasswordTooShort\x10\x1b\x12\x1b\n\x17RespAccountNotActivated\x10\x1c\x12\x1c\n\x18RespRegistrationDisabled\x10\x1d\x12\x1a\n\x16RespRegistrationFailed\x10\x1e\x12\x1a\n\x16RespActivationAccepted\x10\x1f\x12\x18\n\x14RespActivationFailed\x10 \x12+\n\'RespRegistrationAcceptedNeedsActivation\x10!\x12\x18\n\x14RespClientIdRequired\x10\"\x12\x1c\n\x18RespClientUpdateRequired\x10#\x12\x12\n\x0eRespServerFull\x10$\x12\x18\n\x14RespEmailBlackListed\x10%\"\x90\x03\n\x0cResponseType\x12\x0e\n\tJOIN_ROOM\x10\xe8\x07\x12\x0f\n\nLIST_USERS\x10\xe9\x07\x12\x16\n\x11GET_GAMES_OF_USER\x10\xea\x07\x12\x12\n\rGET_USER_INFO\x10\xeb\x07\x12\x0e\n\tDUMP_ZONE\x10\xec\x07\x12\n\n\x05LOGIN\x10\xed\x07\x12\x0e\n\tDECK_LIST\x10\xee\x07\x12\x12\n\rDECK_DOWNLOAD\x10\xef\x07\x12\x10\n\x0b\x44\x45\x43K_UPLOAD\x10\xf0\x07\x12\r\n\x08REGISTER\x10\xf1\x07\x12\r\n\x08\x41\x43TIVATE\x10\xf2\x07\x12\x0f\n\nADJUST_MOD\x10\xf3\x07\x12\x10\n\x0b\x42\x41N_HISTORY\x10\xf4\x07\x12\x11\n\x0cWARN_HISTORY\x10\xf5\x07\x12\x0e\n\tWARN_LIST\x10\xf6\x07\x12\r\n\x08VIEW_LOG\x10\xf7\x07\x12\x1c\n\x17\x46ORGOT_PASSWORD_REQUEST\x10\xf8\x07\x12\x12\n\rPASSWORD_SALT\x10\xf9\x07\x12\x14\n\x0fGET_ADMIN_NOTES\x10\xfa\x07\x12\x10\n\x0bREPLAY_LIST\x10\xcc\x08\x12\x14\n\x0fREPLAY_DOWNLOAD\x10\xcd\x08*\x08\x08\x64\x10\x80\x80\x80\x80\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'response_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_RESPONSE']._serialized_start=19
  _globals['_RESPONSE']._serialized_end=1506
  _globals['_RESPONSE_RESPONSECODE']._serialized_start=95
  _globals['_RESPONSE_RESPONSECODE']._serialized_end=1093
  _globals['_RESPONSE_RESPONSETYPE']._serialized_start=1096
  _globals['_RESPONSE_RESPONSETYPE']._serialized_end=1496
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/agent/v0/communicate.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#services/agent/v0/communicate.proto\x12\x11services.agent.v0\"\x1d\n\x07\x43hannel\x12\x12\n\x04kind\x18\x01 \x01(\tR\x04kind\"Y\n\x07Message\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\"|\n\x07\x44isplay\x12\x38\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32$.services.agent.v0.Display.DataEntryR\x04\x64\x61ta\x1a\x37\n\tDataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"#\n\x07\x43onfirm\x12\x18\n\x07\x64\x65\x66\x61ult\x18\x01 \x01(\x08R\x07\x64\x65\x66\x61ult\"-\n\rConfirmAnswer\x12\x1c\n\tconfirmed\x18\x01 \x01(\x08R\tconfirmed\"^\n\x05Input\x12\'\n\x0estring_default\x18\x01 \x01(\tH\x00R\rstringDefault\x12!\n\x0bint_default\x18\x02 \x01(\x05H\x00R\nintDefaultB\t\n\x07\x64\x65\x66\x61ult\"[\n\x0bInputAnswer\x12#\n\x0cstring_value\x18\x01 \x01(\tH\x00R\x0bstringValue\x12\x1d\n\tint_value\x18\x02 \x01(\x05H\x00R\x08intValueB\x08\n\x06\x61nswer\">\n\x06\x43hoice\x12\x34\n\x07options\x18\x01 \x03(\x0b\x32\x1a.services.agent.v0.MessageR\x07options\"&\n\x0c\x43hoiceAnswer\x12\x16\n\x06option\x18\x01 \x01(\tR\x06option\"A\n\tSelection\x12\x34\n\x07options\x18\x01 \x03(\x0b\x32\x1a.services.agent.v0.MessageR\x07options\"-\n\x0fSelectionAnswer\x12\x1a\n\x08selected\x18\x01 \x03(\tR\x08selected\"\xaa\x03\n\x08Question\x12\x34\n\x07\x63hannel\x18\x01 \x01(\x0b\x32\x1a.services.agent.v0.ChannelR\x07\x63hannel\x12\x14\n\x05round\x18\x02 \x01(\x05R\x05round\x12\x34\n\x07message\x18\x03 \x01(\x0b\x32\x1a.services.agent.v0.MessageR\x07message\x12\x36\n\x07\x64isplay\x18\x04 \x01(\x0b\x32\x1a.services.agent.v0.DisplayH\x00R\x07\x64isplay\x12\x36\n\x07\x63onfirm\x18\x05 \x01(\x0b\x32\x1a.services.agent.v0.ConfirmH\x00R\x07\x63onfirm\x12\x30\n\x05input\x18\x06 \x01(\x0b\x32\x18.services.agent.v0.InputH\x00R\x05input\x12\x33\n\x06\x63hoice\x18\x07 \x01(\x0b\x32\x19.services.agent.v0.ChoiceH\x00R\x06\x63hoice\x12<\n\tselection\x18\x08 \x01(\x0b\x32\x1c.services.agent.v0.SelectionH\x00R\tselectionB\x07\n\x05value\"\xfc\x02\n\x06\x41nswer\x12\x12\n\x04\x64one\x18\x01 \x01(\x08R\x04\x64one\x12\x34\n\x07\x63hannel\x18\x02 \x01(\x0b\x32\x1a.services.agent.v0.ChannelR\x07\x63hannel\x12\x14\n\x05round\x18\x03 \x01(\x05R\x05round\x12\x14\n\x05\x65rror\x18\x04 \x01(\tR\x05\x65rror\x12<\n\x07\x63onfirm\x18\x05 \x01(\x0b\x32 .services.agent.v0.ConfirmAnswerH\x00R\x07\x63onfirm\x12\x36\n\x05input\x18\x06 \x01(\x0b\x32\x1e.services.agent.v0.InputAnswerH\x00R\x05input\x12\x39\n\x06\x63hoice\x18\x07 \x01(\x0b\x32\x1f.services.agent.v0.ChoiceAnswerH\x00R\x06\x63hoice\x12\x42\n\tselection\x18\x08 \x01(\x0b\x32\".services.agent.v0.SelectionAnswerH\x00R\tselectionB\x07\n\x05value\"\xe4\x01\n\x06\x45ngage\x12\x32\n\x04mode\x18\x01 \x01(\x0e\x32\x1e.services.agent.v0.Engage.ModeR\x04mode\x12\x14\n\x05stage\x18\x02 \x01(\tR\x05stage\x12\x34\n\x07\x63hannel\x18\x03 \x01(\x0b\x32\x1a.services.agent.v0.ChannelR\x07\x63hannel\x12\x31\n\x06\x61nswer\x18\x04 \x01(\x0b\x32\x19.services.agent.v0.AnswerR\x06\x61nswer\"\'\n\x04Mode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05START\x10\x01\x12\x07\n\x03\x45ND\x10\x02\"a\n\x12InformationRequest\x12\x37\n\x08question\x18\x01 \x01(\x0b\x32\x1b.services.agent.v0.QuestionR\x08question\x12\x12\n\x04\x64one\x18\x02 \x01(\x08R\x04\x64oneB\xcb\x01\n\x15\x63om.services.agent.v0B\x10\x43ommunicateProtoP\x01Z:github.com/codefly-dev/core/generated/go/services/agent/v0\xa2\x02\x03SAV\xaa\x02\x11Services.Agent.V0\xca\x02\x11Services\\Agent\\V0\xe2\x02\x1dServices\\Agent\\V0\\GPBMetadata\xea\x02\x13Services::Agent::V0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.agent.v0.communicate_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.services.agent.v0B\020CommunicateProtoP\001Z:github.com/codefly-dev/core/generated/go/services/agent/v0\242\002\003SAV\252\002\021Services.Agent.V0\312\002\021Services\\Agent\\V0\342\002\035Services\\Agent\\V0\\GPBMetadata\352\002\023Services::Agent::V0'
  _globals['_DISPLAY_DATAENTRY']._options = None
  _globals['_DISPLAY_DATAENTRY']._serialized_options = b'8\001'
  _globals['_CHANNEL']._serialized_start=58
  _globals['_CHANNEL']._serialized_end=87
  _globals['_MESSAGE']._serialized_start=89
  _globals['_MESSAGE']._serialized_end=178
  _globals['_DISPLAY']._serialized_start=180
  _globals['_DISPLAY']._serialized_end=304
  _globals['_DISPLAY_DATAENTRY']._serialized_start=249
  _globals['_DISPLAY_DATAENTRY']._serialized_end=304
  _globals['_CONFIRM']._serialized_start=306
  _globals['_CONFIRM']._serialized_end=341
  _globals['_CONFIRMANSWER']._serialized_start=343
  _globals['_CONFIRMANSWER']._serialized_end=388
  _globals['_INPUT']._serialized_start=390
  _globals['_INPUT']._serialized_end=484
  _globals['_INPUTANSWER']._serialized_start=486
  _globals['_INPUTANSWER']._serialized_end=577
  _globals['_CHOICE']._serialized_start=579
  _globals['_CHOICE']._serialized_end=641
  _globals['_CHOICEANSWER']._serialized_start=643
  _globals['_CHOICEANSWER']._serialized_end=681
  _globals['_SELECTION']._serialized_start=683
  _globals['_SELECTION']._serialized_end=748
  _globals['_SELECTIONANSWER']._serialized_start=750
  _globals['_SELECTIONANSWER']._serialized_end=795
  _globals['_QUESTION']._serialized_start=798
  _globals['_QUESTION']._serialized_end=1224
  _globals['_ANSWER']._serialized_start=1227
  _globals['_ANSWER']._serialized_end=1607
  _globals['_ENGAGE']._serialized_start=1610
  _globals['_ENGAGE']._serialized_end=1838
  _globals['_ENGAGE_MODE']._serialized_start=1799
  _globals['_ENGAGE_MODE']._serialized_end=1838
  _globals['_INFORMATIONREQUEST']._serialized_start=1840
  _globals['_INFORMATIONREQUEST']._serialized_end=1937
# @@protoc_insertion_point(module_scope)
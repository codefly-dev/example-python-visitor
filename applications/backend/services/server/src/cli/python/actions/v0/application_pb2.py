# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: actions/v0/application.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61\x63tions/v0/application.proto\x12\nactions.v0\x1a\x1b\x62uf/validate/validate.proto\"\x91\x01\n\x0eNewApplication\x12\x12\n\x04kind\x18\x01 \x01(\tR\x04kind\x12\x1d\n\x04name\x18\x02 \x01(\tB\t\xbaH\x06r\x04\x10\x03\x18\x32R\x04name\x12*\n\x0cproject_path\x18\x03 \x01(\tB\x07\xbaH\x04r\x02\x10\x03R\x0bprojectPath\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\"\x9c\x01\n\x19\x41\x64\x64\x41pplicationToWorkspace\x12\x12\n\x04kind\x18\x01 \x01(\tR\x04kind\x12\x1d\n\x04name\x18\x02 \x01(\tB\t\xbaH\x06r\x04\x10\x03\x18\x32R\x04name\x12#\n\x07project\x18\x03 \x01(\tB\t\xbaH\x06r\x04\x10\x03\x18\x32R\x07project\x12\'\n\tworkspace\x18\x04 \x01(\tB\t\xbaH\x06r\x04\x10\x03\x18\x32R\tworkspace\"\x97\x01\n\x14SetApplicationActive\x12\x12\n\x04kind\x18\x01 \x01(\tR\x04kind\x12\x1d\n\x04name\x18\x02 \x01(\tB\t\xbaH\x06r\x04\x10\x03\x18\x32R\x04name\x12#\n\x07project\x18\x03 \x01(\tB\t\xbaH\x06r\x04\x10\x03\x18\x32R\x07project\x12\'\n\tworkspace\x18\x04 \x01(\tB\t\xbaH\x06r\x04\x10\x03\x18\x32R\tworkspaceB\xa0\x01\n\x0e\x63om.actions.v0B\x10\x41pplicationProtoP\x01Z3github.com/codefly-dev/core/generated/go/actions/v0\xa2\x02\x03\x41VX\xaa\x02\nActions.V0\xca\x02\nActions\\V0\xe2\x02\x16\x41\x63tions\\V0\\GPBMetadata\xea\x02\x0b\x41\x63tions::V0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'actions.v0.application_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\016com.actions.v0B\020ApplicationProtoP\001Z3github.com/codefly-dev/core/generated/go/actions/v0\242\002\003AVX\252\002\nActions.V0\312\002\nActions\\V0\342\002\026Actions\\V0\\GPBMetadata\352\002\013Actions::V0'
  _globals['_NEWAPPLICATION'].fields_by_name['name']._options = None
  _globals['_NEWAPPLICATION'].fields_by_name['name']._serialized_options = b'\272H\006r\004\020\003\0302'
  _globals['_NEWAPPLICATION'].fields_by_name['project_path']._options = None
  _globals['_NEWAPPLICATION'].fields_by_name['project_path']._serialized_options = b'\272H\004r\002\020\003'
  _globals['_ADDAPPLICATIONTOWORKSPACE'].fields_by_name['name']._options = None
  _globals['_ADDAPPLICATIONTOWORKSPACE'].fields_by_name['name']._serialized_options = b'\272H\006r\004\020\003\0302'
  _globals['_ADDAPPLICATIONTOWORKSPACE'].fields_by_name['project']._options = None
  _globals['_ADDAPPLICATIONTOWORKSPACE'].fields_by_name['project']._serialized_options = b'\272H\006r\004\020\003\0302'
  _globals['_ADDAPPLICATIONTOWORKSPACE'].fields_by_name['workspace']._options = None
  _globals['_ADDAPPLICATIONTOWORKSPACE'].fields_by_name['workspace']._serialized_options = b'\272H\006r\004\020\003\0302'
  _globals['_SETAPPLICATIONACTIVE'].fields_by_name['name']._options = None
  _globals['_SETAPPLICATIONACTIVE'].fields_by_name['name']._serialized_options = b'\272H\006r\004\020\003\0302'
  _globals['_SETAPPLICATIONACTIVE'].fields_by_name['project']._options = None
  _globals['_SETAPPLICATIONACTIVE'].fields_by_name['project']._serialized_options = b'\272H\006r\004\020\003\0302'
  _globals['_SETAPPLICATIONACTIVE'].fields_by_name['workspace']._options = None
  _globals['_SETAPPLICATIONACTIVE'].fields_by_name['workspace']._serialized_options = b'\272H\006r\004\020\003\0302'
  _globals['_NEWAPPLICATION']._serialized_start=74
  _globals['_NEWAPPLICATION']._serialized_end=219
  _globals['_ADDAPPLICATIONTOWORKSPACE']._serialized_start=222
  _globals['_ADDAPPLICATIONTOWORKSPACE']._serialized_end=378
  _globals['_SETAPPLICATIONACTIVE']._serialized_start=381
  _globals['_SETAPPLICATIONACTIVE']._serialized_end=532
# @@protoc_insertion_point(module_scope)
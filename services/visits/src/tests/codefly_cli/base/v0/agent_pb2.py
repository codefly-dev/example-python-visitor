# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base/v0/agent.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x62\x61se/v0/agent.proto\x12\x07\x62\x61se.v0\x1a\x1b\x62uf/validate/validate.proto\"\xb4\x01\n\x05\x41gent\x12\'\n\x04kind\x18\x01 \x01(\x0e\x32\x13.base.v0.Agent.KindR\x04kind\x12\x1d\n\x04name\x18\x02 \x01(\tB\t\xbaH\x06r\x04\x10\x02\x18\x32R\x04name\x12\'\n\tpublisher\x18\x03 \x01(\tB\t\xbaH\x06r\x04\x10\x03\x18\x32R\tpublisher\x12\x18\n\x07version\x18\x04 \x01(\tR\x07version\" \n\x04Kind\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SERVICE\x10\x01\x42\x88\x01\n\x0b\x63om.base.v0B\nAgentProtoP\x01Z0github.com/codefly-dev/core/generated/go/base/v0\xa2\x02\x03\x42VX\xaa\x02\x07\x42\x61se.V0\xca\x02\x07\x42\x61se\\V0\xe2\x02\x13\x42\x61se\\V0\\GPBMetadata\xea\x02\x08\x42\x61se::V0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'base.v0.agent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\013com.base.v0B\nAgentProtoP\001Z0github.com/codefly-dev/core/generated/go/base/v0\242\002\003BVX\252\002\007Base.V0\312\002\007Base\\V0\342\002\023Base\\V0\\GPBMetadata\352\002\010Base::V0'
  _globals['_AGENT'].fields_by_name['name']._loaded_options = None
  _globals['_AGENT'].fields_by_name['name']._serialized_options = b'\272H\006r\004\020\002\0302'
  _globals['_AGENT'].fields_by_name['publisher']._loaded_options = None
  _globals['_AGENT'].fields_by_name['publisher']._serialized_options = b'\272H\006r\004\020\003\0302'
  _globals['_AGENT']._serialized_start=62
  _globals['_AGENT']._serialized_end=242
  _globals['_AGENT_KIND']._serialized_start=210
  _globals['_AGENT_KIND']._serialized_end=242
# @@protoc_insertion_point(module_scope)
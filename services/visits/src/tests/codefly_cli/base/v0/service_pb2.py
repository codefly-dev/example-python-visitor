# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base/v0/service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from base.v0 import endpoint_pb2 as base_dot_v0_dot_endpoint__pb2
from base.v0 import agent_pb2 as base_dot_v0_dot_agent__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x62\x61se/v0/service.proto\x12\x07\x62\x61se.v0\x1a\x1b\x62uf/validate/validate.proto\x1a\x16\x62\x61se/v0/endpoint.proto\x1a\x13\x62\x61se/v0/agent.proto\"T\n\x10ServiceReference\x12\x1d\n\x04name\x18\x01 \x01(\tB\t\xbaH\x06r\x04\x10\x03\x18\x32R\x04name\x12!\n\x06module\x18\x02 \x01(\tB\t\xbaH\x06r\x04\x10\x03\x18\x32R\x06module\"\xef\x01\n\x07Service\x12\x1d\n\x04name\x18\x01 \x01(\tB\t\xbaH\x06r\x04\x10\x03\x18\x32R\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12$\n\x05\x61gent\x18\x03 \x01(\x0b\x32\x0e.base.v0.AgentR\x05\x61gent\x12/\n\tendpoints\x18\x04 \x03(\x0b\x32\x11.base.v0.EndpointR\tendpoints\x12L\n\x14service_dependencies\x18\x05 \x03(\x0b\x32\x19.base.v0.ServiceReferenceR\x13serviceDependencies\"#\n\x07Version\x12\x18\n\x07version\x18\x01 \x01(\tR\x07version\"\xc8\x01\n\x0fServiceIdentity\x12\x1d\n\x04name\x18\x01 \x01(\tB\t\xbaH\x06r\x04\x10\x03\x18\x32R\x04name\x12!\n\x06module\x18\x02 \x01(\tB\t\xbaH\x06r\x04\x10\x03\x18\x32R\x06module\x12\'\n\tworkspace\x18\x03 \x01(\tB\t\xbaH\x06r\x04\x10\x03\x18\x32R\tworkspace\x12#\n\x07version\x18\x04 \x01(\tB\t\xbaH\x06r\x04\x10\x03\x18\x32R\x07version\x12%\n\x08location\x18\x05 \x01(\tB\t\xbaH\x06r\x04\x10\x03\x18\x32R\x08locationB\x8a\x01\n\x0b\x63om.base.v0B\x0cServiceProtoP\x01Z0github.com/codefly-dev/core/generated/go/base/v0\xa2\x02\x03\x42VX\xaa\x02\x07\x42\x61se.V0\xca\x02\x07\x42\x61se\\V0\xe2\x02\x13\x42\x61se\\V0\\GPBMetadata\xea\x02\x08\x42\x61se::V0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'base.v0.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\013com.base.v0B\014ServiceProtoP\001Z0github.com/codefly-dev/core/generated/go/base/v0\242\002\003BVX\252\002\007Base.V0\312\002\007Base\\V0\342\002\023Base\\V0\\GPBMetadata\352\002\010Base::V0'
  _globals['_SERVICEREFERENCE'].fields_by_name['name']._loaded_options = None
  _globals['_SERVICEREFERENCE'].fields_by_name['name']._serialized_options = b'\272H\006r\004\020\003\0302'
  _globals['_SERVICEREFERENCE'].fields_by_name['module']._loaded_options = None
  _globals['_SERVICEREFERENCE'].fields_by_name['module']._serialized_options = b'\272H\006r\004\020\003\0302'
  _globals['_SERVICE'].fields_by_name['name']._loaded_options = None
  _globals['_SERVICE'].fields_by_name['name']._serialized_options = b'\272H\006r\004\020\003\0302'
  _globals['_SERVICEIDENTITY'].fields_by_name['name']._loaded_options = None
  _globals['_SERVICEIDENTITY'].fields_by_name['name']._serialized_options = b'\272H\006r\004\020\003\0302'
  _globals['_SERVICEIDENTITY'].fields_by_name['module']._loaded_options = None
  _globals['_SERVICEIDENTITY'].fields_by_name['module']._serialized_options = b'\272H\006r\004\020\003\0302'
  _globals['_SERVICEIDENTITY'].fields_by_name['workspace']._loaded_options = None
  _globals['_SERVICEIDENTITY'].fields_by_name['workspace']._serialized_options = b'\272H\006r\004\020\003\0302'
  _globals['_SERVICEIDENTITY'].fields_by_name['version']._loaded_options = None
  _globals['_SERVICEIDENTITY'].fields_by_name['version']._serialized_options = b'\272H\006r\004\020\003\0302'
  _globals['_SERVICEIDENTITY'].fields_by_name['location']._loaded_options = None
  _globals['_SERVICEIDENTITY'].fields_by_name['location']._serialized_options = b'\272H\006r\004\020\003\0302'
  _globals['_SERVICEREFERENCE']._serialized_start=108
  _globals['_SERVICEREFERENCE']._serialized_end=192
  _globals['_SERVICE']._serialized_start=195
  _globals['_SERVICE']._serialized_end=434
  _globals['_VERSION']._serialized_start=436
  _globals['_VERSION']._serialized_end=471
  _globals['_SERVICEIDENTITY']._serialized_start=474
  _globals['_SERVICEIDENTITY']._serialized_end=674
# @@protoc_insertion_point(module_scope)
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base/v0/network.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base.v0 import scope_pb2 as base_dot_v0_dot_scope__pb2
from base.v0 import endpoint_pb2 as base_dot_v0_dot_endpoint__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x62\x61se/v0/network.proto\x12\x07\x62\x61se.v0\x1a\x13\x62\x61se/v0/scope.proto\x1a\x16\x62\x61se/v0/endpoint.proto\"w\n\x0eNetworkMapping\x12-\n\x08\x65ndpoint\x18\x01 \x01(\x0b\x32\x11.base.v0.EndpointR\x08\x65ndpoint\x12\x36\n\tinstances\x18\x02 \x03(\x0b\x32\x18.base.v0.NetworkInstanceR\tinstances\"\x9f\x01\n\x03\x44NS\x12\x18\n\x07project\x18\x01 \x01(\tR\x07project\x12 \n\x0b\x61pplication\x18\x02 \x01(\tR\x0b\x61pplication\x12\x18\n\x07service\x18\x03 \x01(\tR\x07service\x12\x1a\n\x08\x65ndpoint\x18\x04 \x01(\tR\x08\x65ndpoint\x12\x12\n\x04host\x18\x05 \x01(\tR\x04host\x12\x12\n\x04port\x18\x06 \x01(\rR\x04port\"\x80\x01\n\x0fNetworkInstance\x12+\n\x05scope\x18\x01 \x01(\x0e\x32\x15.base.v0.NetworkScopeR\x05scope\x12\x12\n\x04host\x18\x03 \x01(\tR\x04host\x12\x12\n\x04port\x18\x04 \x01(\rR\x04port\x12\x18\n\x07\x61\x64\x64ress\x18\x05 \x01(\tR\x07\x61\x64\x64ressB\x8a\x01\n\x0b\x63om.base.v0B\x0cNetworkProtoP\x01Z0github.com/codefly-dev/core/generated/go/base/v0\xa2\x02\x03\x42VX\xaa\x02\x07\x42\x61se.V0\xca\x02\x07\x42\x61se\\V0\xe2\x02\x13\x42\x61se\\V0\\GPBMetadata\xea\x02\x08\x42\x61se::V0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'base.v0.network_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\013com.base.v0B\014NetworkProtoP\001Z0github.com/codefly-dev/core/generated/go/base/v0\242\002\003BVX\252\002\007Base.V0\312\002\007Base\\V0\342\002\023Base\\V0\\GPBMetadata\352\002\010Base::V0'
  _globals['_NETWORKMAPPING']._serialized_start=79
  _globals['_NETWORKMAPPING']._serialized_end=198
  _globals['_DNS']._serialized_start=201
  _globals['_DNS']._serialized_end=360
  _globals['_NETWORKINSTANCE']._serialized_start=363
  _globals['_NETWORKINSTANCE']._serialized_end=491
# @@protoc_insertion_point(module_scope)

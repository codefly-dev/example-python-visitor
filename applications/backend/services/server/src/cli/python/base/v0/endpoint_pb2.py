# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base/v0/endpoint.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x62\x61se/v0/endpoint.proto\x12\x07\x62\x61se.v0\x1a\x1b\x62uf/validate/validate.proto\"\x81\x03\n\x08\x45ndpoint\x12)\n\x04name\x18\x01 \x01(\tB\x15\xbaH\x12r\x10\x10\x03\x18\x14\x32\x08^[a-z]+$h\x01R\x04name\x12\x38\n\x07service\x18\x02 \x01(\tB\x1e\xbaH\x1br\x19\x10\x03\x18\x19\x32\x0c^[a-z0-9-]+$h\x01\xba\x01\x02--R\x07service\x12@\n\x0b\x61pplication\x18\x03 \x01(\tB\x1e\xbaH\x1br\x19\x10\x03\x18\x19\x32\x0c^[a-z0-9-]+$h\x01\xba\x01\x02--R\x0b\x61pplication\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12M\n\nvisibility\x18\x05 \x01(\tB-\xbaH*r(R\x08\x65xternalR\x06publicR\x0b\x61pplicationR\x07privateR\nvisibility\x12.\n\x03\x61pi\x18\x06 \x01(\tB\x1c\xbaH\x19r\x17R\x04httpR\x04grpcR\x03tcpR\x04restR\x03\x61pi\x12-\n\x0b\x61pi_details\x18\x07 \x01(\x0b\x32\x0c.base.v0.APIR\napiDetails\"\xab\x01\n\x03\x41PI\x12#\n\x03tcp\x18\x01 \x01(\x0b\x32\x0f.base.v0.TcpAPIH\x00R\x03tcp\x12&\n\x04http\x18\x02 \x01(\x0b\x32\x10.base.v0.HttpAPIH\x00R\x04http\x12&\n\x04rest\x18\x03 \x01(\x0b\x32\x10.base.v0.RestAPIH\x00R\x04rest\x12&\n\x04grpc\x18\x04 \x01(\x0b\x32\x10.base.v0.GrpcAPIH\x00R\x04grpcB\x07\n\x05value\"n\n\x0eRestRouteGroup\x12\x30\n\x04path\x18\x01 \x01(\tB\x1c\xbaH\x19r\x17\x10\x03\x18\x19\x32\x11^/([a-z0-9-/]+)*$R\x04path\x12*\n\x06routes\x18\x02 \x03(\x0b\x32\x12.base.v0.RestRouteR\x06routes\"j\n\tRestRoute\x12\x30\n\x04path\x18\x01 \x01(\tB\x1c\xbaH\x19r\x17\x10\x03\x18\x19\x32\x11^/([a-z0-9-/]+)*$R\x04path\x12+\n\x06method\x18\x02 \x01(\x0e\x32\x13.base.v0.HTTPMethodR\x06method\"\xaa\x01\n\x07RestAPI\x12\x18\n\x07service\x18\x01 \x01(\tR\x07service\x12 \n\x0b\x61pplication\x18\x02 \x01(\tR\x0b\x61pplication\x12/\n\x06groups\x18\x03 \x03(\x0b\x32\x17.base.v0.RestRouteGroupR\x06groups\x12\x18\n\x07openapi\x18\x04 \x01(\x0cR\x07openapi\x12\x18\n\x07secured\x18\x05 \x01(\x08R\x07secured\"<\n\x03RPC\x12!\n\x0cservice_name\x18\x01 \x01(\tR\x0bserviceName\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"\xb1\x01\n\x07GrpcAPI\x12\x18\n\x07service\x18\x01 \x01(\tR\x07service\x12 \n\x0b\x61pplication\x18\x02 \x01(\tR\x0b\x61pplication\x12\x18\n\x07package\x18\x03 \x01(\tR\x07package\x12 \n\x04rpcs\x18\x04 \x03(\x0b\x32\x0c.base.v0.RPCR\x04rpcs\x12\x14\n\x05proto\x18\x05 \x01(\x0cR\x05proto\x12\x18\n\x07secured\x18\x06 \x01(\x08R\x07secured\"#\n\x07HttpAPI\x12\x18\n\x07secured\x18\x01 \x01(\x08R\x07secured\"\x08\n\x06TcpAPI*n\n\nHTTPMethod\x12\x07\n\x03GET\x10\x00\x12\x08\n\x04POST\x10\x01\x12\x07\n\x03PUT\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\x12\t\n\x05PATCH\x10\x04\x12\x0b\n\x07OPTIONS\x10\x05\x12\x08\n\x04HEAD\x10\x06\x12\x0b\n\x07\x43ONNECT\x10\x07\x12\t\n\x05TRACE\x10\x08\x42\x8b\x01\n\x0b\x63om.base.v0B\rEndpointProtoP\x01Z0github.com/codefly-dev/core/generated/go/base/v0\xa2\x02\x03\x42VX\xaa\x02\x07\x42\x61se.V0\xca\x02\x07\x42\x61se\\V0\xe2\x02\x13\x42\x61se\\V0\\GPBMetadata\xea\x02\x08\x42\x61se::V0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'base.v0.endpoint_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\013com.base.v0B\rEndpointProtoP\001Z0github.com/codefly-dev/core/generated/go/base/v0\242\002\003BVX\252\002\007Base.V0\312\002\007Base\\V0\342\002\023Base\\V0\\GPBMetadata\352\002\010Base::V0'
  _globals['_ENDPOINT'].fields_by_name['name']._options = None
  _globals['_ENDPOINT'].fields_by_name['name']._serialized_options = b'\272H\022r\020\020\003\030\0242\010^[a-z]+$h\001'
  _globals['_ENDPOINT'].fields_by_name['service']._options = None
  _globals['_ENDPOINT'].fields_by_name['service']._serialized_options = b'\272H\033r\031\020\003\030\0312\014^[a-z0-9-]+$h\001\272\001\002--'
  _globals['_ENDPOINT'].fields_by_name['application']._options = None
  _globals['_ENDPOINT'].fields_by_name['application']._serialized_options = b'\272H\033r\031\020\003\030\0312\014^[a-z0-9-]+$h\001\272\001\002--'
  _globals['_ENDPOINT'].fields_by_name['visibility']._options = None
  _globals['_ENDPOINT'].fields_by_name['visibility']._serialized_options = b'\272H*r(R\010externalR\006publicR\013applicationR\007private'
  _globals['_ENDPOINT'].fields_by_name['api']._options = None
  _globals['_ENDPOINT'].fields_by_name['api']._serialized_options = b'\272H\031r\027R\004httpR\004grpcR\003tcpR\004rest'
  _globals['_RESTROUTEGROUP'].fields_by_name['path']._options = None
  _globals['_RESTROUTEGROUP'].fields_by_name['path']._serialized_options = b'\272H\031r\027\020\003\030\0312\021^/([a-z0-9-/]+)*$'
  _globals['_RESTROUTE'].fields_by_name['path']._options = None
  _globals['_RESTROUTE'].fields_by_name['path']._serialized_options = b'\272H\031r\027\020\003\030\0312\021^/([a-z0-9-/]+)*$'
  _globals['_HTTPMETHOD']._serialized_start=1308
  _globals['_HTTPMETHOD']._serialized_end=1418
  _globals['_ENDPOINT']._serialized_start=65
  _globals['_ENDPOINT']._serialized_end=450
  _globals['_API']._serialized_start=453
  _globals['_API']._serialized_end=624
  _globals['_RESTROUTEGROUP']._serialized_start=626
  _globals['_RESTROUTEGROUP']._serialized_end=736
  _globals['_RESTROUTE']._serialized_start=738
  _globals['_RESTROUTE']._serialized_end=844
  _globals['_RESTAPI']._serialized_start=847
  _globals['_RESTAPI']._serialized_end=1017
  _globals['_RPC']._serialized_start=1019
  _globals['_RPC']._serialized_end=1079
  _globals['_GRPCAPI']._serialized_start=1082
  _globals['_GRPCAPI']._serialized_end=1259
  _globals['_HTTPAPI']._serialized_start=1261
  _globals['_HTTPAPI']._serialized_end=1296
  _globals['_TCPAPI']._serialized_start=1298
  _globals['_TCPAPI']._serialized_end=1306
# @@protoc_insertion_point(module_scope)

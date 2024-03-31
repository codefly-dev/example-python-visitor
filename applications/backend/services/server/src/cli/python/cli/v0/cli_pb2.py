# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cli/v0/cli.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base.v0 import endpoint_pb2 as base_dot_v0_dot_endpoint__pb2
from base.v0 import project_pb2 as base_dot_v0_dot_project__pb2
from base.v0 import configuration_pb2 as base_dot_v0_dot_configuration__pb2
from services.agent.v0 import agent_pb2 as services_dot_agent_dot_v0_dot_agent__pb2
from services.runtime.v0 import runtime_pb2 as services_dot_runtime_dot_v0_dot_runtime__pb2
from observability.v0 import inventory_pb2 as observability_dot_v0_dot_inventory__pb2
from observability.v0 import dependencies_pb2 as observability_dot_v0_dot_dependencies__pb2
from observability.v0 import logs_pb2 as observability_dot_v0_dot_logs__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63li/v0/cli.proto\x12\x10observability.v0\x1a\x16\x62\x61se/v0/endpoint.proto\x1a\x15\x62\x61se/v0/project.proto\x1a\x1b\x62\x61se/v0/configuration.proto\x1a\x1dservices/agent/v0/agent.proto\x1a!services/runtime/v0/runtime.proto\x1a observability/v0/inventory.proto\x1a#observability/v0/dependencies.proto\x1a\x1bobservability/v0/logs.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"1\n\x13GetProjectsResponse\x12\x1a\n\x08projects\x18\x01 \x03(\tR\x08projects\"*\n\x0eProjectRequest\x12\x18\n\x07project\x18\x01 \x01(\tR\x07project\"2\n\x1aGetAgentInformationRequest\x12\x14\n\x05\x61gent\x18\x01 \x01(\tR\x05\x61gent\"M\n\x12MultiGraphResponse\x12\x37\n\x06graphs\x18\x01 \x03(\x0b\x32\x1f.observability.v0.GraphResponseR\x06graphs\"f\n\x0e\x41\x63tiveResponse\x12\x18\n\x07project\x18\x01 \x01(\tR\x07project\x12 \n\x0b\x61pplication\x18\x02 \x01(\tR\x0b\x61pplication\x12\x18\n\x07service\x18\x03 \x01(\tR\x07service\"m\n\x12RunningInformation\x12 \n\x0b\x61pplication\x18\x01 \x01(\tR\x0b\x61pplication\x12\x18\n\x07service\x18\x02 \x01(\tR\x07service\x12\x1b\n\tagent_pid\x18\x03 \x01(\x05R\x08\x61gentPid\"k\n\x11GetAddressRequest\x12 \n\x0b\x61pplication\x18\x01 \x01(\tR\x0b\x61pplication\x12\x18\n\x07service\x18\x02 \x01(\tR\x07service\x12\x1a\n\x08\x65ndpoint\x18\x03 \x01(\tR\x08\x65ndpoint\".\n\x12GetAddressResponse\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\"U\n\x17GetConfigurationRequest\x12 \n\x0b\x61pplication\x18\x01 \x01(\tR\x0b\x61pplication\x12\x18\n\x07service\x18\x02 \x01(\tR\x07service\"Z\n\x18GetConfigurationResponse\x12>\n\x0e\x63onfigurations\x18\x01 \x03(\x0b\x32\x16.base.v0.ConfigurationR\x0e\x63onfigurations\"\"\n\nFlowStatus\x12\x14\n\x05ready\x18\x01 \x01(\x08R\x05ready2\x82\x0e\n\x03\x43LI\x12\x45\n\x04Ping\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\r\x82\xd3\xe4\x93\x02\x07\x12\x05/ping\x12\x94\x01\n\x13GetAgentInformation\x12,.observability.v0.GetAgentInformationRequest\x1a#.services.agent.v0.AgentInformation\"*\x82\xd3\xe4\x93\x02$\x12\"/overall/agent/{agent}/information\x12r\n\x0bGetProjects\x12\x16.google.protobuf.Empty\x1a%.observability.v0.GetProjectsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/overall/project/information\x12w\n\x13GetProjectInventory\x12 .observability.v0.ProjectRequest\x1a\x10.base.v0.Project\",\x82\xd3\xe4\x93\x02&\x12$/overall/project/{project}/inventory\x12\xa2\x01\n GetProjectServiceDependencyGraph\x12 .observability.v0.ProjectRequest\x1a\x1f.observability.v0.GraphResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/overall/project/{project}/service-dependency-graph\x12\xb3\x01\n+GetProjectPublicApplicationsDependencyGraph\x12 .observability.v0.ProjectRequest\x1a$.observability.v0.MultiGraphResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/overall/project/{project}/public-applications-graph\x12p\n\nLogHistory\x12\x1c.observability.v0.LogRequest\x1a\x1d.observability.v0.LogResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/overall/project/logs/history\x12j\n\tGetActive\x12\x16.google.protobuf.Empty\x1a .observability.v0.ActiveResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/active/project/information\x12\xa5\x01\n\x0cGetAddresses\x12#.observability.v0.GetAddressRequest\x1a$.observability.v0.GetAddressResponse\"J\x82\xd3\xe4\x93\x02\x44\x12\x42/active/project/network-mapping/{application}/{service}/{endpoint}\x12\xb5\x01\n\x16GetSharedConfiguration\x12).observability.v0.GetConfigurationRequest\x1a*.observability.v0.GetConfigurationResponse\"D\x82\xd3\xe4\x93\x02>\x12</active/project/shared-configuration/{application}/{service}\x12U\n\x04Logs\x12\x16.google.protobuf.Empty\x1a\x15.observability.v0.Log\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/active/project/logs0\x01\x12u\n\x10\x41\x63tiveLogHistory\x12\x1c.observability.v0.LogRequest\x1a\x1d.observability.v0.LogResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/active/project/logs/history\x12j\n\rGetFlowStatus\x12\x16.google.protobuf.Empty\x1a\x1c.observability.v0.FlowStatus\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/active/project/flow/status\x12]\n\x08StopFlow\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"!\x82\xd3\xe4\x93\x02\x1b\"\x19/active/project/flow/stopB\xb2\x01\n\x14\x63om.observability.v0B\x08\x43liProtoP\x01Z/github.com/codefly-dev/core/generated/go/cli/v0\xa2\x02\x03OVX\xaa\x02\x10Observability.V0\xca\x02\x10Observability\\V0\xe2\x02\x1cObservability\\V0\\GPBMetadata\xea\x02\x11Observability::V0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cli.v0.cli_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.observability.v0B\010CliProtoP\001Z/github.com/codefly-dev/core/generated/go/cli/v0\242\002\003OVX\252\002\020Observability.V0\312\002\020Observability\\V0\342\002\034Observability\\V0\\GPBMetadata\352\002\021Observability::V0'
  _globals['_CLI'].methods_by_name['Ping']._options = None
  _globals['_CLI'].methods_by_name['Ping']._serialized_options = b'\202\323\344\223\002\007\022\005/ping'
  _globals['_CLI'].methods_by_name['GetAgentInformation']._options = None
  _globals['_CLI'].methods_by_name['GetAgentInformation']._serialized_options = b'\202\323\344\223\002$\022\"/overall/agent/{agent}/information'
  _globals['_CLI'].methods_by_name['GetProjects']._options = None
  _globals['_CLI'].methods_by_name['GetProjects']._serialized_options = b'\202\323\344\223\002\036\022\034/overall/project/information'
  _globals['_CLI'].methods_by_name['GetProjectInventory']._options = None
  _globals['_CLI'].methods_by_name['GetProjectInventory']._serialized_options = b'\202\323\344\223\002&\022$/overall/project/{project}/inventory'
  _globals['_CLI'].methods_by_name['GetProjectServiceDependencyGraph']._options = None
  _globals['_CLI'].methods_by_name['GetProjectServiceDependencyGraph']._serialized_options = b'\202\323\344\223\0025\0223/overall/project/{project}/service-dependency-graph'
  _globals['_CLI'].methods_by_name['GetProjectPublicApplicationsDependencyGraph']._options = None
  _globals['_CLI'].methods_by_name['GetProjectPublicApplicationsDependencyGraph']._serialized_options = b'\202\323\344\223\0026\0224/overall/project/{project}/public-applications-graph'
  _globals['_CLI'].methods_by_name['LogHistory']._options = None
  _globals['_CLI'].methods_by_name['LogHistory']._serialized_options = b'\202\323\344\223\002\037\022\035/overall/project/logs/history'
  _globals['_CLI'].methods_by_name['GetActive']._options = None
  _globals['_CLI'].methods_by_name['GetActive']._serialized_options = b'\202\323\344\223\002\035\022\033/active/project/information'
  _globals['_CLI'].methods_by_name['GetAddresses']._options = None
  _globals['_CLI'].methods_by_name['GetAddresses']._serialized_options = b'\202\323\344\223\002D\022B/active/project/network-mapping/{application}/{service}/{endpoint}'
  _globals['_CLI'].methods_by_name['GetSharedConfiguration']._options = None
  _globals['_CLI'].methods_by_name['GetSharedConfiguration']._serialized_options = b'\202\323\344\223\002>\022</active/project/shared-configuration/{application}/{service}'
  _globals['_CLI'].methods_by_name['Logs']._options = None
  _globals['_CLI'].methods_by_name['Logs']._serialized_options = b'\202\323\344\223\002\026\022\024/active/project/logs'
  _globals['_CLI'].methods_by_name['ActiveLogHistory']._options = None
  _globals['_CLI'].methods_by_name['ActiveLogHistory']._serialized_options = b'\202\323\344\223\002\036\022\034/active/project/logs/history'
  _globals['_CLI'].methods_by_name['GetFlowStatus']._options = None
  _globals['_CLI'].methods_by_name['GetFlowStatus']._serialized_options = b'\202\323\344\223\002\035\022\033/active/project/flow/status'
  _globals['_CLI'].methods_by_name['StopFlow']._options = None
  _globals['_CLI'].methods_by_name['StopFlow']._serialized_options = b'\202\323\344\223\002\033\"\031/active/project/flow/stop'
  _globals['_GETPROJECTSRESPONSE']._serialized_start=372
  _globals['_GETPROJECTSRESPONSE']._serialized_end=421
  _globals['_PROJECTREQUEST']._serialized_start=423
  _globals['_PROJECTREQUEST']._serialized_end=465
  _globals['_GETAGENTINFORMATIONREQUEST']._serialized_start=467
  _globals['_GETAGENTINFORMATIONREQUEST']._serialized_end=517
  _globals['_MULTIGRAPHRESPONSE']._serialized_start=519
  _globals['_MULTIGRAPHRESPONSE']._serialized_end=596
  _globals['_ACTIVERESPONSE']._serialized_start=598
  _globals['_ACTIVERESPONSE']._serialized_end=700
  _globals['_RUNNINGINFORMATION']._serialized_start=702
  _globals['_RUNNINGINFORMATION']._serialized_end=811
  _globals['_GETADDRESSREQUEST']._serialized_start=813
  _globals['_GETADDRESSREQUEST']._serialized_end=920
  _globals['_GETADDRESSRESPONSE']._serialized_start=922
  _globals['_GETADDRESSRESPONSE']._serialized_end=968
  _globals['_GETCONFIGURATIONREQUEST']._serialized_start=970
  _globals['_GETCONFIGURATIONREQUEST']._serialized_end=1055
  _globals['_GETCONFIGURATIONRESPONSE']._serialized_start=1057
  _globals['_GETCONFIGURATIONRESPONSE']._serialized_end=1147
  _globals['_FLOWSTATUS']._serialized_start=1149
  _globals['_FLOWSTATUS']._serialized_end=1183
  _globals['_CLI']._serialized_start=1186
  _globals['_CLI']._serialized_end=2980
# @@protoc_insertion_point(module_scope)

from google.protobuf import any_pb2 as _any_pb2
from xds.annotations.v3 import status_pb2 as _status_pb2
from xds.core.v3 import resource_name_pb2 as _resource_name_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Resource(_message.Message):
    __slots__ = ("name", "version", "resource")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    name: _resource_name_pb2.ResourceName
    version: str
    resource: _any_pb2.Any
    def __init__(self, name: _Optional[_Union[_resource_name_pb2.ResourceName, _Mapping]] = ..., version: _Optional[str] = ..., resource: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

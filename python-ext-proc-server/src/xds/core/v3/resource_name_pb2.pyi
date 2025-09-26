from xds.annotations.v3 import status_pb2 as _status_pb2
from xds.core.v3 import context_params_pb2 as _context_params_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceName(_message.Message):
    __slots__ = ("id", "authority", "resource_type", "context")
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    authority: str
    resource_type: str
    context: _context_params_pb2.ContextParams
    def __init__(self, id: _Optional[str] = ..., authority: _Optional[str] = ..., resource_type: _Optional[str] = ..., context: _Optional[_Union[_context_params_pb2.ContextParams, _Mapping]] = ...) -> None: ...

from xds.annotations.v3 import status_pb2 as _status_pb2
from xds.core.v3 import context_params_pb2 as _context_params_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceLocator(_message.Message):
    __slots__ = ("scheme", "id", "authority", "resource_type", "exact_context", "directives")
    class Scheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        XDSTP: _ClassVar[ResourceLocator.Scheme]
        HTTP: _ClassVar[ResourceLocator.Scheme]
        FILE: _ClassVar[ResourceLocator.Scheme]
    XDSTP: ResourceLocator.Scheme
    HTTP: ResourceLocator.Scheme
    FILE: ResourceLocator.Scheme
    class Directive(_message.Message):
        __slots__ = ("alt", "entry")
        ALT_FIELD_NUMBER: _ClassVar[int]
        ENTRY_FIELD_NUMBER: _ClassVar[int]
        alt: ResourceLocator
        entry: str
        def __init__(self, alt: _Optional[_Union[ResourceLocator, _Mapping]] = ..., entry: _Optional[str] = ...) -> None: ...
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXACT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DIRECTIVES_FIELD_NUMBER: _ClassVar[int]
    scheme: ResourceLocator.Scheme
    id: str
    authority: str
    resource_type: str
    exact_context: _context_params_pb2.ContextParams
    directives: _containers.RepeatedCompositeFieldContainer[ResourceLocator.Directive]
    def __init__(self, scheme: _Optional[_Union[ResourceLocator.Scheme, str]] = ..., id: _Optional[str] = ..., authority: _Optional[str] = ..., resource_type: _Optional[str] = ..., exact_context: _Optional[_Union[_context_params_pb2.ContextParams, _Mapping]] = ..., directives: _Optional[_Iterable[_Union[ResourceLocator.Directive, _Mapping]]] = ...) -> None: ...

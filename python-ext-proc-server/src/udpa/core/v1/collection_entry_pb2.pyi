from google.protobuf import any_pb2 as _any_pb2
from udpa.annotations import status_pb2 as _status_pb2
from udpa.core.v1 import resource_locator_pb2 as _resource_locator_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CollectionEntry(_message.Message):
    __slots__ = ("locator", "inline_entry")
    class InlineEntry(_message.Message):
        __slots__ = ("name", "version", "resource")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        name: str
        version: str
        resource: _any_pb2.Any
        def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., resource: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
    LOCATOR_FIELD_NUMBER: _ClassVar[int]
    INLINE_ENTRY_FIELD_NUMBER: _ClassVar[int]
    locator: _resource_locator_pb2.ResourceLocator
    inline_entry: CollectionEntry.InlineEntry
    def __init__(self, locator: _Optional[_Union[_resource_locator_pb2.ResourceLocator, _Mapping]] = ..., inline_entry: _Optional[_Union[CollectionEntry.InlineEntry, _Mapping]] = ...) -> None: ...

from xds.annotations.v3 import status_pb2 as _status_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CidrRange(_message.Message):
    __slots__ = ("address_prefix", "prefix_len")
    ADDRESS_PREFIX_FIELD_NUMBER: _ClassVar[int]
    PREFIX_LEN_FIELD_NUMBER: _ClassVar[int]
    address_prefix: str
    prefix_len: _wrappers_pb2.UInt32Value
    def __init__(self, address_prefix: _Optional[str] = ..., prefix_len: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...

from xds.type.v3 import cel_pb2 as _cel_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CelMatcher(_message.Message):
    __slots__ = ("expr_match", "description")
    EXPR_MATCH_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    expr_match: _cel_pb2.CelExpression
    description: str
    def __init__(self, expr_match: _Optional[_Union[_cel_pb2.CelExpression, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

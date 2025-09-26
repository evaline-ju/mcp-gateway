from google.api.expr.v1alpha1 import checked_pb2 as _checked_pb2
from google.api.expr.v1alpha1 import syntax_pb2 as _syntax_pb2
from cel.expr import checked_pb2 as _checked_pb2_1
from cel.expr import syntax_pb2 as _syntax_pb2_1
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from xds.annotations.v3 import status_pb2 as _status_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CelExpression(_message.Message):
    __slots__ = ("parsed_expr", "checked_expr", "cel_expr_parsed", "cel_expr_checked", "cel_expr_string")
    PARSED_EXPR_FIELD_NUMBER: _ClassVar[int]
    CHECKED_EXPR_FIELD_NUMBER: _ClassVar[int]
    CEL_EXPR_PARSED_FIELD_NUMBER: _ClassVar[int]
    CEL_EXPR_CHECKED_FIELD_NUMBER: _ClassVar[int]
    CEL_EXPR_STRING_FIELD_NUMBER: _ClassVar[int]
    parsed_expr: _syntax_pb2.ParsedExpr
    checked_expr: _checked_pb2.CheckedExpr
    cel_expr_parsed: _syntax_pb2_1.ParsedExpr
    cel_expr_checked: _checked_pb2_1.CheckedExpr
    cel_expr_string: str
    def __init__(self, parsed_expr: _Optional[_Union[_syntax_pb2.ParsedExpr, _Mapping]] = ..., checked_expr: _Optional[_Union[_checked_pb2.CheckedExpr, _Mapping]] = ..., cel_expr_parsed: _Optional[_Union[_syntax_pb2_1.ParsedExpr, _Mapping]] = ..., cel_expr_checked: _Optional[_Union[_checked_pb2_1.CheckedExpr, _Mapping]] = ..., cel_expr_string: _Optional[str] = ...) -> None: ...

class CelExtractString(_message.Message):
    __slots__ = ("expr_extract", "default_value")
    EXPR_EXTRACT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    expr_extract: CelExpression
    default_value: _wrappers_pb2.StringValue
    def __init__(self, expr_extract: _Optional[_Union[CelExpression, _Mapping]] = ..., default_value: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

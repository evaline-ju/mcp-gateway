from xds.annotations.v3 import status_pb2 as _status_pb2
from xds.core.v3 import cidr_pb2 as _cidr_pb2
from xds.type.matcher.v3 import matcher_pb2 as _matcher_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IPMatcher(_message.Message):
    __slots__ = ("range_matchers",)
    class IPRangeMatcher(_message.Message):
        __slots__ = ("ranges", "on_match", "exclusive")
        RANGES_FIELD_NUMBER: _ClassVar[int]
        ON_MATCH_FIELD_NUMBER: _ClassVar[int]
        EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
        ranges: _containers.RepeatedCompositeFieldContainer[_cidr_pb2.CidrRange]
        on_match: _matcher_pb2.Matcher.OnMatch
        exclusive: bool
        def __init__(self, ranges: _Optional[_Iterable[_Union[_cidr_pb2.CidrRange, _Mapping]]] = ..., on_match: _Optional[_Union[_matcher_pb2.Matcher.OnMatch, _Mapping]] = ..., exclusive: bool = ...) -> None: ...
    RANGE_MATCHERS_FIELD_NUMBER: _ClassVar[int]
    range_matchers: _containers.RepeatedCompositeFieldContainer[IPMatcher.IPRangeMatcher]
    def __init__(self, range_matchers: _Optional[_Iterable[_Union[IPMatcher.IPRangeMatcher, _Mapping]]] = ...) -> None: ...

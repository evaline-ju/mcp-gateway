from xds.type.v3 import range_pb2 as _range_pb2
from xds.type.matcher.v3 import matcher_pb2 as _matcher_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Int64RangeMatcher(_message.Message):
    __slots__ = ("range_matchers",)
    class RangeMatcher(_message.Message):
        __slots__ = ("ranges", "on_match")
        RANGES_FIELD_NUMBER: _ClassVar[int]
        ON_MATCH_FIELD_NUMBER: _ClassVar[int]
        ranges: _containers.RepeatedCompositeFieldContainer[_range_pb2.Int64Range]
        on_match: _matcher_pb2.Matcher.OnMatch
        def __init__(self, ranges: _Optional[_Iterable[_Union[_range_pb2.Int64Range, _Mapping]]] = ..., on_match: _Optional[_Union[_matcher_pb2.Matcher.OnMatch, _Mapping]] = ...) -> None: ...
    RANGE_MATCHERS_FIELD_NUMBER: _ClassVar[int]
    range_matchers: _containers.RepeatedCompositeFieldContainer[Int64RangeMatcher.RangeMatcher]
    def __init__(self, range_matchers: _Optional[_Iterable[_Union[Int64RangeMatcher.RangeMatcher, _Mapping]]] = ...) -> None: ...

class Int32RangeMatcher(_message.Message):
    __slots__ = ("range_matchers",)
    class RangeMatcher(_message.Message):
        __slots__ = ("ranges", "on_match")
        RANGES_FIELD_NUMBER: _ClassVar[int]
        ON_MATCH_FIELD_NUMBER: _ClassVar[int]
        ranges: _containers.RepeatedCompositeFieldContainer[_range_pb2.Int32Range]
        on_match: _matcher_pb2.Matcher.OnMatch
        def __init__(self, ranges: _Optional[_Iterable[_Union[_range_pb2.Int32Range, _Mapping]]] = ..., on_match: _Optional[_Union[_matcher_pb2.Matcher.OnMatch, _Mapping]] = ...) -> None: ...
    RANGE_MATCHERS_FIELD_NUMBER: _ClassVar[int]
    range_matchers: _containers.RepeatedCompositeFieldContainer[Int32RangeMatcher.RangeMatcher]
    def __init__(self, range_matchers: _Optional[_Iterable[_Union[Int32RangeMatcher.RangeMatcher, _Mapping]]] = ...) -> None: ...

class DoubleRangeMatcher(_message.Message):
    __slots__ = ("range_matchers",)
    class RangeMatcher(_message.Message):
        __slots__ = ("ranges", "on_match")
        RANGES_FIELD_NUMBER: _ClassVar[int]
        ON_MATCH_FIELD_NUMBER: _ClassVar[int]
        ranges: _containers.RepeatedCompositeFieldContainer[_range_pb2.DoubleRange]
        on_match: _matcher_pb2.Matcher.OnMatch
        def __init__(self, ranges: _Optional[_Iterable[_Union[_range_pb2.DoubleRange, _Mapping]]] = ..., on_match: _Optional[_Union[_matcher_pb2.Matcher.OnMatch, _Mapping]] = ...) -> None: ...
    RANGE_MATCHERS_FIELD_NUMBER: _ClassVar[int]
    range_matchers: _containers.RepeatedCompositeFieldContainer[DoubleRangeMatcher.RangeMatcher]
    def __init__(self, range_matchers: _Optional[_Iterable[_Union[DoubleRangeMatcher.RangeMatcher, _Mapping]]] = ...) -> None: ...

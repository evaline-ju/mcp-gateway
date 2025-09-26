from xds.annotations.v3 import status_pb2 as _status_pb2
from xds.type.matcher.v3 import matcher_pb2 as _matcher_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServerNameMatcher(_message.Message):
    __slots__ = ("domain_matchers",)
    class DomainMatcher(_message.Message):
        __slots__ = ("domains", "on_match")
        DOMAINS_FIELD_NUMBER: _ClassVar[int]
        ON_MATCH_FIELD_NUMBER: _ClassVar[int]
        domains: _containers.RepeatedScalarFieldContainer[str]
        on_match: _matcher_pb2.Matcher.OnMatch
        def __init__(self, domains: _Optional[_Iterable[str]] = ..., on_match: _Optional[_Union[_matcher_pb2.Matcher.OnMatch, _Mapping]] = ...) -> None: ...
    DOMAIN_MATCHERS_FIELD_NUMBER: _ClassVar[int]
    domain_matchers: _containers.RepeatedCompositeFieldContainer[ServerNameMatcher.DomainMatcher]
    def __init__(self, domain_matchers: _Optional[_Iterable[_Union[ServerNameMatcher.DomainMatcher, _Mapping]]] = ...) -> None: ...

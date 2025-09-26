from validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegexMatcher(_message.Message):
    __slots__ = ("google_re2", "regex")
    class GoogleRE2(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    GOOGLE_RE2_FIELD_NUMBER: _ClassVar[int]
    REGEX_FIELD_NUMBER: _ClassVar[int]
    google_re2: RegexMatcher.GoogleRE2
    regex: str
    def __init__(self, google_re2: _Optional[_Union[RegexMatcher.GoogleRE2, _Mapping]] = ..., regex: _Optional[str] = ...) -> None: ...

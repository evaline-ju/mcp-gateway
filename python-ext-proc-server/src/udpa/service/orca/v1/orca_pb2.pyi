import datetime

from udpa.data.orca.v1 import orca_load_report_pb2 as _orca_load_report_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrcaLoadReportRequest(_message.Message):
    __slots__ = ("report_interval", "request_cost_names")
    REPORT_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_COST_NAMES_FIELD_NUMBER: _ClassVar[int]
    report_interval: _duration_pb2.Duration
    request_cost_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, report_interval: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., request_cost_names: _Optional[_Iterable[str]] = ...) -> None: ...

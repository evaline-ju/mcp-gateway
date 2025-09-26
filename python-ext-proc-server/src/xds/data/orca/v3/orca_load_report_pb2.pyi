from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OrcaLoadReport(_message.Message):
    __slots__ = ("cpu_utilization", "mem_utilization", "rps", "request_cost", "utilization", "rps_fractional", "eps", "named_metrics", "application_utilization")
    class RequestCostEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    class UtilizationEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    class NamedMetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    CPU_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    MEM_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    RPS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_COST_FIELD_NUMBER: _ClassVar[int]
    UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    RPS_FRACTIONAL_FIELD_NUMBER: _ClassVar[int]
    EPS_FIELD_NUMBER: _ClassVar[int]
    NAMED_METRICS_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    cpu_utilization: float
    mem_utilization: float
    rps: int
    request_cost: _containers.ScalarMap[str, float]
    utilization: _containers.ScalarMap[str, float]
    rps_fractional: float
    eps: float
    named_metrics: _containers.ScalarMap[str, float]
    application_utilization: float
    def __init__(self, cpu_utilization: _Optional[float] = ..., mem_utilization: _Optional[float] = ..., rps: _Optional[int] = ..., request_cost: _Optional[_Mapping[str, float]] = ..., utilization: _Optional[_Mapping[str, float]] = ..., rps_fractional: _Optional[float] = ..., eps: _Optional[float] = ..., named_metrics: _Optional[_Mapping[str, float]] = ..., application_utilization: _Optional[float] = ...) -> None: ...

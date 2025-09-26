from xds.core.v3 import extension_pb2 as _extension_pb2
from xds.type.matcher.v3 import string_pb2 as _string_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Matcher(_message.Message):
    __slots__ = ("matcher_list", "matcher_tree", "on_no_match")
    class OnMatch(_message.Message):
        __slots__ = ("matcher", "action", "keep_matching")
        MATCHER_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        KEEP_MATCHING_FIELD_NUMBER: _ClassVar[int]
        matcher: Matcher
        action: _extension_pb2.TypedExtensionConfig
        keep_matching: bool
        def __init__(self, matcher: _Optional[_Union[Matcher, _Mapping]] = ..., action: _Optional[_Union[_extension_pb2.TypedExtensionConfig, _Mapping]] = ..., keep_matching: bool = ...) -> None: ...
    class MatcherList(_message.Message):
        __slots__ = ("matchers",)
        class Predicate(_message.Message):
            __slots__ = ("single_predicate", "or_matcher", "and_matcher", "not_matcher")
            class SinglePredicate(_message.Message):
                __slots__ = ("input", "value_match", "custom_match")
                INPUT_FIELD_NUMBER: _ClassVar[int]
                VALUE_MATCH_FIELD_NUMBER: _ClassVar[int]
                CUSTOM_MATCH_FIELD_NUMBER: _ClassVar[int]
                input: _extension_pb2.TypedExtensionConfig
                value_match: _string_pb2.StringMatcher
                custom_match: _extension_pb2.TypedExtensionConfig
                def __init__(self, input: _Optional[_Union[_extension_pb2.TypedExtensionConfig, _Mapping]] = ..., value_match: _Optional[_Union[_string_pb2.StringMatcher, _Mapping]] = ..., custom_match: _Optional[_Union[_extension_pb2.TypedExtensionConfig, _Mapping]] = ...) -> None: ...
            class PredicateList(_message.Message):
                __slots__ = ("predicate",)
                PREDICATE_FIELD_NUMBER: _ClassVar[int]
                predicate: _containers.RepeatedCompositeFieldContainer[Matcher.MatcherList.Predicate]
                def __init__(self, predicate: _Optional[_Iterable[_Union[Matcher.MatcherList.Predicate, _Mapping]]] = ...) -> None: ...
            SINGLE_PREDICATE_FIELD_NUMBER: _ClassVar[int]
            OR_MATCHER_FIELD_NUMBER: _ClassVar[int]
            AND_MATCHER_FIELD_NUMBER: _ClassVar[int]
            NOT_MATCHER_FIELD_NUMBER: _ClassVar[int]
            single_predicate: Matcher.MatcherList.Predicate.SinglePredicate
            or_matcher: Matcher.MatcherList.Predicate.PredicateList
            and_matcher: Matcher.MatcherList.Predicate.PredicateList
            not_matcher: Matcher.MatcherList.Predicate
            def __init__(self, single_predicate: _Optional[_Union[Matcher.MatcherList.Predicate.SinglePredicate, _Mapping]] = ..., or_matcher: _Optional[_Union[Matcher.MatcherList.Predicate.PredicateList, _Mapping]] = ..., and_matcher: _Optional[_Union[Matcher.MatcherList.Predicate.PredicateList, _Mapping]] = ..., not_matcher: _Optional[_Union[Matcher.MatcherList.Predicate, _Mapping]] = ...) -> None: ...
        class FieldMatcher(_message.Message):
            __slots__ = ("predicate", "on_match")
            PREDICATE_FIELD_NUMBER: _ClassVar[int]
            ON_MATCH_FIELD_NUMBER: _ClassVar[int]
            predicate: Matcher.MatcherList.Predicate
            on_match: Matcher.OnMatch
            def __init__(self, predicate: _Optional[_Union[Matcher.MatcherList.Predicate, _Mapping]] = ..., on_match: _Optional[_Union[Matcher.OnMatch, _Mapping]] = ...) -> None: ...
        MATCHERS_FIELD_NUMBER: _ClassVar[int]
        matchers: _containers.RepeatedCompositeFieldContainer[Matcher.MatcherList.FieldMatcher]
        def __init__(self, matchers: _Optional[_Iterable[_Union[Matcher.MatcherList.FieldMatcher, _Mapping]]] = ...) -> None: ...
    class MatcherTree(_message.Message):
        __slots__ = ("input", "exact_match_map", "prefix_match_map", "custom_match")
        class MatchMap(_message.Message):
            __slots__ = ("map",)
            class MapEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: Matcher.OnMatch
                def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Matcher.OnMatch, _Mapping]] = ...) -> None: ...
            MAP_FIELD_NUMBER: _ClassVar[int]
            map: _containers.MessageMap[str, Matcher.OnMatch]
            def __init__(self, map: _Optional[_Mapping[str, Matcher.OnMatch]] = ...) -> None: ...
        INPUT_FIELD_NUMBER: _ClassVar[int]
        EXACT_MATCH_MAP_FIELD_NUMBER: _ClassVar[int]
        PREFIX_MATCH_MAP_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_MATCH_FIELD_NUMBER: _ClassVar[int]
        input: _extension_pb2.TypedExtensionConfig
        exact_match_map: Matcher.MatcherTree.MatchMap
        prefix_match_map: Matcher.MatcherTree.MatchMap
        custom_match: _extension_pb2.TypedExtensionConfig
        def __init__(self, input: _Optional[_Union[_extension_pb2.TypedExtensionConfig, _Mapping]] = ..., exact_match_map: _Optional[_Union[Matcher.MatcherTree.MatchMap, _Mapping]] = ..., prefix_match_map: _Optional[_Union[Matcher.MatcherTree.MatchMap, _Mapping]] = ..., custom_match: _Optional[_Union[_extension_pb2.TypedExtensionConfig, _Mapping]] = ...) -> None: ...
    MATCHER_LIST_FIELD_NUMBER: _ClassVar[int]
    MATCHER_TREE_FIELD_NUMBER: _ClassVar[int]
    ON_NO_MATCH_FIELD_NUMBER: _ClassVar[int]
    matcher_list: Matcher.MatcherList
    matcher_tree: Matcher.MatcherTree
    on_no_match: Matcher.OnMatch
    def __init__(self, matcher_list: _Optional[_Union[Matcher.MatcherList, _Mapping]] = ..., matcher_tree: _Optional[_Union[Matcher.MatcherTree, _Mapping]] = ..., on_no_match: _Optional[_Union[Matcher.OnMatch, _Mapping]] = ...) -> None: ...

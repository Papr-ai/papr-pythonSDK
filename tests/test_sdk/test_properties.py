"""Tests for papr_memory.lib._properties module."""

import pytest

from papr_memory.lib._schema import node
from papr_memory.lib._properties import (
    Auto,
    PropertyRef,
    EdgeDescriptor,
    PropDescriptor,
    edge,
    prop,
    exact,
    fuzzy,
    semantic,
    _resolve_node_name,
)


class TestAuto:
    def test_no_longer_singleton(self) -> None:
        a1 = Auto()
        a2 = Auto()
        assert a1 is not a2

    def test_to_dict(self) -> None:
        assert Auto().to_dict() == {"mode": "auto"}

    def test_to_dict_with_prompt(self) -> None:
        result = Auto("Summarize in 1-2 sentences").to_dict()
        assert result == {"mode": "auto", "prompt": "Summarize in 1-2 sentences"}

    def test_prompt_attribute(self) -> None:
        assert Auto("a").prompt == "a"
        assert Auto().prompt is None

    def test_repr(self) -> None:
        assert repr(Auto()) == "Auto()"

    def test_repr_with_prompt(self) -> None:
        assert repr(Auto("summarize")) == "Auto('summarize')"

    def test_bool(self) -> None:
        assert bool(Auto()) is True


class TestSearchMode:
    def test_exact(self) -> None:
        sm = exact()
        assert sm.mode == "exact"
        assert sm.threshold is None
        assert sm.value is None

    def test_exact_with_value(self) -> None:
        sm = exact("TASK-123")
        assert sm.mode == "exact"
        assert sm.value == "TASK-123"

    def test_semantic_default(self) -> None:
        sm = semantic()
        assert sm.mode == "semantic"
        assert sm.threshold == 0.85
        assert sm.value is None

    def test_semantic_custom(self) -> None:
        sm = semantic(0.90, "auth bug")
        assert sm.mode == "semantic"
        assert sm.threshold == 0.90
        assert sm.value == "auth bug"

    def test_fuzzy_default(self) -> None:
        sm = fuzzy()
        assert sm.mode == "fuzzy"
        assert sm.threshold == 0.80

    def test_fuzzy_custom(self) -> None:
        sm = fuzzy(0.75)
        assert sm.mode == "fuzzy"
        assert sm.threshold == 0.75

    def test_to_search_property_exact(self) -> None:
        result = exact().to_search_property("id")
        assert result == {"name": "id", "mode": "exact"}

    def test_to_search_property_semantic(self) -> None:
        result = semantic(0.90).to_search_property("title")
        assert result == {"name": "title", "mode": "semantic", "threshold": 0.90}

    def test_to_search_property_with_value(self) -> None:
        result = exact("ABC").to_search_property("id")
        assert result == {"name": "id", "mode": "exact", "value": "ABC"}

    def test_repr(self) -> None:
        assert "mode='exact'" in repr(exact())
        assert "threshold=0.85" in repr(semantic())


class TestPropertyRef:
    def test_basic(self) -> None:
        ref = PropertyRef("Task", "title")
        assert ref._node_type == "Task"
        assert ref._prop_name == "title"

    def test_repr(self) -> None:
        ref = PropertyRef("Task", "title")
        assert repr(ref) == "PropertyRef('Task', 'title')"

    def test_exact(self) -> None:
        ref = PropertyRef("Task", "id").exact("T-1")
        assert ref._mode == "exact"
        assert ref._value == "T-1"

    def test_exact_no_value(self) -> None:
        ref = PropertyRef("Task", "id").exact()
        assert ref._mode == "exact"
        assert ref._value is None

    def test_semantic(self) -> None:
        ref = PropertyRef("Task", "title").semantic(0.90)
        assert ref._mode == "semantic"
        assert ref._threshold == 0.90

    def test_semantic_with_value(self) -> None:
        ref = PropertyRef("Task", "title").semantic(0.90, "fix bug")
        assert ref._mode == "semantic"
        assert ref._threshold == 0.90
        assert ref._value == "fix bug"

    def test_fuzzy(self) -> None:
        ref = PropertyRef("Task", "name").fuzzy(0.75)
        assert ref._mode == "fuzzy"
        assert ref._threshold == 0.75

    def test_to_link_to_string_basic(self) -> None:
        ref = PropertyRef("Task", "title")
        assert ref.to_link_to_string() == "Task:title"

    def test_to_link_to_string_exact_value(self) -> None:
        ref = PropertyRef("Task", "id").exact("TASK-123")
        assert ref.to_link_to_string() == "Task:id=TASK-123"

    def test_to_link_to_string_semantic_value(self) -> None:
        ref = PropertyRef("Task", "title").semantic(0.85, "auth bug")
        assert ref.to_link_to_string() == "Task:title~auth bug"

    def test_to_link_to_string_no_value_returns_base(self) -> None:
        ref = PropertyRef("Task", "title").semantic(0.85)
        assert ref.to_link_to_string() == "Task:title"

    def test_to_search_property_basic(self) -> None:
        ref = PropertyRef("Task", "title")
        result = ref.to_search_property()
        assert result == {"name": "title"}

    def test_to_search_property_exact(self) -> None:
        ref = PropertyRef("Task", "id").exact()
        result = ref.to_search_property()
        assert result == {"name": "id", "mode": "exact"}

    def test_to_search_property_semantic(self) -> None:
        ref = PropertyRef("Task", "title").semantic(0.90)
        result = ref.to_search_property()
        assert result == {"name": "title", "mode": "semantic", "threshold": 0.90}

    def test_chaining_returns_new_ref(self) -> None:
        base = PropertyRef("Task", "title")
        exact_ref = base.exact("val")
        assert base._mode is None
        assert exact_ref._mode == "exact"


class TestPropDescriptor:
    def test_basic_prop(self) -> None:
        desc = prop()
        assert isinstance(desc, PropDescriptor)
        assert desc.type == "string"
        assert desc.required is False

    def test_required_prop(self) -> None:
        desc = prop(required=True)
        assert desc.required is True

    def test_with_search(self) -> None:
        desc = prop(search=exact())
        assert desc.search is not None
        assert desc.search.mode == "exact"

    def test_with_enum(self) -> None:
        desc = prop(enum_values=["a", "b", "c"])
        assert desc.enum_values == ["a", "b", "c"]

    def test_with_type(self) -> None:
        desc = prop(type="integer")
        assert desc.type == "integer"

    def test_set_name(self) -> None:
        desc = prop()
        desc.__set_name__(type("Dummy", (), {}), "my_field")
        assert desc._name == "my_field"
        assert desc._owner_name == "Dummy"

    def test_get_returns_property_ref(self) -> None:
        @node
        class Task:
            title: str = prop(search=semantic(0.85))

        ref = Task.title
        assert isinstance(ref, PropertyRef)
        assert ref._node_type == "Task"
        assert ref._prop_name == "title"

    def test_to_property_definition_basic(self) -> None:
        desc = prop()
        result = desc.to_property_definition()
        assert result == {"type": "string"}

    def test_to_property_definition_full(self) -> None:
        desc = prop(
            type="string",
            required=True,
            description="Task title",
            enum_values=["a", "b"],
            default="a",
        )
        result = desc.to_property_definition()
        assert result == {
            "type": "string",
            "required": True,
            "description": "Task title",
            "enum_values": ["a", "b"],
            "default": "a",
        }

    def test_to_search_property_none(self) -> None:
        desc = prop()
        desc.__set_name__(type("X", (), {}), "field")
        assert desc.to_search_property() is None

    def test_to_search_property_exact(self) -> None:
        desc = prop(search=exact())
        desc.__set_name__(type("X", (), {}), "id")
        result = desc.to_search_property()
        assert result == {"name": "id", "mode": "exact"}

    def test_to_search_property_semantic(self) -> None:
        desc = prop(search=semantic(0.90))
        desc.__set_name__(type("X", (), {}), "title")
        result = desc.to_search_property()
        assert result == {"name": "title", "mode": "semantic", "threshold": 0.90}


class TestEdge:
    def test_edge_with_classes(self) -> None:
        @node
        class Source:
            name: str = prop()

        @node
        class Target:
            name: str = prop()

        e = edge(Source, Target)
        assert isinstance(e, EdgeDescriptor)
        assert e.source_type == "Source"
        assert e.target_type == "Target"

    def test_edge_with_strings(self) -> None:
        e = edge("Source", "Target")
        assert e.source_type == "Source"
        assert e.target_type == "Target"

    def test_edge_with_search(self) -> None:
        @node
        class Target:
            id: str = prop(search=exact())
            name: str = prop(search=semantic(0.90))

        e = edge(
            "Source", Target,
            search=(Target.id.exact(), Target.name.semantic(0.90)),
            create="lookup",
        )
        assert e.create == "lookup"
        assert e.search is not None
        assert len(e.search) == 2

    def test_edge_single_search_ref(self) -> None:
        ref = PropertyRef("Target", "id")
        e = edge("Source", "Target", search=ref)
        assert e.search is not None
        assert len(e.search) == 1

    def test_edge_with_options(self) -> None:
        e = edge(
            "A", "B",
            create="lookup",
            when={"status": "active"},
            description="test edge",
            cardinality="one-to-many",
        )
        assert e.create == "lookup"
        assert e.when == {"status": "active"}
        assert e.description == "test edge"
        assert e.cardinality == "one-to-many"

    def test_edge_set_name(self) -> None:
        e = edge("A", "B")
        e.__set_name__(type("Owner", (), {}), "my_edge")
        assert e._name == "my_edge"

    def test_resolve_node_name_string(self) -> None:
        assert _resolve_node_name("Task") == "Task"

    def test_resolve_node_name_class(self) -> None:
        class Task:
            pass
        assert _resolve_node_name(Task) == "Task"

    def test_resolve_node_name_invalid(self) -> None:
        with pytest.raises(TypeError, match="Expected a @node-decorated class"):
            _resolve_node_name(42)

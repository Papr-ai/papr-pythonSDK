"""Tests for papr_memory.lib._builders module."""

import pytest

from papr_memory.lib._properties import (
    Auto,
    PropertyRef,
    edge,
    exact,
    prop,
    semantic,
)
from papr_memory.lib._conditions import And, Not, Or
from papr_memory.lib._schema import (
    constraint,
    lookup,
    node,
    resolve,
    schema,
    upsert,
)
from papr_memory.lib._builders import (
    build_link_to,
    build_memory_policy,
    build_schema_params,
    serialize_set_values,
)


class TestBuildLinkTo:
    def test_single_ref(self) -> None:
        ref = PropertyRef("Task", "title")
        result = build_link_to(ref)
        assert result == "Task:title"

    def test_multiple_refs(self) -> None:
        ref1 = PropertyRef("Task", "title")
        ref2 = PropertyRef("Person", "email")
        result = build_link_to(ref1, ref2)
        assert result == ["Task:title", "Person:email"]

    def test_exact_value(self) -> None:
        ref = PropertyRef("Task", "id").exact("TASK-123")
        result = build_link_to(ref)
        assert result == "Task:id=TASK-123"

    def test_semantic_value(self) -> None:
        ref = PropertyRef("Task", "title").semantic(0.85, "auth bug")
        result = build_link_to(ref)
        assert result == "Task:title~auth bug"

    def test_from_decorated_class(self) -> None:
        @node
        class Task:
            title: str = prop(search=semantic(0.85))

        result = build_link_to(Task.title)
        assert result == "Task:title"

    def test_from_decorated_class_with_exact(self) -> None:
        @node
        class Task:
            id: str = prop(search=exact())

        result = build_link_to(Task.id.exact("T-1"))
        assert result == "Task:id=T-1"


class TestBuildSchemaParams:
    def test_not_decorated(self) -> None:
        class Foo:
            pass

        with pytest.raises(ValueError, match="not decorated with @schema"):
            build_schema_params(Foo)

    def test_basic_schema(self) -> None:
        @schema("test_schema")
        class TestSchema:
            @node
            class Task:
                title: str = prop(required=True, search=semantic(0.85))
                status: str = prop()

        params = build_schema_params(TestSchema)
        assert params["name"] == "test_schema"
        assert params["status"] == "active"
        assert "Task" in params["node_types"]

        task_type = params["node_types"]["Task"]
        assert task_type["name"] == "Task"
        assert task_type["label"] == "Task"
        assert "title" in task_type["properties"]
        assert "status" in task_type["properties"]
        assert task_type["properties"]["title"]["required"] is True
        assert task_type["required_properties"] == ["title"]
        assert task_type["resolution_policy"] == "upsert"

    def test_constraint_search(self) -> None:
        @schema("test")
        class TestSchema:
            @node
            class Task:
                id: str = prop(search=exact())
                title: str = prop(search=semantic(0.85))

        params = build_schema_params(TestSchema)
        task_type = params["node_types"]["Task"]
        search_props = task_type["constraint"]["search"]["properties"]
        assert len(search_props) == 2
        modes = {p["name"]: p["mode"] for p in search_props}
        assert modes["id"] == "exact"
        assert modes["title"] == "semantic"

    def test_lookup_policy(self) -> None:
        @schema("test")
        class TestSchema:
            @node
            @lookup
            class Ref:
                id: str = prop(search=exact())

        params = build_schema_params(TestSchema)
        ref_type = params["node_types"]["Ref"]
        assert ref_type["constraint"]["create"] == "lookup"
        assert ref_type["resolution_policy"] == "lookup"

    def test_resolve_on_miss(self) -> None:
        @schema("test")
        class TestSchema:
            @node
            @resolve(on_miss="error")
            class StrictRef:
                id: str = prop(search=exact())

        params = build_schema_params(TestSchema)
        ref_type = params["node_types"]["StrictRef"]
        assert ref_type["constraint"]["create"] == "lookup"
        assert ref_type["constraint"]["on_miss"] == "error"

    def test_constraint_when_and_set(self) -> None:
        @schema("test")
        class TestSchema:
            @node
            @upsert
            @constraint(
                when={"priority": "critical"},
                set={"flagged": True, "summary": Auto()},
            )
            class Task:
                title: str = prop(search=semantic(0.85))
                priority: str = prop()

        params = build_schema_params(TestSchema)
        task_constraint = params["node_types"]["Task"]["constraint"]
        assert task_constraint["when"] == {"priority": "critical"}
        assert task_constraint["set"] == {
            "flagged": True,
            "summary": {"mode": "auto"},
        }

    def test_edge_relationship_type(self) -> None:
        @schema("test")
        class TestSchema:
            @node
            class Source:
                name: str = prop(search=semantic(0.85))

            @node
            class Target:
                id: str = prop(search=exact())

            relates_to = edge(Source, Target, create="lookup")

        params = build_schema_params(TestSchema)
        assert "RELATES_TO" in params["relationship_types"]
        rel = params["relationship_types"]["RELATES_TO"]
        assert rel["name"] == "RELATES_TO"
        assert rel["label"] == "Relates To"
        assert rel["allowed_source_types"] == ["Source"]
        assert rel["allowed_target_types"] == ["Target"]
        assert rel["constraint"]["create"] == "lookup"

    def test_edge_with_search(self) -> None:
        @schema("test")
        class TestSchema:
            @node
            class Behavior:
                desc: str = prop(search=semantic(0.85))

            @node
            class Tactic:
                id: str = prop(search=exact())
                name: str = prop(search=semantic(0.90))

            mitigates = edge(
                Behavior, Tactic,
                search=(Tactic.id.exact(), Tactic.name.semantic(0.90)),
                create="lookup",
            )

        params = build_schema_params(TestSchema)
        rel = params["relationship_types"]["MITIGATES"]
        search_props = rel["constraint"]["search"]["properties"]
        assert len(search_props) == 2

    def test_with_description(self) -> None:
        @schema("test", description="A test schema")
        class TestSchema:
            @node
            class Task:
                title: str = prop()

        params = build_schema_params(TestSchema)
        assert params["description"] == "A test schema"

    def test_node_with_description(self) -> None:
        @schema("test")
        class TestSchema:
            @node(description="A task node", icon="check", color="#00ff00")
            class Task:
                title: str = prop()

        params = build_schema_params(TestSchema)
        task_type = params["node_types"]["Task"]
        assert task_type["description"] == "A task node"
        assert task_type["icon"] == "check"
        assert task_type["color"] == "#00ff00"

    def test_edge_with_when_condition(self) -> None:
        @schema("test")
        class TestSchema:
            @node
            class A:
                name: str = prop()

            @node
            class B:
                name: str = prop()

            link = edge(
                A, B,
                when=And({"status": "active"}, {"type": "relevant"}),
            )

        params = build_schema_params(TestSchema)
        rel = params["relationship_types"]["LINK"]
        assert rel["constraint"]["when"] == {
            "_and": [{"status": "active"}, {"type": "relevant"}]
        }


class TestBuildMemoryPolicy:
    def test_empty(self) -> None:
        policy = build_memory_policy()
        assert policy == {}

    def test_with_schema_id(self) -> None:
        policy = build_memory_policy(schema_id="abc123")
        assert policy == {"schema_id": "abc123"}

    def test_with_mode(self) -> None:
        policy = build_memory_policy(mode="auto")
        assert policy == {"mode": "auto"}

    def test_with_node_constraints(self) -> None:
        policy = build_memory_policy(
            node_constraints=[
                {"node_type": "Task", "create": "upsert"},
            ]
        )
        assert policy == {
            "node_constraints": [
                {"node_type": "Task", "create": "upsert"},
            ]
        }

    def test_with_edge_constraints(self) -> None:
        policy = build_memory_policy(
            edge_constraints=[
                {"relationship_type": "RELATES_TO", "create": "lookup"},
            ]
        )
        assert policy == {
            "edge_constraints": [
                {"relationship_type": "RELATES_TO", "create": "lookup"},
            ]
        }

    def test_full(self) -> None:
        policy = build_memory_policy(
            schema_id="my_schema",
            mode="manual",
            node_constraints=[{"node_type": "Task", "create": "upsert"}],
            edge_constraints=[{"relationship_type": "DOES", "create": "lookup"}],
        )
        assert policy["schema_id"] == "my_schema"
        assert policy["mode"] == "manual"
        assert len(policy["node_constraints"]) == 1
        assert len(policy["edge_constraints"]) == 1


class TestSerializeSetValues:
    def test_plain_values(self) -> None:
        result = serialize_set_values({"status": "done", "count": 5})
        assert result == {"status": "done", "count": 5}

    def test_auto_values(self) -> None:
        result = serialize_set_values({"summary": Auto(), "status": "done"})
        assert result == {"summary": {"mode": "auto"}, "status": "done"}

    def test_all_auto(self) -> None:
        result = serialize_set_values({"a": Auto(), "b": Auto()})
        assert result == {"a": {"mode": "auto"}, "b": {"mode": "auto"}}

    def test_auto_with_prompt(self) -> None:
        result = serialize_set_values({"summary": Auto("Summarize briefly")})
        assert result == {"summary": {"mode": "auto", "prompt": "Summarize briefly"}}

    def test_mixed_auto_with_and_without_prompt(self) -> None:
        result = serialize_set_values({
            "status": Auto(),
            "summary": Auto("Summarize in 1-2 sentences"),
            "flagged": True,
        })
        assert result == {
            "status": {"mode": "auto"},
            "summary": {"mode": "auto", "prompt": "Summarize in 1-2 sentences"},
            "flagged": True,
        }

    def test_empty(self) -> None:
        result = serialize_set_values({})
        assert result == {}

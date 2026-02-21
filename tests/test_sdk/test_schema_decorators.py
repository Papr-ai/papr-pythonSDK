"""Tests for papr_memory.lib._schema module."""


from papr_memory.lib._schema import (
    NodeMetadata,
    SchemaMetadata,
    node,
    lookup,
    schema,
    upsert,
    resolve,
    constraint,
)
from papr_memory.lib._conditions import And, Not
from papr_memory.lib._properties import (
    Auto,
    PropertyRef,
    edge,
    prop,
    exact,
    semantic,
)


class TestNodeDecorator:
    def test_bare_decorator(self) -> None:
        @node
        class Task:
            title: str = prop()

        assert hasattr(Task, "__papr_node__")
        meta = Task.__papr_node__
        assert isinstance(meta, NodeMetadata)
        assert meta.name == "Task"
        assert meta.label == "Task"

    def test_with_arguments(self) -> None:
        @node(label="My Task", icon="check", color="#ff0000")
        class Task:
            title: str = prop()

        meta = Task.__papr_node__
        assert meta.label == "My Task"
        assert meta.icon == "check"
        assert meta.color == "#ff0000"

    def test_with_description_arg(self) -> None:
        @node(description="A task node")
        class Task:
            title: str = prop()

        meta = Task.__papr_node__
        assert meta.description == "A task node"

    def test_with_docstring(self) -> None:
        @node
        class Task:
            """A task with a docstring."""
            title: str = prop()

        meta = Task.__papr_node__
        assert meta.description == "A task with a docstring."

    def test_collects_properties(self) -> None:
        @node
        class Task:
            id: str = prop(search=exact())
            title: str = prop(required=True, search=semantic(0.85))
            status: str = prop()

        meta = Task.__papr_node__
        assert "id" in meta.properties
        assert "title" in meta.properties
        assert "status" in meta.properties
        assert meta.properties["title"].required is True

    def test_default_create_policy(self) -> None:
        @node
        class Task:
            title: str = prop()

        meta = Task.__papr_node__
        assert meta.create_policy == "upsert"

    def test_property_ref_access(self) -> None:
        @node
        class Task:
            title: str = prop(search=semantic(0.85))

        ref = Task.title
        assert isinstance(ref, PropertyRef)
        assert ref._node_type == "Task"
        assert ref._prop_name == "title"


class TestLookupDecorator:
    def test_bare(self) -> None:
        @node
        @lookup
        class TacticDef:
            id: str = prop(search=exact())

        meta = TacticDef.__papr_node__
        assert meta.create_policy == "lookup"

    def test_stacking_order(self) -> None:
        """@lookup before @node should also work."""
        @lookup
        @node
        class TacticDef:
            id: str = prop(search=exact())

        meta = TacticDef.__papr_node__
        assert meta.create_policy == "lookup"


class TestUpsertDecorator:
    def test_bare(self) -> None:
        @node
        @upsert
        class Event:
            name: str = prop()

        meta = Event.__papr_node__
        assert meta.create_policy == "upsert"

    def test_explicit_upsert(self) -> None:
        """When default is already upsert, @upsert is explicit."""
        @upsert
        @node
        class Event:
            name: str = prop()

        meta = Event.__papr_node__
        assert meta.create_policy == "upsert"


class TestResolveDecorator:
    def test_default_on_miss(self) -> None:
        @node
        @resolve()
        class RequiredRef:
            id: str = prop(search=exact())

        meta = RequiredRef.__papr_node__
        assert meta.on_miss == "error"
        assert meta.create_policy == "lookup"

    def test_custom_on_miss(self) -> None:
        @node
        @resolve(on_miss="create")
        class FlexRef:
            id: str = prop(search=exact())

        meta = FlexRef.__papr_node__
        assert meta.on_miss == "create"

    def test_bare_resolve(self) -> None:
        @node
        @resolve
        class StrictRef:
            id: str = prop(search=exact())

        meta = StrictRef.__papr_node__
        assert meta.on_miss == "error"
        assert meta.create_policy == "lookup"


class TestConstraintDecorator:
    def test_with_when(self) -> None:
        @node
        @constraint(when={"priority": "critical"})
        class Task:
            title: str = prop()
            priority: str = prop()

        meta = Task.__papr_node__
        assert meta.when == {"priority": "critical"}

    def test_with_set(self) -> None:
        @node
        @constraint(set={"flagged": True, "summary": Auto()})
        class Task:
            title: str = prop()

        meta = Task.__papr_node__
        assert meta.set == {"flagged": True, "summary": {"mode": "auto"}}

    def test_with_when_and_set(self) -> None:
        @node
        @constraint(
            when={"priority": "critical"},
            set={"flagged": True, "reviewed_by": Auto()},
        )
        class Task:
            title: str = prop()

        meta = Task.__papr_node__
        assert meta.when == {"priority": "critical"}
        assert meta.set == {"flagged": True, "reviewed_by": {"mode": "auto"}}

    def test_with_logical_operators(self) -> None:
        @node
        @constraint(when=And({"priority": "high"}, Not({"status": "completed"})))
        class Task:
            title: str = prop()

        meta = Task.__papr_node__
        assert meta.when == {
            "_and": [
                {"priority": "high"},
                {"_not": {"status": "completed"}},
            ]
        }

    def test_stacking_with_upsert(self) -> None:
        @node
        @upsert
        @constraint(when={"type": "bug"}, set={"priority": Auto()})
        class Task:
            title: str = prop()

        meta = Task.__papr_node__
        assert meta.create_policy == "upsert"
        assert meta.when == {"type": "bug"}
        assert meta.set == {"priority": {"mode": "auto"}}


class TestSchemaDecorator:
    def test_basic_schema(self) -> None:
        @schema("test_schema")
        class TestSchema:
            @node
            class Task:
                title: str = prop()

        assert hasattr(TestSchema, "__papr_schema__")
        meta = TestSchema.__papr_schema__
        assert isinstance(meta, SchemaMetadata)
        assert meta.name == "test_schema"

    def test_collects_nodes(self) -> None:
        @schema("test")
        class TestSchema:
            @node
            @lookup
            class Person:
                email: str = prop(search=exact())

            @node
            @upsert
            class Task:
                title: str = prop()

        meta = TestSchema.__papr_schema__
        assert "Person" in meta.node_types
        assert "Task" in meta.node_types
        assert meta.node_types["Person"].create_policy == "lookup"
        assert meta.node_types["Task"].create_policy == "upsert"

    def test_collects_edges(self) -> None:
        @schema("test")
        class TestSchema:
            @node
            class Source:
                name: str = prop()

            @node
            class Target:
                id: str = prop(search=exact())

            relates_to = edge(Source, Target, create="lookup")

        meta = TestSchema.__papr_schema__
        assert "relates_to" in meta.edges
        e = meta.edges["relates_to"]
        assert e.source_type == "Source"
        assert e.target_type == "Target"
        assert e.create == "lookup"

    def test_default_name(self) -> None:
        @schema()
        class MySchema:
            @node
            class Task:
                title: str = prop()

        meta = MySchema.__papr_schema__
        assert meta.name == "MySchema"

    def test_with_description(self) -> None:
        @schema("test", description="A test schema")
        class TestSchema:
            @node
            class Task:
                title: str = prop()

        meta = TestSchema.__papr_schema__
        assert meta.description == "A test schema"

    def test_docstring_as_description(self) -> None:
        @schema("test")
        class TestSchema:
            """Schema doc."""

            @node
            class Task:
                title: str = prop()

        meta = TestSchema.__papr_schema__
        assert meta.description == "Schema doc."

    def test_ignores_private_attrs(self) -> None:
        @schema("test")
        class TestSchema:
            _internal = "skip"

            @node
            class Task:
                title: str = prop()

        meta = TestSchema.__papr_schema__
        assert "Task" in meta.node_types
        assert len(meta.node_types) == 1

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

        meta = TestSchema.__papr_schema__
        e = meta.edges["mitigates"]
        assert e.source_type == "Behavior"
        assert e.target_type == "Tactic"
        assert e.search is not None
        assert len(e.search) == 2


class TestNodeMetadata:
    def test_repr(self) -> None:
        meta = NodeMetadata("Task", "Task")
        assert "Task" in repr(meta)
        assert "upsert" in repr(meta)


class TestSchemaMetadata:
    def test_repr(self) -> None:
        meta = SchemaMetadata("test")
        meta.node_types["Task"] = NodeMetadata("Task", "Task")
        r = repr(meta)
        assert "test" in r
        assert "Task" in r

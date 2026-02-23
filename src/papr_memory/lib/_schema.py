"""
Schema definition decorators for the Papr SDK.

Provides ``@schema``, ``@node``, ``@lookup``, ``@upsert``, ``@resolve``,
and ``@constraint`` decorators for defining graph schemas with full IDE support.

Usage::

    from papr_memory.lib import schema, node, lookup, upsert, resolve, constraint
    from papr_memory.lib import prop, exact, semantic, Auto

    @schema("my_schema")
    class MySchema:

        @node
        @lookup
        class Person:
            email: str = prop(search=exact())
            name: str = prop(required=True, search=semantic(0.90))

        @node
        @upsert
        @constraint(
            when={"priority": "critical"},
            set={"flagged": True, "reviewed_by": Auto()}
        )
        class Task:
            id: str = prop(search=exact())
            title: str = prop(required=True, search=semantic(0.85))
            status: str = prop()
            priority: str = prop()
"""

from typing import Any, Dict, Callable, Optional

from ._conditions import Or, And, Not
from ._properties import Auto, EdgeDescriptor, PropDescriptor


class NodeMetadata:
    """Metadata collected from a ``@node``-decorated class."""

    def __init__(
        self,
        name: str,
        label: str,
        description: Optional[str] = None,
        icon: Optional[str] = None,
        color: Optional[str] = None,
    ) -> None:
        self.name = name
        self.label = label
        self.description = description
        self.icon = icon
        self.color = color
        self.create_policy: str = "upsert"
        self.on_miss: Optional[str] = None
        self.properties: Dict[str, PropDescriptor] = {}
        self.when: Optional[Dict[str, Any]] = None
        self.set: Optional[Dict[str, Any]] = None

    def __repr__(self) -> str:
        return f"NodeMetadata({self.name!r}, create={self.create_policy!r})"


class SchemaMetadata:
    """Metadata collected from a ``@schema``-decorated class."""

    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
    ) -> None:
        self.name = name
        self.description = description
        self.node_types: Dict[str, NodeMetadata] = {}
        self.edges: Dict[str, EdgeDescriptor] = {}

    def __repr__(self) -> str:
        nodes = list(self.node_types.keys())
        return f"SchemaMetadata({self.name!r}, nodes={nodes})"


def _ensure_node_meta(cls: type) -> NodeMetadata:
    """Get or create NodeMetadata on a class."""
    if not hasattr(cls, "__papr_node__"):
        meta = NodeMetadata(
            name=cls.__name__,
            label=cls.__name__,
            description=cls.__doc__,
        )
        # Collect PropDescriptors from class body
        for attr_name in list(vars(cls)):
            attr_val = vars(cls).get(attr_name)
            if isinstance(attr_val, PropDescriptor):
                attr_val.__set_name__(cls, attr_name)
                meta.properties[attr_name] = attr_val
        cls.__papr_node__ = meta  # type: ignore[attr-defined]
    return cls.__papr_node__  # type: ignore[attr-defined]


def node(
    cls: Optional[type] = None,
    *,
    label: Optional[str] = None,
    description: Optional[str] = None,
    icon: Optional[str] = None,
    color: Optional[str] = None,
) -> Any:
    """Decorator to mark a class as a node type definition.

    Can be used with or without arguments::

        @node
        class Task: ...

        @node(label="My Task", icon="check")
        class Task: ...
    """
    def decorator(cls: type) -> type:
        meta = _ensure_node_meta(cls)
        if label is not None:
            meta.label = label
        if description is not None:
            meta.description = description
        elif cls.__doc__:
            meta.description = cls.__doc__
        if icon is not None:
            meta.icon = icon
        if color is not None:
            meta.color = color
        return cls

    if cls is not None:
        return decorator(cls)
    return decorator


def lookup(cls: Optional[type] = None) -> Any:
    """Decorator: node is controlled vocabulary (never create new).

    Equivalent to ``create="lookup"``. Use for pre-populated reference data
    like MITRE tactics, users from IdP, product catalogs.

    Usage::

        @node
        @lookup
        class TacticDef:
            id: str = prop(search=exact())
            name: str = prop(search=semantic(0.90))
    """
    def decorator(cls: type) -> type:
        meta = _ensure_node_meta(cls)
        meta.create_policy = "lookup"
        return cls

    if cls is not None:
        return decorator(cls)
    return decorator


def upsert(cls: Optional[type] = None) -> Any:
    """Decorator: create node if not found (default behavior).

    Equivalent to ``create="upsert"``. Use for dynamic entities
    like conversations, actions, events.

    Usage::

        @node
        @upsert
        class Conversation:
            call_id: str = prop(required=True, search=exact())
    """
    def decorator(cls: type) -> type:
        meta = _ensure_node_meta(cls)
        meta.create_policy = "upsert"
        return cls

    if cls is not None:
        return decorator(cls)
    return decorator


def resolve(
    cls: Optional[type] = None,
    *,
    on_miss: str = "error",
) -> Any:
    """Decorator: strict validation - fail if node not found.

    Sets ``on_miss="error"`` so that graph generation raises a ``ValueError``
    when no matching node is found.

    Usage::

        @node
        @resolve(on_miss="error")
        class RequiredRef:
            id: str = prop(search=exact())

    Args:
        on_miss: Behavior when no match found. "error" (default), "create", or "ignore".
    """
    def decorator(cls: type) -> type:
        meta = _ensure_node_meta(cls)
        meta.on_miss = on_miss
        if on_miss == "error":
            meta.create_policy = "lookup"
        return cls

    if cls is not None:
        return decorator(cls)
    return decorator


def constraint(
    cls: Optional[type] = None,
    *,
    when: Optional[Any] = None,
    set: Optional[Dict[str, Any]] = None,
) -> Any:
    """Decorator: add conditional logic and property values to a node type.

    Usage::

        @node
        @upsert
        @constraint(
            when={"priority": "critical"},
            set={"flagged": True, "sla_hours": 4, "reviewed_by": Auto()}
        )
        class Task:
            id: str = prop(search=exact())
            title: str = prop(required=True, search=semantic(0.85))

    Args:
        when: Condition for when this constraint applies.
              Accepts dicts or ``And``/``Or``/``Not`` operators.
        set: Property values to set. Use ``Auto()`` for LLM extraction.
    """
    def decorator(cls: type) -> type:
        meta = _ensure_node_meta(cls)
        if when is not None:
            if isinstance(when, (And, Or, Not)):
                meta.when = when.to_dict()
            else:
                meta.when = when
        if set is not None:
            meta.set = _serialize_set_values(set)
        return cls

    if cls is not None:
        return decorator(cls)
    return decorator


def _serialize_set_values(values: Dict[str, Any]) -> Dict[str, Any]:
    """Convert set values, replacing Auto() sentinels with {"mode": "auto"}."""
    result: Dict[str, Any] = {}
    for key, val in values.items():
        if isinstance(val, Auto):
            result[key] = val.to_dict()
        else:
            result[key] = val
    return result


def schema(
    name: Optional[str] = None,
    *,
    description: Optional[str] = None,
) -> Callable[[type], type]:
    """Decorator to mark a class as a schema definition.

    Collects all ``@node``-decorated inner classes and ``edge()`` descriptors.

    Usage::

        @schema("security_monitoring")
        class SecuritySchema:
            @node
            @lookup
            class TacticDef:
                id: str = prop(search=exact())
                name: str = prop(search=semantic(0.90))

            @node
            @upsert
            class DetectedTactic:
                tactic_name: str = prop(search=semantic(0.85))

            maps_to = edge(
                DetectedTactic >> TacticDef,
                search=(TacticDef.id.exact(), TacticDef.name.semantic(0.90)),
                create="lookup"
            )

    Args:
        name: Schema name. Defaults to class name.
        description: Schema description.
    """
    def decorator(cls: type) -> type:
        schema_name = name or cls.__name__
        schema_desc = description or cls.__doc__

        meta = SchemaMetadata(name=schema_name, description=schema_desc)

        # Collect @node inner classes and edge() descriptors
        for attr_name in list(vars(cls)):
            if attr_name.startswith("_"):
                continue
            attr_val = vars(cls).get(attr_name)
            if attr_val is None:
                continue

            if isinstance(attr_val, type) and hasattr(attr_val, "__papr_node__"):
                node_meta: NodeMetadata = attr_val.__papr_node__
                meta.node_types[node_meta.name] = node_meta
            elif isinstance(attr_val, EdgeDescriptor):
                attr_val.__set_name__(cls, attr_name)
                meta.edges[attr_name] = attr_val

        cls.__papr_schema__ = meta  # type: ignore[attr-defined]
        return cls

    return decorator

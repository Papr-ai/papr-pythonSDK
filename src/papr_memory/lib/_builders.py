"""
Builder functions that convert decorated schemas and property refs
to API-compatible dicts (SchemaCreateParams, link_to, memory_policy).
"""

from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

from ._properties import Auto, EdgeDescriptor, PropDescriptor, PropertyRef
from ._conditions import And, Not, Or, _condition_to_dict
from ._schema import NodeMetadata, SchemaMetadata


def build_link_to(
    *refs: PropertyRef,
) -> Union[str, List[str]]:
    """Convert PropertyRef objects to ``link_to`` DSL strings.

    Usage::

        from papr_memory.lib import build_link_to

        # Single ref -> string
        build_link_to(Task.title)
        # -> "Task:title"

        # Multiple refs -> list
        build_link_to(Task.title, Person.email)
        # -> ["Task:title", "Person:email"]

        # With exact value
        build_link_to(Task.id.exact("TASK-123"))
        # -> "Task:id=TASK-123"

    Args:
        *refs: PropertyRef objects to convert.

    Returns:
        A single string or list of strings for the ``link_to`` parameter.
    """
    strings = [ref.to_link_to_string() for ref in refs]
    if len(strings) == 1:
        return strings[0]
    return strings


def build_schema_params(schema_cls: type) -> Dict[str, Any]:
    """Convert a ``@schema``-decorated class to a ``SchemaCreateParams`` dict.

    The output is compatible with ``client.schemas.create(**params)``.

    Usage::

        from papr_memory.lib import build_schema_params

        params = build_schema_params(MySchema)
        response = client.schemas.create(**params)

    Args:
        schema_cls: A class decorated with ``@schema``.

    Returns:
        Dict matching the ``SchemaCreateParams`` TypedDict structure.

    Raises:
        ValueError: If the class is not decorated with ``@schema``.
    """
    if not hasattr(schema_cls, "__papr_schema__"):
        raise ValueError(
            f"{schema_cls.__name__} is not decorated with @schema. "
            "Apply @schema() decorator first."
        )

    meta: SchemaMetadata = schema_cls.__papr_schema__

    # Build node_types
    node_types: Dict[str, Dict[str, Any]] = {}
    for type_name, node_meta in meta.node_types.items():
        node_types[type_name] = _build_node_type(node_meta)

    # Build relationship_types from edges
    relationship_types: Dict[str, Dict[str, Any]] = {}
    for edge_name, edge_desc in meta.edges.items():
        rel_name = edge_name.upper()
        relationship_types[rel_name] = _build_relationship_type(edge_name, edge_desc)

    params: Dict[str, Any] = {
        "name": meta.name,
        "node_types": node_types,
        "relationship_types": relationship_types,
        "status": "active",
    }
    if meta.description:
        params["description"] = meta.description

    return params


def _build_node_type(meta: NodeMetadata) -> Dict[str, Any]:
    """Convert NodeMetadata to a NodeTypes dict."""
    # Build properties
    properties: Dict[str, Dict[str, Any]] = {}
    required_properties: List[str] = []
    search_properties: List[Dict[str, Any]] = []

    for prop_name, prop_desc in meta.properties.items():
        properties[prop_name] = prop_desc.to_property_definition()
        if prop_desc.required:
            required_properties.append(prop_name)
        search_prop = prop_desc.to_search_property()
        if search_prop is not None:
            search_properties.append(search_prop)

    node_type: Dict[str, Any] = {
        "name": meta.name,
        "label": meta.label,
        "properties": properties,
    }

    if meta.description:
        node_type["description"] = meta.description
    if meta.icon:
        node_type["icon"] = meta.icon
    if meta.color:
        node_type["color"] = meta.color
    if required_properties:
        node_type["required_properties"] = required_properties

    # Build constraint
    constraint: Dict[str, Any] = {
        "create": meta.create_policy,
    }
    if meta.on_miss is not None:
        constraint["on_miss"] = meta.on_miss
    if search_properties:
        constraint["search"] = {"properties": search_properties}
    if meta.when is not None:
        constraint["when"] = meta.when
    if meta.set is not None:
        constraint["set"] = meta.set

    node_type["constraint"] = constraint
    node_type["resolution_policy"] = meta.create_policy

    return node_type


def _build_relationship_type(edge_name: str, edge_desc: EdgeDescriptor) -> Dict[str, Any]:
    """Convert EdgeDescriptor to a RelationshipTypes dict."""
    rel_name = edge_name.upper()

    rel_type: Dict[str, Any] = {
        "name": rel_name,
        "label": edge_name.replace("_", " ").title(),
        "allowed_source_types": [edge_desc.source_type],
        "allowed_target_types": [edge_desc.target_type],
    }

    if edge_desc.cardinality:
        rel_type["cardinality"] = edge_desc.cardinality
    if edge_desc.description:
        rel_type["description"] = edge_desc.description

    # Build edge constraint
    constraint: Dict[str, Any] = {
        "create": edge_desc.create,
    }
    if edge_desc.search:
        search_props = [ref.to_search_property() for ref in edge_desc.search]
        constraint["search"] = {"properties": search_props}
    if edge_desc.when:
        if isinstance(edge_desc.when, (And, Or, Not)):
            constraint["when"] = edge_desc.when.to_dict()
        else:
            constraint["when"] = edge_desc.when

    rel_type["constraint"] = constraint

    return rel_type


def build_memory_policy(
    node_constraints: Optional[List[Dict[str, Any]]] = None,
    edge_constraints: Optional[List[Dict[str, Any]]] = None,
    schema_id: Optional[str] = None,
    mode: Optional[str] = None,
) -> Dict[str, Any]:
    """Build a ``memory_policy`` dict from structured inputs.

    Usage::

        policy = build_memory_policy(
            schema_id="my_schema_id",
            node_constraints=[
                {"node_type": "Task", "create": "upsert",
                 "set": {"status": Auto().to_dict()}}
            ]
        )
        client.memory.add(content="...", memory_policy=policy)

    Args:
        node_constraints: List of NodeConstraintInput dicts.
        edge_constraints: List of EdgeConstraintInput dicts.
        schema_id: Schema ID to reference.
        mode: Graph generation mode ("auto" or "manual").

    Returns:
        Dict matching the ``MemoryPolicy`` structure.
    """
    policy: Dict[str, Any] = {}
    if mode is not None:
        policy["mode"] = mode
    if schema_id is not None:
        policy["schema_id"] = schema_id
    if node_constraints:
        policy["node_constraints"] = node_constraints
    if edge_constraints:
        policy["edge_constraints"] = edge_constraints
    return policy


def serialize_set_values(values: Dict[str, Any]) -> Dict[str, Any]:
    """Convert set values dict, replacing ``Auto()`` sentinels with ``{"mode": "auto"}``.

    Usage::

        serialize_set_values({"status": "done", "summary": Auto()})
        # -> {"status": "done", "summary": {"mode": "auto"}}
    """
    result: Dict[str, Any] = {}
    for key, val in values.items():
        if isinstance(val, Auto):
            result[key] = val.to_dict()
        else:
            result[key] = val
    return result

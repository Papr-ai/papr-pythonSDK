"""
Papr SDK Builder API - Simplified memory policy definitions.

This module provides a decorator-based API for defining graph schemas
and type-safe builders for memory operations, reducing boilerplate by ~80%.

Quick Start::

    from papr_memory.lib import (
        schema, node, lookup, upsert, resolve, constraint,
        prop, edge, exact, semantic, fuzzy, Auto,
        And, Or, Not,
        build_link_to, build_schema_params,
    )

    @schema("my_project")
    class MySchema:

        @node
        @lookup
        class Person:
            email: str = prop(search=exact())
            name: str = prop(required=True, search=semantic(0.90))

        @node
        @upsert
        class Task:
            id: str = prop(search=exact())
            title: str = prop(required=True, search=semantic(0.85))
            status: str = prop()

    # Register schema
    params = build_schema_params(MySchema)
    client.schemas.create(**params)

    # Add memory with type-safe linking
    client.memory.add(
        content="John fixed the auth bug",
        link_to=build_link_to(MySchema.Task.title, MySchema.Person.email),
    )
"""

# Decorators
from ._schema import node, lookup, schema, upsert, resolve, constraint

# Builders
from ._builders import build_link_to, build_memory_policy, build_schema_params, serialize_set_values

# Logical operators
from ._conditions import Or, And, Not

# Property/search helpers
from ._properties import Auto, PropertyRef, edge, prop, exact, fuzzy, semantic

__all__ = [
    # Decorators
    "schema",
    "node",
    "lookup",
    "upsert",
    "resolve",
    "constraint",
    # Property/search helpers
    "prop",
    "edge",
    "exact",
    "semantic",
    "fuzzy",
    "Auto",
    "PropertyRef",
    # Logical operators
    "And",
    "Or",
    "Not",
    # Builders
    "build_link_to",
    "build_schema_params",
    "build_memory_policy",
    "serialize_set_values",
]

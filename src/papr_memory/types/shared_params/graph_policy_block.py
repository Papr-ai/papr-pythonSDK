# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr
from .node_spec import NodeSpec
from .relationship_spec import RelationshipSpec
from .edge_constraint_input import EdgeConstraintInput
from .node_constraint_input import NodeConstraintInput

__all__ = ["GraphPolicyBlock"]


class GraphPolicyBlock(TypedDict, total=False):
    edge_constraints: Optional[Iterable[EdgeConstraintInput]]
    """Full edge constraint objects.

    Same rules as edge entries in policy.graph.link_to after expansion; both may be
    set in the same request.
    """

    link_to: Union[str, SequenceNotStr[str], Dict[str, object], None]
    """Shorthand DSL for node/edge constraints under policy.graph.

    Not a separate graph mode — expands into node_constraints and edge_constraints
    at resolve time and merges with any explicit constraints in the same request.
    Default create policy is upsert (create if not found); use dict form with
    create='lookup' for link-only. Prefer over deprecated top-level link_to.
    """

    mode: Literal["none", "auto", "manual"]

    node_constraints: Optional[Iterable[NodeConstraintInput]]
    """Full node constraint objects.

    Same rules as policy.graph.link_to after expansion; use link_to for compact DSL
    or this field for explicit control. Both may be set.
    """

    nodes: Optional[Iterable[NodeSpec]]

    relationships: Optional[Iterable[RelationshipSpec]]

    schema_id: Optional[str]

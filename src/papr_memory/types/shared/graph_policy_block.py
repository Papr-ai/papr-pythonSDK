# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .node_spec import NodeSpec
from .relationship_spec import RelationshipSpec
from .edge_constraint_input import EdgeConstraintInput
from .node_constraint_input import NodeConstraintInput

__all__ = ["GraphPolicyBlock"]


class GraphPolicyBlock(BaseModel):
    edge_constraints: Optional[List[EdgeConstraintInput]] = None
    """Full edge constraint objects.

    Same rules as edge entries in policy.graph.link_to after expansion; both may be
    set in the same request.
    """

    link_to: Union[str, List[str], Dict[str, object], None] = None
    """Shorthand DSL for node/edge constraints under policy.graph.

    Not a separate graph mode — expands into node_constraints and edge_constraints
    at resolve time and merges with any explicit constraints in the same request.
    Default create policy is upsert (create if not found); use dict form with
    create='lookup' for link-only. Prefer over deprecated top-level link_to.
    """

    mode: Optional[Literal["none", "auto", "manual"]] = None

    node_constraints: Optional[List[NodeConstraintInput]] = None
    """Full node constraint objects.

    Same rules as policy.graph.link_to after expansion; use link_to for compact DSL
    or this field for explicit control. Both may be set.
    """

    nodes: Optional[List[NodeSpec]] = None

    relationships: Optional[List[RelationshipSpec]] = None

    schema_id: Optional[str] = None

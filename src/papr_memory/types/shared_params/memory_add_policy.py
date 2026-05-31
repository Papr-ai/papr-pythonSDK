# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .acl_config import ACLConfig
from .graph_policy_block import GraphPolicyBlock
from .transform_embedding_policy import TransformEmbeddingPolicy

__all__ = ["MemoryAddPolicy"]


class MemoryAddPolicy(TypedDict, total=False):
    """Policy for add / batch / document / message ingestion."""

    acl: Optional[ACLConfig]
    """Simplified Access Control List configuration.

    Aligned with Open Memory Object (OMO) standard. See:
    https://github.com/anthropics/open-memory-object

    **Supported Entity Prefixes:**

    | Prefix           | Description           | Validation                           |
    | ---------------- | --------------------- | ------------------------------------ |
    | `user:`          | Internal Papr user ID | Validated against Parse users        |
    | `external_user:` | Your app's user ID    | Not validated (your responsibility)  |
    | `organization:`  | Organization ID       | Validated against your organizations |
    | `namespace:`     | Namespace ID          | Validated against your namespaces    |
    | `workspace:`     | Workspace ID          | Validated against your workspaces    |
    | `role:`          | Parse role ID         | Validated against your roles         |

    **Examples:**

    ```python
    acl = ACLConfig(
        read=["external_user:alice_123", "organization:org_acme"],
        write=["external_user:alice_123"]
    )
    ```

    **Validation Rules:**

    - Internal entities (user, organization, namespace, workspace, role) are
      validated
    - External entities (external_user) are NOT validated - your app is responsible
    - Invalid internal entities will return an error
    - Unprefixed values default to `external_user:` for backwards compatibility
    """

    consent: Literal["explicit", "implicit", "terms", "none"]
    """How the data owner allowed this memory to be stored/used.

    Aligned with Open Memory Object (OMO) standard.
    """

    graph: Optional[GraphPolicyBlock]

    risk: Literal["none", "sensitive", "flagged"]
    """Post-ingest safety assessment of memory content.

    Aligned with Open Memory Object (OMO) standard.
    """

    transform_embedding: Optional[TransformEmbeddingPolicy]

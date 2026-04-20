# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["ACLConfig"]


class ACLConfig(TypedDict, total=False):
    """Simplified Access Control List configuration.

    Aligned with Open Memory Object (OMO) standard.
    See: https://github.com/anthropics/open-memory-object

    **Supported Entity Prefixes:**

    | Prefix | Description | Validation |
    |--------|-------------|------------|
    | `user:` | Internal Papr user ID | Validated against Parse users |
    | `external_user:` | Your app's user ID | Not validated (your responsibility) |
    | `organization:` | Organization ID | Validated against your organizations |
    | `namespace:` | Namespace ID | Validated against your namespaces |
    | `workspace:` | Workspace ID | Validated against your workspaces |
    | `role:` | Parse role ID | Validated against your roles |

    **Examples:**
    ```python
    acl = ACLConfig(read=["external_user:alice_123", "organization:org_acme"], write=["external_user:alice_123"])
    ```

    **Validation Rules:**
    - Internal entities (user, organization, namespace, workspace, role) are validated
    - External entities (external_user) are NOT validated - your app is responsible
    - Invalid internal entities will return an error
    - Unprefixed values default to `external_user:` for backwards compatibility
    """

    read: SequenceNotStr[str]
    """Entity IDs that can read this memory.

    Format: 'prefix:id' (e.g., 'external_user:alice', 'organization:org_123').
    Supported prefixes: user, external_user, organization, namespace, workspace,
    role. Unprefixed values treated as external_user for backwards compatibility.
    """

    write: SequenceNotStr[str]
    """Entity IDs that can write/modify this memory.

    Format: 'prefix:id' (e.g., 'external_user:alice'). Supported prefixes: user,
    external_user, organization, namespace, workspace, role.
    """

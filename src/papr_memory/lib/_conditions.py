"""
Logical operators for conditional constraints.

Provides ``And``, ``Or``, ``Not`` for building ``when`` conditions
with full composability.
"""

from typing import Any, Dict, List, Union

Condition = Union[Dict[str, Any], "And", "Or", "Not"]


def _condition_to_dict(condition: Condition) -> Dict[str, Any]:
    """Convert a condition (dict or operator) to its dict representation."""
    if isinstance(condition, (And, Or, Not)):
        return condition.to_dict()
    return condition


class And:
    """Logical AND for ``when`` conditions.

    All conditions must match.

    Usage::

        @constraint(when=And({"priority": "high"}, {"status": "active"}))
        class Task: ...

    Serializes to::

        {"_and": [{"priority": "high"}, {"status": "active"}]}
    """

    def __init__(self, *conditions: Condition) -> None:
        self.conditions = list(conditions)

    def __repr__(self) -> str:
        return f"And({', '.join(repr(c) for c in self.conditions)})"

    def to_dict(self) -> Dict[str, Any]:
        return {"_and": [_condition_to_dict(c) for c in self.conditions]}


class Or:
    """Logical OR for ``when`` conditions.

    Any condition must match.

    Usage::

        @constraint(when=Or({"status": "active"}, {"status": "pending"}))
        class Task: ...

    Serializes to::

        {"_or": [{"status": "active"}, {"status": "pending"}]}
    """

    def __init__(self, *conditions: Condition) -> None:
        self.conditions = list(conditions)

    def __repr__(self) -> str:
        return f"Or({', '.join(repr(c) for c in self.conditions)})"

    def to_dict(self) -> Dict[str, Any]:
        return {"_or": [_condition_to_dict(c) for c in self.conditions]}


class Not:
    """Logical NOT for ``when`` conditions.

    Negates the condition.

    Usage::

        @constraint(when=Not({"status": "completed"}))
        class Task: ...

    Serializes to::

        {"_not": {"status": "completed"}}
    """

    def __init__(self, condition: Condition) -> None:
        self.condition = condition

    def __repr__(self) -> str:
        return f"Not({self.condition!r})"

    def to_dict(self) -> Dict[str, Any]:
        return {"_not": _condition_to_dict(self.condition)}

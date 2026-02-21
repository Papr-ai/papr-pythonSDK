"""
Core primitives for the Papr SDK builder API.

Provides type-safe property references, search mode helpers, and descriptors
for defining node schemas with full IDE support.
"""

from typing import Any, Dict, List, Tuple, Union, Optional


class Auto:
    """Sentinel indicating the LLM should extract this value from content.

    Optionally accepts a prompt to guide extraction::

        Auto()                                    -> {"mode": "auto"}
        Auto("Summarize in 1-2 sentences")        -> {"mode": "auto", "prompt": "Summarize in 1-2 sentences"}

    Usage::

        @constraint(set={"status": Auto(), "summary": Auto("Summarize briefly")})
        class Task: ...

    Serializes to ``{"mode": "auto"}`` (or ``{"mode": "auto", "prompt": "..."}``).
    """

    def __init__(self, prompt: Optional[str] = None) -> None:
        self.prompt = prompt

    def __repr__(self) -> str:
        if self.prompt is not None:
            return f"Auto({self.prompt!r})"
        return "Auto()"

    def __bool__(self) -> bool:
        return True

    def to_dict(self) -> Dict[str, str]:
        result: Dict[str, str] = {"mode": "auto"}
        if self.prompt is not None:
            result["prompt"] = self.prompt
        return result


class SearchMode:
    """Describes how a property should be matched during node search.

    Not typically constructed directly - use ``exact()``, ``semantic()``, or ``fuzzy()``.
    """

    def __init__(
        self,
        mode: str,
        threshold: Optional[float] = None,
        value: object = None,
    ) -> None:
        self.mode = mode
        self.threshold = threshold
        self.value = value

    def __repr__(self) -> str:
        parts = [f"mode={self.mode!r}"]
        if self.threshold is not None:
            parts.append(f"threshold={self.threshold}")
        if self.value is not None:
            parts.append(f"value={self.value!r}")
        return f"SearchMode({', '.join(parts)})"

    def to_search_property(self, name: str) -> Dict[str, Any]:
        """Convert to a SearchConfigInput.Property dict."""
        result: Dict[str, Any] = {"name": name, "mode": self.mode}
        if self.threshold is not None:
            result["threshold"] = self.threshold
        if self.value is not None:
            result["value"] = self.value
        return result


def exact(value: object = None) -> SearchMode:
    """Exact string match.

    Usage::

        id: str = prop(search=exact())
        id: str = prop(search=exact("TASK-123"))  # with specific value
    """
    return SearchMode("exact", value=value)


def semantic(threshold: float = 0.85, value: object = None) -> SearchMode:
    """Semantic similarity match using embeddings.

    Usage::

        title: str = prop(search=semantic(0.85))
        title: str = prop(search=semantic(0.90, "auth bug"))
    """
    return SearchMode("semantic", threshold=threshold, value=value)


def fuzzy(threshold: float = 0.80, value: object = None) -> SearchMode:
    """Fuzzy string match (Levenshtein distance).

    Usage::

        name: str = prop(search=fuzzy(0.80))
    """
    return SearchMode("fuzzy", threshold=threshold, value=value)


class PropertyRef:
    """Type-safe reference to a property on a node type.

    Created automatically when accessing properties on ``@node``-decorated classes::

        Task.title          # -> PropertyRef("Task", "title")
        Task.title.exact()  # -> PropertyRef with exact mode

    Used with ``build_link_to()`` to generate ``link_to`` DSL strings.
    """

    def __init__(
        self,
        node_type: str,
        prop_name: str,
        mode: Optional[str] = None,
        threshold: Optional[float] = None,
        value: object = None,
    ) -> None:
        self._node_type = node_type
        self._prop_name = prop_name
        self._mode = mode
        self._threshold = threshold
        self._value = value

    def __repr__(self) -> str:
        return f"PropertyRef({self._node_type!r}, {self._prop_name!r})"

    def exact(self, value: object = None) -> "PropertyRef":
        """Create an exact-match version of this reference."""
        return PropertyRef(
            self._node_type,
            self._prop_name,
            mode="exact",
            value=value,
        )

    def semantic(self, threshold: float = 0.85, value: object = None) -> "PropertyRef":
        """Create a semantic-match version of this reference."""
        return PropertyRef(
            self._node_type,
            self._prop_name,
            mode="semantic",
            threshold=threshold,
            value=value,
        )

    def fuzzy(self, threshold: float = 0.80, value: object = None) -> "PropertyRef":
        """Create a fuzzy-match version of this reference."""
        return PropertyRef(
            self._node_type,
            self._prop_name,
            mode="fuzzy",
            threshold=threshold,
            value=value,
        )

    def to_link_to_string(self) -> str:
        """Convert to link_to DSL string.

        Examples::

            "Task:title"
            "Task:id=TASK-123"
            "Task:title~auth bug"
        """
        base = f"{self._node_type}:{self._prop_name}"
        if self._value is not None:
            if self._mode == "exact":
                return f"{base}={self._value}"
            elif self._mode == "semantic":
                return f"{base}~{self._value}"
        return base

    def to_search_property(self) -> Dict[str, Any]:
        """Convert to a SearchConfigInput.Property dict."""
        result: Dict[str, Any] = {"name": self._prop_name}
        if self._mode is not None:
            result["mode"] = self._mode
        if self._threshold is not None:
            result["threshold"] = self._threshold
        if self._value is not None:
            result["value"] = self._value
        return result


class PropDescriptor:
    """Descriptor returned by ``prop()`` that defines a node property.

    Captures metadata from class body and provides ``PropertyRef`` on attribute access.
    Uses ``__set_name__`` to learn the attribute name and owner class.
    """

    def __init__(
        self,
        type: str = "string",
        required: bool = False,
        description: Optional[str] = None,
        enum_values: Optional[List[str]] = None,
        default: object = None,
        search: Optional[SearchMode] = None,
    ) -> None:
        self.type = type
        self.required = required
        self.description = description
        self.enum_values = enum_values
        self.default = default
        self.search = search
        self._name: Optional[str] = None
        self._owner_name: Optional[str] = None

    def __set_name__(self, owner: type, name: str) -> None:
        self._name = name
        self._owner_name = owner.__name__

    def __get__(self, obj: Any, objtype: Optional[type] = None) -> "PropertyRef":
        """Return a PropertyRef when accessed on the class."""
        owner = objtype if objtype is not None else type(obj)
        name = self._name or ""
        return PropertyRef(owner.__name__, name)

    def __repr__(self) -> str:
        return f"PropDescriptor(name={self._name!r}, type={self.type!r})"

    def to_property_definition(self) -> Dict[str, Any]:
        """Convert to a PropertyDefinitionParam dict."""
        result: Dict[str, Any] = {"type": self.type}
        if self.required:
            result["required"] = True
        if self.description is not None:
            result["description"] = self.description
        if self.enum_values is not None:
            result["enum_values"] = self.enum_values
        if self.default is not None:
            result["default"] = self.default
        return result

    def to_search_property(self) -> Optional[Dict[str, Any]]:
        """Convert search config to a Property dict, or None if no search."""
        if self.search is None or self._name is None:
            return None
        return self.search.to_search_property(self._name)


def prop(
    type: str = "string",
    required: bool = False,
    description: Optional[str] = None,
    enum_values: Optional[List[str]] = None,
    default: object = None,
    search: Optional[SearchMode] = None,
) -> Any:
    """Define a property on a node type.

    Usage::

        @node
        class Task:
            id: str = prop(search=exact())
            title: str = prop(required=True, search=semantic(0.85))
            status: str = prop(enum_values=["open", "in_progress", "completed"])
            priority: Optional[str] = prop()

    Args:
        type: Property type ("string", "integer", "float", "boolean", "array", "datetime", "object")
        required: Whether this property is required
        description: Property description
        enum_values: List of allowed values
        default: Default value
        search: Search mode for node matching (``exact()``, ``semantic()``, ``fuzzy()``)
    """
    return PropDescriptor(
        type=type,
        required=required,
        description=description,
        enum_values=enum_values,
        default=default,
        search=search,
    )


class EdgeDescriptor:
    """Descriptor returned by ``edge()`` that defines a relationship between node types.

    Usage::

        @schema("my_schema")
        class MySchema:
            @node
            class SecurityBehavior: ...

            @node
            class TacticDef: ...

            mitigates = edge(
                SecurityBehavior, TacticDef,
                search=(TacticDef.id.exact(), TacticDef.name.semantic(0.90)),
                create="lookup"
            )
    """

    def __init__(
        self,
        source_type: str,
        target_type: str,
        search: Optional[Tuple[PropertyRef, ...]] = None,
        create: str = "upsert",
        when: Optional[Dict[str, Any]] = None,
        description: Optional[str] = None,
        cardinality: str = "many-to-many",
    ) -> None:
        self.source_type = source_type
        self.target_type = target_type
        self.search = search
        self.create = create
        self.when = when
        self.description = description
        self.cardinality = cardinality
        self._name: Optional[str] = None

    def __set_name__(self, owner: type, name: str) -> None:
        self._name = name

    def __repr__(self) -> str:
        return f"EdgeDescriptor({self.source_type}->{self.target_type}, name={self._name!r})"


def _resolve_node_name(node_ref: Any) -> str:
    """Extract node type name from a class or string."""
    if isinstance(node_ref, str):
        return node_ref
    if isinstance(node_ref, type):
        return node_ref.__name__
    raise TypeError(
        f"Expected a @node-decorated class or string, got {type(node_ref).__name__}"
    )


def edge(
    source: Any,
    target: Any,
    search: Optional[Union[Tuple[PropertyRef, ...], PropertyRef]] = None,
    create: str = "upsert",
    when: Optional[Dict[str, Any]] = None,
    description: Optional[str] = None,
    cardinality: str = "many-to-many",
) -> Any:
    """Define an edge (relationship) between node types.

    Usage::

        mitigates = edge(
            SecurityBehavior, TacticDef,
            search=(TacticDef.id.exact(), TacticDef.name.semantic(0.90)),
            create="lookup"
        )

    Args:
        source: Source node class or name string.
        target: Target node class or name string.
        search: PropertyRef(s) for matching target nodes.
        create: Resolution policy ("upsert" or "lookup").
        when: Conditional dict for when this edge applies.
        description: Edge description.
        cardinality: "one-to-one", "one-to-many", or "many-to-many".
    """
    if isinstance(search, PropertyRef):
        search = (search,)
    return EdgeDescriptor(
        source_type=_resolve_node_name(source),
        target_type=_resolve_node_name(target),
        search=search,
        create=create,
        when=when,
        description=description,
        cardinality=cardinality,
    )

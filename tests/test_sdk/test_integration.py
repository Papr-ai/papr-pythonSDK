"""End-to-end integration tests for the SDK builder API.

Tests full decorator -> build_schema_params -> API-compatible output flow.
"""

from papr_memory.lib import (
    Or,
    And,
    Not,
    Auto,
    edge,
    node,
    prop,
    exact,
    lookup,
    schema,
    upsert,
    resolve,
    semantic,
    constraint,
    build_link_to,
    build_memory_policy,
    build_schema_params,
    serialize_set_values,
)


class TestDeepTrustStyleSchema:
    """Integration test based on the DeepTrust security monitoring use case."""

    def setup_method(self) -> None:
        @schema("security_monitoring", description="DeepTrust security schema")
        class SecuritySchema:
            @node
            @lookup
            class TacticDef:
                """MITRE ATT&CK tactic definition."""
                id: str = prop(search=exact())
                name: str = prop(required=True, search=semantic(0.90))
                description: str = prop()

            @node
            @upsert
            class SecurityBehavior:
                """Observed security behavior."""
                description: str = prop(required=True, search=semantic(0.85))
                severity: str = prop(enum_values=["low", "medium", "high", "critical"])

            @node
            @upsert
            @constraint(
                when={"severity": "critical"},
                set={"flagged": True, "reviewed_by": Auto()},
            )
            class Alert:
                """Security alert."""
                alert_id: str = prop(search=exact())
                title: str = prop(required=True, search=semantic(0.85))
                severity: str = prop()

            @node
            @resolve(on_miss="error")
            class RequiredTactic:
                """Must exist in knowledge base."""
                id: str = prop(search=exact())

            mitigates = edge(
                SecurityBehavior, TacticDef,
                search=(TacticDef.id.exact(), TacticDef.name.semantic(0.90)),
                create="lookup",
            )

            triggers = edge(
                SecurityBehavior, Alert,
                search=(Alert.alert_id.exact(),),
                create="upsert",
            )

        self.schema_cls = SecuritySchema
        self.params = build_schema_params(SecuritySchema)

    def test_schema_name(self) -> None:
        assert self.params["name"] == "security_monitoring"
        assert self.params["description"] == "DeepTrust security schema"
        assert self.params["status"] == "active"

    def test_node_types_present(self) -> None:
        node_types = self.params["node_types"]
        assert "TacticDef" in node_types
        assert "SecurityBehavior" in node_types
        assert "Alert" in node_types
        assert "RequiredTactic" in node_types

    def test_tactic_def_lookup(self) -> None:
        tactic = self.params["node_types"]["TacticDef"]
        assert tactic["constraint"]["create"] == "lookup"
        assert tactic["resolution_policy"] == "lookup"
        assert tactic["description"] == "MITRE ATT&CK tactic definition."
        search_props = tactic["constraint"]["search"]["properties"]
        assert len(search_props) == 2

    def test_security_behavior_upsert(self) -> None:
        behavior = self.params["node_types"]["SecurityBehavior"]
        assert behavior["constraint"]["create"] == "upsert"
        assert behavior["resolution_policy"] == "upsert"
        assert behavior["required_properties"] == ["description"]
        assert "severity" in behavior["properties"]
        assert behavior["properties"]["severity"]["enum_values"] == [
            "low", "medium", "high", "critical"
        ]

    def test_alert_constraint(self) -> None:
        alert = self.params["node_types"]["Alert"]
        assert alert["constraint"]["when"] == {"severity": "critical"}
        assert alert["constraint"]["set"] == {
            "flagged": True,
            "reviewed_by": {"mode": "auto"},
        }

    def test_required_tactic_resolve(self) -> None:
        req = self.params["node_types"]["RequiredTactic"]
        assert req["constraint"]["create"] == "lookup"
        assert req["constraint"]["on_miss"] == "error"

    def test_mitigates_edge(self) -> None:
        rels = self.params["relationship_types"]
        assert "MITIGATES" in rels
        mit = rels["MITIGATES"]
        assert mit["allowed_source_types"] == ["SecurityBehavior"]
        assert mit["allowed_target_types"] == ["TacticDef"]
        assert mit["constraint"]["create"] == "lookup"
        search_props = mit["constraint"]["search"]["properties"]
        assert len(search_props) == 2

    def test_triggers_edge(self) -> None:
        rels = self.params["relationship_types"]
        assert "TRIGGERS" in rels
        trig = rels["TRIGGERS"]
        assert trig["allowed_source_types"] == ["SecurityBehavior"]
        assert trig["allowed_target_types"] == ["Alert"]
        assert trig["constraint"]["create"] == "upsert"

    def test_link_to_single(self) -> None:
        result = build_link_to(self.schema_cls.Alert.title)
        assert result == "Alert:title"

    def test_link_to_multiple(self) -> None:
        result = build_link_to(
            self.schema_cls.Alert.title,
            self.schema_cls.TacticDef.name,
        )
        assert result == ["Alert:title", "TacticDef:name"]

    def test_link_to_with_exact_value(self) -> None:
        result = build_link_to(self.schema_cls.Alert.alert_id.exact("ALERT-001"))
        assert result == "Alert:alert_id=ALERT-001"

    def test_link_to_with_semantic_value(self) -> None:
        result = build_link_to(
            self.schema_cls.TacticDef.name.semantic(0.90, "credential access")
        )
        assert result == "TacticDef:name~credential access"


class TestConversationSchema:
    """Integration test for a simple conversation tracking use case."""

    def setup_method(self) -> None:
        @schema("conversations")
        class ConvSchema:
            @node
            @upsert
            class Customer:
                email: str = prop(search=exact())
                name: str = prop(required=True, search=semantic(0.85))

            @node
            @upsert
            class Conversation:
                call_id: str = prop(search=exact())
                topic: str = prop(search=semantic(0.85))
                sentiment: str = prop(enum_values=["positive", "neutral", "negative"])

            @node
            @lookup
            class Product:
                sku: str = prop(search=exact())
                name: str = prop(search=semantic(0.90))

            participates_in = edge(Customer, Conversation, create="upsert")
            discusses = edge(Conversation, Product, create="lookup")

        self.schema_cls = ConvSchema
        self.params = build_schema_params(ConvSchema)

    def test_all_nodes_present(self) -> None:
        assert set(self.params["node_types"].keys()) == {
            "Customer", "Conversation", "Product"
        }

    def test_all_edges_present(self) -> None:
        assert set(self.params["relationship_types"].keys()) == {
            "PARTICIPATES_IN", "DISCUSSES"
        }

    def test_customer_properties(self) -> None:
        cust = self.params["node_types"]["Customer"]
        assert "email" in cust["properties"]
        assert "name" in cust["properties"]
        assert cust["required_properties"] == ["name"]

    def test_product_lookup(self) -> None:
        prod = self.params["node_types"]["Product"]
        assert prod["constraint"]["create"] == "lookup"

    def test_build_link_to_integration(self) -> None:
        link = build_link_to(
            self.schema_cls.Customer.email.exact("john@example.com"),
            self.schema_cls.Conversation.topic,
        )
        assert link == [
            "Customer:email=john@example.com",
            "Conversation:topic",
        ]


class TestComplexConditions:
    """Integration test for complex when conditions with And/Or/Not."""

    def test_complex_when_round_trip(self) -> None:
        @schema("test")
        class TestSchema:
            @node
            @upsert
            @constraint(
                when=And(
                    Or({"severity": "high"}, {"severity": "critical"}),
                    Not({"status": "resolved"}),
                    {"team": "security"},
                ),
                set={"needs_review": True, "summary": Auto()},
            )
            class Incident:
                title: str = prop(search=semantic(0.85))
                severity: str = prop()
                status: str = prop()

        params = build_schema_params(TestSchema)
        inc = params["node_types"]["Incident"]
        assert inc["constraint"]["when"] == {
            "_and": [
                {"_or": [{"severity": "high"}, {"severity": "critical"}]},
                {"_not": {"status": "resolved"}},
                {"team": "security"},
            ]
        }
        assert inc["constraint"]["set"] == {
            "needs_review": True,
            "summary": {"mode": "auto"},
        }


class TestMemoryPolicyIntegration:
    """Integration test for build_memory_policy."""

    def test_full_policy(self) -> None:
        policy = build_memory_policy(
            schema_id="sec_monitoring_v1",
            mode="manual",
            node_constraints=[
                {
                    "node_type": "Alert",
                    "create": "upsert",
                    "search": {
                        "properties": [
                            {"name": "alert_id", "mode": "exact"},
                        ]
                    },
                    "set": serialize_set_values({"summary": Auto(), "status": "open"}),
                }
            ],
            edge_constraints=[
                {
                    "relationship_type": "TRIGGERS",
                    "create": "upsert",
                }
            ],
        )
        assert policy["schema_id"] == "sec_monitoring_v1"
        assert policy["mode"] == "manual"
        assert len(policy["node_constraints"]) == 1
        assert policy["node_constraints"][0]["set"] == {
            "summary": {"mode": "auto"},
            "status": "open",
        }
        assert len(policy["edge_constraints"]) == 1


class TestAutoPromptIntegration:
    """Integration test for Auto('prompt') through schema -> build_schema_params."""

    def test_constraint_with_auto_prompt(self) -> None:
        @schema("test")
        class TestSchema:
            @node
            @upsert
            @constraint(
                when={"severity": "critical"},
                set={
                    "flagged": True,
                    "summary": Auto("Summarize the security incident in 1-2 sentences"),
                },
            )
            class Alert:
                title: str = prop(search=semantic(0.85))
                severity: str = prop()

        params = build_schema_params(TestSchema)
        alert_constraint = params["node_types"]["Alert"]["constraint"]
        assert alert_constraint["set"] == {
            "flagged": True,
            "summary": {"mode": "auto", "prompt": "Summarize the security incident in 1-2 sentences"},
        }

    def test_memory_policy_with_auto_prompt(self) -> None:
        policy = build_memory_policy(
            schema_id="my_schema",
            node_constraints=[
                {
                    "node_type": "Task",
                    "create": "upsert",
                    "set": serialize_set_values({
                        "summary": Auto("Summarize briefly"),
                        "status": "open",
                    }),
                }
            ],
        )
        assert policy["node_constraints"][0]["set"] == {
            "summary": {"mode": "auto", "prompt": "Summarize briefly"},
            "status": "open",
        }


class TestImportPaths:
    """Verify all public imports work from papr_memory.lib."""

    def test_all_imports(self) -> None:
        from papr_memory.lib import (  # noqa: F401
            Or,
            And,
            Not,
            Auto,
            PropertyRef,
            edge,
            node,
            prop,
            exact,
            fuzzy,
            lookup,
            schema,
            upsert,
            resolve,
            semantic,
            constraint,
            build_link_to,
            build_memory_policy,
            build_schema_params,
            serialize_set_values,
        )
        # Verify they're the right types
        assert callable(schema)
        assert callable(node)
        assert callable(build_schema_params)
        assert callable(build_link_to)

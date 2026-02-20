"""Tests for papr_memory.lib._conditions module."""

from papr_memory.lib._conditions import And, Not, Or, _condition_to_dict


class TestAnd:
    def test_basic(self) -> None:
        result = And({"a": 1}, {"b": 2}).to_dict()
        assert result == {"_and": [{"a": 1}, {"b": 2}]}

    def test_single(self) -> None:
        result = And({"a": 1}).to_dict()
        assert result == {"_and": [{"a": 1}]}

    def test_three_conditions(self) -> None:
        result = And({"a": 1}, {"b": 2}, {"c": 3}).to_dict()
        assert result == {"_and": [{"a": 1}, {"b": 2}, {"c": 3}]}

    def test_repr(self) -> None:
        r = repr(And({"a": 1}, {"b": 2}))
        assert "And(" in r

    def test_nested_or(self) -> None:
        result = And({"a": 1}, Or({"b": 2}, {"c": 3})).to_dict()
        assert result == {
            "_and": [
                {"a": 1},
                {"_or": [{"b": 2}, {"c": 3}]},
            ]
        }


class TestOr:
    def test_basic(self) -> None:
        result = Or({"status": "active"}, {"status": "pending"}).to_dict()
        assert result == {"_or": [{"status": "active"}, {"status": "pending"}]}

    def test_repr(self) -> None:
        r = repr(Or({"a": 1}))
        assert "Or(" in r

    def test_nested_and(self) -> None:
        result = Or(
            And({"a": 1}, {"b": 2}),
            {"c": 3},
        ).to_dict()
        assert result == {
            "_or": [
                {"_and": [{"a": 1}, {"b": 2}]},
                {"c": 3},
            ]
        }


class TestNot:
    def test_basic(self) -> None:
        result = Not({"status": "completed"}).to_dict()
        assert result == {"_not": {"status": "completed"}}

    def test_repr(self) -> None:
        r = repr(Not({"a": 1}))
        assert "Not(" in r

    def test_nested(self) -> None:
        result = Not(And({"a": 1}, {"b": 2})).to_dict()
        assert result == {"_not": {"_and": [{"a": 1}, {"b": 2}]}}


class TestConditionToDict:
    def test_dict_passthrough(self) -> None:
        d = {"key": "value"}
        assert _condition_to_dict(d) is d

    def test_and(self) -> None:
        result = _condition_to_dict(And({"a": 1}))
        assert result == {"_and": [{"a": 1}]}

    def test_or(self) -> None:
        result = _condition_to_dict(Or({"a": 1}))
        assert result == {"_or": [{"a": 1}]}

    def test_not(self) -> None:
        result = _condition_to_dict(Not({"a": 1}))
        assert result == {"_not": {"a": 1}}


class TestDeepNesting:
    def test_complex_nesting(self) -> None:
        """And(Or(dict, Not(dict)), And(dict, dict))"""
        result = And(
            Or({"priority": "high"}, Not({"status": "completed"})),
            And({"team": "security"}, {"flagged": True}),
        ).to_dict()
        assert result == {
            "_and": [
                {
                    "_or": [
                        {"priority": "high"},
                        {"_not": {"status": "completed"}},
                    ]
                },
                {
                    "_and": [
                        {"team": "security"},
                        {"flagged": True},
                    ]
                },
            ]
        }

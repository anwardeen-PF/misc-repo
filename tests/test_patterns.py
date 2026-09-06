from datetime import datetime, timedelta

from noc_patterns.correlation import Alert, correlate
from noc_patterns.operator_card import Field, Section, render_card


def test_correlation_same_node_and_window():
    alerts = [
        Alert("1", "node-a", "disk", "hardware", datetime(2026, 1, 1, 0, 0)),
        Alert("2", "node-a", "disk", "service", datetime(2026, 1, 1, 0, 5)),
    ]
    result = correlate(alerts, timedelta(minutes=10))
    assert result.same_node is True
    assert result.within_window is True
    assert result.likely_same_incident is True


def test_card_wraps_long_values():
    card = render_card(
        "TEST",
        [Section("DETAILS", (Field("FQDD", "x" * 120),))],
        width=72,
    )
    lines = card.splitlines()
    assert all(len(line) == 72 for line in lines)
    assert len(lines) > 5

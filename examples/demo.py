from datetime import datetime, timedelta

from noc_patterns.correlation import Alert, correlate
from noc_patterns.operator_card import Field, Section, render_card


alerts = [
    Alert(
        alert_id="A-1001",
        node="edge-node-01",
        component="storage",
        family="disk-health",
        occurred_at=datetime(2026, 9, 6, 4, 20),
    ),
    Alert(
        alert_id="A-1002",
        node="edge-node-01",
        component="storage",
        family="service-health",
        occurred_at=datetime(2026, 9, 6, 4, 24),
    ),
]

result = correlate(alerts, window=timedelta(minutes=10))

print(
    render_card(
        "INCIDENT CORRELATION",
        [
            Section(
                "INCIDENT",
                (
                    Field("Alerts", ", ".join(result.alert_ids)),
                    Field("Same Node", str(result.same_node)),
                    Field("Time Window", str(result.within_window)),
                ),
            ),
            Section(
                "INTERPRETATION",
                (
                    Field(
                        "Finding",
                        "[WARN] Likely one incident candidate"
                        if result.likely_same_incident
                        else "[INFO] Independent review required",
                    ),
                ),
            ),
            Section(
                "NEXT ACTION",
                (
                    Field(
                        "Decision",
                        "Correlate supporting evidence before escalation.",
                    ),
                ),
            ),
        ],
    )
)

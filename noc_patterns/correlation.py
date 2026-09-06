from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Iterable


@dataclass(frozen=True)
class Alert:
    alert_id: str
    node: str
    component: str
    family: str
    occurred_at: datetime
    scope: str = ""


@dataclass(frozen=True)
class CorrelationResult:
    alert_ids: tuple[str, ...]
    same_node: bool
    same_component: bool
    same_family: bool
    within_window: bool

    @property
    def likely_same_incident(self) -> bool:
        return self.same_node and self.within_window and (
            self.same_component or self.same_family
        )


def correlate(alerts: Iterable[Alert], window: timedelta = timedelta(minutes=10)) -> CorrelationResult:
    """Correlate a small alert set without pretending to determine root cause."""
    alerts = tuple(alerts)
    if not alerts:
        raise ValueError("at least one alert is required")

    nodes = {a.node for a in alerts}
    components = {a.component for a in alerts}
    families = {a.family for a in alerts}
    times = [a.occurred_at for a in alerts]

    return CorrelationResult(
        alert_ids=tuple(a.alert_id for a in alerts),
        same_node=len(nodes) == 1,
        same_component=len(components) == 1,
        same_family=len(families) == 1,
        within_window=max(times) - min(times) <= window,
    )

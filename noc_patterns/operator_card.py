from __future__ import annotations

import shutil
import textwrap
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Field:
    label: str
    value: str


@dataclass(frozen=True)
class Section:
    title: str
    fields: tuple[Field, ...]


def _terminal_width(default: int = 80) -> int:
    cols = shutil.get_terminal_size((default, 24)).columns
    return max(64, min(cols, 100))


def render_card(title: str, sections: Iterable[Section], width: int | None = None) -> str:
    """Render a human-first NOC card with wrapped values."""
    width = width or _terminal_width()
    inner = width - 2
    label_width = 16
    value_width = inner - label_width - 3

    out: list[str] = []

    def border(left: str, fill: str, right: str) -> None:
        out.append(left + fill * (width - 2) + right)

    def row(label: str, value: str) -> None:
        value = " ".join(str(value).split()) or "—"
        wrapped = textwrap.wrap(
            value,
            width=value_width,
            break_long_words=True,
            break_on_hyphens=False,
        ) or ["—"]

        for index, part in enumerate(wrapped):
            shown_label = label if index == 0 else ""
            out.append(f"│ {shown_label:<{label_width}} {part:<{value_width}} │")

    border("╭", "─", "╮")
    row("VIEW", title)

    for section in sections:
        text = f" {section.title} "
        out.append("├" + text + "─" * max(0, width - 2 - len(text)) + "┤")
        for field in section.fields:
            row(field.label, field.value)

    border("╰", "─", "╯")
    return "\n".join(out)

from __future__ import annotations

from dataclasses import asdict, dataclass, field, is_dataclass
from typing import Any


@dataclass(slots=True)
class HistoryEntry:
    modified_date: str | None
    version: str | None
    order_number: str | None
    modified_by: str | None
    modified: str | None
    extra_attributes: dict[str, str] = field(default_factory=dict)


@dataclass(slots=True)
class ParameterDecl:
    category: str
    param_id: str
    uuid: str | None
    param_type: str | None
    type_name: str | None
    name: str | None
    comments: str | None
    default_value: str | None
    flags: str | None
    extra_attributes: dict[str, str] = field(default_factory=dict)


@dataclass(slots=True)
class CodeStatement:
    kind: str
    line_start: int
    line_end: int
    raw: str
    tag: str | None = None
    name: str | None = None
    groups: list[str] = field(default_factory=list)
    arguments: list[list[dict[str, str]]] = field(default_factory=list)
    condition: str | None = None
    target: str | None = None
    reads: list[str] = field(default_factory=list)
    writes: list[str] = field(default_factory=list)


@dataclass(slots=True)
class ParsedUnit:
    path: str
    file_name: str
    unit_kind: str
    prefix: str
    name: str
    chinese_name: str | None
    object_id: str | None
    attributes: dict[str, str] = field(default_factory=dict)
    histories: list[HistoryEntry] = field(default_factory=list)
    parameters: list[ParameterDecl] = field(default_factory=list)
    statements: list[CodeStatement] = field(default_factory=list)
    code_line_count: int = 0
    code_text: str = ""

    def to_dict(self) -> dict[str, Any]:
        return _to_plain(self)


def _to_plain(value: Any) -> Any:
    if is_dataclass(value):
        return {key: _to_plain(val) for key, val in asdict(value).items()}
    if isinstance(value, list):
        return [_to_plain(item) for item in value]
    if isinstance(value, dict):
        return {key: _to_plain(val) for key, val in value.items()}
    return value

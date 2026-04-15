from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

from .metadata_parser import MetadataFileParser, SUPPORTED_METADATA_SUFFIXES, is_metadata_path
from .models import CodeStatement, HistoryEntry, ParameterDecl, ParsedUnit

SUPPORTED_CODE_SUFFIXES = {
    ".uftfunction",
    ".uftservice",
    ".uftatomfunction",
    ".uftatomservice",
    ".uftfactorservice",
    ".extinterface",
}
SUPPORTED_SUFFIXES = SUPPORTED_CODE_SUFFIXES | SUPPORTED_METADATA_SUFFIXES

CALL_PREFIXES = ("LF_", "LS_", "AF_", "AS_", "RS_")
PARAM_TAG_MAP = {
    "inputParameters": "input",
    "outputParameters": "output",
    "internalParams": "internal",
}

TAG_PREFIX_RE = re.compile(r"^(?P<tag><[A-Za-z_]+>)\s*")
LABEL_RE = re.compile(r"^(?P<label><[A-Za-z_]+>|[A-Za-z_][A-Za-z0-9_]*)\s*:\s*$")
CONTROL_RE = re.compile(r"^(if|else if|else|while|switch|break|continue)\b")
VAR_TOKEN_RE = re.compile(r"@[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)?(?:\[[^\]]+\])?")
ASSIGN_RE = re.compile(r"(?P<lhs>@[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)?)\s*=")
GOTO_RE = re.compile(r"^goto\s+(?P<label>[A-Za-z_][A-Za-z0-9_]*)\s*;?\s*$")
PREFIX_INC_RE = re.compile(r"(\+\+|--)\s*(?P<var>@[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)?)")
SUFFIX_INC_RE = re.compile(r"(?P<var>@[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)?)\s*(\+\+|--)")
WRITE_CALL_PATTERNS = [
    re.compile(r"(?:hs_strcpy|strcpy|sprintf|snprintf|hs_snprintf)\s*\(\s*(?P<var>@[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)?)"),
    re.compile(r"substr\s*\([^,]+,[^,]+,[^,]+,\s*(?P<var>@[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)?)\s*\)"),
]


class UftDslParser:
    def __init__(self) -> None:
        self.metadata_parser = MetadataFileParser()

    def parse_path(self, path: str | Path) -> ParsedUnit:
        file_path = Path(path)
        if is_metadata_path(file_path):
            return self.metadata_parser.parse_path(file_path)

        if file_path.suffix not in SUPPORTED_CODE_SUFFIXES:
            raise ValueError(f"Unsupported file suffix: {file_path.suffix}")

        root = ET.parse(file_path).getroot()
        unit_kind = _local_name(root.tag)
        file_name = file_path.name
        stem = file_name.rsplit(".", 1)[0]
        prefix = stem.split("_", 1)[0] if "_" in stem else stem
        attributes = {key: value for key, value in root.attrib.items()}

        unit = ParsedUnit(
            path=str(file_path),
            file_name=file_name,
            unit_kind=unit_kind,
            prefix=prefix,
            name=stem,
            chinese_name=root.attrib.get("chineseName"),
            object_id=root.attrib.get("objectId"),
            attributes=attributes,
        )

        for child in root:
            local_name = _local_name(child.tag)
            if local_name == "histories":
                unit.histories.append(
                    HistoryEntry(
                        modified_date=child.attrib.get("modifiedDate"),
                        version=child.attrib.get("version"),
                        order_number=child.attrib.get("orderNumber"),
                        modified_by=child.attrib.get("modifiedBy"),
                        modified=child.attrib.get("modified"),
                        extra_attributes=_extra_attributes(
                            child.attrib,
                            {"modifiedDate", "version", "orderNumber", "modifiedBy", "modified"},
                        ),
                    )
                )
            elif local_name in PARAM_TAG_MAP:
                unit.parameters.append(
                    ParameterDecl(
                        category=PARAM_TAG_MAP[local_name],
                        param_id=child.attrib.get("id", ""),
                        uuid=child.attrib.get("uuid"),
                        param_type=child.attrib.get("paramType"),
                        type_name=child.attrib.get("type"),
                        name=child.attrib.get("name"),
                        comments=child.attrib.get("comments"),
                        default_value=child.attrib.get("defaultValue"),
                        flags=child.attrib.get("flags"),
                        extra_attributes=_extra_attributes(
                            child.attrib,
                            {
                                "id",
                                "uuid",
                                "paramType",
                                "type",
                                "name",
                                "comments",
                                "defaultValue",
                                "flags",
                            },
                        ),
                    )
                )
            elif local_name == "code":
                code_text = child.text or ""
                unit.code_text = code_text
                unit.statements = self._parse_code(code_text)
                unit.code_line_count = len(code_text.splitlines())

        return unit

    def _parse_code(self, code_text: str) -> list[CodeStatement]:
        lines = code_text.splitlines()
        statements: list[CodeStatement] = []
        index = 0

        while index < len(lines):
            raw_line = lines[index]
            stripped = raw_line.strip()
            line_no = index + 1

            if not stripped:
                index += 1
                continue

            if stripped.startswith("//"):
                statements.append(
                    self._make_statement(
                        kind="comment",
                        start=line_no,
                        end=line_no,
                        raw=raw_line,
                    )
                )
                index += 1
                continue

            if LABEL_RE.match(stripped):
                label = LABEL_RE.match(stripped).group("label")
                statements.append(
                    self._make_statement(
                        kind="label",
                        start=line_no,
                        end=line_no,
                        raw=raw_line,
                        target=label.strip("<>"),
                    )
                )
                index += 1
                continue

            if stripped in {"{", "}"}:
                statements.append(
                    self._make_statement(
                        kind="brace",
                        start=line_no,
                        end=line_no,
                        raw=raw_line,
                        name=stripped,
                    )
                )
                index += 1
                continue

            if self._looks_like_action(stripped):
                block, end_index = self._collect_action(lines, index)
                statements.append(self._parse_action_statement(block, line_no, end_index + 1))
                index = end_index + 1
                continue

            if CONTROL_RE.match(stripped):
                block, end_index = self._collect_control(lines, index)
                statements.append(self._parse_control_statement(block, line_no, end_index + 1))
                index = end_index + 1
                continue

            goto_match = GOTO_RE.match(stripped)
            if goto_match:
                statements.append(
                    self._make_statement(
                        kind="goto",
                        start=line_no,
                        end=line_no,
                        raw=raw_line,
                        target=goto_match.group("label"),
                    )
                )
                index += 1
                continue

            block, end_index = self._collect_raw(lines, index)
            statements.append(self._parse_raw_statement(block, line_no, end_index + 1))
            index = end_index + 1

        return statements

    def _looks_like_action(self, stripped: str) -> bool:
        candidate = stripped
        tag_match = TAG_PREFIX_RE.match(candidate)
        if tag_match:
            candidate = candidate[tag_match.end():].lstrip()
        return candidate.startswith("[")

    def _collect_action(self, lines: list[str], start_index: int) -> tuple[str, int]:
        balance = 0
        end_index = start_index
        parts: list[str] = []

        while end_index < len(lines):
            current = lines[end_index]
            parts.append(current)
            balance += _bracket_balance(current)
            if balance <= 0 and end_index > start_index:
                break
            if balance == 0 and current.strip():
                break
            end_index += 1

        return "\n".join(parts), end_index

    def _collect_control(self, lines: list[str], start_index: int) -> tuple[str, int]:
        balance = 0
        end_index = start_index
        parts: list[str] = []

        while end_index < len(lines):
            current = lines[end_index]
            parts.append(current)
            balance += _paren_balance(current)
            stripped = current.strip()
            if stripped.startswith("break") or stripped.startswith("continue"):
                break
            if balance <= 0 and (stripped.endswith("{") or stripped.endswith(")") or stripped == "else"):
                break
            if stripped.startswith("else") and balance == 0 and end_index == start_index:
                break
            end_index += 1

        return "\n".join(parts), end_index

    def _collect_raw(self, lines: list[str], start_index: int) -> tuple[str, int]:
        end_index = start_index
        parts: list[str] = [lines[start_index]]

        while end_index < len(lines) - 1:
            stripped = lines[end_index].strip()
            if stripped.endswith(";") or stripped.endswith("{") or stripped.endswith("}") or stripped.endswith(":"):
                break
            if not stripped:
                break

            next_line = lines[end_index + 1].strip()
            if not next_line or next_line.startswith("//") or self._looks_like_action(next_line) or CONTROL_RE.match(next_line):
                break

            end_index += 1
            parts.append(lines[end_index])
            if lines[end_index].strip().endswith(";"):
                break

        return "\n".join(parts), end_index

    def _parse_action_statement(self, raw: str, start: int, end: int) -> CodeStatement:
        stripped = raw.strip()
        tag = None
        tag_match = TAG_PREFIX_RE.match(stripped)
        if tag_match:
            tag = tag_match.group("tag").strip("<>")
            stripped = stripped[tag_match.end():].lstrip()

        groups = _extract_bracket_groups(stripped)
        name = groups[0] if groups else None
        kind = "call" if name and name.startswith(CALL_PREFIXES) else "action"
        arguments = [_parse_group_arguments(group) for group in groups[1:]]

        return self._make_statement(
            kind=kind,
            start=start,
            end=end,
            raw=raw,
            tag=tag,
            name=name,
            groups=groups,
            arguments=arguments,
        )

    def _parse_control_statement(self, raw: str, start: int, end: int) -> CodeStatement:
        stripped = raw.strip()
        kind = "control"
        name = None
        condition = None

        if stripped.startswith("else if"):
            name = "else if"
            condition = _extract_condition(stripped[len("else if"):].strip())
        elif stripped.startswith("if"):
            name = "if"
            condition = _extract_condition(stripped[len("if"):].strip())
        elif stripped.startswith("while"):
            name = "while"
            condition = _extract_condition(stripped[len("while"):].strip())
        elif stripped.startswith("switch"):
            name = "switch"
            condition = _extract_condition(stripped[len("switch"):].strip())
        elif stripped.startswith("else"):
            name = "else"
        elif stripped.startswith("break"):
            name = "break"
        elif stripped.startswith("continue"):
            name = "continue"

        return self._make_statement(
            kind=kind,
            start=start,
            end=end,
            raw=raw,
            name=name,
            condition=condition,
        )

    def _parse_raw_statement(self, raw: str, start: int, end: int) -> CodeStatement:
        stripped = raw.strip()
        writes = _extract_writes(stripped)
        kind = "assignment" if writes else "raw"

        return self._make_statement(
            kind=kind,
            start=start,
            end=end,
            raw=raw,
            writes=writes,
        )

    def _make_statement(
        self,
        *,
        kind: str,
        start: int,
        end: int,
        raw: str,
        tag: str | None = None,
        name: str | None = None,
        groups: list[str] | None = None,
        arguments: list[list[dict[str, str]]] | None = None,
        condition: str | None = None,
        target: str | None = None,
        writes: list[str] | None = None,
    ) -> CodeStatement:
        return CodeStatement(
            kind=kind,
            line_start=start,
            line_end=end,
            raw=raw,
            tag=tag,
            name=name,
            groups=groups or [],
            arguments=arguments or [],
            condition=condition,
            target=target,
            reads=_extract_reads(raw),
            writes=writes or _extract_writes(raw),
        )


def is_supported_path(path: str | Path) -> bool:
    file_path = Path(path)
    return file_path.suffix in SUPPORTED_CODE_SUFFIXES or is_metadata_path(file_path)


def _local_name(tag: str) -> str:
    if "}" in tag:
        return tag.split("}", 1)[1]
    return tag


def _extra_attributes(attrs: dict[str, str], known: set[str]) -> dict[str, str]:
    return {key: value for key, value in attrs.items() if key not in known}


def _bracket_balance(text: str) -> int:
    return text.count("[") - text.count("]")


def _paren_balance(text: str) -> int:
    return text.count("(") - text.count(")")


def _extract_bracket_groups(text: str) -> list[str]:
    groups: list[str] = []
    index = 0

    while index < len(text):
        if text[index] != "[":
            index += 1
            continue

        depth = 1
        start = index + 1
        index += 1

        while index < len(text) and depth > 0:
            char = text[index]
            if char == "[":
                depth += 1
            elif char == "]":
                depth -= 1
                if depth == 0:
                    groups.append(text[start:index].strip())
                    break
            index += 1

        index += 1

    return groups


def _extract_condition(text: str) -> str | None:
    text = text.strip()
    if not text.startswith("("):
        return None
    depth = 0
    start = None
    for index, char in enumerate(text):
        if char == "(":
            if start is None:
                start = index + 1
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0 and start is not None:
                return text[start:index].strip()
    return None


def _extract_reads(text: str) -> list[str]:
    seen: list[str] = []
    for match in VAR_TOKEN_RE.finditer(text):
        token = match.group(0)
        if token not in seen:
            seen.append(token)
    return seen


def _extract_writes(text: str) -> list[str]:
    seen: list[str] = []
    for match in ASSIGN_RE.finditer(text):
        token = match.group("lhs")
        if token not in seen:
            seen.append(token)
    for match in PREFIX_INC_RE.finditer(text):
        token = match.group("var")
        if token not in seen:
            seen.append(token)
    for match in SUFFIX_INC_RE.finditer(text):
        token = match.group("var")
        if token not in seen:
            seen.append(token)
    for pattern in WRITE_CALL_PATTERNS:
        for match in pattern.finditer(text):
            token = match.group("var")
            if token not in seen:
                seen.append(token)
    return seen


def _parse_group_arguments(group: str) -> list[dict[str, str]]:
    if not group:
        return []
    if "=" not in group:
        return [{"raw": group}]

    result: list[dict[str, str]] = []
    for item in _split_top_level(group):
        if "=" in item:
            key, value = item.split("=", 1)
            result.append({"key": key.strip(), "value": value.strip()})
        else:
            result.append({"raw": item.strip()})
    return result


def _split_top_level(text: str) -> list[str]:
    parts: list[str] = []
    current: list[str] = []
    paren_depth = 0
    bracket_depth = 0
    quote: str | None = None

    for char in text:
        if quote:
            current.append(char)
            if char == quote:
                quote = None
            continue

        if char in {"'", '"'}:
            quote = char
            current.append(char)
            continue

        if char == "(":
            paren_depth += 1
        elif char == ")" and paren_depth > 0:
            paren_depth -= 1
        elif char == "[":
            bracket_depth += 1
        elif char == "]" and bracket_depth > 0:
            bracket_depth -= 1

        if char == "," and paren_depth == 0 and bracket_depth == 0:
            item = "".join(current).strip()
            if item:
                parts.append(item)
            current = []
            continue

        current.append(char)

    tail = "".join(current).strip()
    if tail:
        parts.append(tail)
    return parts

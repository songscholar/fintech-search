from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

from .models import CodeStatement, HistoryEntry, ParsedUnit

SUPPORTED_METADATA_SUFFIXES = {
    ".xml",
    ".commondatatype",
    ".stdfield",
    ".datatype",
    ".constant",
    ".dict",
    ".defaultvalue",
    ".defaulttype",
    ".sysconfig",
    ".errorno",
}

METADATA_FILE_LABELS = {
    "stdfield.stdfield": "标准字段",
    "stdobj.xml": "标准组件",
    "datatype.datatype": "业务数据类型",
    "commondatatype.commondatatype": "标准数据类型",
    "defaultvalue.defaultvalue": "默认值",
    "dict.dict": "数据字典",
    "constant.constant": "用户常量",
    "errorno.errorno": "标准错误号",
    "systemmacro.xml": "系统内置宏",
    "usermacro.xml": "用户自定义宏",
    "multicast.xml": "组播域",
    "heterogeneouscomponent.xml": "异构组件",
    "serialNumber.xml": "序列号",
    "interfaceStruct.xml": "接口结构体",
    "wordChangeRule.xml": "词根转换规则",
    "userContext.xml": "用户自定义上下文",
    "topic.xml": "主题域",
    "status.xml": "业务状态域",
    "sysconfig.sysconfig": "系统配置",
    "component.xml": "表数据组件",
    "memoperation.xml": "缓存表定义",
}

ENTRY_TAGS = {"items", "macroItems", "structs", "operations", "indexs", "data"}
PRIMARY_ATTR_KEYS = (
    "name",
    "aliasName",
    "memoryTableName",
    "dbTableName",
    "topicName",
    "serialName",
    "status",
    "display",
    "title",
    "type",
    "paramType",
    "id",
    "key",
    "value",
)
LINE_HINT_ATTR_KEYS = (
    "name",
    "aliasName",
    "memoryTableName",
    "dbTableName",
    "topicName",
    "serialName",
    "status",
    "display",
    "title",
    "paramType",
    "id",
    "key",
)
REF_TOKEN_RE = re.compile(
    r"CNST_[A-Z0-9_]+|ERR_[A-Z0-9_]+|LDP_[A-Z0-9_]+|UFTCORE_ERR_[A-Z0-9_]+|"
    r"comp_[A-Za-z0-9_]+|Hs[A-Za-z0-9_]+|uft[0-9A-Za-z_.]+"
)
BRACKET_NAME_RE = re.compile(r"\[([^\[\]\r\n]+)\]")


def is_metadata_path(path: str | Path) -> bool:
    file_path = Path(path)
    return (
        "metadata" in file_path.parts
        and file_path.is_file()
        and file_path.suffix in SUPPORTED_METADATA_SUFFIXES
    )


class MetadataFileParser:
    def parse_path(self, path: str | Path) -> ParsedUnit:
        file_path = Path(path)
        if not is_metadata_path(file_path):
            raise ValueError(f"Unsupported metadata path: {file_path}")

        text = file_path.read_text(encoding="utf-8", errors="ignore")
        root = ET.fromstring(text)
        core_name = _metadata_core_name(file_path)
        unit = ParsedUnit(
            path=str(file_path),
            file_name=file_path.name,
            unit_kind=f"Metadata::{_local_name(root.tag)}",
            prefix="META",
            name=_metadata_unit_name(file_path),
            chinese_name=f"{core_name} 元数据 {METADATA_FILE_LABELS.get(file_path.name, file_path.name)}",
            object_id=None,
            attributes={
                "metadata_core": core_name,
                "metadata_file_name": file_path.name,
                "metadata_label": METADATA_FILE_LABELS.get(file_path.name, file_path.name),
                "root_tag": _local_name(root.tag),
            },
            code_line_count=len(text.splitlines()),
            code_text=text,
        )

        locator = _MetadataLineLocator(text)
        statements: list[CodeStatement] = []
        cursor = 0
        max_line = max(len(locator.lines), 1) - 1

        for child in root:
            local_name = _local_name(child.tag)
            if local_name == "histories":
                unit.histories.append(_parse_history(child))
                continue
            if local_name == "root":
                if unit.object_id is None:
                    unit.object_id = child.attrib.get("id")
                continue

            child_statements, cursor = self._parse_children(
                element=child,
                file_path=file_path,
                locator=locator,
                search_start=cursor,
                search_end=max_line,
                parent_names=[],
                parent_tag=None,
            )
            statements.extend(child_statements)

        if not statements:
            line_end = max(1, len(locator.lines))
            statements.append(
                CodeStatement(
                    kind="metadata_item",
                    line_start=1,
                    line_end=line_end,
                    raw=_build_empty_metadata_summary(
                        file_name=file_path.name,
                        root_tag=_local_name(root.tag),
                        attributes=unit.attributes,
                    ),
                    tag=_metadata_file_fallback_tag(file_path.name),
                    name=METADATA_FILE_LABELS.get(file_path.name, file_path.stem),
                    groups=[],
                    arguments=[_flatten_attributes(unit.attributes)],
                    condition=None,
                    target=None,
                    reads=[],
                    writes=[],
                )
            )

        unit.statements = statements
        unit.attributes["metadata_entry_count"] = str(len(statements))
        return unit

    def _parse_children(
        self,
        *,
        element: ET.Element,
        file_path: Path,
        locator: "_MetadataLineLocator",
        search_start: int,
        search_end: int,
        parent_names: list[str],
        parent_tag: str | None,
    ) -> tuple[list[CodeStatement], int]:
        statements: list[CodeStatement] = []
        local_name = _local_name(element.tag)

        line_start, line_end = locator.locate(
            element_local=local_name,
            attrs=_normalized_attrs(element.attrib),
            search_start=search_start,
            search_end=search_end,
            hints=_line_hints(element, parent_names),
        )

        statement = self._build_statement(
            file_name=file_path.name,
            element=element,
            line_start=line_start,
            line_end=line_end,
            parent_names=parent_names,
            parent_tag=parent_tag,
        )
        if statement is not None:
            statements.append(statement)

        next_parent_names = parent_names
        next_parent_tag = parent_tag
        if statement is not None:
            next_parent_names = [*parent_names, statement.name] if statement.name else list(parent_names)
            next_parent_tag = statement.tag

        child_cursor = max(line_start - 1, search_start)
        for child in element:
            child_local_name = _local_name(child.tag)
            if child_local_name in {"histories", "root"}:
                continue
            child_statements, child_cursor = self._parse_children(
                element=child,
                file_path=file_path,
                locator=locator,
                search_start=child_cursor,
                search_end=max(line_end - 1, child_cursor),
                parent_names=next_parent_names,
                parent_tag=next_parent_tag,
            )
            statements.extend(child_statements)

        return statements, max(line_end - 1, search_start)

    def _build_statement(
        self,
        *,
        file_name: str,
        element: ET.Element,
        line_start: int,
        line_end: int,
        parent_names: list[str],
        parent_tag: str | None,
    ) -> CodeStatement | None:
        local_name = _local_name(element.tag)
        if local_name not in ENTRY_TAGS:
            return None

        attrs = _normalized_attrs(element.attrib)
        entry_tag = _metadata_entry_tag(
            file_name=file_name,
            local_name=local_name,
            parent_tag=parent_tag,
            parent_names=parent_names,
        )
        entry_name = _metadata_entry_name(
            file_name=file_name,
            local_name=local_name,
            attrs=attrs,
            parent_names=parent_names,
        )
        if entry_name is None:
            entry_name = _fallback_entry_name(local_name=local_name, attrs=attrs, parent_names=parent_names)

        child_items = _child_items(element)
        child_indexes = _child_indexes(element)
        data_mappings = _data_mappings(element)
        refs = _collect_refs(
            entry_name=entry_name,
            attrs=attrs,
            child_items=child_items,
            child_indexes=child_indexes,
            data_mappings=data_mappings,
        )
        raw = _metadata_raw_text(
            file_name=file_name,
            entry_tag=entry_tag,
            entry_name=entry_name,
            attrs=attrs,
            parent_names=parent_names,
            child_items=child_items,
            child_indexes=child_indexes,
            data_mappings=data_mappings,
        )
        arguments = _build_arguments(
            attrs=attrs,
            child_items=child_items,
            child_indexes=child_indexes,
            data_mappings=data_mappings,
            refs=refs,
            parent_names=parent_names,
        )

        return CodeStatement(
            kind="metadata_item",
            line_start=line_start,
            line_end=max(line_end, line_start),
            raw=raw,
            tag=entry_tag,
            name=entry_name,
            groups=list(parent_names),
            arguments=[arguments],
            condition=" > ".join(parent_names) if parent_names else None,
            target=_metadata_primary_target(entry_tag=entry_tag, attrs=attrs, parent_names=parent_names),
            reads=[],
            writes=[],
        )


def _metadata_core_name(file_path: Path) -> str:
    if file_path.parent.name == "metadata" and file_path.parent.parent.name:
        return file_path.parent.parent.name
    return file_path.parent.name


def _metadata_unit_name(file_path: Path) -> str:
    core_name = _metadata_core_name(file_path)
    normalized_name = file_path.name.replace(".", "_")
    return f"META_{core_name}_{normalized_name}"


def _local_name(tag: str) -> str:
    if "}" in tag:
        return tag.split("}", 1)[1]
    return tag


def _normalized_attrs(attrs: dict[str, str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for key, value in attrs.items():
        result[_local_name(key)] = value
    return result


def _parse_history(element: ET.Element) -> HistoryEntry:
    attrs = _normalized_attrs(element.attrib)
    return HistoryEntry(
        modified_date=attrs.get("modifiedDate"),
        version=attrs.get("version"),
        order_number=attrs.get("orderNumber"),
        modified_by=attrs.get("modifiedBy"),
        modified=attrs.get("modified"),
        extra_attributes={
            key: value
            for key, value in attrs.items()
            if key not in {"modifiedDate", "version", "orderNumber", "modifiedBy", "modified"}
        },
    )


def _line_hints(element: ET.Element, parent_names: list[str]) -> list[str]:
    attrs = _normalized_attrs(element.attrib)
    hints: list[str] = []
    for key in LINE_HINT_ATTR_KEYS:
        value = attrs.get(key)
        if value:
            hints.append(f'{key}="{value}"')
            hints.append(value)
    if parent_names:
        hints.append(parent_names[-1])
    return hints


class _MetadataLineLocator:
    def __init__(self, text: str) -> None:
        self.lines = text.splitlines()

    def locate(
        self,
        *,
        element_local: str,
        attrs: dict[str, str],
        search_start: int,
        search_end: int,
        hints: list[str],
    ) -> tuple[int, int]:
        open_line = self._find_open_line(
            element_local=element_local,
            search_start=search_start,
            search_end=search_end,
            hints=hints,
        )
        close_line = self._find_close_line(
            element_local=element_local,
            open_line=open_line,
            search_end=search_end,
        )
        return open_line + 1, close_line + 1

    def _find_open_line(
        self,
        *,
        element_local: str,
        search_start: int,
        search_end: int,
        hints: list[str],
    ) -> int:
        upper = min(search_end, len(self.lines) - 1)
        exact_hints = [hint for hint in hints if '="' in hint]
        loose_hints = [hint for hint in hints if '="' not in hint]
        for line_index in range(max(search_start, 0), upper + 1):
            line = self.lines[line_index]
            if f"<{element_local}" not in line:
                continue
            if any(hint and hint in line for hint in exact_hints):
                return line_index

        for line_index in range(max(search_start, 0), upper + 1):
            line = self.lines[line_index]
            if f"<{element_local}" not in line:
                continue
            if any(hint and hint in line for hint in loose_hints):
                return line_index

        for line_index in range(max(search_start, 0), upper + 1):
            if f"<{element_local}" in self.lines[line_index]:
                return line_index
        return max(min(search_start, len(self.lines) - 1), 0)

    def _find_close_line(
        self,
        *,
        element_local: str,
        open_line: int,
        search_end: int,
    ) -> int:
        if not self.lines:
            return 0

        upper = min(search_end, len(self.lines) - 1)
        if f"<{element_local}" in self.lines[open_line] and "/>" in self.lines[open_line]:
            return open_line

        close_token = f"</{element_local}>"
        for line_index in range(open_line, upper + 1):
            if close_token in self.lines[line_index]:
                return line_index
        return open_line


def _metadata_entry_tag(
    *,
    file_name: str,
    local_name: str,
    parent_tag: str | None,
    parent_names: list[str],
) -> str:
    if local_name == "operations":
        return "metadata_operation"
    if file_name in {"usermacro.xml", "systemmacro.xml"} and local_name == "macroItems":
        return "metadata_macro"
    if file_name == "topic.xml" and local_name == "items":
        return "metadata_topic"
    if file_name == "constant.constant" and local_name == "items":
        return "metadata_constant"
    if file_name == "errorno.errorno" and local_name == "items":
        return "metadata_errorno"
    if file_name == "stdfield.stdfield":
        if local_name == "items":
            return "metadata_standard_field"
        if local_name == "data":
            return "metadata_standard_field_property"
    if file_name == "datatype.datatype" and local_name == "items":
        return "metadata_business_datatype"
    if file_name == "commondatatype.commondatatype" and local_name == "items":
        return "metadata_common_datatype"
    if file_name == "defaulttype.defaulttype":
        if local_name == "items":
            return "metadata_standard_datatype"
        if local_name == "data":
            return "metadata_standard_datatype_mapping"
    if file_name == "defaultvalue.defaultvalue":
        if local_name == "items":
            return "metadata_default_value"
        if local_name == "data":
            return "metadata_default_value_mapping"
    if file_name == "dict.dict" and local_name == "items":
        return "metadata_dictionary"
    if file_name == "component.xml":
        if local_name == "items" and not parent_names:
            return "metadata_component"
        if local_name == "items":
            return "metadata_component_field"
        if local_name == "indexs":
            return "metadata_component_index"
    if file_name == "memoperation.xml":
        if local_name == "items" and not parent_names:
            return "metadata_memory_table"
        if local_name == "indexs":
            return "metadata_memory_index"
    if file_name == "stdobj.xml" and local_name == "items":
        return "metadata_standard_object"
    if file_name == "serialNumber.xml" and local_name == "items":
        return "metadata_serial_number"
    if file_name == "status.xml" and local_name == "items":
        return "metadata_status"
    if file_name == "sysconfig.sysconfig" and local_name == "items":
        return "metadata_sysconfig"
    if file_name == "userContext.xml" and local_name == "structs":
        return "metadata_user_context"
    if file_name == "interfaceStruct.xml" and local_name in {"items", "structs"}:
        return "metadata_interface_struct"
    if file_name == "multicast.xml" and local_name == "items":
        return "metadata_multicast"
    if file_name == "heterogeneouscomponent.xml" and local_name == "items":
        return "metadata_heterogeneous_component"
    if file_name == "wordChangeRule.xml" and local_name == "items":
        return "metadata_word_change_rule"
    if local_name == "indexs":
        return "metadata_index"
    if local_name == "data":
        return "metadata_data_mapping"
    return "metadata_item"


def _metadata_entry_name(
    *,
    file_name: str,
    local_name: str,
    attrs: dict[str, str],
    parent_names: list[str],
) -> str | None:
    base_name = None
    for key in PRIMARY_ATTR_KEYS:
        value = attrs.get(key)
        if value:
            base_name = value
            break

    if local_name == "indexs":
        current_name = attrs.get("name") or attrs.get("fields")
        if current_name and parent_names:
            return f"{parent_names[-1]}.{current_name}"
        return current_name

    if local_name == "data":
        data_key = attrs.get("key") or attrs.get("name")
        if data_key and parent_names:
            return f"{parent_names[-1]}.{data_key}"
        return data_key or attrs.get("value")

    if local_name == "structs":
        type_name = attrs.get("type")
        param_type = attrs.get("paramType")
        if type_name and param_type:
            return f"{param_type}:{type_name}"
        return type_name or param_type

    if local_name == "operations":
        return attrs.get("title") or attrs.get("file")

    if file_name == "component.xml" and local_name == "items" and parent_names:
        if base_name:
            return f"{parent_names[-1]}.{base_name}"
    if file_name == "memoperation.xml" and local_name == "indexs" and parent_names:
        return attrs.get("name") and f"{parent_names[-1]}.{attrs['name']}" or base_name

    return base_name


def _fallback_entry_name(*, local_name: str, attrs: dict[str, str], parent_names: list[str]) -> str:
    if parent_names:
        return f"{parent_names[-1]}.{local_name}"
    if attrs:
        first_key = next(iter(attrs))
        return f"{local_name}:{attrs[first_key]}"
    return local_name


def _metadata_primary_target(
    *,
    entry_tag: str,
    attrs: dict[str, str],
    parent_names: list[str],
) -> str | None:
    if entry_tag == "metadata_topic":
        return attrs.get("topicName")
    if entry_tag == "metadata_standard_field":
        return attrs.get("dataType")
    if entry_tag in {"metadata_business_datatype", "metadata_common_datatype"}:
        return attrs.get("stdType")
    if entry_tag == "metadata_standard_datatype":
        return attrs.get("description")
    if entry_tag == "metadata_constant":
        return attrs.get("value")
    if entry_tag == "metadata_errorno":
        return attrs.get("no")
    if entry_tag == "metadata_default_value":
        return attrs.get("name")
    if entry_tag == "metadata_standard_object":
        return attrs.get("type")
    if entry_tag == "metadata_memory_table":
        return attrs.get("dbTableName") or attrs.get("syncTableName")
    if entry_tag == "metadata_component":
        return attrs.get("name")
    if entry_tag == "metadata_sysconfig":
        return attrs.get("name")
    if entry_tag == "metadata_user_context":
        return attrs.get("type")
    if entry_tag == "metadata_serial_number":
        return attrs.get("id")
    if entry_tag == "metadata_status":
        return attrs.get("value")
    if entry_tag == "metadata_operation":
        return attrs.get("file")
    return None


def _child_items(element: ET.Element) -> list[str]:
    names: list[str] = []
    for child in element:
        if _local_name(child.tag) != "items":
            continue
        attrs = _normalized_attrs(child.attrib)
        child_name = attrs.get("name") or attrs.get("aliasName") or attrs.get("memoryTableName") or attrs.get("topicName")
        if child_name and child_name not in names:
            names.append(child_name)
    return names


def _child_indexes(element: ET.Element) -> list[str]:
    names: list[str] = []
    for child in element:
        if _local_name(child.tag) != "indexs":
            continue
        attrs = _normalized_attrs(child.attrib)
        index_name = attrs.get("name") or attrs.get("fields")
        fields = attrs.get("fields")
        if not index_name:
            continue
        value = f"{index_name}({fields})" if fields else index_name
        if value not in names:
            names.append(value)
    return names


def _data_mappings(element: ET.Element) -> list[str]:
    items: list[str] = []
    for child in element:
        if _local_name(child.tag) != "data":
            continue
        attrs = _normalized_attrs(child.attrib)
        key = attrs.get("key")
        value = attrs.get("value")
        if key and value:
            rendered = f"{key}={value}"
        else:
            rendered = key or value or ""
        if rendered and rendered not in items:
            items.append(rendered)
    return items


def _collect_refs(
    *,
    entry_name: str,
    attrs: dict[str, str],
    child_items: list[str],
    child_indexes: list[str],
    data_mappings: list[str],
) -> list[str]:
    refs: list[str] = []
    seen: set[str] = set()
    text_parts = [entry_name, *attrs.values(), *child_items, *child_indexes, *data_mappings]
    for text in text_parts:
        for match in REF_TOKEN_RE.findall(text):
            if match not in seen:
                seen.add(match)
                refs.append(match)
        for match in BRACKET_NAME_RE.findall(text):
            stripped = match.strip()
            if stripped and stripped not in seen and len(stripped) <= 64:
                seen.add(stripped)
                refs.append(stripped)
    return refs


def _metadata_raw_text(
    *,
    file_name: str,
    entry_tag: str,
    entry_name: str,
    attrs: dict[str, str],
    parent_names: list[str],
    child_items: list[str],
    child_indexes: list[str],
    data_mappings: list[str],
) -> str:
    label = METADATA_FILE_LABELS.get(file_name, file_name)
    lines = [
        f"[{entry_tag}] {entry_name}",
        f"metadata_file: {file_name}",
        f"metadata_label: {label}",
    ]
    if parent_names:
        lines.append(f"context: {' > '.join(parent_names)}")

    multiline_keys = {"content", "description", "flagDescription", "message", "modified"}
    for key, value in attrs.items():
        if not value:
            continue
        if key in multiline_keys and ("\n" in value or "\r" in value or len(value) > 80):
            lines.append(f"{key}:")
            lines.extend(line for line in value.replace("\r\n", "\n").split("\n") if line)
        else:
            lines.append(f"{key}: {value}")

    if child_items:
        lines.append(f"child_items: {', '.join(child_items)}")
    if child_indexes:
        lines.append(f"child_indexes: {', '.join(child_indexes)}")
    if data_mappings:
        lines.append(f"data_mappings: {', '.join(data_mappings)}")
    return "\n".join(lines)


def _build_arguments(
    *,
    attrs: dict[str, str],
    child_items: list[str],
    child_indexes: list[str],
    data_mappings: list[str],
    refs: list[str],
    parent_names: list[str],
) -> list[dict[str, str]]:
    arguments = _flatten_attributes(attrs)
    for value in child_items:
        arguments.append({"key": "child_item", "value": value})
    for value in child_indexes:
        arguments.append({"key": "child_index", "value": value})
    for value in data_mappings:
        arguments.append({"key": "data_mapping", "value": value})
    for value in refs:
        arguments.append({"key": "ref", "value": value})
    for value in parent_names:
        arguments.append({"key": "context", "value": value})
    return arguments


def _flatten_attributes(attrs: dict[str, str]) -> list[dict[str, str]]:
    return [{"key": key, "value": value} for key, value in attrs.items() if value]


def _build_empty_metadata_summary(
    *,
    file_name: str,
    root_tag: str,
    attributes: dict[str, str],
) -> str:
    lines = [
        f"[metadata_file] {file_name}",
        f"root_tag: {root_tag}",
    ]
    for key, value in attributes.items():
        if value:
            lines.append(f"{key}: {value}")
    return "\n".join(lines)


def _metadata_file_fallback_tag(file_name: str) -> str:
    return f"metadata_file::{file_name.replace('.', '_')}"

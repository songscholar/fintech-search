from __future__ import annotations

import re

from .constants import TABLE_WITH_INDEX_RE
from .models import CodeStatement


def derive_target(statement: CodeStatement) -> tuple[str | None, str]:
    from .semantic_recovery import classify_mc_publish

    if statement.kind == "metadata_item":
        if statement.target:
            return statement.target, _metadata_target_kind(statement)
        if statement.name:
            return statement.name, _metadata_entity_kind(statement.tag)
        return None, "metadata"

    if statement.kind == "call" and statement.name:
        return statement.name, "procedure"

    mc_publish_detail = classify_mc_publish(statement)
    if mc_publish_detail is not None and mc_publish_detail.get("topic_name"):
        return str(mc_publish_detail["topic_name"]), "mc_topic"

    if not statement.groups or len(statement.groups) < 2:
        return None, "unknown"

    candidate = statement.groups[1].strip()
    if not candidate:
        return None, "unknown"

    if candidate.startswith("@"):
        return candidate, "variable"

    table_match = TABLE_WITH_INDEX_RE.match(candidate)
    if table_match:
        return table_match.group("table"), "table"

    if "(" in candidate and ")" in candidate:
        return candidate, "expression"

    if "=" in candidate:
        return candidate, "expression"

    lowered = candidate.lower()
    if lowered.startswith(("select ", "update ", "delete ", "insert ")):
        return candidate, "sql"

    if candidate.startswith("comp_"):
        return candidate, "component"

    return candidate, "table"


def metadata_edges_for_statement(statement: CodeStatement) -> list[dict[str, object]]:
    if statement.kind != "metadata_item":
        return []

    edges: list[dict[str, object]] = []
    seen: set[tuple[str, str, str]] = set()

    def add(edge_type: str, target_name: str | None, target_kind: str, detail: dict[str, object] | None = None) -> None:
        name = str(target_name or "").strip()
        if not name:
            return
        key = (edge_type, name, target_kind)
        if key in seen:
            return
        seen.add(key)
        edges.append(
            {
                "edge_type": edge_type,
                "target_name": name,
                "target_kind": target_kind,
                "detail": detail or {},
            }
        )

    if statement.name:
        add(
            _metadata_definition_edge_type(statement),
            statement.name,
            _metadata_entity_kind(statement.tag),
            {"metadata_name": statement.name},
        )

    primary_target = statement.target
    if primary_target:
        if statement.tag == "metadata_topic":
            add("maps_topic_name", primary_target, "mc_topic")
        elif statement.tag == "metadata_memory_table":
            add("maps_db_table", primary_target, "table")
        elif statement.tag == "metadata_component":
            add("maps_component_name", primary_target, "component")
        elif statement.tag == "metadata_standard_field":
            add("uses_datatype", primary_target, "datatype")
        elif statement.tag in {"metadata_business_datatype", "metadata_common_datatype"}:
            add("uses_standard_type", primary_target, "standard_type")
        elif statement.tag == "metadata_standard_object":
            add("maps_object_type", primary_target, "type_reference")
        elif statement.tag == "metadata_errorno":
            add("maps_error_number", primary_target, "error_number")
        elif statement.tag == "metadata_constant":
            add("maps_constant_value", primary_target, "constant_value")
        elif statement.tag == "metadata_operation":
            add("maps_tool_file", primary_target, "tool_file")

    data_type = _metadata_first_value(statement, "dataType", "stdType")
    if data_type:
        edge_type = "uses_standard_type" if _metadata_first_value(statement, "stdType") == data_type else "uses_datatype"
        target_kind = "standard_type" if edge_type == "uses_standard_type" else "datatype"
        add(edge_type, data_type, target_kind)

    default_value = _metadata_first_value(statement, "defaultValue")
    if default_value:
        add("uses_default_value", default_value, "default_value")

    memory_table_name = _metadata_first_value(statement, "memoryTableName")
    if memory_table_name:
        add("maps_memory_table", memory_table_name, "table")

    db_table_name = _metadata_first_value(statement, "dbTableName", "dbTableAliasName")
    if db_table_name:
        add("maps_db_table", db_table_name, "table")

    sync_table_name = _metadata_first_value(statement, "syncTableName")
    if sync_table_name:
        add("maps_sync_table", sync_table_name, "table")

    alias_name = _metadata_first_value(statement, "aliasName")
    if alias_name and statement.tag == "metadata_topic":
        add("defines_topic_alias", alias_name, "topic_alias")

    for key in ("condition1", "condition2", "condition3", "condition4", "condition5", "condition6"):
        for value in _metadata_argument_values(statement, key):
            add("topic_filter_field", value, "field")

    for raw_fields in _metadata_argument_values(statement, "fields"):
        for field_name in _split_csv_values(raw_fields):
            add("contains_field", field_name, "field")

    for child_item in _metadata_argument_values(statement, "child_item"):
        add("contains_field", child_item, "field")

    for child_index in _metadata_argument_values(statement, "child_index"):
        add("contains_index", child_index, "index")

    for data_mapping in _metadata_argument_values(statement, "data_mapping"):
        add("maps_data_value", data_mapping, "mapping")

    for ref in _metadata_argument_values(statement, "ref"):
        if statement.name and ref == statement.name:
            continue
        if primary_target and ref == primary_target:
            continue
        edge_type, target_kind = _classify_metadata_ref(ref)
        add(edge_type, ref, target_kind)

    return edges


def _metadata_entity_kind(tag: str | None) -> str:
    mapping = {
        "metadata_macro": "macro",
        "metadata_topic": "topic_alias",
        "metadata_constant": "constant",
        "metadata_errorno": "error_code",
        "metadata_standard_field": "standard_field",
        "metadata_business_datatype": "business_datatype",
        "metadata_common_datatype": "common_datatype",
        "metadata_standard_datatype": "standard_datatype",
        "metadata_default_value": "default_value",
        "metadata_dictionary": "dictionary",
        "metadata_component": "component",
        "metadata_component_field": "component_field",
        "metadata_component_index": "component_index",
        "metadata_memory_table": "memory_table",
        "metadata_memory_index": "memory_index",
        "metadata_standard_object": "standard_object",
        "metadata_serial_number": "serial_number",
        "metadata_status": "status",
        "metadata_sysconfig": "sysconfig",
        "metadata_user_context": "user_context",
        "metadata_interface_struct": "interface_struct",
        "metadata_multicast": "multicast",
        "metadata_heterogeneous_component": "heterogeneous_component",
        "metadata_word_change_rule": "word_change_rule",
        "metadata_operation": "operation",
        "metadata_standard_datatype_mapping": "data_mapping",
        "metadata_default_value_mapping": "data_mapping",
        "metadata_standard_field_property": "field_property",
        "metadata_data_mapping": "data_mapping",
        "metadata_index": "index",
    }
    return mapping.get(str(tag or ""), "metadata")


def _metadata_target_kind(statement: CodeStatement) -> str:
    tag = str(statement.tag or "")
    if tag == "metadata_topic":
        return "mc_topic"
    if tag == "metadata_errorno":
        return "error_number"
    if tag in {"metadata_standard_field", "metadata_business_datatype", "metadata_common_datatype"}:
        return "datatype"
    if tag == "metadata_constant":
        return "constant_value"
    if tag in {"metadata_memory_table", "metadata_component"}:
        return "table"
    if tag in {"metadata_standard_object", "metadata_user_context", "metadata_interface_struct"}:
        return "type_reference"
    if tag == "metadata_operation":
        return "tool_file"
    return _metadata_entity_kind(statement.tag)


def _metadata_argument_values(statement: CodeStatement, key: str) -> list[str]:
    values: list[str] = []
    for group in statement.arguments:
        for item in group:
            if item.get("key") != key:
                continue
            value = str(item.get("value") or "").strip()
            if value:
                values.append(value)
    return values


def _metadata_first_value(statement: CodeStatement, *keys: str) -> str | None:
    for key in keys:
        values = _metadata_argument_values(statement, key)
        if values:
            return values[0]
    return None


def _split_csv_values(raw: str) -> list[str]:
    if raw == "*":
        return []
    return [item.strip() for item in raw.split(",") if item.strip()]


def _classify_metadata_ref(value: str) -> tuple[str, str]:
    if value.startswith("CNST_"):
        return "references_constant", "constant"
    if value.startswith(("ERR_", "LDP_", "UFTCORE_ERR_")) or re.fullmatch(r"-?\d+", value):
        return "references_error_code", "error_code"
    if value.startswith("comp_"):
        return "references_component", "component"
    if value.startswith("Hs"):
        return "references_datatype", "datatype"
    if value.startswith("uft") and "." in value:
        return "references_topic_name", "mc_topic"
    if value.startswith("idx_"):
        return "references_index", "index"
    return "references_metadata", "metadata"


def _metadata_definition_edge_type(statement: CodeStatement) -> str:
    entity_kind = _metadata_entity_kind(statement.tag)
    if entity_kind == "metadata":
        return "defines_metadata_item"
    return f"defines_{entity_kind}"

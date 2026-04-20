from __future__ import annotations

import re

from .constants import EXIT_LABEL_NAMES, TABLE_WITH_INDEX_RE
from .metadata_semantics import derive_target
from .models import CodeStatement
from .parser import ASSIGN_RE


CHUNK_SIGNIFICANT_LIMIT = 6
PAIRED_BLOCK_ACTIONS = {
    "transaction": ("事务处理开始", "事务处理结束"),
    "sql_query": ("查询SQL语句开始", "查询SQL语句结束"),
    "record_loop": ("遍历记录开始", "遍历记录结束"),
    "record_pool_loop": ("遍历记录池开始", "遍历记录池结束"),
    "component_loop": ("遍历组件开始", "遍历组件结束"),
}
SINGLE_BLOCK_ACTIONS = {
    "通用SQL执行": "sql_execute",
}
BRACE_ATTACHED_BLOCK_ACTIONS = {
    "处理失败": "failure_handler",
    "EXCEPTION": "exception_handler",
    "WHEN_OTHERS": "when_others_handler",
}
SQL_FROM_JOIN_RE = re.compile(r"\b(?:from|join)\s+([A-Za-z_][A-Za-z0-9_$.]*)", re.IGNORECASE)
SQL_UPDATE_RE = re.compile(r"\bupdate\s+([A-Za-z_][A-Za-z0-9_$.]*)", re.IGNORECASE)
SQL_INSERT_RE = re.compile(r"\binsert\s+into\s+([A-Za-z_][A-Za-z0-9_$.]*)", re.IGNORECASE)
SQL_DELETE_RE = re.compile(r"\bdelete\s+from\s+([A-Za-z_][A-Za-z0-9_$.]*)", re.IGNORECASE)
SQL_MERGE_RE = re.compile(r"\bmerge\s+into\s+([A-Za-z_][A-Za-z0-9_$.]*)", re.IGNORECASE)
SQL_STRING_RE = re.compile(r"'(?:''|[^'])*'")
SQL_SKIP_TABLES = {"dual"}
DOUBLE_QUOTED_STRING_RE = re.compile(r'"((?:\\.|[^"\\])*)"')
CALL_EXPR_RE = re.compile(r"(?P<func>hs_snprintf|snprintf|sprintf|hs_strcpy|strcpy)\s*\((?P<args>.*)\)\s*;?\s*$", re.DOTALL)
TRACKED_STRING_VAR_TOKENS = ("sql", "table", "where", "column", "group", "order", "join")
MC_PUBLISH_ACTIONS = {
    "同步消息发布": ("sync", "同步发布"),
    "消息发布": ("async", "异步发布"),
}
LOCAL_CALL_RULES = {
    ("LS", "LF"),
    ("LS", "AF"),
    ("LF", "LF"),
    ("LF", "AF"),
    ("AF", "AF"),
}
RPC_CALL_RULES = {
    ("LS", "LS"),
    ("LF", "LS"),
    ("AF", "LS"),
}
SEMANTIC_RULE_REGISTRY = {
    "call.local": {
        "kind": "call_semantics",
        "label": "本地函数调用",
        "call_kind": "local_function_call",
        "rule_pairs": sorted(f"{source}->{target}" for source, target in LOCAL_CALL_RULES),
    },
    "call.rpc": {
        "kind": "call_semantics",
        "label": "系统间RPC调用",
        "call_kind": "rpc_call",
        "rule_pairs": sorted(f"{source}->{target}" for source, target in RPC_CALL_RULES),
    },
    "message.mc_publish": {
        "kind": "message_publish",
        "label": "消息中心主题发布",
        "actions": sorted(MC_PUBLISH_ACTIONS),
        "publish_modes": {
            action: mode
            for action, (mode, _mode_label) in sorted(MC_PUBLISH_ACTIONS.items())
        },
    },
}


def recover_blocks(statements: list[CodeStatement]) -> list[dict[str, object]]:
    if not statements:
        return []

    brace_pairs = _brace_pairs(statements)
    blocks: list[dict[str, object]] = []
    paired_stacks: dict[str, list[int]] = {block_type: [] for block_type in PAIRED_BLOCK_ACTIONS}

    for seq, statement in enumerate(statements, start=1):
        if statement.kind == "goto" and statement.target:
            block_type = "goto_exit" if statement.target in EXIT_LABEL_NAMES else "goto_jump"
            blocks.append(
                _make_recovered_block(
                    statements=statements,
                    block_type=block_type,
                    anchor_name=statement.target,
                    anchor_seq=seq,
                    statement_start_seq=seq,
                    statement_end_seq=seq,
                )
            )
            continue

        if statement.kind == "label" and statement.target in EXIT_LABEL_NAMES:
            blocks.append(
                _make_recovered_block(
                    statements=statements,
                    block_type="exit_label",
                    anchor_name=statement.target,
                    anchor_seq=seq,
                    statement_start_seq=seq,
                    statement_end_seq=seq,
                )
            )
            continue

        if statement.kind != "action" or not statement.name:
            continue

        for block_type, (start_name, end_name) in PAIRED_BLOCK_ACTIONS.items():
            if statement.name == start_name:
                paired_stacks[block_type].append(seq)
                break
            if statement.name == end_name and paired_stacks[block_type]:
                start_seq = paired_stacks[block_type].pop()
                blocks.append(
                    _make_recovered_block(
                        statements=statements,
                        block_type=block_type,
                        anchor_name=start_name,
                        anchor_seq=start_seq,
                        statement_start_seq=start_seq,
                        statement_end_seq=seq,
                    )
                )
                break

        single_block_type = SINGLE_BLOCK_ACTIONS.get(statement.name)
        if single_block_type is not None:
            blocks.append(
                _make_recovered_block(
                    statements=statements,
                    block_type=single_block_type,
                    anchor_name=statement.name,
                    anchor_seq=seq,
                    statement_start_seq=seq,
                    statement_end_seq=seq,
                )
            )

        brace_block_type = BRACE_ATTACHED_BLOCK_ACTIONS.get(statement.name)
        if brace_block_type is not None:
            end_seq = _find_brace_attached_end(statements, start_seq=seq, brace_pairs=brace_pairs)
            blocks.append(
                _make_recovered_block(
                    statements=statements,
                    block_type=brace_block_type,
                    anchor_name=statement.name,
                    anchor_seq=seq,
                    statement_start_seq=seq,
                    statement_end_seq=end_seq,
                )
            )

    blocks.sort(key=lambda item: (int(item["statement_start_seq"]), int(item["statement_end_seq"]), str(item["block_type"])))
    deduped: list[dict[str, object]] = []
    seen: set[tuple[object, ...]] = set()
    for block in blocks:
        key = (
            block["block_type"],
            block["statement_start_seq"],
            block["statement_end_seq"],
            block["anchor_name"],
        )
        if key in seen:
            continue
        seen.add(key)
        deduped.append(block)
    return deduped


def build_semantic_chunks(
    procedure_name: str,
    statements: list[CodeStatement],
) -> list[dict[str, object]]:
    chunks: list[dict[str, object]] = []
    current: list[tuple[int, CodeStatement]] = []
    significant_count = 0

    def flush() -> None:
        nonlocal current, significant_count
        chunk = _make_chunk(procedure_name, current)
        if chunk is not None:
            chunks.append(chunk)
        current = []
        significant_count = 0

    for seq, statement in enumerate(statements, start=1):
        if statement.kind == "brace":
            if current:
                current.append((seq, statement))
            continue

        if current and _should_start_new_chunk(current, statement, significant_count):
            flush()

        current.append((seq, statement))
        if statement.kind != "comment":
            significant_count += 1

    flush()
    return chunks


def extract_sql_access_edges(
    statement: CodeStatement,
    string_hints: dict[str, str],
) -> list[dict[str, str]]:
    if statement.kind != "action" or statement.name not in {"通用SQL执行", "查询SQL语句开始"}:
        return []
    if len(statement.groups) < 2:
        return []

    sql_text = _resolve_sql_text(statement.groups[1].strip(), string_hints)
    if not sql_text:
        return []

    normalized = _normalize_sql(sql_text)
    if not normalized:
        return []

    accesses: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()

    def add(edge_type: str, table_name: str, operation: str) -> None:
        normalized_table, normalized_edge_type = _normalize_table_reference(table_name, edge_type)
        if not normalized_table or not normalized_edge_type:
            return
        key = (normalized_edge_type, normalized_table)
        if key in seen:
            return
        seen.add(key)
        accesses.append(
            {
                "edge_type": normalized_edge_type,
                "target_name": normalized_table,
                "operation": operation,
                "sql_source": _truncate_text(normalized, 160),
            }
        )

    lower = normalized.lower()
    if lower.startswith("select "):
        for table_name in SQL_FROM_JOIN_RE.findall(normalized):
            add("reads_table", table_name, "select")
        return accesses
    if lower.startswith("update "):
        for table_name in SQL_UPDATE_RE.findall(normalized):
            add("writes_table", table_name, "update")
        for table_name in SQL_FROM_JOIN_RE.findall(normalized):
            add("reads_table", table_name, "update_context")
        return accesses
    if lower.startswith("insert "):
        for table_name in SQL_INSERT_RE.findall(normalized):
            add("writes_table", table_name, "insert")
        for table_name in SQL_FROM_JOIN_RE.findall(normalized):
            add("reads_table", table_name, "insert_select")
        return accesses
    if lower.startswith("delete "):
        for table_name in SQL_DELETE_RE.findall(normalized):
            add("writes_table", table_name, "delete")
        for table_name in SQL_FROM_JOIN_RE.findall(normalized):
            add("reads_table", table_name, "delete_context")
        return accesses
    if lower.startswith("merge "):
        for table_name in SQL_MERGE_RE.findall(normalized):
            add("writes_table", table_name, "merge")
        for table_name in SQL_FROM_JOIN_RE.findall(normalized):
            add("reads_table", table_name, "merge_context")
        return accesses
    return accesses


def update_string_hints(string_hints: dict[str, str], statement: CodeStatement) -> None:
    updates = _extract_string_hint_updates(statement, string_hints)
    for var_name, value in updates.items():
        if value is None:
            string_hints.pop(var_name, None)
        else:
            string_hints[var_name] = value


def format_excerpt(statements: list[dict[str, object]]) -> str:
    lines: list[str] = []
    for statement in statements:
        raw = str(statement["raw"]).strip("\n")
        if not raw:
            continue
        raw_lines = raw.splitlines()
        for index, raw_line in enumerate(raw_lines):
            prefix = f"L{statement['line_start'] + index}: " if index == 0 else "    "
            lines.append(f"{prefix}{raw_line.rstrip()}")
    return "\n".join(lines)


def dedupe_strings(values: list[str]) -> list[str]:
    return list(dict.fromkeys(value for value in values if value))


def maybe_int(value: object) -> int | None:
    if value is None:
        return None
    return int(value)


def _brace_pairs(statements: list[CodeStatement]) -> dict[int, int]:
    stack: list[int] = []
    pairs: dict[int, int] = {}
    for seq, statement in enumerate(statements, start=1):
        if statement.kind != "brace":
            continue
        if statement.name == "{":
            stack.append(seq)
        elif statement.name == "}" and stack:
            pairs[stack.pop()] = seq
    return pairs


def _find_brace_attached_end(
    statements: list[CodeStatement],
    *,
    start_seq: int,
    brace_pairs: dict[int, int],
) -> int:
    for seq in range(start_seq + 1, len(statements) + 1):
        statement = statements[seq - 1]
        if statement.kind == "comment":
            continue
        if statement.kind == "action" and statement.name in {"EXCEPTION", "WHEN_OTHERS"}:
            continue
        if statement.kind == "brace" and statement.name == "{":
            return brace_pairs.get(seq, seq)
        return seq
    return start_seq


def _make_recovered_block(
    *,
    statements: list[CodeStatement],
    block_type: str,
    anchor_name: str,
    anchor_seq: int,
    statement_start_seq: int,
    statement_end_seq: int,
) -> dict[str, object]:
    block_statements = statements[statement_start_seq - 1 : statement_end_seq]
    line_start = min(statement.line_start for statement in block_statements)
    line_end = max(statement.line_end for statement in block_statements)
    return {
        "block_type": block_type,
        "anchor_name": anchor_name,
        "anchor_seq": anchor_seq,
        "statement_start_seq": statement_start_seq,
        "statement_end_seq": statement_end_seq,
        "line_start": line_start,
        "line_end": line_end,
    }


def collect_block_entities(statements: list[CodeStatement]) -> tuple[list[str], list[str], list[str]]:
    action_names = sorted({statement.name for statement in statements if statement.name})
    target_names: set[str] = set()
    variable_names: set[str] = set()
    for statement in statements:
        target_name, _ = derive_target(statement)
        if target_name:
            target_names.add(target_name)
        variable_names.update(statement.reads)
        variable_names.update(statement.writes)
    return action_names, sorted(target_names), sorted(variable_names)


def summarize_block(
    *,
    procedure_name: str,
    block_type: str,
    anchor_name: str,
    statements: list[CodeStatement],
    action_names: list[str],
    target_names: list[str],
) -> str:
    sql_preview = _extract_sql_preview(statements)
    action_preview = ", ".join(action_names[:4])
    target_preview = ", ".join(target_names[:3])
    statement_count = len(statements)

    if block_type == "transaction":
        summary = f"{procedure_name} 的事务块，包含 {statement_count} 条语句"
    elif block_type == "sql_query":
        summary = f"{procedure_name} 的 SQL 查询块"
    elif block_type == "sql_execute":
        summary = f"{procedure_name} 的 SQL 执行语句"
    elif block_type == "failure_handler":
        summary = f"{procedure_name} 的失败处理块"
    elif block_type == "exception_handler":
        summary = f"{procedure_name} 的 EXCEPTION 异常处理块"
    elif block_type == "when_others_handler":
        summary = f"{procedure_name} 的 WHEN_OTHERS 兜底处理块"
    elif block_type == "goto_exit":
        summary = f"{procedure_name} 的退出跳转语句，跳向 {anchor_name}"
    elif block_type == "goto_jump":
        summary = f"{procedure_name} 的跳转语句，跳向 {anchor_name}"
    elif block_type == "exit_label":
        summary = f"{procedure_name} 的退出标签 {anchor_name}"
    elif block_type.endswith("_loop"):
        summary = f"{procedure_name} 的 {anchor_name} 代码块"
    else:
        summary = f"{procedure_name} 的 {anchor_name} 代码块"

    parts = [summary]
    if sql_preview:
        parts.append(f"SQL={sql_preview}")
    if action_preview:
        parts.append(f"actions={action_preview}")
    if target_preview:
        parts.append(f"targets={target_preview}")
    return " | ".join(parts)


def _should_start_new_chunk(
    current: list[tuple[int, CodeStatement]],
    statement: CodeStatement,
    significant_count: int,
) -> bool:
    if statement.kind == "metadata_item":
        return bool(current)
    if any(item.kind == "metadata_item" for _, item in current):
        return True
    if statement.kind == "label":
        return True
    if significant_count >= CHUNK_SIGNIFICANT_LIMIT:
        return True
    if statement.kind in {"control", "goto"} and significant_count >= 2:
        return True
    if statement.kind in {"call", "action"} and any(item.kind == "control" for _, item in current):
        return True
    return False


def _make_chunk(
    procedure_name: str,
    entries: list[tuple[int, CodeStatement]],
) -> dict[str, object] | None:
    if not entries:
        return None

    significant_entries = [(seq, statement) for seq, statement in entries if statement.kind != "brace"]
    if not significant_entries:
        return None

    non_comment_entries = [
        (seq, statement)
        for seq, statement in significant_entries
        if statement.kind != "comment"
    ]
    if not non_comment_entries:
        return None

    line_start = min(statement.line_start for _, statement in significant_entries)
    line_end = max(statement.line_end for _, statement in significant_entries)
    statement_start_seq = min(seq for seq, _ in significant_entries)
    statement_end_seq = max(seq for seq, _ in significant_entries)

    anchor_kinds = _unique_preserve_order(statement.kind for _, statement in non_comment_entries)
    action_names = _unique_preserve_order(
        statement.name
        for _, statement in non_comment_entries
        if statement.kind in {"action", "call"} and statement.name
    )
    metadata_names = _unique_preserve_order(
        statement.name
        for _, statement in non_comment_entries
        if statement.kind == "metadata_item" and statement.name
    )
    target_names = _unique_preserve_order(
        target
        for _, statement in non_comment_entries
        for target in _statement_targets(statement)
    )
    variable_names = _unique_preserve_order(
        variable
        for _, statement in non_comment_entries
        for variable in [*statement.reads, *statement.writes]
    )
    conditions = _unique_preserve_order(
        statement.condition
        for _, statement in non_comment_entries
        if statement.condition
    )
    comment_fragments = _unique_preserve_order(
        _clean_comment(statement.raw)
        for _, statement in significant_entries
        if statement.kind == "comment" and _clean_comment(statement.raw)
    )

    chunk_type = _infer_chunk_type(non_comment_entries)
    summary_parts = [procedure_name, chunk_type]
    if action_names:
        summary_parts.append(f"actions: {', '.join(action_names[:4])}")
    if metadata_names:
        summary_parts.append(f"metadata: {', '.join(metadata_names[:4])}")
    if target_names:
        summary_parts.append(f"targets: {', '.join(target_names[:4])}")
    if conditions:
        summary_parts.append(f"conditions: {', '.join(conditions[:2])}")
    if variable_names:
        summary_parts.append(f"vars: {', '.join(variable_names[:6])}")
    if comment_fragments:
        summary_parts.append(f"notes: {'; '.join(comment_fragments[:2])}")

    content = "\n".join(statement.raw.rstrip("\n") for _, statement in entries if statement.raw.strip())
    return {
        "chunk_type": chunk_type,
        "line_start": line_start,
        "line_end": line_end,
        "statement_start_seq": statement_start_seq,
        "statement_end_seq": statement_end_seq,
        "statement_count": len(significant_entries),
        "anchor_kinds": anchor_kinds,
        "action_names": action_names,
        "target_names": target_names,
        "variable_names": variable_names,
        "content": content,
        "summary_text": " | ".join(summary_parts),
    }


def _infer_chunk_type(entries: list[tuple[int, CodeStatement]]) -> str:
    kinds = {statement.kind for _, statement in entries}
    if kinds == {"metadata_item"}:
        return "metadata_block"
    if "control" in kinds:
        return "control_block"
    if "call" in kinds and "action" in kinds:
        return "call_flow"
    if "call" in kinds:
        return "call_block"
    if "action" in kinds:
        return "action_block"
    if "assignment" in kinds:
        return "assignment_block"
    if "raw" in kinds:
        return "raw_block"
    return "statement_block"


def _statement_targets(statement: CodeStatement) -> list[str]:
    targets: list[str] = []
    derived_target, derived_kind = derive_target(statement)
    if derived_target and derived_kind != "unknown":
        targets.append(derived_target)
    if statement.target and statement.target not in targets:
        targets.append(statement.target)
    return targets


def _clean_comment(raw: str) -> str:
    stripped = raw.strip()
    if stripped.startswith("//"):
        return stripped[2:].strip()
    return stripped


def _unique_preserve_order(values: object) -> list[str]:
    items = list(values)
    result: list[str] = []
    seen: set[str] = set()
    for value in items:
        if value is None:
            continue
        text = str(value).strip()
        if not text or text in seen:
            continue
        seen.add(text)
        result.append(text)
    return result


def _extract_sql_preview(statements: list[CodeStatement]) -> str | None:
    for statement in statements:
        if statement.kind != "action" or statement.name not in {"查询SQL语句开始", "通用SQL执行"}:
            continue
        if len(statement.groups) < 2:
            continue
        sql_text = " ".join(statement.groups[1].split())
        if sql_text:
            return _truncate_text(sql_text, 120)
    return None


def _normalize_sql(sql_text: str) -> str:
    without_strings = SQL_STRING_RE.sub(" ", sql_text)
    return " ".join(without_strings.replace("\n", " ").replace("\t", " ").split())


def _resolve_sql_text(raw_group: str, string_hints: dict[str, str]) -> str | None:
    candidate = raw_group.strip()
    if not candidate:
        return None
    if candidate.startswith("@"):
        return string_hints.get(candidate)
    return candidate


def _normalize_table_reference(name: str, edge_type: str) -> tuple[str | None, str | None]:
    normalized_table = _normalize_table_name(name)
    if normalized_table:
        return normalized_table, edge_type
    dynamic_table = _normalize_dynamic_table_name(name)
    if dynamic_table:
        dynamic_edge = "reads_dynamic_table" if edge_type == "reads_table" else "writes_dynamic_table"
        return dynamic_table, dynamic_edge
    return None, None


def _normalize_table_name(name: str) -> str | None:
    candidate = name.strip().strip(",;")
    if not candidate:
        return None
    if candidate.startswith("@") or "%" in candidate:
        return None
    if "." in candidate:
        candidate = candidate.split(".")[-1]
    lower = candidate.lower()
    if lower in SQL_SKIP_TABLES:
        return None
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_$]*", candidate):
        return None
    return candidate


def _normalize_dynamic_table_name(name: str) -> str | None:
    candidate = name.strip().strip(",;")
    if not candidate.startswith("@"):
        return None
    if not re.fullmatch(r"@[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)?", candidate):
        return None
    return candidate


def _extract_string_hint_updates(statement: CodeStatement, string_hints: dict[str, str]) -> dict[str, str | None]:
    if not statement.writes:
        return {}

    tracked_writes = [var_name for var_name in statement.writes if _is_tracked_string_var(var_name)]
    if not tracked_writes:
        return {}

    raw = statement.raw.strip()
    updates: dict[str, str | None] = {}

    assignment_match = ASSIGN_RE.match(raw)
    if assignment_match:
        lhs = assignment_match.group("lhs")
        rhs = raw.split("=", 1)[1].rstrip(";").strip()
        updates[lhs] = _resolve_string_expression(rhs, string_hints)
        return updates

    call_match = CALL_EXPR_RE.match(raw)
    if call_match:
        func = call_match.group("func")
        args = _split_call_args(call_match.group("args"))
        if func in {"hs_strcpy", "strcpy"} and len(args) >= 2:
            dest = args[0].strip()
            if _is_tracked_string_var(dest):
                updates[dest] = _resolve_string_expression(args[1], string_hints)
            return updates

        if func in {"sprintf", "snprintf", "hs_snprintf"}:
            dest_index = 0
            format_index = 1 if func == "sprintf" else 2
            if len(args) <= format_index:
                return updates
            dest = args[dest_index].strip()
            if not _is_tracked_string_var(dest):
                return updates
            updates[dest] = _render_format_call(
                format_expr=args[format_index],
                value_exprs=args[format_index + 1 :],
                string_hints=string_hints,
            )
            return updates

    for var_name in tracked_writes:
        updates[var_name] = None
    return updates


def _is_tracked_string_var(var_name: str) -> bool:
    lowered = var_name.lower()
    return any(token in lowered for token in TRACKED_STRING_VAR_TOKENS)


def _resolve_string_expression(expr: str, string_hints: dict[str, str]) -> str | None:
    candidate = expr.strip()
    quoted = _parse_double_quoted_string(candidate)
    if quoted is not None:
        return quoted
    if candidate.startswith("@"):
        return string_hints.get(candidate, candidate if _is_tracked_string_var(candidate) else None)
    return None


def _render_format_call(
    *,
    format_expr: str,
    value_exprs: list[str],
    string_hints: dict[str, str],
) -> str | None:
    format_template = _resolve_string_expression(format_expr, string_hints)
    if format_template is None:
        return None

    rendered_parts: list[str] = []
    value_index = 0
    index = 0
    while index < len(format_template):
        if format_template[index] != "%":
            rendered_parts.append(format_template[index])
            index += 1
            continue
        if index + 1 < len(format_template) and format_template[index + 1] == "%":
            rendered_parts.append("%")
            index += 2
            continue

        match = re.match(r"%[-+#0-9.]*[A-Za-z]", format_template[index:])
        if not match:
            rendered_parts.append(format_template[index])
            index += 1
            continue

        placeholder = match.group(0)
        if value_index >= len(value_exprs):
            rendered_parts.append(placeholder)
        else:
            rendered_parts.append(_render_format_value(value_exprs[value_index], string_hints))
            value_index += 1
        index += len(placeholder)

    return "".join(rendered_parts)


def _render_format_value(expr: str, string_hints: dict[str, str]) -> str:
    resolved = _resolve_string_expression(expr, string_hints)
    if resolved is not None:
        return resolved
    candidate = expr.strip()
    if candidate.startswith("@"):
        return candidate
    return candidate


def _parse_double_quoted_string(expr: str) -> str | None:
    match = DOUBLE_QUOTED_STRING_RE.fullmatch(expr.strip())
    if match is None:
        return None
    return bytes(match.group(1), "utf-8").decode("unicode_escape")


def _split_call_args(raw_args: str) -> list[str]:
    args: list[str] = []
    current: list[str] = []
    depth = 0
    in_string = False
    escape = False

    for char in raw_args:
        if in_string:
            current.append(char)
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
            current.append(char)
            continue
        if char == "(":
            depth += 1
            current.append(char)
            continue
        if char == ")":
            depth = max(depth - 1, 0)
            current.append(char)
            continue
        if char == "," and depth == 0:
            args.append("".join(current).strip())
            current = []
            continue
        current.append(char)

    tail = "".join(current).strip()
    if tail:
        args.append(tail)
    return args


def _classify_mc_publish(statement: CodeStatement) -> dict[str, object] | None:
    if statement.kind != "action" or statement.name not in MC_PUBLISH_ACTIONS:
        return None
    topic_name = _extract_action_argument(statement, "topic_name")
    if not topic_name:
        return None
    publish_mode, publish_mode_label = MC_PUBLISH_ACTIONS[str(statement.name)]
    return {
        "transport": "mc",
        "topic_name": topic_name,
        "message_kind": "mc_topic_publish",
        "message_label": "消息中心主题发布",
        "publish_mode": publish_mode,
        "publish_mode_label": publish_mode_label,
        "communication_kind": "cross_core_message_publish",
        "communication_label": "跨核心消息发布",
    }


def call_prefix(name: str | None) -> str | None:
    if not name:
        return None
    prefix, _, _ = str(name).partition("_")
    return prefix or None


def classify_call_semantics(source_name: str, target_name: str) -> dict[str, object]:
    source_prefix = call_prefix(source_name)
    target_prefix = call_prefix(target_name)
    call_rule = f"{source_prefix}->{target_prefix}" if source_prefix and target_prefix else None
    if source_prefix and target_prefix and (source_prefix, target_prefix) in LOCAL_CALL_RULES:
        return {
            "source_prefix": source_prefix,
            "target_prefix": target_prefix,
            "call_rule": call_rule,
            "call_kind": "local_function_call",
            "call_label": "本地函数调用",
        }
    if source_prefix and target_prefix and (source_prefix, target_prefix) in RPC_CALL_RULES:
        return {
            "source_prefix": source_prefix,
            "target_prefix": target_prefix,
            "call_rule": call_rule,
            "call_kind": "rpc_call",
            "call_label": "系统间RPC调用",
        }
    return {
        "source_prefix": source_prefix,
        "target_prefix": target_prefix,
        "call_rule": call_rule,
        "call_kind": "unknown_call_kind",
        "call_label": "未归类调用",
    }


def coerce_call_semantics(
    detail: dict[str, object],
    *,
    source_name: str,
    target_name: str,
) -> dict[str, object]:
    semantic = classify_call_semantics(source_name, target_name)
    semantic.update(
        {
            "source_prefix": detail.get("source_prefix") or semantic["source_prefix"],
            "target_prefix": detail.get("target_prefix") or semantic["target_prefix"],
            "call_rule": detail.get("call_rule") or semantic["call_rule"],
            "call_kind": detail.get("call_kind") or semantic["call_kind"],
            "call_label": detail.get("call_label") or semantic["call_label"],
        }
    )
    return semantic


def classify_mc_publish(statement: CodeStatement) -> dict[str, object] | None:
    return _classify_mc_publish(statement)


def format_call_edge_label(item: dict[str, object]) -> str:
    procedure_name = str(item["procedure_name"])
    call_label = str(item.get("call_label") or "")
    call_rule = str(item.get("call_rule") or "")
    if call_label and call_rule:
        return f"{procedure_name}({call_label} {call_rule})"
    if call_label:
        return f"{procedure_name}({call_label})"
    return procedure_name


def format_mc_topic_label(item: dict[str, object]) -> str:
    topic_name = str(item["topic_name"])
    message_label = str(item.get("message_label") or "消息中心主题发布")
    publish_mode_label = str(item.get("publish_mode_label") or "")
    if publish_mode_label:
        return f"{topic_name}({message_label} {publish_mode_label})"
    return f"{topic_name}({message_label})"


def _extract_action_argument(statement: CodeStatement, key: str) -> str | None:
    for group in statement.arguments:
        for item in group:
            if item.get("key") == key and item.get("value"):
                return _normalize_argument_value(str(item["value"]))
    return None


def _normalize_argument_value(value: str) -> str:
    candidate = value.strip()
    quoted = _parse_double_quoted_string(candidate)
    if quoted is not None:
        return quoted
    if candidate.startswith("'") and candidate.endswith("'") and len(candidate) >= 2:
        return candidate[1:-1]
    return candidate


def _truncate_text(value: str, limit: int) -> str:
    if len(value) <= limit:
        return value
    return value[: limit - 3].rstrip() + "..."

#!/usr/bin/env python3
"""Parse .uftstructure XML files and generate MD files into docs/common_data/."""

import os
import xml.etree.ElementTree as ET
from pathlib import Path
from html import unescape
import re

UFTSTRUCTURE_ROOT = Path("/Users/songzuoqiang/Documents/agent/code/upub_codes/uftstructure")
OUTPUT_DIR = Path("/Users/songzuoqiang/Documents/agent/condex/codes/docs/common_data")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def clean_text(text: str) -> str:
    """Clean XML text content."""
    if not text:
        return ""
    text = unescape(text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("&#xD;&#xA;", "\n").replace("&#x9;", "\t")
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def parse_uftstructure_file(filepath: Path) -> dict:
    """Parse a single .uftstructure file and return structured data."""
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
    except ET.ParseError as e:
        return {"error": f"XML解析失败: {e}"}

    data = {
        "chinese_name": root.get("chineseName", ""),
        "object_id": root.get("objectId", ""),
        "space": root.get("space", ""),
        "start_todb": root.get("startTodb", ""),
        "run_mode": root.get("runMode", ""),
        "fields": [],
        "indexes": [],
        "db_indexes": [],
        "histories": [],
    }

    # Parse properties (fields)
    for prop in root.findall(".//{*}properties") + root.findall(".//properties"):
        field = {
            "id": prop.get("id", ""),
            "allow_null": prop.get("allowNull", "true"),
            "flags": prop.get("flags", ""),
            "comments": clean_text(prop.get("comments", "")),
            "uuid": prop.get("uuid", ""),
        }
        data["fields"].append(field)

    # Parse indexes
    for idx in root.findall(".//{*}indexs") + root.findall(".//indexs"):
        index = {
            "name": idx.get("name", ""),
            "global": idx.get("global", "false"),
            "flags": idx.get("flags", ""),
            "index_type": idx.get("indexTypeEx", ""),
            "items": [],
        }
        for item in idx.findall("{*}items") + idx.findall("items"):
            index["items"].append(item.get("attrname", ""))
        data["indexes"].append(index)

    # Parse db indexes
    for idx in root.findall(".//{*}dbIndexs") + root.findall(".//dbIndexs"):
        index = {
            "name": idx.get("name", ""),
            "items": [],
        }
        for item in idx.findall("{*}items") + idx.findall("items"):
            index["items"].append(item.get("attrname", ""))
        data["db_indexes"].append(index)

    # Parse histories
    for h in root.findall(".//{*}histories") + root.findall(".//histories"):
        entry = {
            "date": h.get("modifiedDate", ""),
            "version": h.get("version", ""),
            "order": h.get("orderNumber", ""),
            "author": h.get("modifiedBy", ""),
            "desc": h.get("modified", ""),
        }
        if entry["date"]:
            data["histories"].append(entry)

    return data


def generate_md(filepath: Path, data: dict) -> str:
    """Generate markdown content from parsed data."""
    if "error" in data:
        return f"# {filepath.stem}\n\n> {data['error']}\n"

    chinese_name = data["chinese_name"]
    object_id = data["object_id"]
    fname = filepath.stem
    module = filepath.parent.name if filepath.parent.name != "uftstructure" else ""

    lines = []
    lines.append(f"# {fname} - {chinese_name}\n")
    lines.append(f"**表对象ID**: {object_id}")
    if module:
        lines.append(f"**所属模块**: {module}")
    if data["space"]:
        lines.append(f"**数据空间**: {data['space']}")
    if data["run_mode"]:
        lines.append(f"**运行模式**: {data['run_mode']}")
    if data["start_todb"]:
        lines.append(f"**持久化**: {data['start_todb']}")
    lines.append("")

    # Fields table
    fields = data["fields"]
    if fields:
        lines.append(f"## 字段列表（共 {len(fields)} 个）\n")
        lines.append("| # | 字段名 | 允许为空 | 标记 | 备注 |")
        lines.append("|---|--------|----------|------|------|")
        for i, f in enumerate(fields, 1):
            null_str = "否" if f["allow_null"] == "false" else "是"
            flags = f["flags"] if f["flags"] else ""
            comments = f["comments"][:60].replace("\n", " ") if f["comments"] else ""
            lines.append(f"| {i} | {f['id']} | {null_str} | {flags} | {comments} |")
        lines.append("")

    # Indexes
    indexes = data["indexes"]
    if indexes:
        lines.append(f"## 索引（共 {len(indexes)} 个）\n")
        lines.append("| 索引名 | 类型 | 全局 | 字段 |")
        lines.append("|--------|------|------|------|")
        for idx in indexes:
            idx_type = idx["index_type"] if idx["index_type"] else "默认"
            global_str = "是" if idx["global"] == "true" else "否"
            fields_str = ", ".join(idx["items"])
            lines.append(f"| {idx['name']} | {idx_type} | {global_str} | {fields_str} |")
        lines.append("")

    # DB Indexes
    db_indexes = data["db_indexes"]
    if db_indexes:
        lines.append(f"## 数据库索引（共 {len(db_indexes)} 个）\n")
        lines.append("| 索引名 | 字段 |")
        lines.append("|--------|------|")
        for idx in db_indexes:
            fields_str = ", ".join(idx["items"])
            lines.append(f"| {idx['name']} | {fields_str} |")
        lines.append("")

    # Histories
    histories = data["histories"]
    if histories:
        lines.append(f"## 修改历史\n")
        lines.append("| 日期 | 版本 | 作者 | 说明 |")
        lines.append("|------|------|------|------|")
        for h in histories[:15]:
            desc = h["desc"][:60] + ("..." if len(h["desc"]) > 60 else "")
            lines.append(f"| {h['date']} | {h['version']} | {h['author']} | {desc} |")
        if len(histories) > 15:
            lines.append(f"\n> 共 {len(histories)} 条修改记录，仅显示最近15条")
        lines.append("")

    return "\n".join(lines)


def main():
    print("=== 解析 .uftstructure 文件 ===\n")

    if not UFTSTRUCTURE_ROOT.exists():
        print(f"目录不存在: {UFTSTRUCTURE_ROOT}")
        return

    total = 0
    success = 0
    errors = 0

    # Find all .uftstructure files
    uft_files = sorted(UFTSTRUCTURE_ROOT.rglob("*.uftstructure"))
    total = len(uft_files)
    print(f"找到 {total} 个 .uftstructure 文件\n")

    for filepath in uft_files:
        # Determine output filename
        # Use module prefix to avoid conflicts: e.g. sms_etf_cash_balanceinfo.md
        module = filepath.parent.name if filepath.parent.name != "uftstructure" else ""
        stem = filepath.stem
        if module:
            out_name = f"uftstructure_{module}_{stem}.md"
        else:
            out_name = f"uftstructure_{stem}.md"

        out_path = OUTPUT_DIR / out_name

        # Parse and generate
        data = parse_uftstructure_file(filepath)
        md_content = generate_md(filepath, data)

        out_path.write_text(md_content, encoding="utf-8")

        if "error" in data:
            errors += 1
        else:
            success += 1

        if total <= 20 or (success + errors) % 100 == 0:
            print(f"  [{success + errors}/{total}] {out_name}")

    print(f"\n=== 完成 ===")
    print(f"总计: {total} 个文件")
    print(f"成功: {success} 个")
    print(f"失败: {errors} 个")
    print(f"输出目录: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()

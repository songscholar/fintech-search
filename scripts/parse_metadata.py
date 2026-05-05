#!/usr/bin/env python3
"""Parse metadata XML files from all projects and generate MD files into docs/common_data/."""

import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from html import unescape

CODE_ROOT = Path("/Users/songzuoqiang/Documents/agent/code")
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


def parse_histories(root) -> list[dict]:
    """Parse history entries from XML."""
    histories = []
    for h in root.findall(".//{*}histories") + root.findall(".//histories"):
        entry = {
            "date": h.get("modifiedDate", ""),
            "version": h.get("version", ""),
            "order": h.get("orderNumber", ""),
            "author": h.get("modifiedBy", ""),
            "desc": h.get("modified", ""),
        }
        if entry["date"]:
            histories.append(entry)
    # Deduplicate
    seen = set()
    unique = []
    for h in histories:
        key = (h["date"], h["author"], h["desc"])
        if key not in seen:
            seen.add(key)
            unique.append(h)
    return unique


def format_histories_md(histories: list[dict]) -> str:
    """Format histories as markdown table."""
    if not histories:
        return ""
    lines = ["## 修改历史\n", "| 日期 | 版本 | 作者 | 说明 |", "|------|------|------|------|"]
    for h in histories[:20]:  # Limit to 20 most recent
        desc = h["desc"][:80] + ("..." if len(h["desc"]) > 80 else "")
        lines.append(f"| {h['date']} | {h['version']} | {h['author']} | {desc} |")
    if len(histories) > 20:
        lines.append(f"\n> 共 {len(histories)} 条修改记录，仅显示最近20条")
    return "\n".join(lines) + "\n"


def parse_stdobj(root, project: str) -> str:
    """Parse stdobj.xml - Standard Object Field List."""
    lines = [f"# {project} - 标准对象字段列表\n"]
    lines.append("标准对象字段定义，包含对象间的引用关系。\n")
    histories = parse_histories(root)
    lines.append(format_histories_md(histories))
    # Parse root/children references
    root_elem = root.find(".//{*}root") or root.find(".//root")
    if root_elem is not None:
        root_id = root_elem.get("id", "")
        lines.append(f"\n## 根对象\n\n- ID: `{root_id}`\n")
        for child in root_elem.findall("{*}children") + root_elem.findall("children"):
            child_id = child.get("id", "")
            lines.append(f"  - 子对象: `{child_id}`")
    return "\n".join(lines)


def parse_usermacro(root, project: str) -> str:
    """Parse usermacro.xml - User Macro definitions."""
    lines = [f"# {project} - 用户自定义宏\n"]
    lines.append("用户自定义宏定义，包含宏名称、参数、内容和使用说明。\n")
    histories = parse_histories(root)
    lines.append(format_histories_md(histories))

    macros = root.findall(".//{*}macroItems") + root.findall(".//macroItems")
    if macros:
        lines.append(f"\n## 宏列表（共 {len(macros)} 个）\n")
        for m in macros:
            name = m.get("name", "")
            seq = m.get("sequence", "")
            content = clean_text(m.get("content", ""))
            mtype = m.get("type", "")
            desc = clean_text(m.get("description", ""))
            flag_desc = clean_text(m.get("flagDescription", ""))
            max_type = m.get("maxType", "")

            lines.append(f"### {name}\n")
            if seq:
                lines.append(f"- **参数**: `{seq}`")
            if mtype:
                lines.append(f"- **适用类型**: {mtype}")
            if max_type:
                lines.append(f"- **最大类型**: {max_type}")
            if content:
                lines.append(f"\n```\n{content}\n```")
            if desc:
                lines.append(f"\n**说明**: {desc}")
            if flag_desc:
                lines.append(f"\n**标记说明**: {flag_desc}")
            lines.append("")
    return "\n".join(lines)


def parse_component(root, project: str) -> str:
    """Parse component.xml - Component List."""
    lines = [f"# {project} - 组件列表\n"]
    lines.append("组件定义列表，包含组件的修改历史。\n")
    histories = parse_histories(root)
    lines.append(format_histories_md(histories))
    return "\n".join(lines)


def parse_commondatatype(root, project: str) -> str:
    """Parse commondatatype - Common Data Type definitions."""
    lines = [f"# {project} - 通用数据类型\n"]
    lines.append("通用数据类型定义，包含类型名称、中文名、C类型映射等。\n")

    items = root.findall(".//{*}items") + root.findall(".//items")
    if items:
        lines.append(f"\n## 类型列表（共 {len(items)} 个）\n")
        lines.append("| 名称 | 中文名 | 说明 | 默认值 | C类型 |")
        lines.append("|------|--------|------|--------|-------|")
        for item in items:
            name = item.get("name", "")
            cn = item.get("chineseName", "")
            desc = item.get("description", "")
            default = item.get("defaultValue", "")
            ctype = ""
            for data in item.findall(".//{*}value") + item.findall(".//value"):
                if data.get("{http://www.w3.org/2001/XMLSchema-instance}type", "").endswith("CommonDataTypeExt"):
                    ctype = data.get("CType", "")
                    break
            lines.append(f"| {name} | {cn} | {desc} | {default} | {ctype} |")
    return "\n".join(lines)


def parse_constant(root, project: str) -> str:
    """Parse constant.constant - Constant definitions."""
    lines = [f"# {project} - 常量定义\n"]
    lines.append("系统常量定义。\n")
    histories = parse_histories(root)
    lines.append(format_histories_md(histories))
    return "\n".join(lines)


def parse_datatype(root, project: str) -> str:
    """Parse datatype.datatype - Business Data Type definitions."""
    lines = [f"# {project} - 业务数据类型\n"]
    lines.append("业务数据类型定义，包含类型名称、中文名、标准类型、长度、精度等。\n")
    histories = parse_histories(root)
    lines.append(format_histories_md(histories))

    items = root.findall(".//{*}items") + root.findall(".//items")
    if items:
        lines.append(f"\n## 类型列表（共 {len(items)} 个）\n")
        lines.append("| 名称 | 中文名 | 标准类型 | 长度 | 精度 | 默认值 |")
        lines.append("|------|--------|----------|------|------|--------|")
        for item in items:
            name = item.get("name", "")
            cn = item.get("chineseName", "")
            std = item.get("stdType", "")
            length = item.get("length", "")
            precision = item.get("precision", "")
            default = item.get("defaultValue", "")
            lines.append(f"| {name} | {cn} | {std} | {length} | {precision} | {default} |")
    return "\n".join(lines)


def parse_defaulttype(root, project: str) -> str:
    """Parse defaulttype - Standard Data Type definitions."""
    lines = [f"# {project} - 标准数据类型\n"]
    lines.append("标准数据类型定义，包含各数据库类型的映射。\n")
    histories = parse_histories(root)
    lines.append(format_histories_md(histories))

    items = root.findall(".//{*}items") + root.findall(".//items")
    if items:
        lines.append(f"\n## 类型列表（共 {len(items)} 个）\n")
        for item in items:
            name = item.get("name", "")
            cn = item.get("chineseName", "")
            desc = item.get("description", "")
            lines.append(f"### {name} ({cn})\n")
            if desc:
                lines.append(f"- {desc}")
            mappings = {}
            for data in item.findall("{*}data") + item.findall("data"):
                key = data.get("key", "")
                val = data.get("value", "")
                if key and val:
                    mappings[key] = val
            if mappings:
                lines.append("\n| 数据库 | 类型 |")
                lines.append("|--------|------|")
                for db, typ in mappings.items():
                    lines.append(f"| {db} | `{typ}` |")
            lines.append("")
    return "\n".join(lines)


def parse_defaultvalue(root, project: str) -> str:
    """Parse defaultvalue - Type Default Value definitions."""
    lines = [f"# {project} - 类型默认值\n"]
    lines.append("各类型的默认值定义。\n")

    items = root.findall(".//{*}items") + root.findall(".//items")
    if items:
        lines.append(f"\n## 默认值列表（共 {len(items)} 个）\n")
        lines.append("| 名称 | C默认值 |")
        lines.append("|------|---------|")
        for item in items:
            name = item.get("name", "")
            c_val = ""
            for data in item.findall("{*}data") + item.findall("data"):
                if data.get("key") == "c":
                    c_val = data.get("value", "")
                    break
            lines.append(f"| {name} | `{c_val}` |")
    return "\n".join(lines)


def parse_dict(root, project: str) -> str:
    """Parse dict.dict - Dictionary definitions."""
    lines = [f"# {project} - 字典定义\n"]
    lines.append("系统字典定义，包含字典编码、名称和字典项。\n")
    histories = parse_histories(root)
    lines.append(format_histories_md(histories))

    # Parse dict items from modifiedAction
    dict_items = []
    for ma in root.findall(".//{*}modifiedAction") + root.findall(".//modifiedAction"):
        for item in ma.findall("{*}items") + ma.findall("items"):
            dict_name = item.get("name", "")
            dict_cn = item.get("chineseName", "")
            entries = []
            for sub in item.findall("{*}items") + sub.findall("items") if (sub := item) else []:
                val = sub.get("value", "")
                cn = sub.get("chineseName", "")
                if val:
                    entries.append((val, cn))
            if dict_name:
                dict_items.append({"name": dict_name, "cn": dict_cn, "entries": entries})

    if dict_items:
        lines.append(f"\n## 字典项（共 {len(dict_items)} 个）\n")
        for d in dict_items[:100]:
            lines.append(f"### 字典 {d['name']} - {d['cn']}\n")
            if d["entries"]:
                lines.append("| 值 | 中文名 |")
                lines.append("|-----|--------|")
                for val, cn in d["entries"]:
                    lines.append(f"| {val} | {cn} |")
                lines.append("")
    return "\n".join(lines)


def parse_errorno(root, project: str) -> str:
    """Parse errorno.errorno - Error Number definitions."""
    lines = [f"# {project} - 错误号定义\n"]
    lines.append("系统错误号定义。\n")
    histories = parse_histories(root)
    lines.append(format_histories_md(histories))

    items = root.findall(".//{*}items") + root.findall(".//items")
    if items:
        lines.append(f"\n## 错误号列表（共 {len(items)} 个）\n")
        lines.append("| 错误号 | 中文名 | 说明 |")
        lines.append("|--------|--------|------|")
        for item in items:
            name = item.get("name", "")
            cn = item.get("chineseName", "")
            desc = item.get("description", "")[:60]
            lines.append(f"| {name} | {cn} | {desc} |")
    return "\n".join(lines)


def parse_status(root, project: str) -> str:
    """Parse status.xml - Status Item definitions."""
    lines = [f"# {project} - 状态定义\n"]
    lines.append("系统状态项定义。\n")
    histories = parse_histories(root)
    lines.append(format_histories_md(histories))

    items = root.findall(".//{*}items") + root.findall(".//items")
    if items:
        lines.append(f"\n## 状态列表（共 {len(items)} 个）\n")
        lines.append("| 状态ID | 显示名 | 值 | 默认 |")
        lines.append("|--------|--------|-----|------|")
        for item in items:
            sid = item.get("status", "")
            display = item.get("display", "")
            val = item.get("value", "")
            default = "是" if item.get("default") == "true" else ""
            lines.append(f"| {sid} | {display} | {val} | {default} |")
    return "\n".join(lines)


def parse_stdfield(root, project: str) -> str:
    """Parse stdfield - Standard Field definitions."""
    lines = [f"# {project} - 标准字段\n"]
    lines.append("标准字段定义列表。\n")
    histories = parse_histories(root)
    lines.append(format_histories_md(histories))

    items = root.findall(".//{*}items") + root.findall(".//items")
    if items:
        lines.append(f"\n## 字段列表（共 {len(items)} 个）\n")
        lines.append("| 字段名 | 中文名 | 数据类型 | 长度 | 精度 |")
        lines.append("|--------|--------|----------|------|------|")
        for item in items[:200]:
            name = item.get("name", "")
            cn = item.get("chineseName", "")
            dtype = item.get("dataType", "")
            length = item.get("length", "")
            precision = item.get("precision", "")
            lines.append(f"| {name} | {cn} | {dtype} | {length} | {precision} |")
        if len(items) > 200:
            lines.append(f"\n> 共 {len(items)} 个字段，仅显示前200个")
    return "\n".join(lines)


def parse_sysconfig(root, project: str) -> str:
    """Parse sysconfig - System Config definitions."""
    lines = [f"# {project} - 系统配置\n"]
    lines.append("系统配置开关定义。\n")
    histories = parse_histories(root)
    lines.append(format_histories_md(histories))

    items = root.findall(".//{*}items") + root.findall(".//items")
    if items:
        lines.append(f"\n## 配置项（共 {len(items)} 个）\n")
        for item in items:
            name = item.get("name", "")
            cn = item.get("chineseName", "")
            desc = clean_text(item.get("description", ""))
            explain = clean_text(item.get("explain", ""))
            char_val = item.get("charValue", "")
            str_val = item.get("stringValue", "")
            lines.append(f"### {name} - {cn}\n")
            if desc:
                lines.append(f"{desc}\n")
            if explain:
                lines.append(f"**补充说明**: {explain}\n")
            if char_val:
                lines.append(f"- 默认值: `{char_val}`")
            if str_val:
                lines.append(f"- 字符串值: `{str_val}`")
            lines.append("")
    return "\n".join(lines)


def parse_serialnumber(root, project: str) -> str:
    """Parse serialNumber.xml - Serial Number definitions."""
    lines = [f"# {project} - 序列号定义\n"]
    lines.append("系统序列号定义。\n")
    histories = parse_histories(root)
    lines.append(format_histories_md(histories))

    items = root.findall(".//{*}items") + root.findall(".//items")
    if items:
        lines.append(f"\n## 序列号列表（共 {len(items)} 个）\n")
        lines.append("| 序列号ID | 名称 | 中文名 | 初始值 | 步进 |")
        lines.append("|----------|------|--------|--------|------|")
        for item in items[:200]:
            sid = item.get("serialId", item.get("id", ""))
            name = item.get("name", "")
            cn = item.get("chineseName", "")
            init = item.get("initValue", item.get("startValue", ""))
            step = item.get("step", "")
            lines.append(f"| {sid} | {name} | {cn} | {init} | {step} |")
    return "\n".join(lines)


def parse_memoperation(root, project: str) -> str:
    """Parse memoperation.xml - Memory Table definitions."""
    lines = [f"# {project} - 内存表定义\n"]
    lines.append("内存表（缓存表）定义，包含表名、同步表、索引等信息。\n")
    histories = parse_histories(root)
    lines.append(format_histories_md(histories))

    items = root.findall(".//{*}items") + root.findall(".//items")
    if items:
        lines.append(f"\n## 内存表列表（共 {len(items)} 个）\n")
        for item in items:
            db_table = item.get("dbTableName", "")
            mem_table = item.get("memoryTableName", "")
            comment = item.get("memoryTableComment", "")
            user = item.get("user", "")
            fields = item.get("fields", "")
            sync = item.get("syncTableName", "")

            lines.append(f"### {mem_table}\n")
            lines.append(f"- **数据库表**: {db_table}")
            lines.append(f"- **说明**: {comment}")
            if user:
                lines.append(f"- **用户**: {user}")
            if fields:
                lines.append(f"- **字段**: {fields}")
            if sync:
                lines.append(f"- **同步表**: {sync}")

            # Parse indexes
            indexes = item.findall("{*}indexs") + item.findall("indexs")
            if indexes:
                lines.append("- **索引**:")
                for idx in indexes:
                    idx_name = idx.get("name", "")
                    idx_fields = idx.get("fields", "")
                    idx_type = idx.get("indexType", "唯一")
                    lines.append(f"  - `{idx_name}` ({idx_type}): {idx_fields}")
            lines.append("")
    return "\n".join(lines)


def parse_systemmacro(root, project: str) -> str:
    """Parse systemmacro.xml - System Macro definitions."""
    lines = [f"# {project} - 系统宏\n"]
    lines.append("系统内置宏定义，包含宏名称、参数、内容和使用说明。\n")
    histories = parse_histories(root)
    lines.append(format_histories_md(histories))

    macros = root.findall(".//{*}macroItems") + root.findall(".//macroItems")
    if macros:
        lines.append(f"\n## 系统宏列表（共 {len(macros)} 个）\n")
        for m in macros:
            name = m.get("name", "")
            seq = m.get("sequence", "")
            content = clean_text(m.get("content", ""))
            mtype = m.get("type", "")
            desc = clean_text(m.get("description", ""))
            flag_desc = clean_text(m.get("flagDescription", ""))

            lines.append(f"### {name}\n")
            if seq:
                lines.append(f"- **参数**: `{seq}`")
            if mtype:
                lines.append(f"- **适用类型**: {mtype}")
            if content:
                lines.append(f"\n```\n{content}\n```")
            if desc:
                lines.append(f"\n**说明**: {desc}")
            if flag_desc:
                lines.append(f"\n**标记说明**: {flag_desc}")
            lines.append("")
    return "\n".join(lines)


def parse_generic_xml(filepath: Path, project: str) -> str:
    """Generic XML parser for unknown metadata types."""
    fname = filepath.stem
    lines = [f"# {project} - {fname}\n"]
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        histories = parse_histories(root)
        if histories:
            lines.append(format_histories_md(histories))

        items = root.findall(".//{*}items") + root.findall(".//items")
        if items:
            lines.append(f"\n## 条目列表（共 {len(items)} 个）\n")
            for item in items[:100]:
                attrs = dict(item.attrib)
                # Remove xmlns
                attrs = {k.split("}")[-1]: v for k, v in attrs.items()}
                if attrs:
                    name = attrs.get("name", attrs.get("id", ""))
                    if name:
                        lines.append(f"### {name}\n")
                    for k, v in attrs.items():
                        if k != "name" and v:
                            lines.append(f"- **{k}**: {v}")
                    lines.append("")
    except ET.ParseError:
        lines.append(f"\n> 文件解析失败: {filepath.name}")
    return "\n".join(lines)


# Map of file patterns to parsers
PARSERS = {
    "stdobj.xml": parse_stdobj,
    "usermacro.xml": parse_usermacro,
    "component.xml": parse_component,
    "systemmacro.xml": parse_systemmacro,
    "serialNumber.xml": parse_serialnumber,
    "memoperation.xml": parse_memoperation,
    "status.xml": parse_status,
    "heterogeneouscomponent.xml": parse_component,
    "interfaceStruct.xml": parse_component,
    "multicast.xml": parse_component,
    "topic.xml": parse_component,
    "userContext.xml": parse_component,
    "wordChangeRule.xml": parse_component,
}

EXT_PARSERS = {
    ".commondatatype": parse_commondatatype,
    ".constant": parse_constant,
    ".datatype": parse_datatype,
    ".defaulttype": parse_defaulttype,
    ".defaultvalue": parse_defaultvalue,
    ".dict": parse_dict,
    ".errorno": parse_errorno,
    ".stdfield": parse_stdfield,
    ".sysconfig": parse_sysconfig,
}


def process_metadata_file(filepath: Path, project: str):
    """Process a single metadata file and generate MD."""
    fname = filepath.name
    stem = filepath.stem
    ext = filepath.suffix

    # Determine parser
    parser = None
    if fname in PARSERS:
        parser = PARSERS[fname]
    elif ext in EXT_PARSERS:
        parser = EXT_PARSERS[ext]

    # Generate output filename with project prefix
    out_name = f"{project}_metadata_{stem}.md"
    out_path = OUTPUT_DIR / out_name

    if parser:
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            md_content = parser(root, project)
        except ET.ParseError:
            md_content = f"# {project} - {stem}\n\n> XML解析失败: {fname}\n"
    else:
        md_content = parse_generic_xml(filepath, project)

    out_path.write_text(md_content, encoding="utf-8")
    print(f"  -> {out_name}")


def main():
    print("=== 解析元数据文件 ===\n")

    total_files = 0
    for project_dir in sorted(CODE_ROOT.iterdir()):
        if not project_dir.is_dir():
            continue
        metadata_dir = project_dir / "metadata"
        if not metadata_dir.exists():
            continue

        project = project_dir.name.replace("_codes", "")
        print(f"\n[{project}]")

        for f in sorted(metadata_dir.iterdir()):
            if f.is_file():
                process_metadata_file(f, project)
                total_files += 1

    print(f"\n=== 完成：共处理 {total_files} 个元数据文件 ===")


if __name__ == "__main__":
    main()

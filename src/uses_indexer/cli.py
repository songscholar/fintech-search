from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from .indexer import SQLiteIndexer
from .parser import SUPPORTED_SUFFIXES, UftDslParser


def main() -> int:
    parser = argparse.ArgumentParser(description="Parse USES UFT DSL files.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parse_file_parser = subparsers.add_parser("parse-file", help="Parse a single file.")
    parse_file_parser.add_argument("path", help="Path to a single UFT file.")
    parse_file_parser.add_argument("--output", help="Optional JSON output path.")

    scan_dir_parser = subparsers.add_parser("scan-dir", help="Parse a directory tree.")
    scan_dir_parser.add_argument("path", help="Directory containing UFT files.")
    scan_dir_parser.add_argument("--limit", type=int, default=20, help="How many parsed files to include in the sample output.")
    scan_dir_parser.add_argument("--output", help="Optional JSON output path.")

    build_index_parser = subparsers.add_parser("build-index", help="Build a SQLite index for a directory tree.")
    build_index_parser.add_argument("path", help="Directory containing UFT files.")
    build_index_parser.add_argument("--db", required=True, help="SQLite database path.")
    build_index_parser.add_argument("--output", help="Optional JSON summary output path.")

    db_summary_parser = subparsers.add_parser("db-summary", help="Show SQLite index summary.")
    db_summary_parser.add_argument("--db", required=True, help="SQLite database path.")
    db_summary_parser.add_argument("--output", help="Optional JSON summary output path.")

    query_index_parser = subparsers.add_parser("query-index", help="Query SQLite index.")
    query_index_parser.add_argument("--db", required=True, help="SQLite database path.")
    query_index_parser.add_argument("--query", required=True, help="Keyword to search for.")
    query_index_parser.add_argument("--limit", type=int, default=20, help="Maximum number of hits.")
    query_index_parser.add_argument("--output", help="Optional JSON output path.")

    args = parser.parse_args()
    parser_impl = UftDslParser()
    indexer = SQLiteIndexer(parser_impl)

    if args.command == "parse-file":
        data = parser_impl.parse_path(args.path).to_dict()
    elif args.command == "scan-dir":
        data = _scan_dir(parser_impl, Path(args.path), args.limit)
    elif args.command == "build-index":
        data = indexer.build_index(args.path, args.db)
    elif args.command == "query-index":
        data = indexer.query_index(args.db, args.query, limit=args.limit)
    else:
        data = indexer.summarize_db(args.db)

    rendered = json.dumps(data, ensure_ascii=False, indent=2)
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered, encoding="utf-8")
    else:
        print(rendered)

    return 0


def _scan_dir(parser: UftDslParser, root: Path, limit: int) -> dict[str, object]:
    files = sorted(
        path
        for path in root.rglob("*")
        if path.is_file() and path.suffix in SUPPORTED_SUFFIXES
    )

    parsed_units = []
    unit_kind_counter: Counter[str] = Counter()
    prefix_counter: Counter[str] = Counter()
    statement_counter: Counter[str] = Counter()

    for path in files:
        unit = parser.parse_path(path)
        parsed_units.append(unit)
        unit_kind_counter[unit.unit_kind] += 1
        prefix_counter[unit.prefix] += 1
        statement_counter.update(statement.kind for statement in unit.statements)

    sample = [unit.to_dict() for unit in parsed_units[:limit]]

    return {
        "root": str(root),
        "file_count": len(files),
        "unit_kind_counts": dict(unit_kind_counter),
        "prefix_counts": dict(prefix_counter),
        "statement_counts": dict(statement_counter),
        "sample": sample,
    }

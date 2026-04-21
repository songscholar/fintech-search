from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from .api import CodebaseApi
from .answering import CodebaseAnswerer
from .config import bootstrap_env
from .evaluation import EvaluationThresholds, RetrievalEvaluator, compare_eval_reports, evaluate_thresholds
from .index_catalog import DEFAULT_DB_CANDIDATES, discover_default_db
from .integration import CodexIntegrationInstaller
from .indexer import SQLiteIndexer
from .mcp_server import CodebaseMcpServer
from .parser import UftDslParser, is_supported_path
from .qa import CodebaseQA
from .table_indexer import TableIndexer

def main() -> int:
    bootstrap_env()
    parser = argparse.ArgumentParser(description="Parse USES UFT DSL files.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parse_file_parser = subparsers.add_parser("parse-file", help="Parse a single indexed file.")
    parse_file_parser.add_argument("path", help="Path to a single UFT or metadata file.")
    parse_file_parser.add_argument("--output", help="Optional JSON output path.")

    scan_dir_parser = subparsers.add_parser("scan-dir", help="Parse a directory tree.")
    scan_dir_parser.add_argument("path", help="Directory containing UFT and metadata files.")
    scan_dir_parser.add_argument("--limit", type=int, default=20, help="How many parsed files to include in the sample output.")
    scan_dir_parser.add_argument("--output", help="Optional JSON output path.")

    build_index_parser = subparsers.add_parser("build-index", help="Build a SQLite index for a directory tree.")
    build_index_parser.add_argument("path", help="Directory containing UFT and metadata files.")
    build_index_parser.add_argument("--db", required=True, help="SQLite database path.")
    build_index_parser.add_argument("--output", help="Optional JSON summary output path.")
    build_index_parser.add_argument(
        "--resume-vectors",
        action="store_true",
        help="Reuse an existing index and only populate missing chunk vectors.",
    )
    build_index_parser.add_argument(
        "--index-type",
        choices=["all", "code", "metadata"],
        default="all",
        help="Index type: all (default), code (only code files), metadata (only metadata files).",
    )
    build_index_parser.add_argument(
        "--incremental",
        action="store_true",
        help="Incrementally update an existing SQLite index by re-indexing changed files only.",
    )

    db_summary_parser = subparsers.add_parser("db-summary", help="Show SQLite index summary.")
    db_summary_parser.add_argument("--db", required=True, help="SQLite database path.")
    db_summary_parser.add_argument("--output", help="Optional JSON summary output path.")

    query_index_parser = subparsers.add_parser("query-index", help="Query SQLite index.")
    query_index_parser.add_argument("--db", required=True, help="SQLite database path.")
    query_index_parser.add_argument("--query", required=True, help="Keyword to search for.")
    query_index_parser.add_argument("--limit", type=int, default=20, help="Maximum number of hits.")
    query_index_parser.add_argument("--debug", action="store_true", help="Include retrieval debug traces and rerank breakdown.")
    query_index_parser.add_argument("--output", help="Optional JSON output path.")

    eval_parser = subparsers.add_parser("eval-retrieval", help="Evaluate retrieval quality against JSON cases.")
    eval_parser.add_argument("--db", required=True, help="SQLite database path.")
    eval_parser.add_argument("--cases", required=True, help="Evaluation cases JSON path.")
    eval_parser.add_argument("--limit", type=int, default=10, help="Maximum number of hits per case.")
    eval_parser.add_argument("--top-k", default="1,3,5,10", help="Comma-separated top-k cutoffs to report.")
    eval_parser.add_argument("--min-pass-at-k", action="append", default=[], help="Threshold like 5=0.9; can be provided multiple times.")
    eval_parser.add_argument("--min-evidence-coverage", type=float, help="Minimum summary.evidence_coverage.")
    eval_parser.add_argument("--min-top-hit-expectation-coverage", type=float, help="Minimum summary.top_hit_expectation_coverage.")
    eval_parser.add_argument("--min-avg-feature-rerank-hit-count", type=float, help="Minimum summary.avg_feature_rerank_hit_count.")
    eval_parser.add_argument("--fail-on-thresholds", action="store_true", help="Exit with non-zero status when threshold checks fail.")
    eval_parser.add_argument("--output", help="Optional JSON report output path.")

    compare_eval_parser = subparsers.add_parser("compare-eval", help="Compare two retrieval evaluation reports.")
    compare_eval_parser.add_argument("--before", required=True, help="Baseline evaluation report JSON path.")
    compare_eval_parser.add_argument("--after", required=True, help="New evaluation report JSON path.")
    compare_eval_parser.add_argument("--output", help="Optional JSON comparison output path.")

    evidence_parser = subparsers.add_parser("assemble-evidence", help="Assemble retrieval evidence for LLM answering.")
    evidence_parser.add_argument("--db", required=True, help="SQLite database path.")
    evidence_parser.add_argument("--query", required=True, help="Question or keyword to search for.")
    evidence_parser.add_argument("--limit", type=int, default=6, help="Maximum number of evidence blocks.")
    evidence_parser.add_argument("--context-window", type=int, default=2, help="Neighbor statement window around an anchor hit.")
    evidence_parser.add_argument("--related-limit", type=int, default=3, help="Maximum related calls or tables per evidence block.")
    evidence_parser.add_argument("--debug", action="store_true", help="Include retrieval and evidence pruning debug traces.")
    evidence_parser.add_argument("--output", help="Optional JSON output path.")

    ask_parser = subparsers.add_parser("ask-codebase", help="Build a QA package from indexed evidence.")
    ask_parser.add_argument("--db", required=True, help="SQLite database path.")
    ask_parser.add_argument("--question", required=True, help="Natural language question about the codebase.")
    ask_parser.add_argument("--evidence-limit", type=int, default=6, help="Maximum number of evidence blocks.")
    ask_parser.add_argument("--context-window", type=int, default=2, help="Neighbor statement window around an anchor hit.")
    ask_parser.add_argument("--related-limit", type=int, default=3, help="Maximum related calls or tables per evidence block.")
    ask_parser.add_argument("--output", help="Optional JSON output path.")

    answer_parser = subparsers.add_parser("answer-codebase", help="Answer a codebase question with optional external LLM support.")
    answer_parser.add_argument("--db", required=True, help="SQLite database path.")
    answer_parser.add_argument("--question", required=True, help="Natural language question about the codebase.")
    answer_parser.add_argument("--evidence-limit", type=int, default=6, help="Maximum number of evidence blocks.")
    answer_parser.add_argument("--context-window", type=int, default=2, help="Neighbor statement window around an anchor hit.")
    answer_parser.add_argument("--related-limit", type=int, default=3, help="Maximum related calls or tables per evidence block.")
    answer_parser.add_argument("--no-draft-fallback", action="store_true", help="Fail instead of returning draft_answer when no LLM is configured.")
    answer_parser.add_argument("--output", help="Optional JSON output path.")

    bundle_parser = subparsers.add_parser("debug-bundle", help="Bundle query, evidence, and answer output for a single question.")
    bundle_parser.add_argument("--db", required=True, help="SQLite database path.")
    bundle_parser.add_argument("--question", required=True, help="Natural language question about the codebase.")
    bundle_parser.add_argument("--limit", type=int, default=6, help="Maximum number of query hits / evidence blocks.")
    bundle_parser.add_argument("--context-window", type=int, default=2, help="Neighbor statement window around an anchor hit.")
    bundle_parser.add_argument("--related-limit", type=int, default=3, help="Maximum related calls or tables per evidence block.")
    bundle_parser.add_argument("--output", help="Optional JSON output path.")

    serve_parser = subparsers.add_parser("serve-api", help="Run a local HTTP API around the index and QA package.")
    serve_parser.add_argument("--db", required=True, help="Default SQLite database path.")
    serve_parser.add_argument("--host", default="127.0.0.1", help="Host to bind the local HTTP server.")
    serve_parser.add_argument("--port", type=int, default=8000, help="Port to bind the local HTTP server.")

    mcp_parser = subparsers.add_parser("serve-mcp", help="Run a local stdio MCP server around the index and QA package.")
    mcp_parser.add_argument(
        "--db",
        help=(
            "Default SQLite code database path. If omitted, the server will try "
            "examples/business_code_index.db first, then examples/business_full_index.db, "
            "then examples/uses_codes_index.db."
        ),
    )
    mcp_parser.add_argument(
        "--metadata-db",
        help="Default metadata index database path.",
    )
    mcp_parser.add_argument(
        "--table-db",
        help="Default table structure index database path.",
    )

    install_parser = subparsers.add_parser("install-codex-integration", help="Install repo-local plugin and skill into the local Codex home via symlinks.")
    install_parser.add_argument("--force", action="store_true", help="Replace an existing local plugin or skill target if needed.")

    build_table_index_parser = subparsers.add_parser("build-table-index", help="Build a SQLite index for table structures.")
    build_table_index_parser.add_argument("path", help="Directory containing .uftstructure files.")
    build_table_index_parser.add_argument("--db", required=True, help="SQLite database path.")
    build_table_index_parser.add_argument("--stdfield", help="Path to stdfield.stdfield file.")
    build_table_index_parser.add_argument("--mdbobject", help="Path to mdbobject.mdbobject file.")
    build_table_index_parser.add_argument("--output", help="Optional JSON summary output path.")

    query_table_index_parser = subparsers.add_parser("query-table-index", help="Query table structure index.")
    query_table_index_parser.add_argument("--db", required=True, help="SQLite database path.")
    query_table_index_parser.add_argument("--query", required=True, help="Keyword to search for.")
    query_table_index_parser.add_argument("--limit", type=int, default=20, help="Maximum number of hits.")
    query_table_index_parser.add_argument("--output", help="Optional JSON output path.")

    args = parser.parse_args()
    parser_impl = UftDslParser()
    indexer = SQLiteIndexer(parser_impl)
    table_indexer = TableIndexer()
    qa = CodebaseQA(indexer)
    answerer = CodebaseAnswerer(qa)
    evaluator = RetrievalEvaluator(indexer)
    installer = CodexIntegrationInstaller()
    api = CodebaseApi(indexer=indexer, qa=qa, answerer=answerer, default_db_path=getattr(args, "db", None))
    default_mcp_db = getattr(args, "db", None) or _discover_default_db(Path.cwd())
    mcp_server = CodebaseMcpServer(
        indexer=indexer, 
        qa=qa, 
        answerer=answerer, 
        table_indexer=table_indexer,
        default_db_path=default_mcp_db,
        default_metadata_db_path=getattr(args, "metadata_db", None),
        default_table_db_path=getattr(args, "table_db", None),
    )

    if args.command == "serve-api":
        api.serve(host=args.host, port=args.port)
        return 0
    if args.command == "serve-mcp":
        mcp_server.serve()
        return 0
    if args.command == "install-codex-integration":
        data = installer.install(force=args.force)
        rendered = json.dumps(data, ensure_ascii=False, indent=2)
        print(rendered)
        return 0

    if args.command == "parse-file":
        data = parser_impl.parse_path(args.path).to_dict()
    elif args.command == "scan-dir":
        data = _scan_dir(parser_impl, Path(args.path), args.limit)
    elif args.command == "build-index":
        data = indexer.build_index(
            args.path,
            args.db,
            resume_vectors=args.resume_vectors,
            incremental=args.incremental,
            index_type=args.index_type,
        )
    elif args.command == "query-index":
        data = indexer.query_index(args.db, args.query, limit=args.limit, debug=args.debug)
    elif args.command == "build-table-index":
        data = table_indexer.build_index(
            source_root=args.path,
            db_path=args.db,
            stdfield_path=args.stdfield,
            mdbobject_path=args.mdbobject,
        )
    elif args.command == "query-table-index":
        data = table_indexer.query_index(args.db, args.query, limit=args.limit)
    elif args.command == "eval-retrieval":
        data = evaluator.evaluate(
            args.db,
            args.cases,
            limit=args.limit,
            top_k=_parse_top_k(args.top_k),
        )
        threshold_report = evaluate_thresholds(
            data,
            EvaluationThresholds(
                min_pass_at_k=_parse_threshold_pairs(args.min_pass_at_k),
                min_evidence_coverage=args.min_evidence_coverage,
                min_top_hit_expectation_coverage=args.min_top_hit_expectation_coverage,
                min_avg_feature_rerank_hit_count=args.min_avg_feature_rerank_hit_count,
            ),
        )
        data["thresholds"] = threshold_report
    elif args.command == "compare-eval":
        data = compare_eval_reports(args.before, args.after)
    elif args.command == "assemble-evidence":
        data = indexer.assemble_evidence(
            args.db,
            args.query,
            limit=args.limit,
            context_window=args.context_window,
            related_limit=args.related_limit,
            debug=args.debug,
        )
    elif args.command == "ask-codebase":
        data = qa.ask(
            args.db,
            args.question,
            evidence_limit=args.evidence_limit,
            context_window=args.context_window,
            related_limit=args.related_limit,
        )
    elif args.command == "answer-codebase":
        data = answerer.answer(
            args.db,
            args.question,
            evidence_limit=args.evidence_limit,
            context_window=args.context_window,
            related_limit=args.related_limit,
            allow_draft_fallback=not args.no_draft_fallback,
        )
    elif args.command == "debug-bundle":
        data = _build_debug_bundle(
            indexer=indexer,
            answerer=answerer,
            db_path=args.db,
            question=args.question,
            limit=args.limit,
            context_window=args.context_window,
            related_limit=args.related_limit,
        )
    else:
        data = indexer.summarize_db(args.db)

    rendered = json.dumps(data, ensure_ascii=False, indent=2)
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered, encoding="utf-8")
    else:
        print(rendered)

    if args.command == "eval-retrieval" and args.fail_on_thresholds and data["thresholds"]["status"] != "pass":
        return 2

    return 0


def _scan_dir(parser: UftDslParser, root: Path, limit: int) -> dict[str, object]:
    files = sorted(
        path
        for path in root.rglob("*")
        if path.is_file() and is_supported_path(path)
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


def _discover_default_db(root: Path) -> str | None:
    return discover_default_db(root)


def _parse_top_k(raw: str) -> tuple[int, ...]:
    values = []
    for item in raw.split(","):
        stripped = item.strip()
        if not stripped:
            continue
        values.append(int(stripped))
    return tuple(values)


def _parse_threshold_pairs(raw_values: list[str]) -> dict[str, float]:
    result: dict[str, float] = {}
    for raw in raw_values:
        key, sep, value = raw.partition("=")
        if not sep:
            raise ValueError(f"Invalid threshold pair: {raw!r}. Expected format like 5=0.9")
        result[str(int(key.strip()))] = float(value.strip())
    return result


def _build_debug_bundle(
    *,
    indexer: SQLiteIndexer,
    answerer: CodebaseAnswerer,
    db_path: str,
    question: str,
    limit: int,
    context_window: int,
    related_limit: int,
) -> dict[str, object]:
    query_result = indexer.query_index(db_path, question, limit=limit, debug=True)
    evidence_result = indexer.assemble_evidence(
        db_path,
        question,
        limit=limit,
        context_window=context_window,
        related_limit=related_limit,
        debug=True,
    )
    answer_result = answerer.answer(
        db_path,
        question,
        evidence_limit=limit,
        context_window=context_window,
        related_limit=related_limit,
    )
    return {
        "db_path": db_path,
        "question": question,
        "bundle_kind": "debug_bundle",
        "query": query_result,
        "evidence": evidence_result,
        "answer": answer_result,
    }

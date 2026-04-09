from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the local USES indexer MCP server.")
    parser.add_argument("--db", help="Optional SQLite database path.")
    args = parser.parse_args()

    repo_root = _repo_root()
    src_root = repo_root / "src"
    if str(src_root) not in sys.path:
        sys.path.insert(0, str(src_root))

    from uses_indexer.mcp_server import CodebaseMcpServer

    default_db = args.db or os.environ.get("USES_INDEXER_DEFAULT_DB") or str(repo_root / "examples" / "uses_codes_index.db")
    server = CodebaseMcpServer(default_db_path=default_db)
    server.serve()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

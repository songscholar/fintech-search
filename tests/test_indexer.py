from __future__ import annotations

import sqlite3
from pathlib import Path

from uses_indexer.indexer import SQLiteIndexer


SAMPLE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="AF_测试_样例" objectId="1">
  <histories modifiedDate="2026-04-09 10:00:00" version="V1" orderNumber="T1" modifiedBy="Tester" modified="新增"/>
  <inputParameters id="stock_code" uuid="u1"/>
  <outputParameters id="row_count" uuid="u2"/>
  <code><![CDATA[
  [AF_系统参数公用_证券代码获取][][usps_stkcode = @usps_stkcode]
  [获取记录][uses_fund_real(idx_x)][fund_account = @fund_account]
  @row_count = 1;
  ]]></code>
</business:Function>
"""


def test_build_index_creates_sqlite_tables(tmp_path: Path) -> None:
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    sample = source_dir / "AF_SAMPLE.uftatomfunction"
    sample.write_text(SAMPLE_XML, encoding="utf-8")

    db_path = tmp_path / "index.db"
    indexer = SQLiteIndexer()
    summary = indexer.build_index(source_dir, db_path)

    assert summary["file_count"] == 1

    conn = sqlite3.connect(db_path)
    assert conn.execute("SELECT COUNT(*) FROM files").fetchone()[0] == 1
    assert conn.execute("SELECT COUNT(*) FROM procedures").fetchone()[0] == 1
    assert conn.execute("SELECT COUNT(*) FROM params").fetchone()[0] == 2
    assert conn.execute("SELECT COUNT(*) FROM actions").fetchone()[0] == 2
    assert conn.execute("SELECT COUNT(*) FROM edges WHERE edge_type = 'calls_procedure'").fetchone()[0] == 1
    assert conn.execute("SELECT COUNT(*) FROM edges WHERE edge_type = 'reads_table'").fetchone()[0] == 1
    conn.close()


def test_query_index_returns_hits(tmp_path: Path) -> None:
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    sample = source_dir / "AF_SAMPLE.uftatomfunction"
    sample.write_text(SAMPLE_XML, encoding="utf-8")

    db_path = tmp_path / "index.db"
    indexer = SQLiteIndexer()
    indexer.build_index(source_dir, db_path)

    result = indexer.query_index(db_path, "uses_fund_real", limit=10)
    assert result["hit_count"] >= 1
    assert any(hit["matched_text"] == "uses_fund_real" for hit in result["hits"])

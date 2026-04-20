from __future__ import annotations

import io
import json
from pathlib import Path

from uses_indexer.answering import CodebaseAnswerer
from uses_indexer.indexer import SQLiteIndexer
from uses_indexer.mcp_server import CodebaseMcpServer
from uses_indexer.qa import CodebaseQA


SAMPLE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="AF_测试_样例" objectId="1">
  <inputParameters id="stock_code" uuid="u1"/>
  <outputParameters id="row_count" uuid="u2"/>
  <code><![CDATA[
  [AF_系统参数公用_证券代码获取][][usps_stkcode = @usps_stkcode]
  [获取记录][uses_fund_real(idx_x)][fund_account = @fund_account]
  @row_count = 1;
  ]]></code>
</business:Function>
"""

CALLER_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Service xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="LS_测试_入口" objectId="2">
  <inputParameters id="fund_account" uuid="u3"/>
  <outputParameters id="row_count" uuid="u4"/>
  <code><![CDATA[
  [AF_SAMPLE][][row_count = @row_count]
  [获取字段][uses_fund_real(idx_x)][fund_account = @fund_account]
  ]]></code>
</business:Service>
"""


class StubLlm:
    def is_configured(self) -> bool:
        return False

    def complete(self, *, system_prompt: str, user_prompt: str) -> dict[str, object]:
        raise AssertionError("complete should not be called when is_configured is false")


def _build_server(tmp_path: Path) -> tuple[CodebaseMcpServer, Path]:
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    (source_dir / "AF_SAMPLE.uftatomfunction").write_text(SAMPLE_XML, encoding="utf-8")
    (source_dir / "LS_FLOW.uftservice").write_text(CALLER_XML, encoding="utf-8")

    db_path = tmp_path / "index.db"
    indexer = SQLiteIndexer()
    indexer.build_index(source_dir, db_path)
    qa = CodebaseQA(indexer)
    answerer = CodebaseAnswerer(qa=qa, llm=StubLlm())
    server = CodebaseMcpServer(indexer=indexer, qa=qa, answerer=answerer, default_db_path=db_path)
    return server, db_path


def test_initialize_and_tool_listing(tmp_path: Path) -> None:
    server, _ = _build_server(tmp_path)

    initialize = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {"protocolVersion": "2025-11-25"},
        }
    )
    assert initialize is not None
    assert initialize["result"]["serverInfo"]["name"] == "uses-indexer-mcp"

    listed = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list",
        }
    )
    assert listed is not None
    tools = listed["result"]["tools"]
    assert any(tool["name"] == "answer_codebase" for tool in tools)


def test_tool_call_returns_grounded_answer(tmp_path: Path) -> None:
    server, _ = _build_server(tmp_path)

    response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "answer_codebase",
                "arguments": {
                    "question": "证券代码获取的逻辑在哪里",
                    "evidence_limit": 2,
                },
            },
        }
    )

    assert response is not None
    result = response["result"]
    assert result["isError"] is False
    structured = result["structuredContent"]
    assert structured["final_answer"]["source"] in {"draft", "draft_fallback", "llm"}
    assert structured["evidence_count"] >= 1
    assert structured["response_kind"] == "answer"


def test_stdio_serve_writes_jsonrpc_lines(tmp_path: Path) -> None:
    server, _ = _build_server(tmp_path)
    input_stream = io.StringIO(
        "\n".join(
            [
                json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "id": 1,
                        "method": "initialize",
                        "params": {"protocolVersion": "2025-11-25"},
                    },
                    ensure_ascii=False,
                ),
                json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "id": 2,
                        "method": "tools/call",
                        "params": {
                            "name": "query_codebase",
                            "arguments": {"query": "证券代码获取", "limit": 2},
                        },
                    },
                    ensure_ascii=False,
                ),
            ]
        )
        + "\n"
    )
    output_stream = io.StringIO()

    server.serve(input_stream=input_stream, output_stream=output_stream)

    lines = [json.loads(line) for line in output_stream.getvalue().splitlines() if line.strip()]
    assert len(lines) == 2
    assert lines[0]["result"]["serverInfo"]["version"] == "0.2.0"
    assert lines[1]["result"]["structuredContent"]["hit_count"] >= 1
    assert lines[1]["result"]["structuredContent"]["response_kind"] == "query"

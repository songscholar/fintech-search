from __future__ import annotations

import json
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from pathlib import Path
from threading import Thread

from uses_indexer.api import CodebaseApi, make_handler_class
from uses_indexer.answering import CodebaseAnswerer
from uses_indexer.indexer import SQLiteIndexer
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


def _build_api(tmp_path: Path) -> tuple[CodebaseApi, Path]:
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    (source_dir / "AF_SAMPLE.uftatomfunction").write_text(SAMPLE_XML, encoding="utf-8")
    (source_dir / "LS_FLOW.uftservice").write_text(CALLER_XML, encoding="utf-8")

    db_path = tmp_path / "index.db"
    indexer = SQLiteIndexer()
    indexer.build_index(source_dir, db_path)
    qa = CodebaseQA(indexer)
    answerer = CodebaseAnswerer(qa=qa, llm=StubLlm())
    api = CodebaseApi(indexer=indexer, qa=qa, answerer=answerer, default_db_path=db_path)
    return api, db_path


def test_api_handle_request_routes(tmp_path: Path) -> None:
    api, _ = _build_api(tmp_path)

    status, health = api.handle_request("GET", "/health")
    assert status == 200
    assert health["status"] == "ok"

    status, summary = api.handle_request("GET", "/db-summary")
    assert status == 200
    assert summary["files"] == 2

    status, query = api.handle_request(
        "POST",
        "/query",
        json.dumps({"query": "证券代码获取", "limit": 2}).encode("utf-8"),
    )
    assert status == 200
    assert query["hit_count"] >= 1

    status, ask = api.handle_request(
        "POST",
        "/ask",
        json.dumps({"question": "证券代码获取的逻辑在哪里", "evidence_limit": 2}).encode("utf-8"),
    )
    assert status == 200
    assert ask["draft_answer"]["status"] == "ok"

    status, answer = api.handle_request(
        "POST",
        "/answer",
        json.dumps({"question": "证券代码获取的逻辑在哪里", "evidence_limit": 2}).encode("utf-8"),
    )
    assert status == 200
    assert answer["final_answer"]["source"] in {"draft", "draft_fallback", "llm"}


def test_http_server_serves_json(tmp_path: Path) -> None:
    api, _ = _build_api(tmp_path)
    server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler_class(api))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        host, port = server.server_address
        conn = HTTPConnection(host, port, timeout=5)

        conn.request("GET", "/health")
        response = conn.getresponse()
        body = json.loads(response.read().decode("utf-8"))
        assert response.status == 200
        assert body["service"] == "uses-indexer-api"

        payload = json.dumps({"question": "证券代码获取的逻辑在哪里", "evidence_limit": 2})
        conn.request("POST", "/ask", body=payload, headers={"Content-Type": "application/json"})
        response = conn.getresponse()
        body = json.loads(response.read().decode("utf-8"))
        assert response.status == 200
        assert body["evidence_count"] >= 1
        assert "prompt_package" in body

        conn.request("POST", "/answer", body=payload, headers={"Content-Type": "application/json"})
        response = conn.getresponse()
        body = json.loads(response.read().decode("utf-8"))
        assert response.status == 200
        assert "final_answer" in body
    finally:
        server.shutdown()
        thread.join(timeout=5)
        server.server_close()

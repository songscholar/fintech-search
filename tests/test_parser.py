from __future__ import annotations

from pathlib import Path

from uses_indexer.parser import UftDslParser


SAMPLE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="AF_测试_样例" objectId="1">
  <histories modifiedDate="2026-04-09 10:00:00" version="V1" orderNumber="T1" modifiedBy="Tester" modified="新增"/>
  <inputParameters id="stock_code" uuid="u1"/>
  <outputParameters id="row_count" uuid="u2"/>
  <code><![CDATA[
  // comment
  [AF_系统参数公用_证券代码获取][][usps_stkcode = @usps_stkcode]
  if (@row_count == 0)
  {
    [业务报错返回][ERR][不存在][@stock_code]
  }
  @row_count = 1;
  ]]></code>
</business:Function>
"""

METADATA_XML = """<?xml version="1.0" encoding="UTF-8"?>
<usermacro:UserMacro xmlns:usermacro="http://www.hundsun.com/ares/studio/usermacro/1.0.0">
  <histories modifiedDate="2026-04-09 10:00:00" version="V1" orderNumber="T2" modifiedBy="Tester" modified="新增宏"/>
  <macroItems
    name="手工打包头"
    sequence="[标准字段列表]{[打包变量]}"
    content="[手工打包头][fund_account]\n[查询缓存表][upbs_arg]\n[通用SQL执行][select 1 from dual][]"
    description="打包和缓存查询示例"/>
</usermacro:UserMacro>
"""


def test_parse_file_extracts_metadata_and_statements(tmp_path: Path) -> None:
    path = tmp_path / "AF_SAMPLE.uftatomfunction"
    path.write_text(SAMPLE_XML, encoding="utf-8")

    parser = UftDslParser()
    unit = parser.parse_path(path)

    assert unit.unit_kind == "Function"
    assert unit.prefix == "AF"
    assert unit.chinese_name == "AF_测试_样例"
    assert len(unit.histories) == 1
    assert len(unit.parameters) == 2
    assert any(stmt.kind == "call" for stmt in unit.statements)
    assert any(stmt.kind == "control" and stmt.name == "if" for stmt in unit.statements)
    assert any(stmt.kind == "assignment" and "@row_count" in stmt.writes for stmt in unit.statements)


def test_parse_metadata_file_extracts_macro_entries(tmp_path: Path) -> None:
    path = tmp_path / "upub_codes" / "metadata" / "systemmacro.xml"
    path.parent.mkdir(parents=True)
    path.write_text(METADATA_XML, encoding="utf-8")

    parser = UftDslParser()
    unit = parser.parse_path(path)

    assert unit.unit_kind == "Metadata::UserMacro"
    assert unit.prefix == "META"
    assert unit.attributes["metadata_file_name"] == "systemmacro.xml"
    assert any(stmt.kind == "metadata_item" for stmt in unit.statements)
    assert any(stmt.name == "手工打包头" for stmt in unit.statements)
    assert any(stmt.tag == "metadata_macro" for stmt in unit.statements)

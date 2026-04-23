from __future__ import annotations

import sqlite3
from pathlib import Path

from uses_indexer.table_indexer import TableIndexer


def test_table_indexer_auto_loads_standard_fields_from_metadata_sibling(tmp_path: Path) -> None:
    root = tmp_path / "upub_codes"
    structure_root = root / "uftstructure"
    table_root = structure_root / "ses" / "sestrade"
    metadata_root = root / "metadata"
    table_root.mkdir(parents=True)
    metadata_root.mkdir(parents=True)

    (metadata_root / "stdfield.stdfield").write_text(
        """<?xml version="1.0" encoding="UTF-8"?>
<StandardFieldList xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <items name="fund_account" chineseName="资产账户" description="客户资产账户" dataType="HsFundAccount" dictionaryType="100">
    <data2 key="user">
      <value xsi:type="UserExtensibleProperty">
        <map key="public_type" value="C18"/>
      </value>
    </data2>
  </items>
</StandardFieldList>
""",
        encoding="utf-8",
    )
    (table_root / "uses_entrust.uftstructure").write_text(
        """<?xml version="1.0" encoding="UTF-8"?>
<structure:Structure xmlns:structure="http://www.hundsun.com/ares/studio/uft/structure/1.0.0" chineseName="证券实时订单表" objectId="5505" space="HS_UFT_DATA" runMode="DB+MDB">
  <properties id="fund_account" comments="主查询键" allowNull="false" uuid="field-1"/>
  <indexs name="idx_uses_entrust">
    <items attrname="fund_account"/>
  </indexs>
</structure:Structure>
""",
        encoding="utf-8",
    )

    db_path = tmp_path / "table.db"
    summary = TableIndexer().build_index(structure_root, db_path)

    assert summary["standard_field_count"] == 1
    conn = sqlite3.connect(db_path)
    try:
        row = conn.execute(
            """
            SELECT field_id, chinese_name, data_type, dictionary_type, description, public_type, comments
            FROM table_fields
            """
        ).fetchone()
    finally:
        conn.close()

    assert row == ("fund_account", "资产账户", "HsFundAccount", "100", "客户资产账户", "C18", "主查询键")

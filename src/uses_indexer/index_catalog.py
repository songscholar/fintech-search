from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class IndexDefinition:
    key: str
    db_name: str
    summary_name: str
    label: str
    description: str
    includes_code: bool
    includes_metadata: bool
    includes_table_structure: bool
    recommended_for_default: bool = False


INDEX_DEFINITIONS: dict[str, IndexDefinition] = {
    "code": IndexDefinition(
        key="code",
        db_name="business_code_index.db",
        summary_name="business_code_index_summary.json",
        label="代码索引",
        description="仅包含 USES/UFT DSL 代码文件，不包含 metadata 元数据文件。",
        includes_code=True,
        includes_metadata=False,
        includes_table_structure=False,
        recommended_for_default=True,
    ),
    "metadata": IndexDefinition(
        key="metadata",
        db_name="business_metadata_index.db",
        summary_name="business_metadata_index_summary.json",
        label="元数据索引",
        description="仅包含 metadata 目录下的标准字段、常量、错误号、宏、主题域等元数据。",
        includes_code=False,
        includes_metadata=True,
        includes_table_structure=False,
    ),
    "full": IndexDefinition(
        key="full",
        db_name="business_full_index.db",
        summary_name="business_full_index_summary.json",
        label="全量索引",
        description="同时包含代码文件和 metadata 元数据文件，用于综合检索。",
        includes_code=True,
        includes_metadata=True,
        includes_table_structure=False,
    ),
    "table": IndexDefinition(
        key="table",
        db_name="business_table_index.db",
        summary_name="business_table_index_summary.json",
        label="表结构索引",
        description="仅包含 .uftstructure 表结构、字段、索引和表空间关系。",
        includes_code=False,
        includes_metadata=False,
        includes_table_structure=True,
    ),
    "subset": IndexDefinition(
        key="subset",
        db_name="uses_codes_index.db",
        summary_name="uses_codes_index_summary.json",
        label="子库回归索引",
        description="仅保留 uses_codes 子目录的较小范围索引，主要用于回归测试。",
        includes_code=True,
        includes_metadata=False,
        includes_table_structure=False,
    ),
}

DEFAULT_CODE_INDEX_KEY = "code"
DEFAULT_METADATA_INDEX_KEY = "metadata"
DEFAULT_FULL_INDEX_KEY = "full"
DEFAULT_TABLE_INDEX_KEY = "table"
DEFAULT_SUBSET_INDEX_KEY = "subset"
DEFAULT_DB_CANDIDATES = tuple(
    INDEX_DEFINITIONS[key].db_name
    for key in (
        DEFAULT_CODE_INDEX_KEY,
        DEFAULT_FULL_INDEX_KEY,
        DEFAULT_SUBSET_INDEX_KEY,
    )
)


def discover_default_db(root: Path) -> str | None:
    examples_dir = root / "examples"
    for filename in DEFAULT_DB_CANDIDATES:
        candidate = examples_dir / filename
        if candidate.exists():
            return str(candidate)
    return None

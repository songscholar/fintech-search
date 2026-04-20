#!/usr/bin/env python3
import sys
import time
import threading
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from uses_indexer.indexer import SQLiteIndexer
from uses_indexer.parser import UftDslParser
from uses_indexer.table_indexer import TableIndexer


def monitor_wal_file(db_path: Path, stop_event: threading.Event):
    wal_path = db_path.with_suffix(".db-wal")
    last_size = 0
    last_update_time = time.time()
    
    while not stop_event.is_set():
        if wal_path.exists():
            current_size = wal_path.stat().st_size
            if current_size != last_size:
                mb_size = current_size / (1024 * 1024)
                print(f"  [监控] WAL 文件大小: {mb_size:.2f} MB")
                last_size = current_size
                last_update_time = time.time()
        time.sleep(5)


def build_single_index(index_name: str, db_path: Path, build_func):
    print(f"[{index_name}] 开始构建...")
    t0 = time.time()
    
    if db_path.exists():
        db_path.unlink()
        db_path.with_suffix(".db-wal").unlink(missing_ok=True)
        db_path.with_suffix(".db-shm").unlink(missing_ok=True)
    
    stop_event = threading.Event()
    monitor_thread = threading.Thread(target=monitor_wal_file, args=(db_path, stop_event), daemon=True)
    monitor_thread.start()
    
    try:
        result = build_func()
        stop_event.set()
        monitor_thread.join(timeout=2)
    except Exception as e:
        stop_event.set()
        monitor_thread.join(timeout=2)
        print(f"  构建失败: {e}")
        raise
    
    t1 = time.time()
    print(f"[{index_name}] 完成! 耗时: {t1 - t0:.2f}s")
    return result


def main():
    print("=" * 80)
    print("构建剩余的两个索引...")
    print("=" * 80)
    print()
    print("[1/4] 代码专用索引 (business_code_index.db) 已存在，跳过...")
    print("[2/4] 元数据专用索引 (business_metadata_index.db) 已存在，跳过...")
    print()

    code_root = Path("/Users/songzuoqiang/Documents/agent/code")
    uftstructure_root = Path("/Users/songzuoqiang/Documents/agent/code/upub_codes/uftstructure")
    examples_dir = Path(__file__).parent / "examples"
    examples_dir.mkdir(exist_ok=True)

    parser = UftDslParser()
    indexer = SQLiteIndexer(parser)
    table_indexer = TableIndexer()

    # 3. 全量索引
    print("[3/4] 构建全量索引 (all)...")
    full_db_path = examples_dir / "business_full_index.db"
    
    def build_full_index():
        return indexer.build_index(str(code_root), str(full_db_path), index_type="all")
    
    try:
        result = build_single_index("3/4", full_db_path, build_full_index)
        print(f"  文件数: {result.get('file_count', 'N/A')}")
        print(f"  过程数: {result.get('procedure_count', 'N/A')}")
        print(f"  元数据条目数: {result.get('metadata_entries', 'N/A')}")
    except Exception as e:
        print(f"  构建全量索引失败: {e}")
    print()

    # 4. 表结构索引
    print("[4/4] 构建表结构索引...")
    table_db_path = examples_dir / "business_table_index.db"
    stdfield_path = uftstructure_root / "stdfield.stdfield"
    mdbobject_path = uftstructure_root / "mdbobject.mdbobject"
    
    def build_table_index():
        return table_indexer.build_index(
            source_root=str(uftstructure_root),
            db_path=str(table_db_path),
            stdfield_path=str(stdfield_path),
            mdbobject_path=str(mdbobject_path),
        )
    
    try:
        result = build_single_index("4/4", table_db_path, build_table_index)
        print(f"  表数量: {result.get('table_count', 'N/A')}")
        print(f"  字段数量: {result.get('field_count', 'N/A')}")
        print(f"  索引数量: {result.get('index_count', 'N/A')}")
    except Exception as e:
        print(f"  构建表结构索引失败: {e}")
    print()

    print("=" * 80)
    print("索引构建完成!")
    print("=" * 80)
    print()
    print("索引文件位置:")
    print(f"  - 代码索引: {examples_dir / 'business_code_index.db'}")
    print(f"  - 元数据索引: {examples_dir / 'business_metadata_index.db'}")
    print(f"  - 全量索引: {full_db_path}")
    print(f"  - 表结构索引: {table_db_path}")
    print()


if __name__ == "__main__":
    main()

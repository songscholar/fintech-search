#!/usr/bin/env python3
import sys
import time
import threading
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

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


def build_table_index():
    print("=" * 80)
    print("构建表结构索引...")
    print("=" * 80)
    print()

    uftstructure_root = Path("/Users/songzuoqiang/Documents/agent/code/upub_codes/uftstructure")
    examples_dir = Path(__file__).parent / "examples"
    examples_dir.mkdir(exist_ok=True)

    table_indexer = TableIndexer()
    table_db_path = examples_dir / "business_table_index.db"
    stdfield_path = uftstructure_root / "stdfield.stdfield"
    mdbobject_path = uftstructure_root / "mdbobject.mdbobject"

    print("[4/4] 构建表结构索引...")
    t0 = time.time()
    
    if table_db_path.exists():
        table_db_path.unlink()
        table_db_path.with_suffix(".db-wal").unlink(missing_ok=True)
        table_db_path.with_suffix(".db-shm").unlink(missing_ok=True)
    
    stop_event = threading.Event()
    monitor_thread = threading.Thread(target=monitor_wal_file, args=(table_db_path, stop_event), daemon=True)
    monitor_thread.start()
    
    try:
        result = table_indexer.build_index(
            source_root=str(uftstructure_root),
            db_path=str(table_db_path),
            stdfield_path=str(stdfield_path),
            mdbobject_path=str(mdbobject_path),
        )
        stop_event.set()
        monitor_thread.join(timeout=2)
    except Exception as e:
        stop_event.set()
        monitor_thread.join(timeout=2)
        print(f"  构建失败: {e}")
        raise
    
    t1 = time.time()
    print(f"[4/4] 完成! 耗时: {t1 - t0:.2f}s")
    print(f"  表数量: {result.get('table_count', 'N/A')}")
    print(f"  字段数量: {result.get('field_count', 'N/A')}")
    print(f"  索引数量: {result.get('index_count', 'N/A')}")
    print()

    print("=" * 80)
    print("表结构索引构建完成!")
    print("=" * 80)
    print()
    print("索引文件位置:")
    print(f"  - 表结构索引: {table_db_path}")
    print()


if __name__ == "__main__":
    build_table_index()

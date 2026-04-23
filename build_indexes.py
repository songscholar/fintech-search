#!/usr/bin/env python3
import sys
import time
import threading
import argparse
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from uses_indexer.index_catalog import INDEX_DEFINITIONS
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


def _write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_index_artifacts(
    *,
    examples_dir: Path,
    index_key: str,
    build_summary: dict,
    db_summary: dict,
) -> None:
    definition = INDEX_DEFINITIONS[index_key]
    merged_summary = dict(build_summary)
    merged_summary["db_summary"] = db_summary
    merged_summary["db_path"] = str(examples_dir / definition.db_name)
    _write_json(examples_dir / definition.summary_name, merged_summary)


def build_code_index(indexer, code_root, examples_dir, *, skip_vectors: bool = False):
    print("[1/4] 构建代码专用索引 (code)...")
    code_db_path = examples_dir / "business_code_index.db"
    
    def build():
        return indexer.build_index(str(code_root), str(code_db_path), index_type="code", skip_vectors=skip_vectors, progress=True)
    
    result = build_single_index("1/4", code_db_path, build)
    write_index_artifacts(
        examples_dir=examples_dir,
        index_key="code",
        build_summary=result,
        db_summary=indexer.summarize_db(code_db_path),
    )
    print(f"  文件数: {result.get('file_count', 'N/A')}")
    print(f"  过程数: {result.get('procedure_count', 'N/A')}")
    print()
    return result


def build_metadata_index(indexer, code_root, examples_dir, *, skip_vectors: bool = False):
    print("[2/4] 构建元数据专用索引 (metadata)...")
    metadata_db_path = examples_dir / "business_metadata_index.db"
    
    def build():
        return indexer.build_index(str(code_root), str(metadata_db_path), index_type="metadata", skip_vectors=skip_vectors, progress=True)
    
    result = build_single_index("2/4", metadata_db_path, build)
    write_index_artifacts(
        examples_dir=examples_dir,
        index_key="metadata",
        build_summary=result,
        db_summary=indexer.summarize_db(metadata_db_path),
    )
    print(f"  文件数: {result.get('file_count', 'N/A')}")
    print(f"  过程数: {result.get('procedure_count', 'N/A')}")
    print(f"  元数据条目数: {result.get('metadata_entries', 'N/A')}")
    print()
    return result


def build_full_index(indexer, code_root, examples_dir, *, skip_vectors: bool = False):
    print("[3/4] 构建全量索引 (all)...")
    full_db_path = examples_dir / "business_full_index.db"
    
    def build():
        return indexer.build_index(str(code_root), str(full_db_path), index_type="all", skip_vectors=skip_vectors, progress=True)
    
    result = build_single_index("3/4", full_db_path, build)
    write_index_artifacts(
        examples_dir=examples_dir,
        index_key="full",
        build_summary=result,
        db_summary=indexer.summarize_db(full_db_path),
    )
    print(f"  文件数: {result.get('file_count', 'N/A')}")
    print(f"  过程数: {result.get('procedure_count', 'N/A')}")
    print(f"  元数据条目数: {result.get('metadata_entries', 'N/A')}")
    print()
    return result


def build_table_index(table_indexer, uftstructure_root, examples_dir):
    print("[4/4] 构建表结构索引...")
    table_db_path = examples_dir / "business_table_index.db"
    stdfield_path = uftstructure_root.parent / "metadata" / "stdfield.stdfield"
    mdbobject_path = uftstructure_root / "mdbobject.mdbobject"
    
    def build():
        return table_indexer.build_index(
            source_root=str(uftstructure_root),
            db_path=str(table_db_path),
            stdfield_path=str(stdfield_path),
            mdbobject_path=str(mdbobject_path),
        )
    
    result = build_single_index("4/4", table_db_path, build)
    write_index_artifacts(
        examples_dir=examples_dir,
        index_key="table",
        build_summary=result,
        db_summary=table_indexer.db_summary(table_db_path),
    )
    print(f"  表数量: {result.get('table_count', 'N/A')}")
    print(f"  字段数量: {result.get('field_count', 'N/A')}")
    print(f"  索引数量: {result.get('index_count', 'N/A')}")
    print()
    return result


def main():
    parser = argparse.ArgumentParser(description="构建索引")
    parser.add_argument(
        "--mode",
        choices=["code", "metadata", "table", "three", "full", "all"],
        default="three",
        help="构建模式：code（仅代码）、metadata（仅元数据）、table（仅表结构）、three（三个索引）、full（仅全量）、all（所有四个）"
    )
    parser.add_argument(
        "--skip-vectors",
        action="store_true",
        help="仅构建结构索引，跳过 chunk 向量；之后可用 CLI build-index --resume-vectors 补齐。",
    )
    
    args = parser.parse_args()
    
    code_root = Path("/Users/songzuoqiang/Documents/agent/code")
    uftstructure_root = Path("/Users/songzuoqiang/Documents/agent/code/upub_codes/uftstructure")
    examples_dir = Path(__file__).parent / "examples"
    examples_dir.mkdir(exist_ok=True)
    
    parser_impl = UftDslParser()
    indexer = SQLiteIndexer(parser_impl)
    table_indexer = TableIndexer()
    
    print("=" * 80)
    if args.mode == "code":
        print("构建代码专用索引...")
    elif args.mode == "metadata":
        print("构建元数据专用索引...")
    elif args.mode == "table":
        print("构建表结构索引...")
    elif args.mode == "three":
        print("构建三个专用索引（代码、元数据、表结构）...")
    elif args.mode == "full":
        print("构建全量索引...")
    elif args.mode == "all":
        print("构建所有四个索引（代码、元数据、全量、表结构）...")
    print("=" * 80)
    print()
    
    results = []
    
    def safe_build(build_func, name):
        try:
            build_func()
            results.append((name, True, None))
        except Exception as e:
            print(f"  [{name}] 构建失败: {e}")
            results.append((name, False, str(e)))
    
    try:
        if args.mode == "code":
            safe_build(lambda: build_code_index(indexer, code_root, examples_dir, skip_vectors=args.skip_vectors), "代码索引")
        elif args.mode == "metadata":
            safe_build(lambda: build_metadata_index(indexer, code_root, examples_dir, skip_vectors=args.skip_vectors), "元数据索引")
        elif args.mode == "table":
            safe_build(lambda: build_table_index(table_indexer, uftstructure_root, examples_dir), "表结构索引")
        elif args.mode == "three":
            safe_build(lambda: build_code_index(indexer, code_root, examples_dir, skip_vectors=args.skip_vectors), "代码索引")
            safe_build(lambda: build_metadata_index(indexer, code_root, examples_dir, skip_vectors=args.skip_vectors), "元数据索引")
            safe_build(lambda: build_table_index(table_indexer, uftstructure_root, examples_dir), "表结构索引")
        elif args.mode == "full":
            safe_build(lambda: build_full_index(indexer, code_root, examples_dir, skip_vectors=args.skip_vectors), "全量索引")
        elif args.mode == "all":
            safe_build(lambda: build_code_index(indexer, code_root, examples_dir, skip_vectors=args.skip_vectors), "代码索引")
            safe_build(lambda: build_metadata_index(indexer, code_root, examples_dir, skip_vectors=args.skip_vectors), "元数据索引")
            safe_build(lambda: build_full_index(indexer, code_root, examples_dir, skip_vectors=args.skip_vectors), "全量索引")
            safe_build(lambda: build_table_index(table_indexer, uftstructure_root, examples_dir), "表结构索引")
        
        print("=" * 80)
        print("索引构建完成!")
        print("=" * 80)
        print()
        print("构建结果汇总:")
        for name, success, error in results:
            status = "✅ 成功" if success else "❌ 失败"
            print(f"  - {name}: {status}")
            if error:
                print(f"    错误: {error}")
        print()
        print("索引文件位置:")
        if args.mode in ["code", "three", "all"]:
            print(f"  - 代码索引: {examples_dir / 'business_code_index.db'}")
        if args.mode in ["metadata", "three", "all"]:
            print(f"  - 元数据索引: {examples_dir / 'business_metadata_index.db'}")
        if args.mode in ["full", "all"]:
            print(f"  - 全量索引: {examples_dir / 'business_full_index.db'}")
        if args.mode in ["table", "three", "all"]:
            print(f"  - 表结构索引: {examples_dir / 'business_table_index.db'}")
        print()
    
    except KeyboardInterrupt:
        print("\n\n用户中断，停止构建。")
    except Exception as e:
        print(f"\n\n构建失败: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

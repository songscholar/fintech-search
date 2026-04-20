#!/usr/bin/env python3
"""快速诊断索引构建问题"""
import sys
import time
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from uses_indexer.parser import UftDslParser, is_supported_path, SUPPORTED_CODE_SUFFIXES, SUPPORTED_METADATA_SUFFIXES

CODE_ROOT = Path("/Users/songzuoqiang/Documents/agent/code")

print("=" * 60)
print("USES Indexer 构建诊断")
print("=" * 60)

# 1. 检查源码目录是否存在
print(f"\n[1] 检查源码目录: {CODE_ROOT}")
if not CODE_ROOT.exists():
    print(f"    ❌ 目录不存在!")
    sys.exit(1)
print(f"    ✅ 目录存在")

# 2. 扫描所有文件，统计后缀
print(f"\n[2] 扫描文件后缀分布...")
suffix_counter = {}
total_files = 0
for path in CODE_ROOT.rglob("*"):
    if path.is_file():
        total_files += 1
        suffix = path.suffix
        suffix_counter[suffix] = suffix_counter.get(suffix, 0) + 1

print(f"    总文件数: {total_files}")
print(f"    后缀分布 (前20):")
for suffix, count in sorted(suffix_counter.items(), key=lambda x: -x[1])[:20]:
    in_code = "✅ 代码" if suffix in SUPPORTED_CODE_SUFFIXES else ""
    in_meta = "✅ 元数据" if suffix in SUPPORTED_METADATA_SUFFIXES else ""
    print(f"      {suffix or '(无后缀)':30s} {count:8d}  {in_code}{in_meta}")

# 3. 检查 is_supported_path 过滤后剩余多少文件
print(f"\n[3] 检查 is_supported_path 过滤...")
supported_files = sorted(
    path for path in CODE_ROOT.rglob("*")
    if path.is_file() and is_supported_path(path)
    and not any(excluded in str(path) for excluded in ["通用数据", "commondata", "tools"])
)
print(f"    过滤后文件数: {len(supported_files)}")

if len(supported_files) == 0:
    print(f"    ❌ 没有文件通过过滤! 索引将为空。")
    print(f"    支持的代码后缀: {SUPPORTED_CODE_SUFFIXES}")
    print(f"    支持的元数据后缀: {SUPPORTED_METADATA_SUFFIXES}")
    sys.exit(1)

# 4. 按后缀统计过滤后的文件
filtered_suffix = {}
for path in supported_files:
    s = path.suffix
    filtered_suffix[s] = filtered_suffix.get(s, 0) + 1
print(f"    过滤后后缀分布:")
for suffix, count in sorted(filtered_suffix.items(), key=lambda x: -x[1]):
    print(f"      {suffix:30s} {count:8d}")

# 5. 尝试解析前10个文件
print(f"\n[4] 尝试解析前10个文件...")
parser = UftDslParser()
error_count = 0
success_count = 0
for path in supported_files[:10]:
    try:
        unit = parser.parse_path(path)
        success_count += 1
        print(f"    ✅ {path.name:50s} kind={unit.unit_kind} stmts={len(unit.statements)}")
    except Exception as e:
        error_count += 1
        print(f"    ❌ {path.name:50s} 错误: {e}")

# 6. 如果前10个都成功，尝试解析所有文件看有没有报错的
if success_count == 10 and len(supported_files) > 10:
    print(f"\n[5] 批量解析所有 {len(supported_files)} 个文件（检查是否有解析错误）...")
    t0 = time.time()
    total_errors = 0
    first_error = None
    for i, path in enumerate(supported_files):
        try:
            parser.parse_path(path)
        except Exception as e:
            total_errors += 1
            if first_error is None:
                first_error = (path, e)
        if (i + 1) % 5000 == 0:
            elapsed = time.time() - t0
            print(f"    已解析 {i+1}/{len(supported_files)} ({elapsed:.1f}s)...")
    
    elapsed = time.time() - t0
    print(f"    解析完成: {len(supported_files)} 个文件, 耗时 {elapsed:.1f}s")
    print(f"    成功: {len(supported_files) - total_errors}, 失败: {total_errors}")
    
    if first_error:
        print(f"\n    ❌ 第一个错误文件: {first_error[0]}")
        print(f"       错误信息: {first_error[1]}")
        traceback.print_exception(type(first_error[1]), first_error[1], first_error[1].__traceback__)

print(f"\n{'=' * 60}")
print("诊断完成")
print("=" * 60)

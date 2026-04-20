#!/usr/bin/env python3
import sys
import sqlite3
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

def get_table_detail(db_path, table_name):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    
    print(f"表名: {table_name}")
    print("=" * 80)
    
    # 获取表基本信息
    table = conn.execute("""
        SELECT * FROM tables WHERE table_name = ?
    """, (table_name,)).fetchone()
    
    if table:
        print(f"中文名称: {table['chinese_name']}")
        print(f"对象ID: {table['object_id']}")
        print(f"表空间: {table['space']}")
        print(f"运行模式: {table['run_mode']}")
        print(f"有历史表: {'是' if table['has_history'] else '否'}")
        print(f"数据存储介质: {table['data_storage_medium'] or '默认'}")
        print()
    
    # 获取字段信息
    print("字段列表:")
    print("-" * 80)
    fields = conn.execute("""
        SELECT * FROM table_fields 
        WHERE table_id = (SELECT id FROM tables WHERE table_name = ?)
        ORDER BY id
    """, (table_name,)).fetchall()
    
    for i, field in enumerate(fields, 1):
        null_str = "允许NULL" if field['allow_null'] else "不允许NULL"
        field_id = field['field_id'] or ""
        data_type = field['data_type'] or ""
        chinese_name = field['chinese_name'] or ""
        print(f"  {i:2d}. {field_id:<30} {data_type:<20} {null_str:<15} {chinese_name}")
        if field['dictionary_type']:
            print(f"       字典类型: {field['dictionary_type']}")
    
    print()
    
    # 获取索引信息
    print("索引列表:")
    print("-" * 80)
    indexes = conn.execute("""
        SELECT * FROM table_indexes 
        WHERE table_id = (SELECT id FROM tables WHERE table_name = ?)
        ORDER BY id
    """, (table_name,)).fetchall()
    
    for i, index in enumerate(indexes, 1):
        field_names = json.loads(index['field_names_json'])
        global_str = "全局索引" if index['global_index'] else "局部索引"
        print(f"  {i:2d}. {index['index_name']:<30} {global_str:<10} 字段: {', '.join(field_names)}")
        if index['flags']:
            print(f"       标志: {index['flags']}")
        if index['index_type_ex']:
            print(f"       索引类型: {index['index_type_ex']}")
    
    conn.close()

if __name__ == "__main__":
    get_table_detail("business_table_index.db", "usps_stkcode")

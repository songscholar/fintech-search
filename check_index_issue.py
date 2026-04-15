import os
import sys
from pathlib import Path

# 添加src目录到Python路径
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from uses_indexer.indexer import SQLiteIndexer
from uses_indexer.parser import UftDslParser, is_supported_path

# 检查默认源代码目录
default_source_dir = Path('/Users/songzuoqiang/Documents/agent/code')
print(f"默认源代码目录: {default_source_dir}")
print(f"目录是否存在: {default_source_dir.exists()}")

if default_source_dir.exists():
    print("\n目录内容:")
    for item in default_source_dir.iterdir():
        if item.is_file():
            print(f"  文件: {item.name}, 支持: {is_supported_path(item)}")
        else:
            print(f"  目录: {item.name}")
else:
    print("\n目录不存在，这可能是索引大小没有变化的原因!")

# 检查examples目录中的索引文件
examples_dir = Path(__file__).parent / 'examples'
print("\nexamples目录中的索引文件:")
for db_file in examples_dir.glob('*.db'):
    if db_file.exists():
        size = os.path.getsize(db_file) / 1024
        print(f"  {db_file.name}: {size:.2f} KB")

# 检查agent_code_full_index.db的内容
test_db = examples_dir / 'agent_code_full_index.db'
if test_db.exists():
    print(f"\n检查 {test_db.name} 的内容:")
    import sqlite3
    conn = sqlite3.connect(test_db)
    cursor = conn.cursor()
    
    # 检查文件数量
    cursor.execute("SELECT COUNT(*) FROM files")
    file_count = cursor.fetchone()[0]
    print(f"  文件数量: {file_count}")
    
    # 检查其他表的数量
    tables = ['procedures', 'statements', 'edges', 'chunks', 'blocks']
    for table in tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"  {table}: {count}")
    
    conn.close()
else:
    print(f"\n{test_db.name} 不存在!")

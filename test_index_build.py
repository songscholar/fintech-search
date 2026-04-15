import os
import sys
import tempfile
from pathlib import Path

# 添加src目录到Python路径
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from uses_indexer.indexer import SQLiteIndexer
from uses_indexer.parser import UftDslParser

# 创建一个临时目录用于测试
temp_dir = tempfile.mkdtemp()
print(f"创建临时测试目录: {temp_dir}")

# 创建一个简单的测试UFT文件
test_file_content = '''<?xml version="1.0" encoding="UTF-8"?>
<uftfunction name="test_function" chineseName="测试函数" objectId="12345">
    <histories modifiedDate="2023-01-01" version="1.0"/>
    <inputParameters id="param1" type="string" name="input1"/>
    <code>// 测试代码
if (@input1 == "test") {
    [LF_TestFunction] [param1="value"]
}
</code>
</uftfunction>
'''

test_file_path = Path(temp_dir) / "test_function.uftfunction"
test_file_path.write_text(test_file_content, encoding="utf-8")
print(f"创建测试文件: {test_file_path}")

# 创建索引器
parser = UftDslParser()
indexer = SQLiteIndexer(parser)

# 构建索引
db_path = Path(temp_dir) / "test_index.db"
print(f"开始构建索引到: {db_path}")

try:
    result = indexer.build_index(temp_dir, db_path)
    print("\n索引构建结果:")
    print(f"文件数: {result['file_count']}")
    print(f"单位类型计数: {result['unit_kind_counts']}")
    print(f"前缀计数: {result['prefix_counts']}")
    print(f"语句计数: {result['statement_counts']}")
    print(f"边缘计数: {result['edge_counts']}")
    print(f"块计数: {result['block_counts']}")
    print(f"向量计数: {result['vector_counts']}")
    
    # 检查索引文件大小
    if db_path.exists():
        size = os.path.getsize(db_path) / 1024
        print(f"\n索引文件大小: {size:.2f} KB")
    else:
        print("\n索引文件不存在!")
        
except Exception as e:
    print(f"\n构建索引时出错: {e}")

# 清理临时文件
import shutil
shutil.rmtree(temp_dir)
print(f"\n清理临时目录: {temp_dir}")

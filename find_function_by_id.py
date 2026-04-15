import sqlite3

db_path = 'examples/agent_code_index.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("查询功能号为333002的文件：")

# 查询object_id为333002的文件
cursor.execute("""
    SELECT id, path, file_name, name, chinese_name, object_id, unit_kind
    FROM files
    WHERE object_id = '333002'
""")
results = cursor.fetchall()

if results:
    print("\n找到匹配的文件：")
    for row in results:
        print(f"  ID: {row[0]}")
        print(f"  路径: {row[1]}")
        print(f"  文件名: {row[2]}")
        print(f"  名称: {row[3]}")
        print(f"  中文名: {row[4]}")
        print(f"  功能号: {row[5]}")
        print(f"  单位类型: {row[6]}")
        print()
else:
    print("\n没有找到object_id为'333002'的文件")

# 查询name或chinese_name中包含333002的文件
print("\n查询名称中包含333002的文件：")
cursor.execute("""
    SELECT id, path, file_name, name, chinese_name, object_id, unit_kind
    FROM files
    WHERE name LIKE '%333002%' OR chinese_name LIKE '%333002%'
""")
results = cursor.fetchall()

if results:
    print("\n找到匹配的文件：")
    for row in results:
        print(f"  ID: {row[0]}")
        print(f"  路径: {row[1]}")
        print(f"  文件名: {row[2]}")
        print(f"  名称: {row[3]}")
        print(f"  中文名: {row[4]}")
        print(f"  功能号: {row[5]}")
        print(f"  单位类型: {row[6]}")
        print()
else:
    print("\n没有找到名称中包含333002的文件")

# 查询常量定义中包含333002的文件
print("\n查询常量定义中包含333002的文件：")
cursor.execute("""
    SELECT DISTINCT f.path, f.file_name, f.name
    FROM files f
    JOIN statements s ON f.id = s.file_id
    WHERE s.kind = 'metadata_item'
      AND (s.raw LIKE '%333002%' OR s.name LIKE '%333002%')
""")
results = cursor.fetchall()

if results:
    print("\n找到匹配的文件：")
    for row in results:
        print(f"  路径: {row[0]}")
        print(f"  文件名: {row[1]}")
        print(f"  名称: {row[2]}")
        print()
else:
    print("\n没有找到常量定义中包含333002的文件")

conn.close()

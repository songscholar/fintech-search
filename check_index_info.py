import sqlite3

# 连接到索引数据库
conn = sqlite3.connect('/Users/songzuoqiang/Documents/agent/condex/codes/indexes/agent_code_index.db')
conn.row_factory = sqlite3.Row

# 查询LS_SESEXT_NORMALORDER_ENTER的信息
print("=== LS_SESEXT_NORMALORDER_ENTER 信息 ===")
cursor = conn.execute('''
SELECT p.name, p.chinese_name, p.object_id, f.path 
FROM procedures p 
JOIN files f ON p.file_id = f.id 
WHERE p.name = 'LS_SESEXT_NORMALORDER_ENTER'
''')
for row in cursor:
    print(f'Name: {row[0]}')
    print(f'Chinese Name: {row[1]}')
    print(f'Object ID: {row[2]}')
    print(f'Path: {row[3]}')

# 查询333002功能号对应的信息
print("\n=== 333002 功能号相关信息 ===")
cursor = conn.execute('''
SELECT p.name, p.chinese_name, p.object_id, f.path 
FROM procedures p 
JOIN files f ON p.file_id = f.id 
WHERE p.object_id = '333002'
''')
for row in cursor:
    print(f'Name: {row[0]}')
    print(f'Chinese Name: {row[1]}')
    print(f'Object ID: {row[2]}')
    print(f'Path: {row[3]}')

# 查询常量定义中的333002
print("\n=== 常量定义中的333002 ===")
cursor = conn.execute('''
SELECT s.raw, f.path 
FROM statements s 
JOIN files f ON s.file_id = f.id 
WHERE s.raw LIKE '%333002%' AND s.kind = 'metadata_item'
''')
for row in cursor:
    print(f'Raw: {row[0]}')
    print(f'Path: {row[1]}')

conn.close()

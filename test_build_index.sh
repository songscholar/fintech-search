#!/bin/bash

# 设置PYTHONPATH
export PYTHONPATH=src

# 尝试构建索引到agent_code_full_index.db
python -m uses_indexer build-index /Users/songzuoqiang/Documents/agent/code --db indexes/agent_code_full_index.db

# 检查索引文件大小
ls -lh indexes/agent_code_full_index.db

# 检查索引文件内容
python -c "import sqlite3; conn = sqlite3.connect('indexes/agent_code_full_index.db'); cursor = conn.cursor(); print('文件数量:', cursor.execute('SELECT COUNT(*) FROM files').fetchone()[0]); conn.close()"

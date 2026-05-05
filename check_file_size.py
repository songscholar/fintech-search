import os
import glob

# 检查examples目录中的索引文件大小
db_files = glob.glob('/Users/songzuoqiang/Documents/agent/condex/codes/indexes/*.db')

print("索引文件大小:")
for db_file in db_files:
    size = os.path.getsize(db_file)
    print(f"{os.path.basename(db_file)}: {size / 1024:.2f} KB")

# 检查默认源代码目录是否存在
source_dir = '/Users/songzuoqiang/Documents/agent/code'
print(f"\n默认源代码目录 {source_dir} 存在: {os.path.exists(source_dir)}")
if os.path.exists(source_dir):
    print("目录内容:")
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        if os.path.isfile(item_path):
            print(f"  文件: {item}")
        else:
            print(f"  目录: {item}")

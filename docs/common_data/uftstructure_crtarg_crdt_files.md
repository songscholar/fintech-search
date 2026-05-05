# crdt_files - 信用文件导入信息表

**表对象ID**: 7092
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | crdtfile_kind | 否 |  |  |
| 2 | filename | 否 |  |  |
| 3 | update_date | 否 |  |  |
| 4 | update_time | 否 |  |  |
| 5 | crdtfile_kind | 否 |  |  |
| 6 | filename | 否 |  |  |
| 7 | update_date | 否 |  |  |
| 8 | update_time | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdt_files | ART | 是 | crdtfile_kind, crdtfile_kind |
| idx_crdt_files | ART | 是 | crdtfile_kind, crdtfile_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdt_files | crdtfile_kind, crdtfile_kind |
| idx_crdt_files | crdtfile_kind, crdtfile_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-17 21:32:38 | 3.0.6.62 | 李想 | 新增表 |
| 2025-02-17 21:32:38 | 3.0.6.62 | 李想 | 新增表 |

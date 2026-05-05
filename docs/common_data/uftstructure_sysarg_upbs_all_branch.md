# upbs_all_branch - 券商机构表

**表对象ID**: 3
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_ctrlstr | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | branch_zone | 否 |  |  |
| 4 | company_no | 否 |  |  |
| 5 | organ_sysnode_id | 否 |  |  |
| 6 | sysnode_id | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | branch_name | 否 |  |  |
| 9 | sys_online_flag | 否 |  |  |
| 10 | transaction_str | 否 |  |  |
| 11 | branch_ctrlstr | 否 |  |  |
| 12 | branch_no | 否 |  |  |
| 13 | branch_zone | 否 |  |  |
| 14 | company_no | 否 |  |  |
| 15 | organ_sysnode_id | 否 |  |  |
| 16 | sysnode_id | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | branch_name | 否 |  |  |
| 19 | sys_online_flag | 否 |  |  |
| 20 | transaction_str | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_all_branch | ART | 是 | branch_no, branch_no |
| idx_all_branch | ART | 是 | branch_no, branch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_all_branch | branch_no, branch_no |
| idx_all_branch | branch_no, branch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-05 13:53:54 | 8.26.2.96 | 汪杰 | 表空间修改为hs_uft_data |
| 2025-06-13 14:58:38 | 3.0.6.1009 | 汪迎 | 物理表upbs_all_branch，添加了表字段(transaction_str);
 |
| 2025-05-19 19:56:27 | 3.0.6.139 |  | 物理表upbs_all_branch，添加了表字段(sys_online_flag);
 |
| 2023-12-06 16:14:13 | V3.0.1.20 | 牟家乐 | 物理表upbs_all_branch，添加了表字段(branch_name);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 15:59 | 0.0.0.5 | 吴威 | 新增字段transaction_no |
| 2026-01-05 13:53:54 | 8.26.2.96 | 汪杰 | 表空间修改为hs_uft_data |
| 2025-06-13 14:58:38 | 3.0.6.1009 | 汪迎 | 物理表upbs_all_branch，添加了表字段(transaction_str);
 |
| 2025-05-19 19:56:27 | 3.0.6.139 |  | 物理表upbs_all_branch，添加了表字段(sys_online_flag);
 |
| 2023-12-06 16:14:13 | V3.0.1.20 | 牟家乐 | 物理表upbs_all_branch，添加了表字段(branch_name);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 15:59 | 0.0.0.5 | 吴威 | 新增字段transaction_no |

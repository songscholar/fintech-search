# usps_branch_prefix - 机构前缀表

**表对象ID**: 26
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | contract_prefix | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | finance_type | 否 |  |  |
| 5 | rpt_branch_id | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | update_date | 否 |  |  |
| 8 | update_time | 否 |  |  |
| 9 | position_str | 否 |  | branch_no(6)+exchange_type(4)+finance_type(1) |
| 10 | branch_no | 否 |  |  |
| 11 | contract_prefix | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | finance_type | 否 |  |  |
| 14 | rpt_branch_id | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | position_str | 否 |  | branch_no(6)+exchange_type(4)+finance_type(1) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_branchprefix | ART | 是 | branch_no, exchange_type, finance_type, branch_no, exchange_type, finance_type |
| idx_branchprefix | ART | 是 | branch_no, exchange_type, finance_type, branch_no, exchange_type, finance_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_branchprefix | branch_no, exchange_type, finance_type, branch_no, exchange_type, finance_type |
| idx_branchprefix | branch_no, exchange_type, finance_type, branch_no, exchange_type, finance_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-05 14:02:45 | 8.26.2.104 | 汪杰 | 表空间修改为hs_uft_data |
| 2025-02-19 13:57:26 | 3.0.6.87 | 李想 | 物理表usps_branch_prefix，添加了表字段(update_date);
物理表usps_branch_p... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 16:01 | 0.0.0.5 | 吴威 | 新增字段transaction_no |
| 2023-03-30 23:45 | 0.0.0.1 | 程效 | 新增 |
| 2026-01-05 14:02:45 | 8.26.2.104 | 汪杰 | 表空间修改为hs_uft_data |
| 2025-02-19 13:57:26 | 3.0.6.87 | 李想 | 物理表usps_branch_prefix，添加了表字段(update_date);
物理表usps_branch_p... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 16:01 | 0.0.0.5 | 吴威 | 新增字段transaction_no |
| 2023-03-30 23:45 | 0.0.0.1 | 程效 | 新增 |

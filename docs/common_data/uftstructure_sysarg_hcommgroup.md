# hcommgroup - 二级回购佣金组合表

**表对象ID**: 327
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | comm_model | 否 |  |  |
| 2 | index_field | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | en_room_code | 否 |  |  |
| 7 | en_entrust_way | 否 |  |  |
| 8 | en_entrust_type | 否 |  |  |
| 9 | en_stock_type | 否 |  |  |
| 10 | en_exchange_type | 否 |  |  |
| 11 | en_stock_code | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | update_date | 否 |  |  |
| 14 | update_time | 否 |  |  |
| 15 | comm_model | 否 |  |  |
| 16 | index_field | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | fund_account | 否 |  |  |
| 19 | client_id | 否 |  |  |
| 20 | en_room_code | 否 |  |  |
| 21 | en_entrust_way | 否 |  |  |
| 22 | en_entrust_type | 否 |  |  |
| 23 | en_stock_type | 否 |  |  |
| 24 | en_exchange_type | 否 |  |  |
| 25 | en_stock_code | 否 |  |  |
| 26 | transaction_no | 否 |  |  |
| 27 | update_date | 否 |  |  |
| 28 | update_time | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_hcommgroup_bra | 默认 | 否 | branch_no, fund_account, branch_no, fund_account |
| idx_hcommgroup | ART | 是 | index_field, index_field |
| idx_hcommgroup_bra | ART | 是 | branch_no, fund_account, branch_no, fund_account |
| idx_hcommgroup_acct | ART | 是 | fund_account, fund_account |
| idx_hcommgroup_bra | 默认 | 否 | branch_no, fund_account, branch_no, fund_account |
| idx_hcommgroup | ART | 是 | index_field, index_field |
| idx_hcommgroup_bra | ART | 是 | branch_no, fund_account, branch_no, fund_account |
| idx_hcommgroup_acct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_hcommgroup | index_field, index_field |
| idx_hcommgroup_bra | branch_no, fund_account, branch_no, fund_account |
| idx_hcommgroup | index_field, index_field |
| idx_hcommgroup_bra | branch_no, fund_account, branch_no, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-18 16:23:25 | V3.0.2.59 | 钟兆星 | idx_hcommgroup_acct从唯一索引修改为普通索引，同UF20一致 |
| 2025-07-17 14:24:45 | 3.0.6.1017 | 常行 | 物理表hcommgroup，增加索引(idx_hcommgroup_bra:[branch_no,fund_accoun... |
| 2025-02-14 15:36:20 | 3.0.6.29 | 李想 | 物理表hcommgroup，添加了表字段(update_date);
物理表hcommgroup，添加了表字段(upd... |
| 2024-09-26 19:35:12 | 3.0.3.14 | 张明月 | 物理表hcommgroup，添加了表字段(transaction_no);
 |
| 2024-09-23 15:48:09 | 3.0.2.15 | 张明月 | 新增 |
| 2025-07-18 16:23:25 | V3.0.2.59 | 钟兆星 | idx_hcommgroup_acct从唯一索引修改为普通索引，同UF20一致 |
| 2025-07-17 14:24:45 | 3.0.6.1017 | 常行 | 物理表hcommgroup，增加索引(idx_hcommgroup_bra:[branch_no,fund_accoun... |
| 2025-02-14 15:36:20 | 3.0.6.29 | 李想 | 物理表hcommgroup，添加了表字段(update_date);
物理表hcommgroup，添加了表字段(upd... |
| 2024-09-26 19:35:12 | 3.0.3.14 | 张明月 | 物理表hcommgroup，添加了表字段(transaction_no);
 |
| 2024-09-23 15:48:09 | 3.0.2.15 | 张明月 | 新增 |

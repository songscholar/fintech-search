# bond_exemptricon - 证券可转债交易权限豁免名单信息

**表对象ID**: 5708
**所属模块**: sestrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | position_str | 否 |  | branch_no(6)+fund_account(18)+exchange_type(4)+stock_account |
| 8 | transaction_no | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | branch_no | 否 |  |  |
| 12 | client_id | 否 |  |  |
| 13 | fund_account | 否 |  |  |
| 14 | stock_account | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | position_str | 否 |  | branch_no(6)+fund_account(18)+exchange_type(4)+stock_account |
| 18 | transaction_no | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_secuexemptriconbonds | 默认 | 否 | client_id, fund_account, stock_code, exchange_type, client_id, fund_account, stock_code, exchange_type |
| idx_secuexemptriconbonds | ART | 是 | client_id, fund_account, stock_code, exchange_type, client_id, fund_account, stock_code, exchange_type |
| idx_secuexemptriconbonds_pos | ART | 是 | position_str, position_str |
| idx_secuexemptriconbonds | 默认 | 否 | client_id, fund_account, stock_code, exchange_type, client_id, fund_account, stock_code, exchange_type |
| idx_secuexemptriconbonds | ART | 是 | client_id, fund_account, stock_code, exchange_type, client_id, fund_account, stock_code, exchange_type |
| idx_secuexemptriconbonds_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_secuexemptriconbonds_pos | position_str, position_str |
| idx_secuexemptriconbonds | client_id, fund_account, stock_code, exchange_type, client_id, fund_account, stock_code, exchange_type |
| idx_secuexemptriconbonds_pos | position_str, position_str |
| idx_secuexemptriconbonds | client_id, fund_account, stock_code, exchange_type, client_id, fund_account, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:35:42 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-17 15:37:06 | 3.0.6.1002 | 常行 | 物理表bond_exemptricon，增加索引(idx_secuexemptriconbonds:[client_id... |
| 2025-02-19 15:53:36 | 3.0.6.13 | 李想 | 物理表bond_exemptricon，添加了表字段(update_date);
物理表bond_exemptrico... |
| 2024-05-18 14:10:54 | 3.0.2.7 | 祝丁恺 | 物理表bond_exemptricon，添加了表字段(transaction_no);
 |
| 2026-03-09 14:35:42 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-17 15:37:06 | 3.0.6.1002 | 常行 | 物理表bond_exemptricon，增加索引(idx_secuexemptriconbonds:[client_id... |
| 2025-02-19 15:53:36 | 3.0.6.13 | 李想 | 物理表bond_exemptricon，添加了表字段(update_date);
物理表bond_exemptrico... |
| 2024-05-18 14:10:54 | 3.0.2.7 | 祝丁恺 | 物理表bond_exemptricon，添加了表字段(transaction_no);
 |

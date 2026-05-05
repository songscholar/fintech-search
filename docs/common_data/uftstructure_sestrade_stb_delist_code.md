# stb_delist_code - 股转摘牌证券信息表

**表对象ID**: 5568
**所属模块**: sestrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_name | 否 |  |  |
| 5 | relative_code | 否 |  |  |
| 6 | money_type | 否 |  |  |
| 7 | exchange_unit | 否 |  |  |
| 8 | par_value | 否 |  |  |
| 9 | transfer_begin_date | 否 |  |  |
| 10 | stbtrans_flag | 否 |  |  |
| 11 | stbtrans_svr_status | 否 |  |  |
| 12 | stock_type_b | 否 |  |  |
| 13 | stock_level | 否 |  |  |
| 14 | stkaccount_total | 否 |  |  |
| 15 | tot_business_amount | 否 |  |  |
| 16 | total_business_balance | 否 |  |  |
| 17 | capital_amount | 否 |  |  |
| 18 | transaction_no | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 22 | init_date | 否 |  |  |
| 23 | exchange_type | 否 |  |  |
| 24 | stock_code | 否 |  |  |
| 25 | stock_name | 否 |  |  |
| 26 | relative_code | 否 |  |  |
| 27 | money_type | 否 |  |  |
| 28 | exchange_unit | 否 |  |  |
| 29 | par_value | 否 |  |  |
| 30 | transfer_begin_date | 否 |  |  |
| 31 | stbtrans_flag | 否 |  |  |
| 32 | stbtrans_svr_status | 否 |  |  |
| 33 | stock_type_b | 否 |  |  |
| 34 | stock_level | 否 |  |  |
| 35 | stkaccount_total | 否 |  |  |
| 36 | tot_business_amount | 否 |  |  |
| 37 | total_business_balance | 否 |  |  |
| 38 | capital_amount | 否 |  |  |
| 39 | transaction_no | 否 |  |  |
| 40 | update_date | 否 |  |  |
| 41 | update_time | 否 |  |  |
| 42 | position_str | 否 |  | stock_code(8)+exchange_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stb_delist_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_stb_delist_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stb_delist_code | stock_code, exchange_type, stock_code, exchange_type |
| idx_stb_delist_code | stock_code, exchange_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:17:53 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-18 16:47:26 | 3.0.6.9 | 李想 | 物理表stb_delist_code，添加了表字段(update_date);
物理表stb_delist_code，... |
| 2024-07-30 17:02:49 | 3.0.2.31 | 赵良梓 | 新增表结构 |
| 2026-03-09 14:17:53 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-18 16:47:26 | 3.0.6.9 | 李想 | 物理表stb_delist_code，添加了表字段(update_date);
物理表stb_delist_code，... |
| 2024-07-30 17:02:49 | 3.0.2.31 | 赵良梓 | 新增表结构 |

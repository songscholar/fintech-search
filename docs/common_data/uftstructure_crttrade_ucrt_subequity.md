# ucrt_subequity - 融资融券市值申购权益表

**表对象ID**: 7522
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 48 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | seat_no | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | enable_amount | 否 |  |  |
| 8 | register_date | 否 |  |  |
| 9 | stib_enable_quota | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | branch_no | 否 |  |  |
| 12 | update_date | 否 |  |  |
| 13 | update_time | 否 |  |  |
| 14 | position_str | 否 |  | fund_account(18)+stock_account(20)+exchange_type(4) |
| 15 | client_group | 否 | H |  |
| 16 | room_code | 否 | H |  |
| 17 | asset_prop | 否 | H |  |
| 18 | limit_flag | 否 | H |  |
| 19 | risk_level | 否 | H |  |
| 20 | corp_client_group | 否 | H |  |
| 21 | corp_risk_level | 否 | H |  |
| 22 | asset_level | 否 | H |  |
| 23 | client_name | 否 | H |  |
| 24 | client_prop | 否 | H |  |
| 25 | init_date | 否 |  |  |
| 26 | stock_account | 否 |  |  |
| 27 | exchange_type | 否 |  |  |
| 28 | seat_no | 否 |  |  |
| 29 | fund_account | 否 |  |  |
| 30 | client_id | 否 |  |  |
| 31 | enable_amount | 否 |  |  |
| 32 | register_date | 否 |  |  |
| 33 | stib_enable_quota | 否 |  |  |
| 34 | transaction_no | 否 |  |  |
| 35 | branch_no | 否 |  |  |
| 36 | update_date | 否 |  |  |
| 37 | update_time | 否 |  |  |
| 38 | position_str | 否 |  | fund_account(18)+stock_account(20)+exchange_type(4) |
| 39 | client_group | 否 | H |  |
| 40 | room_code | 否 | H |  |
| 41 | asset_prop | 否 | H |  |
| 42 | limit_flag | 否 | H |  |
| 43 | risk_level | 否 | H |  |
| 44 | corp_client_group | 否 | H |  |
| 45 | corp_risk_level | 否 | H |  |
| 46 | asset_level | 否 | H |  |
| 47 | client_name | 否 | H |  |
| 48 | client_prop | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_subequity | ART | 是 | fund_account, stock_account, exchange_type, fund_account, stock_account, exchange_type |
| uk_rpt_ucrtsubequity | ART | 是 | init_date, branch_no, fund_account, stock_account, exchange_type, init_date, branch_no, fund_account, stock_account, exchange_type |
| idx_ucrt_subequity | ART | 是 | fund_account, stock_account, exchange_type, fund_account, stock_account, exchange_type |
| uk_rpt_ucrtsubequity | ART | 是 | init_date, branch_no, fund_account, stock_account, exchange_type, init_date, branch_no, fund_account, stock_account, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_subequity | fund_account, stock_account, exchange_type, fund_account, stock_account, exchange_type |
| idx_ucrt_subequity | fund_account, stock_account, exchange_type, fund_account, stock_account, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-16 09:48:34 | 3.0.2.1 | 沈勋 | 去掉表结构上不回库的勾 |
| 2025-07-29 11:29:10 | 3.0.6.57 | tongck54118 | 物理表ucrt_subequity，添加了表字段(branch_no);
物理表ucrt_subequity，添加了表... |
| 2025-09-02 10:22:27 | 3.0.6.1068 | 牟家乐 | 修改表不回库 |
| 2024-11-11 11:08:44 | 3.0.6.16 | 沈勋 | 物理表ucrt_subequity，添加了表字段(transaction_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-10-16 09:48:34 | 3.0.2.1 | 沈勋 | 去掉表结构上不回库的勾 |
| 2025-07-29 11:29:10 | 3.0.6.57 | tongck54118 | 物理表ucrt_subequity，添加了表字段(branch_no);
物理表ucrt_subequity，添加了表... |
| 2025-09-02 10:22:27 | 3.0.6.1068 | 牟家乐 | 修改表不回库 |
| 2024-11-11 11:08:44 | 3.0.6.16 | 沈勋 | 物理表ucrt_subequity，添加了表字段(transaction_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

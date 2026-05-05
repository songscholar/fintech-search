# uses_stock_frozen_total - 证券股份交易信息冻汇总结表

**表对象ID**: 5754
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | sett_batch_no | 否 |  |  |
| 7 | serial_no | 否 |  |  |
| 8 | occur_amount | 否 |  |  |
| 9 | position_str | 否 |  |  |
| 10 | init_date | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | sett_batch_no | 否 |  |  |
| 16 | serial_no | 否 |  |  |
| 17 | occur_amount | 否 |  |  |
| 18 | position_str | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usesstockfrozentotal | ART | 是 | init_date, sett_batch_no, exchange_type, fund_account, stock_account, stock_code, init_date, sett_batch_no, exchange_type, fund_account, stock_account, stock_code |
| idx_usesstockfrozentotal_pos | ART | 是 | position_str, position_str |
| idx_usesstockfrozentotal_pos | ART | 是 | init_date, position_str, init_date, position_str |
| idx_usesstockfrozentotal | ART | 是 | init_date, sett_batch_no, exchange_type, fund_account, stock_account, stock_code, init_date, sett_batch_no, exchange_type, fund_account, stock_account, stock_code |
| idx_usesstockfrozentotal_pos | ART | 是 | position_str, position_str |
| idx_usesstockfrozentotal_pos | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usesstockfrozentotal | init_date, sett_batch_no, exchange_type, fund_account, stock_account, stock_code, init_date, sett_batch_no, exchange_type, fund_account, stock_account, stock_code |
| idx_usesstockfrozentotal | init_date, sett_batch_no, exchange_type, fund_account, stock_account, stock_code, init_date, sett_batch_no, exchange_type, fund_account, stock_account, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:41:24 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-11-17 10:37:02 | V3.0.2.4 | 洪略 | 增加历史表 |
| 2025-08-19 19:34:33 | 3.0.2.101 | yangxz | 新增表结构 |
| 2026-03-09 14:41:24 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-11-17 10:37:02 | V3.0.2.4 | 洪略 | 增加历史表 |
| 2025-08-19 19:34:33 | 3.0.2.101 | yangxz | 新增表结构 |

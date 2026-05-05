# uopt_entrustaid - 期权非交易辅助委托表

**表对象ID**: 9612
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | entrust_no | 否 |  |  |
| 3 | trace_id | 否 |  |  |
| 4 | entrust_prop | 否 |  |  |
| 5 | fund_account_src | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | client_id_src | 否 |  |  |
| 8 | stock_account_src | 否 |  |  |
| 9 | branch_no_src | 否 |  |  |
| 10 | seat_no_src | 否 |  |  |
| 11 | fund_account_dest | 否 |  |  |
| 12 | client_id_dest | 否 |  |  |
| 13 | stock_account_dest | 否 |  |  |
| 14 | branch_no_dest | 否 |  |  |
| 15 | seat_no_dest | 否 |  |  |
| 16 | stock_account | 否 |  |  |
| 17 | fund_account | 否 |  |  |
| 18 | init_date | 否 |  |  |
| 19 | entrust_no | 否 |  |  |
| 20 | trace_id | 否 |  |  |
| 21 | entrust_prop | 否 |  |  |
| 22 | fund_account_src | 否 |  |  |
| 23 | exchange_type | 否 |  |  |
| 24 | client_id_src | 否 |  |  |
| 25 | stock_account_src | 否 |  |  |
| 26 | branch_no_src | 否 |  |  |
| 27 | seat_no_src | 否 |  |  |
| 28 | fund_account_dest | 否 |  |  |
| 29 | client_id_dest | 否 |  |  |
| 30 | stock_account_dest | 否 |  |  |
| 31 | branch_no_dest | 否 |  |  |
| 32 | seat_no_dest | 否 |  |  |
| 33 | stock_account | 否 |  |  |
| 34 | fund_account | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_entrustaid | 默认 | 否 | init_date, init_date |
| idx_uopt_entrustaid | 默认 | 否 | init_date, entrust_no, init_date, entrust_no |
| idx_uopt_entrustaid_temp | 默认 | 是 | init_date, entrust_no, stock_account, exchange_type, init_date, entrust_no, stock_account, exchange_type |
| idx_uopt_entrustaid | 默认 | 否 | init_date, init_date |
| idx_uopt_entrustaid | 默认 | 否 | init_date, entrust_no, init_date, entrust_no |
| idx_uopt_entrustaid_temp | 默认 | 是 | init_date, entrust_no, stock_account, exchange_type, init_date, entrust_no, stock_account, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_entrustaid | init_date, entrust_no, stock_account, exchange_type, init_date, entrust_no, stock_account, exchange_type |
| idx_uopt_entrustaid | init_date, entrust_no, stock_account, exchange_type, init_date, entrust_no, stock_account, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-07 11:35:26 | V3.0.2.3 | 吴笑东 | 物理表uopt_entrustaid，增加索引字段(索引idx_uopt_entrustaid:增加了索引字段：init... |
| 2025-08-07 11:35:26 | V3.0.2.3 | 吴笑东 | 物理表uopt_entrustaid，增加索引字段(索引idx_uopt_entrustaid:增加了索引字段：init... |

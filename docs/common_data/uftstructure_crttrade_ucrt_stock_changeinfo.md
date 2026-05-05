# ucrt_stock_changeinfo - 融资融券存管股份变更信息表

**表对象ID**: 7558
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 76 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | operator_no | 否 |  |  |
| 3 | op_station | 否 |  |  |
| 4 | op_entrust_way | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | stock_account | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | stock_type | 否 |  |  |
| 11 | current_amount | 否 |  |  |
| 12 | frozen_amount | 否 |  |  |
| 13 | unfrozen_amount | 否 |  |  |
| 14 | correct_amount | 否 |  |  |
| 15 | serial_no | 否 |  |  |
| 16 | sum_sell_amount | 否 |  |  |
| 17 | sum_sell_balance | 否 |  |  |
| 18 | cancel_serial_no | 否 |  |  |
| 19 | cost_price | 否 |  |  |
| 20 | uncome_buy_amount | 否 |  |  |
| 21 | uncome_sell_amount | 否 |  |  |
| 22 | sum_buy_amount | 否 |  |  |
| 23 | sum_buy_balance | 否 |  |  |
| 24 | business_flag | 否 |  |  |
| 25 | remark | 否 |  |  |
| 26 | client_name | 否 | H |  |
| 27 | branch_no | 否 | H |  |
| 28 | client_group | 否 | H |  |
| 29 | room_code | 否 | H |  |
| 30 | asset_prop | 否 | H |  |
| 31 | limit_flag | 否 | H |  |
| 32 | client_prop | 否 | H |  |
| 33 | asset_level | 否 | H |  |
| 34 | risk_level | 否 | H |  |
| 35 | corp_risk_level | 否 | H |  |
| 36 | stock_name | 否 | H |  |
| 37 | sub_stock_type | 否 | H |  |
| 38 | corp_client_group | 否 | H |  |
| 39 | init_date | 否 |  |  |
| 40 | operator_no | 否 |  |  |
| 41 | op_station | 否 |  |  |
| 42 | op_entrust_way | 否 |  |  |
| 43 | fund_account | 否 |  |  |
| 44 | client_id | 否 |  |  |
| 45 | exchange_type | 否 |  |  |
| 46 | stock_account | 否 |  |  |
| 47 | stock_code | 否 |  |  |
| 48 | stock_type | 否 |  |  |
| 49 | current_amount | 否 |  |  |
| 50 | frozen_amount | 否 |  |  |
| 51 | unfrozen_amount | 否 |  |  |
| 52 | correct_amount | 否 |  |  |
| 53 | serial_no | 否 |  |  |
| 54 | sum_sell_amount | 否 |  |  |
| 55 | sum_sell_balance | 否 |  |  |
| 56 | cancel_serial_no | 否 |  |  |
| 57 | cost_price | 否 |  |  |
| 58 | uncome_buy_amount | 否 |  |  |
| 59 | uncome_sell_amount | 否 |  |  |
| 60 | sum_buy_amount | 否 |  |  |
| 61 | sum_buy_balance | 否 |  |  |
| 62 | business_flag | 否 |  |  |
| 63 | remark | 否 |  |  |
| 64 | client_name | 否 | H |  |
| 65 | branch_no | 否 | H |  |
| 66 | client_group | 否 | H |  |
| 67 | room_code | 否 | H |  |
| 68 | asset_prop | 否 | H |  |
| 69 | limit_flag | 否 | H |  |
| 70 | client_prop | 否 | H |  |
| 71 | asset_level | 否 | H |  |
| 72 | risk_level | 否 | H |  |
| 73 | corp_risk_level | 否 | H |  |
| 74 | stock_name | 否 | H |  |
| 75 | sub_stock_type | 否 | H |  |
| 76 | corp_client_group | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_stock_changeinfo | ART | 是 | fund_account, serial_no, fund_account, serial_no |
| uk_rpt_ucrtstockchangeinfo | ART | 是 | init_date, fund_account, serial_no, init_date, fund_account, serial_no |
| idx_ucrt_stock_changeinfo | ART | 是 | fund_account, serial_no, fund_account, serial_no |
| uk_rpt_ucrtstockchangeinfo | ART | 是 | init_date, fund_account, serial_no, init_date, fund_account, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_stock_changeinfo | fund_account, serial_no, fund_account, serial_no |
| idx_ucrt_stock_changeinfo | fund_account, serial_no, fund_account, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-25 10:10:49 | 3.0.2.2001 | 蒋浩 | 新增表结构 |
| 2025-02-25 10:10:49 | 3.0.2.2001 | 蒋浩 | 新增表结构 |

# etf_cash_balanceinfo - ETF预估现金冻结信息表

**表对象ID**: 2840
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 70 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_account | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | order_id | 否 |  |  |
| 9 | business_id | 否 |  |  |
| 10 | entrust_no | 否 |  |  |
| 11 | entrust_bs | 否 |  |  |
| 12 | money_type | 否 |  |  |
| 13 | trade_plat | 否 |  |  |
| 14 | position_str | 否 |  | "%08d%05d%018s%04s%06s%010s%c", @business_date, @branch_no,  |
| 15 | settle_mark | 否 |  |  |
| 16 | frozen_balance | 否 |  |  |
| 17 | business_amount | 否 |  |  |
| 18 | date_clear | 否 |  |  |
| 19 | deal_status | 否 |  |  |
| 20 | remark | 否 |  |  |
| 21 | business_frozen_balance | 否 |  |  |
| 22 | serial_no | 否 |  |  |
| 23 | client_name | 否 | H |  |
| 24 | corp_client_group | 否 | H |  |
| 25 | client_group | 否 | H |  |
| 26 | room_code | 否 | H |  |
| 27 | asset_prop | 否 | H |  |
| 28 | limit_flag | 否 | H |  |
| 29 | client_prop | 否 | H |  |
| 30 | asset_level | 否 | H |  |
| 31 | risk_level | 否 | H |  |
| 32 | corp_risk_level | 否 | H |  |
| 33 | stock_name | 否 | H |  |
| 34 | stock_type | 否 | H |  |
| 35 | sub_stock_type | 否 | H |  |
| 36 | init_date | 否 |  |  |
| 37 | branch_no | 否 |  |  |
| 38 | fund_account | 否 |  |  |
| 39 | client_id | 否 |  |  |
| 40 | exchange_type | 否 |  |  |
| 41 | stock_account | 否 |  |  |
| 42 | stock_code | 否 |  |  |
| 43 | order_id | 否 |  |  |
| 44 | business_id | 否 |  |  |
| 45 | entrust_no | 否 |  |  |
| 46 | entrust_bs | 否 |  |  |
| 47 | money_type | 否 |  |  |
| 48 | trade_plat | 否 |  |  |
| 49 | position_str | 否 |  | "%08d%05d%018s%04s%06s%010s%c", @business_date, @branch_no,  |
| 50 | settle_mark | 否 |  |  |
| 51 | frozen_balance | 否 |  |  |
| 52 | business_amount | 否 |  |  |
| 53 | date_clear | 否 |  |  |
| 54 | deal_status | 否 |  |  |
| 55 | remark | 否 |  |  |
| 56 | business_frozen_balance | 否 |  |  |
| 57 | serial_no | 否 |  |  |
| 58 | client_name | 否 | H |  |
| 59 | corp_client_group | 否 | H |  |
| 60 | client_group | 否 | H |  |
| 61 | room_code | 否 | H |  |
| 62 | asset_prop | 否 | H |  |
| 63 | limit_flag | 否 | H |  |
| 64 | client_prop | 否 | H |  |
| 65 | asset_level | 否 | H |  |
| 66 | risk_level | 否 | H |  |
| 67 | corp_risk_level | 否 | H |  |
| 68 | stock_name | 否 | H |  |
| 69 | stock_type | 否 | H |  |
| 70 | sub_stock_type | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_etfcashbalance_pos  | ART | 是 | position_str, position_str |
| idx_rpt_etfcashbalance_pos  | ART | 是 | init_date, position_str, init_date, position_str |
| idx_etfcashbalance_pos  | ART | 是 | position_str, position_str |
| idx_rpt_etfcashbalance_pos  | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_etfcashbalance_pos  | position_str, position_str |
| idx_etfcashbalance_pos  | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 09:07:00 | V3.0.2.8 | taocong45644 | 数据存储介质修改为DB |
| 2025-12-01 11:28:08 | 3.0.2.5 | 洪略 | 历史表增加asset_prop字段 |
| 2025-11-17 10:09:39 | 3.0.2.5 | 洪略 | 增加历史表 |
| 2025-04-14 14:28:21 | V3.0.2.2002 | 蒋浩 |  |
| 2026-03-06 09:07:00 | V3.0.2.8 | taocong45644 | 数据存储介质修改为DB |
| 2025-12-01 11:28:08 | 3.0.2.5 | 洪略 | 历史表增加asset_prop字段 |
| 2025-11-17 10:09:39 | 3.0.2.5 | 洪略 | 增加历史表 |
| 2025-04-14 14:28:21 | V3.0.2.2002 | 蒋浩 |  |

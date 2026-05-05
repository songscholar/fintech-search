# bpr_entrust_tri_ext - 协议回购委托扩展表

**表对象ID**: 2356
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 64 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | entrust_no | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | stock_type | 否 |  |  |
| 9 | entrust_amount | 否 |  |  |
| 10 | preterm_year_rate | 否 |  |  |
| 11 | entrust_balance | 否 |  |  |
| 12 | asset_net_value | 否 |  |  |
| 13 | back_balance | 否 |  |  |
| 14 | entrust_status | 否 |  |  |
| 15 | cbpconfer_id | 否 |  |  |
| 16 | join_serial_no | 否 |  |  |
| 17 | cbpcontract_id | 否 |  |  |
| 18 | prev_balance | 否 |  |  |
| 19 | serial_no | 否 |  |  |
| 20 | client_id | 否 | H |  |
| 21 | client_name | 否 | H |  |
| 22 | corp_client_group | 否 | H |  |
| 23 | client_group | 否 | H |  |
| 24 | room_code | 否 | H |  |
| 25 | asset_prop | 否 | H |  |
| 26 | limit_flag | 否 | H |  |
| 27 | client_prop | 否 | H |  |
| 28 | asset_level | 否 | H |  |
| 29 | risk_level | 否 | H |  |
| 30 | corp_risk_level | 否 | H |  |
| 31 | stock_name | 否 | H |  |
| 32 | sub_stock_type | 否 | H |  |
| 33 | init_date | 否 |  |  |
| 34 | branch_no | 否 |  |  |
| 35 | fund_account | 否 |  |  |
| 36 | stock_account | 否 |  |  |
| 37 | exchange_type | 否 |  |  |
| 38 | entrust_no | 否 |  |  |
| 39 | stock_code | 否 |  |  |
| 40 | stock_type | 否 |  |  |
| 41 | entrust_amount | 否 |  |  |
| 42 | preterm_year_rate | 否 |  |  |
| 43 | entrust_balance | 否 |  |  |
| 44 | asset_net_value | 否 |  |  |
| 45 | back_balance | 否 |  |  |
| 46 | entrust_status | 否 |  |  |
| 47 | cbpconfer_id | 否 |  |  |
| 48 | join_serial_no | 否 |  |  |
| 49 | cbpcontract_id | 否 |  |  |
| 50 | prev_balance | 否 |  |  |
| 51 | serial_no | 否 |  |  |
| 52 | client_id | 否 | H |  |
| 53 | client_name | 否 | H |  |
| 54 | corp_client_group | 否 | H |  |
| 55 | client_group | 否 | H |  |
| 56 | room_code | 否 | H |  |
| 57 | asset_prop | 否 | H |  |
| 58 | limit_flag | 否 | H |  |
| 59 | client_prop | 否 | H |  |
| 60 | asset_level | 否 | H |  |
| 61 | risk_level | 否 | H |  |
| 62 | corp_risk_level | 否 | H |  |
| 63 | stock_name | 否 | H |  |
| 64 | sub_stock_type | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_bprentrusttriext_code | 默认 | 否 |  |
| idx_bprentrusttriext_code | ART | 是 | entrust_no, stock_code, serial_no, entrust_no, stock_code, serial_no |
| uk_rpt_bprentrusttriext | ART | 是 | init_date, entrust_no, stock_code, serial_no, init_date, entrust_no, stock_code, serial_no |
| idx_bprentrusttriext_code | 默认 | 否 |  |
| idx_bprentrusttriext_code | ART | 是 | entrust_no, stock_code, serial_no, entrust_no, stock_code, serial_no |
| uk_rpt_bprentrusttriext | ART | 是 | init_date, entrust_no, stock_code, serial_no, init_date, entrust_no, stock_code, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_bprentrusttriext_code | entrust_no, stock_code, serial_no, entrust_no, stock_code, serial_no |
| idx_bprentrusttriext_code | entrust_no, stock_code, serial_no, entrust_no, stock_code, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:39:22 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-09-23 17:14:44 | V3.0.2.1007 | 张明月 | 新增 |
| 2026-03-04 15:39:22 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-09-23 17:14:44 | V3.0.2.1007 | 张明月 | 新增 |

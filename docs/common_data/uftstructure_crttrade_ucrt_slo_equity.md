# ucrt_slo_equity - 融券股份权益信息表

**表对象ID**: 7525
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 76 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | stock_type | 否 |  |  |
| 9 | money_type | 否 |  |  |
| 10 | equity_type | 否 |  |  |
| 11 | current_amount | 否 |  |  |
| 12 | recoup_amount | 否 |  |  |
| 13 | recoup_balance | 否 |  |  |
| 14 | recoup_type | 否 |  |  |
| 15 | compact_id | 否 |  |  |
| 16 | equity_discount_ratio | 否 |  |  |
| 17 | equity_discount_flag | 否 |  |  |
| 18 | deal_status | 否 |  |  |
| 19 | cashgroup_no | 否 |  |  |
| 20 | compact_source | 否 |  |  |
| 21 | pre_recoup_balance | 否 |  |  |
| 22 | recoup_amount_decimal | 否 |  |  |
| 23 | register_date | 否 |  |  |
| 24 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5) +serial_no(10) |
| 25 | date_clear | 否 |  |  |
| 26 | branch_no | 否 |  |  |
| 27 | client_group | 否 | H |  |
| 28 | room_code | 否 | H |  |
| 29 | asset_prop | 否 | H |  |
| 30 | limit_flag | 否 | H |  |
| 31 | risk_level | 否 | H |  |
| 32 | corp_client_group | 否 | H |  |
| 33 | corp_risk_level | 否 | H |  |
| 34 | asset_level | 否 | H |  |
| 35 | stock_name | 否 | H |  |
| 36 | client_name | 否 | H |  |
| 37 | client_prop | 否 | H |  |
| 38 | sub_stock_type | 否 | H |  |
| 39 | init_date | 否 |  |  |
| 40 | serial_no | 否 |  |  |
| 41 | client_id | 否 |  |  |
| 42 | fund_account | 否 |  |  |
| 43 | stock_account | 否 |  |  |
| 44 | exchange_type | 否 |  |  |
| 45 | stock_code | 否 |  |  |
| 46 | stock_type | 否 |  |  |
| 47 | money_type | 否 |  |  |
| 48 | equity_type | 否 |  |  |
| 49 | current_amount | 否 |  |  |
| 50 | recoup_amount | 否 |  |  |
| 51 | recoup_balance | 否 |  |  |
| 52 | recoup_type | 否 |  |  |
| 53 | compact_id | 否 |  |  |
| 54 | equity_discount_ratio | 否 |  |  |
| 55 | equity_discount_flag | 否 |  |  |
| 56 | deal_status | 否 |  |  |
| 57 | cashgroup_no | 否 |  |  |
| 58 | compact_source | 否 |  |  |
| 59 | pre_recoup_balance | 否 |  |  |
| 60 | recoup_amount_decimal | 否 |  |  |
| 61 | register_date | 否 |  |  |
| 62 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5) +serial_no(10) |
| 63 | date_clear | 否 |  |  |
| 64 | branch_no | 否 |  |  |
| 65 | client_group | 否 | H |  |
| 66 | room_code | 否 | H |  |
| 67 | asset_prop | 否 | H |  |
| 68 | limit_flag | 否 | H |  |
| 69 | risk_level | 否 | H |  |
| 70 | corp_client_group | 否 | H |  |
| 71 | corp_risk_level | 否 | H |  |
| 72 | asset_level | 否 | H |  |
| 73 | stock_name | 否 | H |  |
| 74 | client_name | 否 | H |  |
| 75 | client_prop | 否 | H |  |
| 76 | sub_stock_type | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_slo_equity | ART | 是 | fund_account, serial_no, init_date, fund_account, serial_no, init_date |
| idx_ucrt_slo_equity_code | ART | 是 | fund_account, stock_code, exchange_type, equity_type, register_date, fund_account, stock_code, exchange_type, equity_type, register_date |
| idx_ucrt_slo_equity_acct | ART | 是 | fund_account, exchange_type, stock_code, register_date, compact_source, fund_account, exchange_type, stock_code, register_date, compact_source |
| idx_ucrt_slo_equity | ART | 是 | fund_account, serial_no, init_date, fund_account, serial_no, init_date |
| uk_rpt_ucrtsloequity | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtsloequity_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_ucrtsloequity_tolast | ART | 是 | date_clear, date_clear |
| idx_ucrt_slo_equity | ART | 是 | fund_account, serial_no, init_date, fund_account, serial_no, init_date |
| idx_ucrt_slo_equity_code | ART | 是 | fund_account, stock_code, exchange_type, equity_type, register_date, fund_account, stock_code, exchange_type, equity_type, register_date |
| idx_ucrt_slo_equity_acct | ART | 是 | fund_account, exchange_type, stock_code, register_date, compact_source, fund_account, exchange_type, stock_code, register_date, compact_source |
| idx_ucrt_slo_equity | ART | 是 | fund_account, serial_no, init_date, fund_account, serial_no, init_date |
| uk_rpt_ucrtsloequity | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtsloequity_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_ucrtsloequity_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_slo_equity | fund_account, serial_no, init_date, fund_account, serial_no, init_date |
| idx_ucrt_slo_equity_acct | fund_account, exchange_type, stock_code, register_date, compact_source, fund_account, exchange_type, stock_code, register_date, compact_source |
| idx_ucrt_slo_equity | fund_account, serial_no, init_date, fund_account, serial_no, init_date |
| idx_ucrt_slo_equity_acct | fund_account, exchange_type, stock_code, register_date, compact_source, fund_account, exchange_type, stock_code, register_date, compact_source |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-15 15:20:59 | 3.0.8.12 | 袁文龙 | 物理表ucrt_slo_equity，增加索引（ idx_ucrt_slo_equity:[fund_account,s... |
| 2025-08-21 14:18:16 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_slo_equity，添加了表字段(branch_no);
 |
| 2025-08-06 18:15:30 | 3.0.6.1064 | 徐世晗 | 物理表ucrt_slo_equity，添加了表字段(date_clear);
 |
| 2025-03-24 10:23:52 | 3.0.6.43 | 汪杰 | 物理表ucrt_slo_equity，添加了表字段(position_str);
 |
| 2024-01-23 13:48:58 | V3.0.1.27 | 程效 | 增加索引idx_ucrt_slo_equity_acct |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-01-15 15:20:59 | 3.0.8.12 | 袁文龙 | 物理表ucrt_slo_equity，增加索引（ idx_ucrt_slo_equity:[fund_account,s... |
| 2025-08-21 14:18:16 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_slo_equity，添加了表字段(branch_no);
 |
| 2025-08-06 18:15:30 | 3.0.6.1064 | 徐世晗 | 物理表ucrt_slo_equity，添加了表字段(date_clear);
 |
| 2025-03-24 10:23:52 | 3.0.6.43 | 汪杰 | 物理表ucrt_slo_equity，添加了表字段(position_str);
 |
| 2024-01-23 13:48:58 | V3.0.1.27 | 程效 | 增加索引idx_ucrt_slo_equity_acct |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

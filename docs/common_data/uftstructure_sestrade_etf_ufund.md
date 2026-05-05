# etf_ufund - 网下现金认购信息表

**表对象ID**: 5541
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 76 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | money_type | 否 |  |  |
| 8 | operator_no | 否 |  |  |
| 9 | entrust_amount | 否 |  |  |
| 10 | entrust_price | 否 |  |  |
| 11 | entrust_status | 否 |  |  |
| 12 | prev_status | 否 |  |  |
| 13 | frozen_balance | 否 |  |  |
| 14 | frozen_fare | 否 |  |  |
| 15 | entrust_date | 否 |  |  |
| 16 | entrust_time | 否 |  |  |
| 17 | entrust_no | 否 |  |  |
| 18 | entrust_operator | 否 |  |  |
| 19 | remark | 否 |  |  |
| 20 | report_amount | 否 |  |  |
| 21 | report_balance | 否 |  |  |
| 22 | entrustno_str | 否 |  |  |
| 23 | report_date | 否 |  |  |
| 24 | position_str | 否 |  | branch_no(5)+exchange_type(4)+stock_account(10)+stock_code(6 |
| 25 | client_name | 否 | H |  |
| 26 | corp_client_group | 否 | H |  |
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
| 37 | stock_type | 否 | H |  |
| 38 | sub_stock_type | 否 | H |  |
| 39 | init_date | 否 |  |  |
| 40 | fund_account | 否 |  |  |
| 41 | stock_account | 否 |  |  |
| 42 | stock_code | 否 |  |  |
| 43 | client_id | 否 |  |  |
| 44 | exchange_type | 否 |  |  |
| 45 | money_type | 否 |  |  |
| 46 | operator_no | 否 |  |  |
| 47 | entrust_amount | 否 |  |  |
| 48 | entrust_price | 否 |  |  |
| 49 | entrust_status | 否 |  |  |
| 50 | prev_status | 否 |  |  |
| 51 | frozen_balance | 否 |  |  |
| 52 | frozen_fare | 否 |  |  |
| 53 | entrust_date | 否 |  |  |
| 54 | entrust_time | 否 |  |  |
| 55 | entrust_no | 否 |  |  |
| 56 | entrust_operator | 否 |  |  |
| 57 | remark | 否 |  |  |
| 58 | report_amount | 否 |  |  |
| 59 | report_balance | 否 |  |  |
| 60 | entrustno_str | 否 |  |  |
| 61 | report_date | 否 |  |  |
| 62 | position_str | 否 |  | branch_no(5)+exchange_type(4)+stock_account(10)+stock_code(6 |
| 63 | client_name | 否 | H |  |
| 64 | corp_client_group | 否 | H |  |
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
| 75 | stock_type | 否 | H |  |
| 76 | sub_stock_type | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_etf_ufund | ART | 是 | position_str, position_str |
| idx_etf_ufund_acct | ART | 是 | fund_account, stock_account, stock_code, fund_account, stock_account, stock_code |
| idx_etf_ufund_id | ART | 是 | client_id, client_id |
| idx_etf_ufund_stk | ART | 是 | stock_code, stock_code |
| uk_rpt_etfufund | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_etfufund_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_etfufund_tolast | ART | 是 | report_date, report_date |
| idx_etf_ufund | ART | 是 | position_str, position_str |
| idx_etf_ufund_acct | ART | 是 | fund_account, stock_account, stock_code, fund_account, stock_account, stock_code |
| idx_etf_ufund_id | ART | 是 | client_id, client_id |
| idx_etf_ufund_stk | ART | 是 | stock_code, stock_code |
| uk_rpt_etfufund | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_etfufund_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_etfufund_tolast | ART | 是 | report_date, report_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_etf_ufund | position_str, position_str |
| idx_etf_ufund | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:54:38 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.28 | 李江霖 | 增加position_str的备注 |
| 2024-07-04 13:20:25 | 3.0.2.27 | 谢宗艺 | 物理表etf_ufund，删除了表字段(branch_no);
物理表etf_ufund，删除了表字段(stock_n... |
| 2024-07-01 17:17:52 | 3.0.2.25 | 谢宗艺 | 新增 |
| 2026-03-09 13:54:38 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.28 | 李江霖 | 增加position_str的备注 |
| 2024-07-04 13:20:25 | 3.0.2.27 | 谢宗艺 | 物理表etf_ufund，删除了表字段(branch_no);
物理表etf_ufund，删除了表字段(stock_n... |
| 2024-07-01 17:17:52 | 3.0.2.25 | 谢宗艺 | 新增 |

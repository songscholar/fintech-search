# etf_ustock - 网下股份认购信息表

**表对象ID**: 5536
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 84 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | component_code | 否 |  |  |
| 8 | component_name | 否 |  |  |
| 9 | money_type | 否 |  |  |
| 10 | operator_no | 否 |  |  |
| 11 | entrust_amount | 否 |  |  |
| 12 | entrust_status | 否 |  |  |
| 13 | prev_status | 否 |  |  |
| 14 | confirm_amount | 否 |  |  |
| 15 | seat_no | 否 |  |  |
| 16 | report_account | 否 |  |  |
| 17 | join_stock_account | 否 |  |  |
| 18 | join_report_account | 否 |  |  |
| 19 | join_seat_no | 否 |  |  |
| 20 | fare_rate | 否 |  |  |
| 21 | entrust_date | 否 |  |  |
| 22 | entrust_time | 否 |  |  |
| 23 | entrust_no | 否 |  |  |
| 24 | entrust_operator | 否 |  |  |
| 25 | remark | 否 |  |  |
| 26 | report_date | 否 |  |  |
| 27 | unfrozen_amount | 否 |  |  |
| 28 | position_str | 否 |  | branch_no(5)+exchange_type(4)+stock_account(10)+stock_code(6 |
| 29 | client_name | 否 | H |  |
| 30 | corp_client_group | 否 | H |  |
| 31 | branch_no | 否 | H |  |
| 32 | client_group | 否 | H |  |
| 33 | room_code | 否 | H |  |
| 34 | asset_prop | 否 | H |  |
| 35 | limit_flag | 否 | H |  |
| 36 | client_prop | 否 | H |  |
| 37 | asset_level | 否 | H |  |
| 38 | risk_level | 否 | H |  |
| 39 | corp_risk_level | 否 | H |  |
| 40 | stock_type | 否 | H |  |
| 41 | stock_name | 否 | H |  |
| 42 | sub_stock_type | 否 | H |  |
| 43 | init_date | 否 |  |  |
| 44 | fund_account | 否 |  |  |
| 45 | stock_account | 否 |  |  |
| 46 | client_id | 否 |  |  |
| 47 | exchange_type | 否 |  |  |
| 48 | stock_code | 否 |  |  |
| 49 | component_code | 否 |  |  |
| 50 | component_name | 否 |  |  |
| 51 | money_type | 否 |  |  |
| 52 | operator_no | 否 |  |  |
| 53 | entrust_amount | 否 |  |  |
| 54 | entrust_status | 否 |  |  |
| 55 | prev_status | 否 |  |  |
| 56 | confirm_amount | 否 |  |  |
| 57 | seat_no | 否 |  |  |
| 58 | report_account | 否 |  |  |
| 59 | join_stock_account | 否 |  |  |
| 60 | join_report_account | 否 |  |  |
| 61 | join_seat_no | 否 |  |  |
| 62 | fare_rate | 否 |  |  |
| 63 | entrust_date | 否 |  |  |
| 64 | entrust_time | 否 |  |  |
| 65 | entrust_no | 否 |  |  |
| 66 | entrust_operator | 否 |  |  |
| 67 | remark | 否 |  |  |
| 68 | report_date | 否 |  |  |
| 69 | unfrozen_amount | 否 |  |  |
| 70 | position_str | 否 |  | branch_no(5)+exchange_type(4)+stock_account(10)+stock_code(6 |
| 71 | client_name | 否 | H |  |
| 72 | corp_client_group | 否 | H |  |
| 73 | branch_no | 否 | H |  |
| 74 | client_group | 否 | H |  |
| 75 | room_code | 否 | H |  |
| 76 | asset_prop | 否 | H |  |
| 77 | limit_flag | 否 | H |  |
| 78 | client_prop | 否 | H |  |
| 79 | asset_level | 否 | H |  |
| 80 | risk_level | 否 | H |  |
| 81 | corp_risk_level | 否 | H |  |
| 82 | stock_type | 否 | H |  |
| 83 | stock_name | 否 | H |  |
| 84 | sub_stock_type | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_etf_ustock | 默认 | 否 | fund_account, stock_account, stock_code, component_code, fund_account, stock_account, stock_code, component_code |
| idx_etf_ustock | ART | 是 | fund_account, stock_account, stock_code, component_code, fund_account, stock_account, stock_code, component_code |
| idx_etf_ustock_id | ART | 是 | client_id, client_id |
| idx_etf_ustock_pos | ART | 是 | position_str, position_str |
| uk_rpt_etfustock | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_etfustock_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_etfustock_tolast | ART | 是 | report_date, report_date |
| idx_etf_ustock | 默认 | 否 | fund_account, stock_account, stock_code, component_code, fund_account, stock_account, stock_code, component_code |
| idx_etf_ustock | ART | 是 | fund_account, stock_account, stock_code, component_code, fund_account, stock_account, stock_code, component_code |
| idx_etf_ustock_id | ART | 是 | client_id, client_id |
| idx_etf_ustock_pos | ART | 是 | position_str, position_str |
| uk_rpt_etfustock | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_etfustock_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_etfustock_tolast | ART | 是 | report_date, report_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_etf_ustock | fund_account, stock_account, stock_code, component_code, fund_account, stock_account, stock_code, component_code |
| idx_etf_ustock | fund_account, stock_account, stock_code, component_code, fund_account, stock_account, stock_code, component_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:52:00 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-07-18 16:23:25 | V3.0.2.59 | 钟兆星 | 删除索引idx_etf_ustock_stk |
| 2024-12-27 14:28:13 | 3.0.2.28 | 李江霖 | 增加position_str的备注 |
| 2024-07-04 13:19:41 | 3.0.2.27 | 谢宗艺 | 物理表etf_ustock，删除了表字段(branch_no);
物理表etf_ustock，删除了表字段(stock... |
| 2023-12-17 20:30:07 | 3.0.0.176 | 全春辉 | 物理表增加索引 |
| 2026-03-09 13:52:00 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-07-18 16:23:25 | V3.0.2.59 | 钟兆星 | 删除索引idx_etf_ustock_stk |
| 2024-12-27 14:28:13 | 3.0.2.28 | 李江霖 | 增加position_str的备注 |
| 2024-07-04 13:19:41 | 3.0.2.27 | 谢宗艺 | 物理表etf_ustock，删除了表字段(branch_no);
物理表etf_ustock，删除了表字段(stock... |
| 2023-12-17 20:30:07 | 3.0.0.176 | 全春辉 | 物理表增加索引 |

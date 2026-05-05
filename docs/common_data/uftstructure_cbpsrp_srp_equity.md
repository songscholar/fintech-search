# srp_equity - 股票质押权益表

**表对象ID**: 2610
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 70 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | contract_id | 否 |  |  |
| 3 | srp_equity_type | 否 |  |  |
| 4 | branch_no | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | stock_type | 否 |  |  |
| 11 | money_type | 否 |  |  |
| 12 | register_amount | 否 |  |  |
| 13 | bonus_amount | 否 |  |  |
| 14 | bonus_balance | 否 |  |  |
| 15 | orig_entrust_date | 否 |  |  |
| 16 | orig_entrust_no | 否 |  |  |
| 17 | entrust_date | 否 |  |  |
| 18 | entrust_no | 否 |  |  |
| 19 | deal_status | 否 |  |  |
| 20 | date_clear | 否 |  |  |
| 21 | date_back | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 24 | client_name | 否 | H |  |
| 25 | corp_client_group | 否 | H |  |
| 26 | client_group | 否 | H |  |
| 27 | room_code | 否 | H |  |
| 28 | asset_prop | 否 | H |  |
| 29 | limit_flag | 否 | H |  |
| 30 | client_prop | 否 | H |  |
| 31 | asset_level | 否 | H |  |
| 32 | risk_level | 否 | H |  |
| 33 | corp_risk_level | 否 | H |  |
| 34 | stock_name | 否 | H |  |
| 35 | sub_stock_type | 否 | H |  |
| 36 | init_date | 否 |  |  |
| 37 | contract_id | 否 |  |  |
| 38 | srp_equity_type | 否 |  |  |
| 39 | branch_no | 否 |  |  |
| 40 | fund_account | 否 |  |  |
| 41 | client_id | 否 |  |  |
| 42 | stock_account | 否 |  |  |
| 43 | exchange_type | 否 |  |  |
| 44 | stock_code | 否 |  |  |
| 45 | stock_type | 否 |  |  |
| 46 | money_type | 否 |  |  |
| 47 | register_amount | 否 |  |  |
| 48 | bonus_amount | 否 |  |  |
| 49 | bonus_balance | 否 |  |  |
| 50 | orig_entrust_date | 否 |  |  |
| 51 | orig_entrust_no | 否 |  |  |
| 52 | entrust_date | 否 |  |  |
| 53 | entrust_no | 否 |  |  |
| 54 | deal_status | 否 |  |  |
| 55 | date_clear | 否 |  |  |
| 56 | date_back | 否 |  |  |
| 57 | remark | 否 |  |  |
| 58 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 59 | client_name | 否 | H |  |
| 60 | corp_client_group | 否 | H |  |
| 61 | client_group | 否 | H |  |
| 62 | room_code | 否 | H |  |
| 63 | asset_prop | 否 | H |  |
| 64 | limit_flag | 否 | H |  |
| 65 | client_prop | 否 | H |  |
| 66 | asset_level | 否 | H |  |
| 67 | risk_level | 否 | H |  |
| 68 | corp_risk_level | 否 | H |  |
| 69 | stock_name | 否 | H |  |
| 70 | sub_stock_type | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpequity | ART | 是 | init_date, contract_id, srp_equity_type, init_date, contract_id, srp_equity_type |
| idx_srpequity_acct | ART | 是 | fund_account, fund_account |
| idx_srpequity_id | ART | 是 | client_id, client_id |
| idx_srpequity_pos | ART | 是 | position_str, position_str |
| uk_rpt_srpequity | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpequity_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_srpequity_tolast | ART | 是 | date_clear, date_clear |
| idx_srpequity | ART | 是 | init_date, contract_id, srp_equity_type, init_date, contract_id, srp_equity_type |
| idx_srpequity_acct | ART | 是 | fund_account, fund_account |
| idx_srpequity_id | ART | 是 | client_id, client_id |
| idx_srpequity_pos | ART | 是 | position_str, position_str |
| uk_rpt_srpequity | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpequity_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_srpequity_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpequity_pos | position_str, position_str |
| idx_srpequity_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:47:55 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:22:00 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:47:55 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:22:00 | 3.0.3.1 | wuxd | 新增 |

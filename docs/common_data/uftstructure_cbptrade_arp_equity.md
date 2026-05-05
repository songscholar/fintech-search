# arp_equity - 约定购回权益表

**表对象ID**: 2506
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 72 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | contract_id | 否 |  |  |
| 3 | arp_equity_type | 否 |  |  |
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
| 22 | report_id | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | position_str | 否 |  | branch_no(5)+contract_id(16) |
| 25 | client_name | 否 | H |  |
| 26 | corp_client_group | 否 | H |  |
| 27 | client_group | 否 | H |  |
| 28 | room_code | 否 | H |  |
| 29 | asset_prop | 否 | H |  |
| 30 | limit_flag | 否 | H |  |
| 31 | client_prop | 否 | H |  |
| 32 | asset_level | 否 | H |  |
| 33 | risk_level | 否 | H |  |
| 34 | corp_risk_level | 否 | H |  |
| 35 | stock_name | 否 | H |  |
| 36 | sub_stock_type | 否 | H |  |
| 37 | init_date | 否 |  |  |
| 38 | contract_id | 否 |  |  |
| 39 | arp_equity_type | 否 |  |  |
| 40 | branch_no | 否 |  |  |
| 41 | fund_account | 否 |  |  |
| 42 | client_id | 否 |  |  |
| 43 | stock_account | 否 |  |  |
| 44 | exchange_type | 否 |  |  |
| 45 | stock_code | 否 |  |  |
| 46 | stock_type | 否 |  |  |
| 47 | money_type | 否 |  |  |
| 48 | register_amount | 否 |  |  |
| 49 | bonus_amount | 否 |  |  |
| 50 | bonus_balance | 否 |  |  |
| 51 | orig_entrust_date | 否 |  |  |
| 52 | orig_entrust_no | 否 |  |  |
| 53 | entrust_date | 否 |  |  |
| 54 | entrust_no | 否 |  |  |
| 55 | deal_status | 否 |  |  |
| 56 | date_clear | 否 |  |  |
| 57 | date_back | 否 |  |  |
| 58 | report_id | 否 |  |  |
| 59 | remark | 否 |  |  |
| 60 | position_str | 否 |  | branch_no(5)+contract_id(16) |
| 61 | client_name | 否 | H |  |
| 62 | corp_client_group | 否 | H |  |
| 63 | client_group | 否 | H |  |
| 64 | room_code | 否 | H |  |
| 65 | asset_prop | 否 | H |  |
| 66 | limit_flag | 否 | H |  |
| 67 | client_prop | 否 | H |  |
| 68 | asset_level | 否 | H |  |
| 69 | risk_level | 否 | H |  |
| 70 | corp_risk_level | 否 | H |  |
| 71 | stock_name | 否 | H |  |
| 72 | sub_stock_type | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arpequity | ART | 是 | contract_id, arp_equity_type, contract_id, arp_equity_type |
| idx_arpequity_id | ART | 是 | client_id, client_id |
| idx_arpequity_acct | ART | 是 | fund_account, fund_account |
| idx_arpequity_pos | ART | 是 | position_str, position_str |
| uk_rpt_arpequity | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_arpequity_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_arpequity_tolast | ART | 是 | date_clear, date_clear |
| idx_arpequity | ART | 是 | contract_id, arp_equity_type, contract_id, arp_equity_type |
| idx_arpequity_id | ART | 是 | client_id, client_id |
| idx_arpequity_acct | ART | 是 | fund_account, fund_account |
| idx_arpequity_pos | ART | 是 | position_str, position_str |
| uk_rpt_arpequity | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_arpequity_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_arpequity_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_arpequity | contract_id, arp_equity_type, contract_id, arp_equity_type |
| idx_arpequity | contract_id, arp_equity_type, contract_id, arp_equity_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:49:27 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-06 16:02:47 | V3.0.2.1009 | 黄积冲 | 新增表 |
| 2026-03-04 15:49:27 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-06 16:02:47 | V3.0.2.1009 | 黄积冲 | 新增表 |

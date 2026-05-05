# bid_contract - 分销认购合同表

**表对象ID**: 5993
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 80 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | op_entrust_way | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | client_id | 否 |  |  |
| 8 | stock_account | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | relative_code | 否 |  |  |
| 12 | money_type | 否 |  |  |
| 13 | contract_id | 否 |  |  |
| 14 | bid_contract_status | 否 |  |  |
| 15 | bid_type | 否 |  |  |
| 16 | bid_rate | 否 |  |  |
| 17 | entrust_amount | 否 |  |  |
| 18 | entrust_balance | 否 |  |  |
| 19 | bid_balance | 否 |  |  |
| 20 | distribute_type | 否 |  |  |
| 21 | winning_rate | 否 |  |  |
| 22 | winning_balance | 否 |  |  |
| 23 | execute_stage | 否 |  |  |
| 24 | date_clear | 否 |  |  |
| 25 | remark | 否 |  |  |
| 26 | position_str | 否 |  |  |
| 27 | bid_frozen_balance | 否 |  |  |
| 28 | client_name | 否 | H |  |
| 29 | corp_client_group | 否 | H |  |
| 30 | client_group | 否 | H |  |
| 31 | room_code | 否 | H |  |
| 32 | asset_prop | 否 | H |  |
| 33 | limit_flag | 否 | H |  |
| 34 | client_prop | 否 | H |  |
| 35 | asset_level | 否 | H |  |
| 36 | risk_level | 否 | H |  |
| 37 | corp_risk_level | 否 | H |  |
| 38 | stock_name | 否 | H |  |
| 39 | stock_type | 否 | H |  |
| 40 | sub_stock_type | 否 | H |  |
| 41 | init_date | 否 |  |  |
| 42 | curr_date | 否 |  |  |
| 43 | curr_time | 否 |  |  |
| 44 | op_entrust_way | 否 |  |  |
| 45 | branch_no | 否 |  |  |
| 46 | fund_account | 否 |  |  |
| 47 | client_id | 否 |  |  |
| 48 | stock_account | 否 |  |  |
| 49 | exchange_type | 否 |  |  |
| 50 | stock_code | 否 |  |  |
| 51 | relative_code | 否 |  |  |
| 52 | money_type | 否 |  |  |
| 53 | contract_id | 否 |  |  |
| 54 | bid_contract_status | 否 |  |  |
| 55 | bid_type | 否 |  |  |
| 56 | bid_rate | 否 |  |  |
| 57 | entrust_amount | 否 |  |  |
| 58 | entrust_balance | 否 |  |  |
| 59 | bid_balance | 否 |  |  |
| 60 | distribute_type | 否 |  |  |
| 61 | winning_rate | 否 |  |  |
| 62 | winning_balance | 否 |  |  |
| 63 | execute_stage | 否 |  |  |
| 64 | date_clear | 否 |  |  |
| 65 | remark | 否 |  |  |
| 66 | position_str | 否 |  |  |
| 67 | bid_frozen_balance | 否 |  |  |
| 68 | client_name | 否 | H |  |
| 69 | corp_client_group | 否 | H |  |
| 70 | client_group | 否 | H |  |
| 71 | room_code | 否 | H |  |
| 72 | asset_prop | 否 | H |  |
| 73 | limit_flag | 否 | H |  |
| 74 | client_prop | 否 | H |  |
| 75 | asset_level | 否 | H |  |
| 76 | risk_level | 否 | H |  |
| 77 | corp_risk_level | 否 | H |  |
| 78 | stock_name | 否 | H |  |
| 79 | stock_type | 否 | H |  |
| 80 | sub_stock_type | 否 | H |  |

## 索引（共 24 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_bid_contract | 默认 | 否 |  |
| idx_bid_contract_acct | 默认 | 否 |  |
| idx_bid_contract_id | 默认 | 否 |  |
| idx_bid_contract_pos | 默认 | 否 |  |
| idx_bid_contract | 默认 | 否 | contract_id, contract_id |
| idx_bid_contract | ART | 是 | contract_id, contract_id |
| idx_bid_contract_acct | ART | 是 | fund_account, fund_account |
| idx_bid_contract_id | ART | 是 | client_id, client_id |
| idx_bid_contract_pos | ART | 是 | position_str, position_str |
| uk_rpt_bidcontract | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_bidcontract_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_bidcontract_tolast | ART | 是 | date_clear, date_clear |
| idx_bid_contract | 默认 | 否 |  |
| idx_bid_contract_acct | 默认 | 否 |  |
| idx_bid_contract_id | 默认 | 否 |  |
| idx_bid_contract_pos | 默认 | 否 |  |
| idx_bid_contract | 默认 | 否 | contract_id, contract_id |
| idx_bid_contract | ART | 是 | contract_id, contract_id |
| idx_bid_contract_acct | ART | 是 | fund_account, fund_account |
| idx_bid_contract_id | ART | 是 | client_id, client_id |
| idx_bid_contract_pos | ART | 是 | position_str, position_str |
| uk_rpt_bidcontract | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_bidcontract_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_bidcontract_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_bid_contract | contract_id, contract_id |
| idx_bid_contract | contract_id, contract_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:55:43 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-12-01 16:18:51 | 3.0.2.105 | taocong45644 | 当前表bid_contract，修改了索引idx_bid_contract,索引字段修改为：(contract_id),... |
| 2025-04-19 17:01:59 | 3.0.6.23 | 陈键中 |  |
| 2023-12-17 20:30:07 | 3.0.1.18 | 全春辉 | 物理表增加索引 |
| 2026-03-09 14:55:43 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-12-01 16:18:51 | 3.0.2.105 | taocong45644 | 当前表bid_contract，修改了索引idx_bid_contract,索引字段修改为：(contract_id),... |
| 2025-04-19 17:01:59 | 3.0.6.23 | 陈键中 |  |
| 2023-12-17 20:30:07 | 3.0.1.18 | 全春辉 | 物理表增加索引 |

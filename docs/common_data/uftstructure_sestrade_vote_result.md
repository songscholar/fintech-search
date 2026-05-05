# vote_result - 投票结果明细表

**表对象ID**: 2582
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 90 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | company_name | 否 |  |  |
| 3 | meeting_seq | 否 |  |  |
| 4 | company_code | 否 |  |  |
| 5 | begin_date | 否 |  |  |
| 6 | end_date | 否 |  |  |
| 7 | meeting_type | 否 |  |  |
| 8 | meeting_name | 否 |  |  |
| 9 | register_date | 否 |  |  |
| 10 | last_trade_date | 否 |  |  |
| 11 | stock_name | 否 |  |  |
| 12 | vote_info | 否 |  |  |
| 13 | vote_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | fund_account | 否 |  |  |
| 17 | stock_account | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | business_amount | 否 |  |  |
| 20 | business_price | 否 |  |  |
| 21 | business_date | 否 |  |  |
| 22 | business_time | 否 |  |  |
| 23 | withdraw_reason | 否 |  |  |
| 24 | spare_flag | 否 |  |  |
| 25 | remark | 否 |  |  |
| 26 | position_str | 否 |  |  |
| 27 | placard_id | 否 |  |  |
| 28 | motion_id | 否 |  |  |
| 29 | approve_amount | 否 |  |  |
| 30 | oppose_amount | 否 |  |  |
| 31 | waive_amount | 否 |  |  |
| 32 | rej_reason | 否 |  |  |
| 33 | client_name | 否 | H |  |
| 34 | corp_client_group | 否 | H |  |
| 35 | branch_no | 否 | H |  |
| 36 | client_group | 否 | H |  |
| 37 | room_code | 否 | H |  |
| 38 | asset_prop | 否 | H |  |
| 39 | limit_flag | 否 | H |  |
| 40 | client_prop | 否 | H |  |
| 41 | asset_level | 否 | H |  |
| 42 | risk_level | 否 | H |  |
| 43 | corp_risk_level | 否 | H |  |
| 44 | stock_type | 否 | H |  |
| 45 | sub_stock_type | 否 | H |  |
| 46 | init_date | 否 |  |  |
| 47 | company_name | 否 |  |  |
| 48 | meeting_seq | 否 |  |  |
| 49 | company_code | 否 |  |  |
| 50 | begin_date | 否 |  |  |
| 51 | end_date | 否 |  |  |
| 52 | meeting_type | 否 |  |  |
| 53 | meeting_name | 否 |  |  |
| 54 | register_date | 否 |  |  |
| 55 | last_trade_date | 否 |  |  |
| 56 | stock_name | 否 |  |  |
| 57 | vote_info | 否 |  |  |
| 58 | vote_type | 否 |  |  |
| 59 | stock_code | 否 |  |  |
| 60 | client_id | 否 |  |  |
| 61 | fund_account | 否 |  |  |
| 62 | stock_account | 否 |  |  |
| 63 | exchange_type | 否 |  |  |
| 64 | business_amount | 否 |  |  |
| 65 | business_price | 否 |  |  |
| 66 | business_date | 否 |  |  |
| 67 | business_time | 否 |  |  |
| 68 | withdraw_reason | 否 |  |  |
| 69 | spare_flag | 否 |  |  |
| 70 | remark | 否 |  |  |
| 71 | position_str | 否 |  |  |
| 72 | placard_id | 否 |  |  |
| 73 | motion_id | 否 |  |  |
| 74 | approve_amount | 否 |  |  |
| 75 | oppose_amount | 否 |  |  |
| 76 | waive_amount | 否 |  |  |
| 77 | rej_reason | 否 |  |  |
| 78 | client_name | 否 | H |  |
| 79 | corp_client_group | 否 | H |  |
| 80 | branch_no | 否 | H |  |
| 81 | client_group | 否 | H |  |
| 82 | room_code | 否 | H |  |
| 83 | asset_prop | 否 | H |  |
| 84 | limit_flag | 否 | H |  |
| 85 | client_prop | 否 | H |  |
| 86 | asset_level | 否 | H |  |
| 87 | risk_level | 否 | H |  |
| 88 | corp_risk_level | 否 | H |  |
| 89 | stock_type | 否 | H |  |
| 90 | sub_stock_type | 否 | H |  |

## 索引（共 20 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_vote_result | 默认 | 否 |  |
| idx_vote_result_acct | 默认 | 否 |  |
| idx_vote_result_code | 默认 | 否 |  |
| idx_vote_result | 默认 | 否 | position_str, position_str |
| idx_vote_result | ART | 是 | position_str, position_str |
| idx_vote_result_acct | ART | 是 | fund_account, fund_account |
| idx_vote_result_code | ART | 是 | exchange_type, company_code, exchange_type, company_code |
| uk_rpt_voteresult | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_voteresult_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_voteresult_tolast | ART | 是 | end_date, end_date |
| idx_vote_result | 默认 | 否 |  |
| idx_vote_result_acct | 默认 | 否 |  |
| idx_vote_result_code | 默认 | 否 |  |
| idx_vote_result | 默认 | 否 | position_str, position_str |
| idx_vote_result | ART | 是 | position_str, position_str |
| idx_vote_result_acct | ART | 是 | fund_account, fund_account |
| idx_vote_result_code | ART | 是 | exchange_type, company_code, exchange_type, company_code |
| uk_rpt_voteresult | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_voteresult_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_voteresult_tolast | ART | 是 | end_date, end_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_vote_result | position_str, position_str |
| idx_vote_result | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 11:00:47 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-04 12:05:58 | 3.0.1.11 | 洪略 | 补齐资源 |
| 2025-12-01 16:53:41 | 3.0.2.104 | taocong45644 | 当前表vote_result，修改了索引idx_vote_result,索引字段修改为：(position_str),索... |
| 2023-12-18 10:30:07 | 3.0.1.11 | 全春辉 | 物理表增加索引 |
| 2026-03-09 11:00:47 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-04 12:05:58 | 3.0.1.11 | 洪略 | 补齐资源 |
| 2025-12-01 16:53:41 | 3.0.2.104 | taocong45644 | 当前表vote_result，修改了索引idx_vote_result,索引字段修改为：(position_str),索... |
| 2023-12-18 10:30:07 | 3.0.1.11 | 全春辉 | 物理表增加索引 |

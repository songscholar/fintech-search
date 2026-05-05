# uref_borrowcompact_jour - 转融通借入合约变更流水表

**表对象ID**: 6106
**所属模块**: reftrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 82 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | operator_no | 否 |  |  |
| 5 | op_branch_no | 否 |  |  |
| 6 | op_entrust_way | 否 |  |  |
| 7 | op_station | 否 |  |  |
| 8 | serial_no | 否 |  |  |
| 9 | business_flag | 否 |  |  |
| 10 | compact_id | 否 |  |  |
| 11 | csfc_compact_id | 否 |  |  |
| 12 | company_no | 否 |  |  |
| 13 | branch_no | 否 |  |  |
| 14 | fund_account | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | exchange_type | 否 |  |  |
| 17 | stock_account | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | money_type | 否 |  |  |
| 20 | occur_amount | 否 |  |  |
| 21 | post_amount | 否 |  |  |
| 22 | occur_balance | 否 |  |  |
| 23 | post_balance | 否 |  |  |
| 24 | remark | 否 |  |  |
| 25 | position_str | 否 |  |  |
| 26 | counter_belonged | 否 |  |  |
| 27 | csfc_borrow_accttype | 否 |  |  |
| 28 | refcompact_source | 否 |  |  |
| 29 | client_group | 否 | H |  |
| 30 | room_code | 否 | H |  |
| 31 | asset_prop | 否 | H |  |
| 32 | limit_flag | 否 | H |  |
| 33 | client_prop | 否 | H |  |
| 34 | risk_level | 否 | H |  |
| 35 | corp_client_group | 否 | H |  |
| 36 | corp_risk_level | 否 | H |  |
| 37 | asset_level | 否 | H |  |
| 38 | client_name | 否 | H |  |
| 39 | stock_name | 否 | H |  |
| 40 | sub_stock_type | 否 | H |  |
| 41 | stock_type | 否 | H |  |
| 42 | init_date | 否 |  |  |
| 43 | curr_date | 否 |  |  |
| 44 | curr_time | 否 |  |  |
| 45 | operator_no | 否 |  |  |
| 46 | op_branch_no | 否 |  |  |
| 47 | op_entrust_way | 否 |  |  |
| 48 | op_station | 否 |  |  |
| 49 | serial_no | 否 |  |  |
| 50 | business_flag | 否 |  |  |
| 51 | compact_id | 否 |  |  |
| 52 | csfc_compact_id | 否 |  |  |
| 53 | company_no | 否 |  |  |
| 54 | branch_no | 否 |  |  |
| 55 | fund_account | 否 |  |  |
| 56 | client_id | 否 |  |  |
| 57 | exchange_type | 否 |  |  |
| 58 | stock_account | 否 |  |  |
| 59 | stock_code | 否 |  |  |
| 60 | money_type | 否 |  |  |
| 61 | occur_amount | 否 |  |  |
| 62 | post_amount | 否 |  |  |
| 63 | occur_balance | 否 |  |  |
| 64 | post_balance | 否 |  |  |
| 65 | remark | 否 |  |  |
| 66 | position_str | 否 |  |  |
| 67 | counter_belonged | 否 |  |  |
| 68 | csfc_borrow_accttype | 否 |  |  |
| 69 | refcompact_source | 否 |  |  |
| 70 | client_group | 否 | H |  |
| 71 | room_code | 否 | H |  |
| 72 | asset_prop | 否 | H |  |
| 73 | limit_flag | 否 | H |  |
| 74 | client_prop | 否 | H |  |
| 75 | risk_level | 否 | H |  |
| 76 | corp_client_group | 否 | H |  |
| 77 | corp_risk_level | 否 | H |  |
| 78 | asset_level | 否 | H |  |
| 79 | client_name | 否 | H |  |
| 80 | stock_name | 否 | H |  |
| 81 | sub_stock_type | 否 | H |  |
| 82 | stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refbcompactjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_refbcompactjour_acct | ART | 是 | fund_account, fund_account |
| idx_refbcompactjour_pos | ART | 是 | position_str, position_str |
| idx_refbcompactjour_comp | ART | 是 | compact_id, compact_id |
| idx_refbcompactjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_refbcompactjour_acct | ART | 是 | fund_account, fund_account |
| idx_refbcompactjour_pos | ART | 是 | position_str, position_str |
| idx_refbcompactjour_comp | ART | 是 | compact_id, compact_id |

## 数据库索引（共 10 个）

| 索引名 | 字段 |
|--------|------|
| idx_refbcompactjour | serial_no, init_date, serial_no, init_date |
| uk_rpt_urefborrowcompactjour | init_date, position_str, init_date, position_str |
| idx_rpt_urefborrowcompactjour_id | client_id, position_str, client_id, position_str |
| idx_rpt_urefborrowcompactjour_acct | fund_account, position_str, fund_account, position_str |
| idx_rpt_urefborrowcompactjour_bra | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_refbcompactjour | serial_no, init_date, serial_no, init_date |
| uk_rpt_urefborrowcompactjour | init_date, position_str, init_date, position_str |
| idx_rpt_urefborrowcompactjour_id | client_id, position_str, client_id, position_str |
| idx_rpt_urefborrowcompactjour_acct | fund_account, position_str, fund_account, position_str |
| idx_rpt_urefborrowcompactjour_bra | init_date, branch_no, position_str, init_date, branch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-16 10:41:44 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-10-16 10:41:44 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

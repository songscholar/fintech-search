# uref_lendcompact_jour - 转融通出借合约变更流水表

**表对象ID**: 6108
**所属模块**: reftrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 76 个）

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
| 10 | branch_no | 否 |  |  |
| 11 | compact_id | 否 |  |  |
| 12 | csfc_compact_id | 否 |  |  |
| 13 | fund_account | 否 |  |  |
| 14 | client_id | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_account | 否 |  |  |
| 17 | stock_code | 否 |  |  |
| 18 | occur_amount | 否 |  |  |
| 19 | post_amount | 否 |  |  |
| 20 | occur_balance | 否 |  |  |
| 21 | post_balance | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | position_str | 否 |  |  |
| 24 | refsvrfare_kind | 否 |  |  |
| 25 | refcompact_source | 否 |  |  |
| 26 | client_name | 否 | H |  |
| 27 | stock_name | 否 | H |  |
| 28 | asset_prop | 否 | H |  |
| 29 | client_group | 否 | H |  |
| 30 | room_code | 否 | H |  |
| 31 | limit_flag | 否 | H |  |
| 32 | risk_level | 否 | H |  |
| 33 | corp_client_group | 否 | H |  |
| 34 | corp_risk_level | 否 | H |  |
| 35 | asset_level | 否 | H |  |
| 36 | client_prop | 否 | H |  |
| 37 | stock_type | 否 | H |  |
| 38 | sub_stock_type | 否 | H |  |
| 39 | init_date | 否 |  |  |
| 40 | curr_date | 否 |  |  |
| 41 | curr_time | 否 |  |  |
| 42 | operator_no | 否 |  |  |
| 43 | op_branch_no | 否 |  |  |
| 44 | op_entrust_way | 否 |  |  |
| 45 | op_station | 否 |  |  |
| 46 | serial_no | 否 |  |  |
| 47 | business_flag | 否 |  |  |
| 48 | branch_no | 否 |  |  |
| 49 | compact_id | 否 |  |  |
| 50 | csfc_compact_id | 否 |  |  |
| 51 | fund_account | 否 |  |  |
| 52 | client_id | 否 |  |  |
| 53 | exchange_type | 否 |  |  |
| 54 | stock_account | 否 |  |  |
| 55 | stock_code | 否 |  |  |
| 56 | occur_amount | 否 |  |  |
| 57 | post_amount | 否 |  |  |
| 58 | occur_balance | 否 |  |  |
| 59 | post_balance | 否 |  |  |
| 60 | remark | 否 |  |  |
| 61 | position_str | 否 |  |  |
| 62 | refsvrfare_kind | 否 |  |  |
| 63 | refcompact_source | 否 |  |  |
| 64 | client_name | 否 | H |  |
| 65 | stock_name | 否 | H |  |
| 66 | asset_prop | 否 | H |  |
| 67 | client_group | 否 | H |  |
| 68 | room_code | 否 | H |  |
| 69 | limit_flag | 否 | H |  |
| 70 | risk_level | 否 | H |  |
| 71 | corp_client_group | 否 | H |  |
| 72 | corp_risk_level | 否 | H |  |
| 73 | asset_level | 否 | H |  |
| 74 | client_prop | 否 | H |  |
| 75 | stock_type | 否 | H |  |
| 76 | sub_stock_type | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_reflcompactjour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_reflcompactjour_acct | ART | 是 | fund_account, fund_account |
| idx_reflcompactjour_pos | ART | 是 | position_str, position_str |
| idx_reflcompactjour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_reflcompactjour_acct | ART | 是 | fund_account, fund_account |
| idx_reflcompactjour_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 12 个）

| 索引名 | 字段 |
|--------|------|
| idx_reflcompactjour | init_date, serial_no, init_date, serial_no |
| uk_rpt_ureflendcompactjour | init_date, position_str, init_date, position_str |
| idx_rpt_ureflendcompactjour_cont | compact_id, position_str, compact_id, position_str |
| idx_rpt_ureflendcompactjour_id | client_id, position_str, client_id, position_str |
| idx_rpt_ureflendcompactjour_acct | fund_account, position_str, fund_account, position_str |
| idx_rpt_ureflendcompactjour_bra | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_reflcompactjour | init_date, serial_no, init_date, serial_no |
| uk_rpt_ureflendcompactjour | init_date, position_str, init_date, position_str |
| idx_rpt_ureflendcompactjour_cont | compact_id, position_str, compact_id, position_str |
| idx_rpt_ureflendcompactjour_id | client_id, position_str, client_id, position_str |
| idx_rpt_ureflendcompactjour_acct | fund_account, position_str, fund_account, position_str |
| idx_rpt_ureflendcompactjour_bra | init_date, branch_no, position_str, init_date, branch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-16 10:41:57 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-10-16 10:41:57 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

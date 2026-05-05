# uref_business - 转融通业务成交表

**表对象ID**: 6150
**所属模块**: refsett
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 98 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | company_no | 否 |  |  |
| 4 | business_flag | 否 |  |  |
| 5 | ref_type | 否 |  |  |
| 6 | refacct_type | 否 |  |  |
| 7 | refcompact_type | 否 |  |  |
| 8 | refsett_bs | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | client_id | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | report_no | 否 |  |  |
| 14 | entrust_no | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | seat_no | 否 |  |  |
| 18 | csfc_compact_id | 否 |  |  |
| 19 | orig_compact_id | 否 |  |  |
| 20 | orig_csfccompact_id | 否 |  |  |
| 21 | compact_amount | 否 |  |  |
| 22 | compact_balance | 否 |  |  |
| 23 | last_price | 否 |  |  |
| 24 | ref_term | 否 |  |  |
| 25 | year_rate | 否 |  |  |
| 26 | pre_interest | 否 |  |  |
| 27 | penalty_balance | 否 |  |  |
| 28 | cbp_business_id | 否 |  |  |
| 29 | cbpconfer_id | 否 |  |  |
| 30 | valid_date | 否 |  |  |
| 31 | remark | 否 |  |  |
| 32 | treat_status | 否 |  |  |
| 33 | position_str | 否 |  |  |
| 34 | refsrcgroup_id | 否 |  |  |
| 35 | batch_id | 否 |  |  |
| 36 | csfc_borrow_accttype | 否 |  |  |
| 37 | client_group | 否 | H |  |
| 38 | room_code | 否 | H |  |
| 39 | asset_prop | 否 | H |  |
| 40 | client_prop | 否 | H |  |
| 41 | limit_flag | 否 | H |  |
| 42 | client_name | 否 | H |  |
| 43 | stock_name | 否 | H |  |
| 44 | stock_type | 否 | H |  |
| 45 | sub_stock_type | 否 | H |  |
| 46 | corp_client_group | 否 | H |  |
| 47 | asset_level | 否 | H |  |
| 48 | risk_level | 否 | H |  |
| 49 | corp_risk_level | 否 | H |  |
| 50 | init_date | 否 |  |  |
| 51 | serial_no | 否 |  |  |
| 52 | company_no | 否 |  |  |
| 53 | business_flag | 否 |  |  |
| 54 | ref_type | 否 |  |  |
| 55 | refacct_type | 否 |  |  |
| 56 | refcompact_type | 否 |  |  |
| 57 | refsett_bs | 否 |  |  |
| 58 | branch_no | 否 |  |  |
| 59 | client_id | 否 |  |  |
| 60 | fund_account | 否 |  |  |
| 61 | stock_account | 否 |  |  |
| 62 | report_no | 否 |  |  |
| 63 | entrust_no | 否 |  |  |
| 64 | exchange_type | 否 |  |  |
| 65 | stock_code | 否 |  |  |
| 66 | seat_no | 否 |  |  |
| 67 | csfc_compact_id | 否 |  |  |
| 68 | orig_compact_id | 否 |  |  |
| 69 | orig_csfccompact_id | 否 |  |  |
| 70 | compact_amount | 否 |  |  |
| 71 | compact_balance | 否 |  |  |
| 72 | last_price | 否 |  |  |
| 73 | ref_term | 否 |  |  |
| 74 | year_rate | 否 |  |  |
| 75 | pre_interest | 否 |  |  |
| 76 | penalty_balance | 否 |  |  |
| 77 | cbp_business_id | 否 |  |  |
| 78 | cbpconfer_id | 否 |  |  |
| 79 | valid_date | 否 |  |  |
| 80 | remark | 否 |  |  |
| 81 | treat_status | 否 |  |  |
| 82 | position_str | 否 |  |  |
| 83 | refsrcgroup_id | 否 |  |  |
| 84 | batch_id | 否 |  |  |
| 85 | csfc_borrow_accttype | 否 |  |  |
| 86 | client_group | 否 | H |  |
| 87 | room_code | 否 | H |  |
| 88 | asset_prop | 否 | H |  |
| 89 | client_prop | 否 | H |  |
| 90 | limit_flag | 否 | H |  |
| 91 | client_name | 否 | H |  |
| 92 | stock_name | 否 | H |  |
| 93 | stock_type | 否 | H |  |
| 94 | sub_stock_type | 否 | H |  |
| 95 | corp_client_group | 否 | H |  |
| 96 | asset_level | 否 | H |  |
| 97 | risk_level | 否 | H |  |
| 98 | corp_risk_level | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refbusiness | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_refbusiness_pos | ART | 是 | position_str, position_str |
| idx_refbusiness | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_refbusiness_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 6 个）

| 索引名 | 字段 |
|--------|------|
| idx_refbusiness | init_date, serial_no, init_date, serial_no |
| idx_refbusiness_pos | position_str, position_str |
| uk_rpt_urefbusiness | init_date, position_str, init_date, position_str |
| idx_refbusiness | init_date, serial_no, init_date, serial_no |
| idx_refbusiness_pos | position_str, position_str |
| uk_rpt_urefbusiness | init_date, position_str, init_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-12 15:39:55 | V3.0.2.3 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_business，添加了表字段(corp_client_group);
... |
| 2025-10-16 10:37:45 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-12-12 15:39:55 | V3.0.2.3 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_business，添加了表字段(corp_client_group);
... |
| 2025-10-16 10:37:45 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

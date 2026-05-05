# uref_equity - 转融通权益信息表

**表对象ID**: 6154
**所属模块**: refsett
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 74 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | company_no | 否 |  |  |
| 4 | refacct_type | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | compact_id | 否 |  |  |
| 9 | csfc_compact_id | 否 |  |  |
| 10 | orig_csfccompact_id | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | equity_type | 否 |  |  |
| 14 | register_date | 否 |  |  |
| 15 | settle_date | 否 |  |  |
| 16 | recoup_bal_ratio | 否 |  |  |
| 17 | recoup_amt_ratio | 否 |  |  |
| 18 | recoup_balance | 否 |  |  |
| 19 | recoup_amount | 否 |  |  |
| 20 | compact_amount | 否 |  |  |
| 21 | remark | 否 |  |  |
| 22 | date_clear | 否 |  |  |
| 23 | position_str | 否 |  |  |
| 24 | csfc_borrow_accttype | 否 |  |  |
| 25 | client_group | 否 | H |  |
| 26 | room_code | 否 | H |  |
| 27 | asset_prop | 否 | H |  |
| 28 | client_prop | 否 | H |  |
| 29 | limit_flag | 否 | H |  |
| 30 | client_name | 否 | H |  |
| 31 | stock_name | 否 | H |  |
| 32 | stock_type | 否 | H |  |
| 33 | sub_stock_type | 否 | H |  |
| 34 | corp_client_group | 否 | H |  |
| 35 | asset_level | 否 | H |  |
| 36 | risk_level | 否 | H |  |
| 37 | corp_risk_level | 否 | H |  |
| 38 | init_date | 否 |  |  |
| 39 | serial_no | 否 |  |  |
| 40 | company_no | 否 |  |  |
| 41 | refacct_type | 否 |  |  |
| 42 | branch_no | 否 |  |  |
| 43 | client_id | 否 |  |  |
| 44 | fund_account | 否 |  |  |
| 45 | compact_id | 否 |  |  |
| 46 | csfc_compact_id | 否 |  |  |
| 47 | orig_csfccompact_id | 否 |  |  |
| 48 | exchange_type | 否 |  |  |
| 49 | stock_code | 否 |  |  |
| 50 | equity_type | 否 |  |  |
| 51 | register_date | 否 |  |  |
| 52 | settle_date | 否 |  |  |
| 53 | recoup_bal_ratio | 否 |  |  |
| 54 | recoup_amt_ratio | 否 |  |  |
| 55 | recoup_balance | 否 |  |  |
| 56 | recoup_amount | 否 |  |  |
| 57 | compact_amount | 否 |  |  |
| 58 | remark | 否 |  |  |
| 59 | date_clear | 否 |  |  |
| 60 | position_str | 否 |  |  |
| 61 | csfc_borrow_accttype | 否 |  |  |
| 62 | client_group | 否 | H |  |
| 63 | room_code | 否 | H |  |
| 64 | asset_prop | 否 | H |  |
| 65 | client_prop | 否 | H |  |
| 66 | limit_flag | 否 | H |  |
| 67 | client_name | 否 | H |  |
| 68 | stock_name | 否 | H |  |
| 69 | stock_type | 否 | H |  |
| 70 | sub_stock_type | 否 | H |  |
| 71 | corp_client_group | 否 | H |  |
| 72 | asset_level | 否 | H |  |
| 73 | risk_level | 否 | H |  |
| 74 | corp_risk_level | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refequity | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_refequity_comp | ART | 是 | csfc_compact_id, company_no, csfc_compact_id, company_no |
| idx_refequity_pos | ART | 是 | position_str, position_str |
| idx_refequity | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_refequity_comp | ART | 是 | csfc_compact_id, company_no, csfc_compact_id, company_no |
| idx_refequity_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 8 个）

| 索引名 | 字段 |
|--------|------|
| idx_refequity | serial_no, init_date, serial_no, init_date |
| idx_refequity_comp | csfc_compact_id, company_no, csfc_compact_id, company_no |
| idx_refequity_pos | position_str, position_str |
| uk_rpt_urefequity | init_date, position_str, init_date, position_str |
| idx_refequity | serial_no, init_date, serial_no, init_date |
| idx_refequity_comp | csfc_compact_id, company_no, csfc_compact_id, company_no |
| idx_refequity_pos | position_str, position_str |
| uk_rpt_urefequity | init_date, position_str, init_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-12 15:50:01 | V3.0.2.3 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_equity，添加了表字段(corp_client_group);
历史... |
| 2025-10-16 10:38:18 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-12-12 15:50:01 | V3.0.2.3 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_equity，添加了表字段(corp_client_group);
历史... |
| 2025-10-16 10:38:18 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

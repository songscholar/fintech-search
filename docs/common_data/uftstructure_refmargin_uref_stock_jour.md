# uref_stock_jour - 保证金股份流水表

**表对象ID**: 6054
**所属模块**: refmargin
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 70 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | serial_no | 否 |  |  |
| 5 | op_branch_no | 否 |  |  |
| 6 | operator_no | 否 |  |  |
| 7 | op_station | 否 |  |  |
| 8 | company_no | 否 |  |  |
| 9 | report_no | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | client_id | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | stock_type | 否 |  |  |
| 16 | exchange_type | 否 |  |  |
| 17 | money_type | 否 |  |  |
| 18 | refbusi_code | 否 |  |  |
| 19 | occur_amount | 否 |  |  |
| 20 | post_amount | 否 |  |  |
| 21 | remark | 否 |  |  |
| 22 | position_str | 否 |  |  |
| 23 | csfc_borrow_accttype | 否 |  |  |
| 24 | client_group | 否 | H |  |
| 25 | room_code | 否 | H |  |
| 26 | asset_prop | 否 | H |  |
| 27 | limit_flag | 否 | H |  |
| 28 | client_prop | 否 | H |  |
| 29 | risk_level | 否 | H |  |
| 30 | corp_client_group | 否 | H |  |
| 31 | asset_level | 否 | H |  |
| 32 | client_name | 否 | H |  |
| 33 | stock_name | 否 | H |  |
| 34 | sub_stock_type | 否 | H |  |
| 35 | corp_risk_level | 否 | H |  |
| 36 | init_date | 否 |  |  |
| 37 | curr_date | 否 |  |  |
| 38 | curr_time | 否 |  |  |
| 39 | serial_no | 否 |  |  |
| 40 | op_branch_no | 否 |  |  |
| 41 | operator_no | 否 |  |  |
| 42 | op_station | 否 |  |  |
| 43 | company_no | 否 |  |  |
| 44 | report_no | 否 |  |  |
| 45 | branch_no | 否 |  |  |
| 46 | fund_account | 否 |  |  |
| 47 | client_id | 否 |  |  |
| 48 | stock_account | 否 |  |  |
| 49 | stock_code | 否 |  |  |
| 50 | stock_type | 否 |  |  |
| 51 | exchange_type | 否 |  |  |
| 52 | money_type | 否 |  |  |
| 53 | refbusi_code | 否 |  |  |
| 54 | occur_amount | 否 |  |  |
| 55 | post_amount | 否 |  |  |
| 56 | remark | 否 |  |  |
| 57 | position_str | 否 |  |  |
| 58 | csfc_borrow_accttype | 否 |  |  |
| 59 | client_group | 否 | H |  |
| 60 | room_code | 否 | H |  |
| 61 | asset_prop | 否 | H |  |
| 62 | limit_flag | 否 | H |  |
| 63 | client_prop | 否 | H |  |
| 64 | risk_level | 否 | H |  |
| 65 | corp_client_group | 否 | H |  |
| 66 | asset_level | 否 | H |  |
| 67 | client_name | 否 | H |  |
| 68 | stock_name | 否 | H |  |
| 69 | sub_stock_type | 否 | H |  |
| 70 | corp_risk_level | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refstockjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_refstockjour_id | ART | 是 | client_id, client_id |
| idx_refstockjour_acct | ART | 是 | fund_account, fund_account |
| idx_refstockjour_pos | ART | 是 | position_str, position_str |
| idx_refstockjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_refstockjour_id | ART | 是 | client_id, client_id |
| idx_refstockjour_acct | ART | 是 | fund_account, fund_account |
| idx_refstockjour_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 10 个）

| 索引名 | 字段 |
|--------|------|
| idx_refstockjour | serial_no, init_date, serial_no, init_date |
| uk_rpt_urefstockjour | init_date, position_str, init_date, position_str |
| idx_rpt_urefstockjour_id | client_id, position_str, client_id, position_str |
| idx_rpt_urefstockjour_acct | fund_account, position_str, fund_account, position_str |
| idx_rpt_urefstockjour_comp | init_date, company_no, position_str, init_date, company_no, position_str |
| idx_refstockjour | serial_no, init_date, serial_no, init_date |
| uk_rpt_urefstockjour | init_date, position_str, init_date, position_str |
| idx_rpt_urefstockjour_id | client_id, position_str, client_id, position_str |
| idx_rpt_urefstockjour_acct | fund_account, position_str, fund_account, position_str |
| idx_rpt_urefstockjour_comp | init_date, company_no, position_str, init_date, company_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-12 16:39:33 | V3.0.2.4 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_stock_jour，添加了表字段(corp_risk_level);
 |
| 2025-10-16 10:35:05 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-12-12 16:39:33 | V3.0.2.4 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_stock_jour，添加了表字段(corp_risk_level);
 |
| 2025-10-16 10:35:05 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

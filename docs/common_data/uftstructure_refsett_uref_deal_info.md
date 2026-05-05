# uref_deal_info - 转融通成交信息表

**表对象ID**: 6168
**所属模块**: refsett
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 50 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | company_no | 否 |  |  |
| 4 | refacct_type | 否 |  |  |
| 5 | report_date | 否 |  |  |
| 6 | refbusi_code | 否 |  |  |
| 7 | report_no | 否 |  |  |
| 8 | money_type | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | stock_account | 否 |  |  |
| 12 | entrust_amount | 否 |  |  |
| 13 | entrust_balance | 否 |  |  |
| 14 | ref_term | 否 |  |  |
| 15 | year_rate | 否 |  |  |
| 16 | cbpconfer_id | 否 |  |  |
| 17 | csfc_report_status | 否 |  |  |
| 18 | business_amount | 否 |  |  |
| 19 | business_balance | 否 |  |  |
| 20 | remark | 否 |  |  |
| 21 | position_str | 否 |  |  |
| 22 | csfc_borrow_accttype | 否 |  |  |
| 23 | stock_name | 否 | H |  |
| 24 | stock_type | 否 | H |  |
| 25 | sub_stock_type | 否 | H |  |
| 26 | init_date | 否 |  |  |
| 27 | serial_no | 否 |  |  |
| 28 | company_no | 否 |  |  |
| 29 | refacct_type | 否 |  |  |
| 30 | report_date | 否 |  |  |
| 31 | refbusi_code | 否 |  |  |
| 32 | report_no | 否 |  |  |
| 33 | money_type | 否 |  |  |
| 34 | exchange_type | 否 |  |  |
| 35 | stock_code | 否 |  |  |
| 36 | stock_account | 否 |  |  |
| 37 | entrust_amount | 否 |  |  |
| 38 | entrust_balance | 否 |  |  |
| 39 | ref_term | 否 |  |  |
| 40 | year_rate | 否 |  |  |
| 41 | cbpconfer_id | 否 |  |  |
| 42 | csfc_report_status | 否 |  |  |
| 43 | business_amount | 否 |  |  |
| 44 | business_balance | 否 |  |  |
| 45 | remark | 否 |  |  |
| 46 | position_str | 否 |  |  |
| 47 | csfc_borrow_accttype | 否 |  |  |
| 48 | stock_name | 否 | H |  |
| 49 | stock_type | 否 | H |  |
| 50 | sub_stock_type | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refdealinfo | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_refdealinfo_pos | ART | 是 | position_str, position_str |
| idx_refdealinfo | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_refdealinfo_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 6 个）

| 索引名 | 字段 |
|--------|------|
| idx_refdealinfo | init_date, serial_no, init_date, serial_no |
| idx_refdealinfo_pos | position_str, position_str |
| uk_rpt_urefdealinfo | init_date, position_str, init_date, position_str |
| idx_refdealinfo | init_date, serial_no, init_date, serial_no |
| idx_refdealinfo_pos | position_str, position_str |
| uk_rpt_urefdealinfo | init_date, position_str, init_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-16 10:39:58 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-10-16 10:39:58 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

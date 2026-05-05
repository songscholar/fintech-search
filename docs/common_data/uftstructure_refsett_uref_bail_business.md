# uref_bail_business - 保证金业务成交表

**表对象ID**: 6151
**所属模块**: refsett
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 94 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | settle_date | 否 |  |  |
| 3 | serial_no | 否 |  |  |
| 4 | company_no | 否 |  |  |
| 5 | business_flag | 否 |  |  |
| 6 | refbusi_code | 否 |  |  |
| 7 | cbp_business_id | 否 |  |  |
| 8 | branch_no | 否 |  |  |
| 9 | client_id | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | stock_account | 否 |  |  |
| 12 | entrust_no | 否 |  |  |
| 13 | entrust_date | 否 |  |  |
| 14 | money_type | 否 |  |  |
| 15 | entrust_amount | 否 |  |  |
| 16 | entrust_balance | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | occur_amount | 否 |  |  |
| 20 | occur_balance | 否 |  |  |
| 21 | correct_balance | 否 |  |  |
| 22 | business_balance | 否 |  |  |
| 23 | exchange_fare0 | 否 |  |  |
| 24 | exchange_fare1 | 否 |  |  |
| 25 | exchange_fare2 | 否 |  |  |
| 26 | exchange_fare3 | 否 |  |  |
| 27 | exchange_fare4 | 否 |  |  |
| 28 | exchange_fare5 | 否 |  |  |
| 29 | exchange_fare6 | 否 |  |  |
| 30 | exchange_farex | 否 |  |  |
| 31 | remark | 否 |  |  |
| 32 | treat_status | 否 |  |  |
| 33 | position_str | 否 |  |  |
| 34 | csfc_borrow_accttype | 否 |  |  |
| 35 | client_group | 否 | H |  |
| 36 | room_code | 否 | H |  |
| 37 | asset_prop | 否 | H |  |
| 38 | client_prop | 否 | H |  |
| 39 | limit_flag | 否 | H |  |
| 40 | client_name | 否 | H |  |
| 41 | stock_name | 否 | H |  |
| 42 | stock_type | 否 | H |  |
| 43 | sub_stock_type | 否 | H |  |
| 44 | corp_client_group | 否 | H |  |
| 45 | asset_level | 否 | H |  |
| 46 | risk_level | 否 | H |  |
| 47 | corp_risk_level | 否 | H |  |
| 48 | init_date | 否 |  |  |
| 49 | settle_date | 否 |  |  |
| 50 | serial_no | 否 |  |  |
| 51 | company_no | 否 |  |  |
| 52 | business_flag | 否 |  |  |
| 53 | refbusi_code | 否 |  |  |
| 54 | cbp_business_id | 否 |  |  |
| 55 | branch_no | 否 |  |  |
| 56 | client_id | 否 |  |  |
| 57 | fund_account | 否 |  |  |
| 58 | stock_account | 否 |  |  |
| 59 | entrust_no | 否 |  |  |
| 60 | entrust_date | 否 |  |  |
| 61 | money_type | 否 |  |  |
| 62 | entrust_amount | 否 |  |  |
| 63 | entrust_balance | 否 |  |  |
| 64 | exchange_type | 否 |  |  |
| 65 | stock_code | 否 |  |  |
| 66 | occur_amount | 否 |  |  |
| 67 | occur_balance | 否 |  |  |
| 68 | correct_balance | 否 |  |  |
| 69 | business_balance | 否 |  |  |
| 70 | exchange_fare0 | 否 |  |  |
| 71 | exchange_fare1 | 否 |  |  |
| 72 | exchange_fare2 | 否 |  |  |
| 73 | exchange_fare3 | 否 |  |  |
| 74 | exchange_fare4 | 否 |  |  |
| 75 | exchange_fare5 | 否 |  |  |
| 76 | exchange_fare6 | 否 |  |  |
| 77 | exchange_farex | 否 |  |  |
| 78 | remark | 否 |  |  |
| 79 | treat_status | 否 |  |  |
| 80 | position_str | 否 |  |  |
| 81 | csfc_borrow_accttype | 否 |  |  |
| 82 | client_group | 否 | H |  |
| 83 | room_code | 否 | H |  |
| 84 | asset_prop | 否 | H |  |
| 85 | client_prop | 否 | H |  |
| 86 | limit_flag | 否 | H |  |
| 87 | client_name | 否 | H |  |
| 88 | stock_name | 否 | H |  |
| 89 | stock_type | 否 | H |  |
| 90 | sub_stock_type | 否 | H |  |
| 91 | corp_client_group | 否 | H |  |
| 92 | asset_level | 否 | H |  |
| 93 | risk_level | 否 | H |  |
| 94 | corp_risk_level | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refbailbusiness | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_refbailbusiness_pos | ART | 是 | position_str, position_str |
| idx_refbailbusiness | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_refbailbusiness_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 6 个）

| 索引名 | 字段 |
|--------|------|
| idx_refbailbusiness | init_date, serial_no, init_date, serial_no |
| idx_refbailbusiness_pos | position_str, position_str |
| uk_rpt_urefbailbusiness | init_date, position_str, init_date, position_str |
| idx_refbailbusiness | init_date, serial_no, init_date, serial_no |
| idx_refbailbusiness_pos | position_str, position_str |
| uk_rpt_urefbailbusiness | init_date, position_str, init_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-12 15:37:34 | V3.0.2.3 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_bail_business，添加了表字段(corp_client_grou... |
| 2025-10-16 10:38:01 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-12-12 15:37:34 | V3.0.2.3 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_bail_business，添加了表字段(corp_client_grou... |
| 2025-10-16 10:38:01 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

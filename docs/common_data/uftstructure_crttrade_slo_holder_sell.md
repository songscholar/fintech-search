# slo_holder_sell - 融券持有卖出记录表

**表对象ID**: 7579
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 60 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | entrust_date | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | slo_sell_amount | 否 |  |  |
| 8 | slo_begin_amount | 否 |  |  |
| 9 | slo_current_amount | 否 |  |  |
| 10 | report_unit | 否 |  |  |
| 11 | prev_status | 否 |  |  |
| 12 | account_group | 否 |  |  |
| 13 | account_count | 否 |  |  |
| 14 | date_clear | 否 |  |  |
| 15 | company_no | 否 |  |  |
| 16 | position_str_long | 否 |  |  |
| 17 | branch_no | 否 | H |  |
| 18 | stock_name | 否 | H |  |
| 19 | sub_stock_type | 否 | H |  |
| 20 | stock_type | 否 | H |  |
| 21 | client_name | 否 | H |  |
| 22 | corp_client_group | 否 | H |  |
| 23 | client_group | 否 | H |  |
| 24 | room_code | 否 | H |  |
| 25 | asset_prop | 否 | H |  |
| 26 | limit_flag | 否 | H |  |
| 27 | client_prop | 否 | H |  |
| 28 | asset_level | 否 | H |  |
| 29 | risk_level | 否 | H |  |
| 30 | corp_risk_level | 否 | H |  |
| 31 | init_date | 否 |  |  |
| 32 | entrust_date | 否 |  |  |
| 33 | exchange_type | 否 |  |  |
| 34 | client_id | 否 |  |  |
| 35 | fund_account | 否 |  |  |
| 36 | stock_code | 否 |  |  |
| 37 | slo_sell_amount | 否 |  |  |
| 38 | slo_begin_amount | 否 |  |  |
| 39 | slo_current_amount | 否 |  |  |
| 40 | report_unit | 否 |  |  |
| 41 | prev_status | 否 |  |  |
| 42 | account_group | 否 |  |  |
| 43 | account_count | 否 |  |  |
| 44 | date_clear | 否 |  |  |
| 45 | company_no | 否 |  |  |
| 46 | position_str_long | 否 |  |  |
| 47 | branch_no | 否 | H |  |
| 48 | stock_name | 否 | H |  |
| 49 | sub_stock_type | 否 | H |  |
| 50 | stock_type | 否 | H |  |
| 51 | client_name | 否 | H |  |
| 52 | corp_client_group | 否 | H |  |
| 53 | client_group | 否 | H |  |
| 54 | room_code | 否 | H |  |
| 55 | asset_prop | 否 | H |  |
| 56 | limit_flag | 否 | H |  |
| 57 | client_prop | 否 | H |  |
| 58 | asset_level | 否 | H |  |
| 59 | risk_level | 否 | H |  |
| 60 | corp_risk_level | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_slo_holder_sell | ART | 是 | fund_account, stock_code, entrust_date, company_no, exchange_type, fund_account, stock_code, entrust_date, company_no, exchange_type |
| idx_slo_holder_sell_pos | ART | 是 | position_str_long, position_str_long |
| idx_slo_holder_sell_poslong | ART | 是 | init_date, position_str_long, init_date, position_str_long |
| uk_rpt_sloholdersell | ART | 是 | init_date, branch_no, position_str_long, init_date, branch_no, position_str_long |
| idx_rpt_sloholdersell_tolast | ART | 是 | date_clear, date_clear |
| idx_slo_holder_sell | ART | 是 | fund_account, stock_code, entrust_date, company_no, exchange_type, fund_account, stock_code, entrust_date, company_no, exchange_type |
| idx_slo_holder_sell_pos | ART | 是 | position_str_long, position_str_long |
| idx_slo_holder_sell_poslong | ART | 是 | init_date, position_str_long, init_date, position_str_long |
| uk_rpt_sloholdersell | ART | 是 | init_date, branch_no, position_str_long, init_date, branch_no, position_str_long |
| idx_rpt_sloholdersell_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_slo_holder_sell | fund_account, stock_code, entrust_date, company_no, exchange_type, fund_account, stock_code, entrust_date, company_no, exchange_type |
| idx_slo_holder_sell | fund_account, stock_code, entrust_date, company_no, exchange_type, fund_account, stock_code, entrust_date, company_no, exchange_type |

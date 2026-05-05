# setttouftdividendtax - 清算股息红利差别化扣税信息表

**表对象ID**: 3023
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 86 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | sett_id | 是 |  |  |
| 3 | serial_no | 是 |  |  |
| 4 | curr_time | 是 |  |  |
| 5 | curr_date | 是 |  |  |
| 6 | operator_no | 是 |  |  |
| 7 | op_branch_no | 是 |  |  |
| 8 | op_station | 是 |  |  |
| 9 | op_entrust_way | 是 |  |  |
| 10 | branch_no | 是 |  |  |
| 11 | client_id | 是 |  |  |
| 12 | fund_account | 是 |  |  |
| 13 | exchange_type | 是 |  |  |
| 14 | stock_account | 是 |  |  |
| 15 | stock_code | 是 |  |  |
| 16 | stock_type | 是 |  |  |
| 17 | money_type | 是 |  |  |
| 18 | seat_no | 是 |  |  |
| 19 | report_date | 是 |  |  |
| 20 | report_time | 是 |  |  |
| 21 | szdc_main_seat | 是 |  |  |
| 22 | dividend_tax | 是 |  |  |
| 23 | settle_date | 是 |  |  |
| 24 | tax_id | 是 |  |  |
| 25 | tax_date | 是 |  |  |
| 26 | date_clear | 是 |  |  |
| 27 | dividendtax_status | 是 |  |  |
| 28 | hold_date | 是 |  |  |
| 29 | register_date | 是 |  |  |
| 30 | pretax_price | 是 |  |  |
| 31 | reduce_amount | 是 |  |  |
| 32 | tax_rate | 是 |  |  |
| 33 | tax_amount | 是 |  |  |
| 34 | tax_type | 是 |  |  |
| 35 | add_balance | 是 |  |  |
| 36 | report_no | 是 |  |  |
| 37 | report_flag | 是 |  |  |
| 38 | error_no | 是 |  |  |
| 39 | remark | 是 |  |  |
| 40 | modify_date | 是 |  |  |
| 41 | position_str | 是 |  |  |
| 42 | uft_data_change_status | 是 |  |  |
| 43 | sub_stock_type | 是 |  | s |
| 44 | init_date | 是 |  |  |
| 45 | sett_id | 是 |  |  |
| 46 | serial_no | 是 |  |  |
| 47 | curr_time | 是 |  |  |
| 48 | curr_date | 是 |  |  |
| 49 | operator_no | 是 |  |  |
| 50 | op_branch_no | 是 |  |  |
| 51 | op_station | 是 |  |  |
| 52 | op_entrust_way | 是 |  |  |
| 53 | branch_no | 是 |  |  |
| 54 | client_id | 是 |  |  |
| 55 | fund_account | 是 |  |  |
| 56 | exchange_type | 是 |  |  |
| 57 | stock_account | 是 |  |  |
| 58 | stock_code | 是 |  |  |
| 59 | stock_type | 是 |  |  |
| 60 | money_type | 是 |  |  |
| 61 | seat_no | 是 |  |  |
| 62 | report_date | 是 |  |  |
| 63 | report_time | 是 |  |  |
| 64 | szdc_main_seat | 是 |  |  |
| 65 | dividend_tax | 是 |  |  |
| 66 | settle_date | 是 |  |  |
| 67 | tax_id | 是 |  |  |
| 68 | tax_date | 是 |  |  |
| 69 | date_clear | 是 |  |  |
| 70 | dividendtax_status | 是 |  |  |
| 71 | hold_date | 是 |  |  |
| 72 | register_date | 是 |  |  |
| 73 | pretax_price | 是 |  |  |
| 74 | reduce_amount | 是 |  |  |
| 75 | tax_rate | 是 |  |  |
| 76 | tax_amount | 是 |  |  |
| 77 | tax_type | 是 |  |  |
| 78 | add_balance | 是 |  |  |
| 79 | report_no | 是 |  |  |
| 80 | report_flag | 是 |  |  |
| 81 | error_no | 是 |  |  |
| 82 | remark | 是 |  |  |
| 83 | modify_date | 是 |  |  |
| 84 | position_str | 是 |  |  |
| 85 | uft_data_change_status | 是 |  |  |
| 86 | sub_stock_type | 是 |  | s |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settdividendtax | 默认 | 是 | serial_no, init_date, serial_no, init_date |
| idx_settdividendtax_taxid | 默认 | 是 | tax_id, exchange_type, tax_id, exchange_type |
| idx_settdividendtax_taxdate | 默认 | 是 | tax_date, exchange_type, tax_date, exchange_type |
| idx_settdividendtax | 默认 | 是 | serial_no, init_date, serial_no, init_date |
| idx_settdividendtax_taxid | 默认 | 是 | tax_id, exchange_type, tax_id, exchange_type |
| idx_settdividendtax_taxdate | 默认 | 是 | tax_date, exchange_type, tax_date, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settdividendtax | serial_no, init_date, serial_no, init_date |
| idx_settdividendtax | serial_no, init_date, serial_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2020-05-15 10:54 | 8.26.1.82 | 张军 | 新增字段sub_stock_type |
| 2020-05-15 10:54 | 8.26.1.82 | 张军 | 新增字段sub_stock_type |

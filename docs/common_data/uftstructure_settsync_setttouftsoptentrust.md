# setttouftsoptentrust - 清算非交易报送委托表

**表对象ID**: 3008
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 88 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | entrust_no | 是 |  |  |
| 3 | op_branch_no | 是 |  |  |
| 4 | operator_no | 是 |  |  |
| 5 | op_entrust_way | 是 |  |  |
| 6 | op_station | 是 |  |  |
| 7 | branch_no | 是 |  |  |
| 8 | fund_account | 是 |  |  |
| 9 | client_id | 是 |  |  |
| 10 | exchange_type | 是 |  |  |
| 11 | stock_account | 是 |  |  |
| 12 | report_account | 是 |  |  |
| 13 | seat_no | 是 |  |  |
| 14 | stock_code | 是 |  |  |
| 15 | stock_type | 是 |  |  |
| 16 | money_type | 是 |  |  |
| 17 | entrust_bs | 是 |  |  |
| 18 | entrust_type | 是 |  |  |
| 19 | entrust_prop | 是 |  |  |
| 20 | entrust_amount | 是 |  |  |
| 21 | entrust_price | 是 |  |  |
| 22 | sopt_tax | 是 |  |  |
| 23 | report_time | 是 |  |  |
| 24 | report_no | 是 |  |  |
| 25 | contract_id | 是 |  |  |
| 26 | business_amount | 是 |  |  |
| 27 | withdraw_amount | 是 |  |  |
| 28 | business_price | 是 |  |  |
| 29 | business_balance | 是 |  |  |
| 30 | clear_balance | 是 |  |  |
| 31 | prev_balance | 是 |  |  |
| 32 | report_bs | 是 |  |  |
| 33 | store_unit | 是 |  |  |
| 34 | report_unit | 是 |  |  |
| 35 | entrust_status | 是 |  |  |
| 36 | company_no | 是 |  |  |
| 37 | sopt_report_code | 是 |  |  |
| 38 | return_serial_no | 是 |  |  |
| 39 | stock_account_dest | 是 |  |  |
| 40 | seat_no_dest | 是 |  |  |
| 41 | return_code | 是 |  |  |
| 42 | return_info | 是 |  |  |
| 43 | error_no | 是 |  |  |
| 44 | join_serial_no | 是 |  |  |
| 45 | init_date | 是 |  |  |
| 46 | entrust_no | 是 |  |  |
| 47 | op_branch_no | 是 |  |  |
| 48 | operator_no | 是 |  |  |
| 49 | op_entrust_way | 是 |  |  |
| 50 | op_station | 是 |  |  |
| 51 | branch_no | 是 |  |  |
| 52 | fund_account | 是 |  |  |
| 53 | client_id | 是 |  |  |
| 54 | exchange_type | 是 |  |  |
| 55 | stock_account | 是 |  |  |
| 56 | report_account | 是 |  |  |
| 57 | seat_no | 是 |  |  |
| 58 | stock_code | 是 |  |  |
| 59 | stock_type | 是 |  |  |
| 60 | money_type | 是 |  |  |
| 61 | entrust_bs | 是 |  |  |
| 62 | entrust_type | 是 |  |  |
| 63 | entrust_prop | 是 |  |  |
| 64 | entrust_amount | 是 |  |  |
| 65 | entrust_price | 是 |  |  |
| 66 | sopt_tax | 是 |  |  |
| 67 | report_time | 是 |  |  |
| 68 | report_no | 是 |  |  |
| 69 | contract_id | 是 |  |  |
| 70 | business_amount | 是 |  |  |
| 71 | withdraw_amount | 是 |  |  |
| 72 | business_price | 是 |  |  |
| 73 | business_balance | 是 |  |  |
| 74 | clear_balance | 是 |  |  |
| 75 | prev_balance | 是 |  |  |
| 76 | report_bs | 是 |  |  |
| 77 | store_unit | 是 |  |  |
| 78 | report_unit | 是 |  |  |
| 79 | entrust_status | 是 |  |  |
| 80 | company_no | 是 |  |  |
| 81 | sopt_report_code | 是 |  |  |
| 82 | return_serial_no | 是 |  |  |
| 83 | stock_account_dest | 是 |  |  |
| 84 | seat_no_dest | 是 |  |  |
| 85 | return_code | 是 |  |  |
| 86 | return_info | 是 |  |  |
| 87 | error_no | 是 |  |  |
| 88 | join_serial_no | 是 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_settsoptentrust | 默认 | 是 | entrust_no, init_date, branch_no, entrust_no, init_date, branch_no |
| idx_settsoptentrust_report | 默认 | 是 | report_account, exchange_type, report_account, exchange_type |
| idx_settsoptentrust_acct | 默认 | 是 | fund_account, fund_account |
| uk_settsoptentrust | 默认 | 是 | entrust_no, init_date, branch_no, entrust_no, init_date, branch_no |
| idx_settsoptentrust_report | 默认 | 是 | report_account, exchange_type, report_account, exchange_type |
| idx_settsoptentrust_acct | 默认 | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| uk_settsoptentrust | entrust_no, init_date, branch_no, entrust_no, init_date, branch_no |
| uk_settsoptentrust | entrust_no, init_date, branch_no, entrust_no, init_date, branch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-05-23 15:56 | 8.26.2.26 | 徐开 | 增加join_serial_no字段 |
| 2021-05-20 14:21 | 8.26.1.70 | 郑天翔 | 增加error_no字段 |
| 2021-04-23 16:25 | 8.26.1.67 | 郑天翔 | 增加表settsoptentrust |
| 2023-05-23 15:56 | 8.26.2.26 | 徐开 | 增加join_serial_no字段 |
| 2021-05-20 14:21 | 8.26.1.70 | 郑天翔 | 增加error_no字段 |
| 2021-04-23 16:25 | 8.26.1.67 | 郑天翔 | 增加表settsoptentrust |

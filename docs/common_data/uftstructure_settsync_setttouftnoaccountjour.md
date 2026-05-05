# setttouftnoaccountjour - 清算无主流水表

**表对象ID**: 3014
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 94 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | sett_batch_no | 是 |  |  |
| 3 | sett_id | 是 |  |  |
| 4 | settserial_no | 是 |  |  |
| 5 | file_type | 是 |  |  |
| 6 | stock_account | 是 |  |  |
| 7 | stock_code | 是 |  |  |
| 8 | branch_no | 是 |  |  |
| 9 | exchange_type | 是 |  |  |
| 10 | curr_date | 是 |  |  |
| 11 | curr_time | 是 |  |  |
| 12 | business_flag | 是 |  |  |
| 13 | operator_no | 是 |  |  |
| 14 | op_station | 是 |  |  |
| 15 | fund_account | 是 |  |  |
| 16 | client_id | 是 |  |  |
| 17 | stock_name | 是 |  |  |
| 18 | occur_amount | 是 |  |  |
| 19 | occur_balance | 是 |  |  |
| 20 | noacctjour_status | 是 |  |  |
| 21 | date_back | 是 |  |  |
| 22 | client_id_dest | 是 |  |  |
| 23 | fund_account_dest | 是 |  |  |
| 24 | seat_no | 是 |  |  |
| 25 | stock_type | 是 |  |  |
| 26 | cancel_serialno | 是 |  |  |
| 27 | position_str | 是 |  |  |
| 28 | remark | 是 |  |  |
| 29 | serial_no | 是 |  |  |
| 30 | sum_buy_amount | 是 |  |  |
| 31 | sum_buy_balance | 是 |  |  |
| 32 | sum_sell_amount | 是 |  |  |
| 33 | sum_sell_balance | 是 |  |  |
| 34 | uncome_buy_amount | 是 |  |  |
| 35 | uncome_sell_amount | 是 |  |  |
| 36 | frozen_amount | 是 |  |  |
| 37 | unfrozen_amount | 是 |  |  |
| 38 | correct_amount | 是 |  |  |
| 39 | money_type | 是 |  |  |
| 40 | frozen_balance | 是 |  |  |
| 41 | unfrozen_balance | 是 |  |  |
| 42 | stock_code_long | 是 |  |  |
| 43 | bourse_amount | 是 |  |  |
| 44 | current_amount | 是 |  |  |
| 45 | correct_balance | 是 |  |  |
| 46 | busiflow_id | 是 |  |  |
| 47 | uft_data_change_status | 是 |  |  |
| 48 | init_date | 是 |  |  |
| 49 | sett_batch_no | 是 |  |  |
| 50 | sett_id | 是 |  |  |
| 51 | settserial_no | 是 |  |  |
| 52 | file_type | 是 |  |  |
| 53 | stock_account | 是 |  |  |
| 54 | stock_code | 是 |  |  |
| 55 | branch_no | 是 |  |  |
| 56 | exchange_type | 是 |  |  |
| 57 | curr_date | 是 |  |  |
| 58 | curr_time | 是 |  |  |
| 59 | business_flag | 是 |  |  |
| 60 | operator_no | 是 |  |  |
| 61 | op_station | 是 |  |  |
| 62 | fund_account | 是 |  |  |
| 63 | client_id | 是 |  |  |
| 64 | stock_name | 是 |  |  |
| 65 | occur_amount | 是 |  |  |
| 66 | occur_balance | 是 |  |  |
| 67 | noacctjour_status | 是 |  |  |
| 68 | date_back | 是 |  |  |
| 69 | client_id_dest | 是 |  |  |
| 70 | fund_account_dest | 是 |  |  |
| 71 | seat_no | 是 |  |  |
| 72 | stock_type | 是 |  |  |
| 73 | cancel_serialno | 是 |  |  |
| 74 | position_str | 是 |  |  |
| 75 | remark | 是 |  |  |
| 76 | serial_no | 是 |  |  |
| 77 | sum_buy_amount | 是 |  |  |
| 78 | sum_buy_balance | 是 |  |  |
| 79 | sum_sell_amount | 是 |  |  |
| 80 | sum_sell_balance | 是 |  |  |
| 81 | uncome_buy_amount | 是 |  |  |
| 82 | uncome_sell_amount | 是 |  |  |
| 83 | frozen_amount | 是 |  |  |
| 84 | unfrozen_amount | 是 |  |  |
| 85 | correct_amount | 是 |  |  |
| 86 | money_type | 是 |  |  |
| 87 | frozen_balance | 是 |  |  |
| 88 | unfrozen_balance | 是 |  |  |
| 89 | stock_code_long | 是 |  |  |
| 90 | bourse_amount | 是 |  |  |
| 91 | current_amount | 是 |  |  |
| 92 | correct_balance | 是 |  |  |
| 93 | busiflow_id | 是 |  |  |
| 94 | uft_data_change_status | 是 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settnoaccountjour | 默认 | 是 | stock_account, branch_no, stock_code, fund_account, exchange_type, stock_code_long, stock_account, branch_no, stock_code, fund_account, exchange_type, stock_code_long |
| idx_settnoaccountjour_acct | 默认 | 是 | stock_account, exchange_type, stock_code, stock_code_long, seat_no, stock_account, exchange_type, stock_code, stock_code_long, seat_no |
| idx_settnoaccountjour_busi | 默认 | 是 | busiflow_id, busiflow_id |
| idx_settnoaccountjour | 默认 | 是 | stock_account, branch_no, stock_code, fund_account, exchange_type, stock_code_long, stock_account, branch_no, stock_code, fund_account, exchange_type, stock_code_long |
| idx_settnoaccountjour_acct | 默认 | 是 | stock_account, exchange_type, stock_code, stock_code_long, seat_no, stock_account, exchange_type, stock_code, stock_code_long, seat_no |
| idx_settnoaccountjour_busi | 默认 | 是 | busiflow_id, busiflow_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settnoaccountjour_acct | stock_account, exchange_type, stock_code, stock_code_long, seat_no, stock_account, exchange_type, stock_code, stock_code_long, seat_no |
| idx_settnoaccountjour_acct | stock_account, exchange_type, stock_code, stock_code_long, seat_no, stock_account, exchange_type, stock_code, stock_code_long, seat_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2022-10-27 15:10 | 8.26.2.38 | 张军 | 增加busiflow_id索引 |
| 2022-06-15 16:39 | 8.26.2.29 | 曾哲 | 增加bourse_amount,current_amount,correct_balance |
| 2022-03-27 14:36 | 8.26.2.22 | 周涛 | 索引增加字段stock_code_long |
| 2022-03-11 20:05 | 8.26.2.21 | 周涛 | 增加字段stock_code_long |
| 2021-09-08 17:23 | 8.26.2.11 | 徐开 | settnoaccountjour增加frozen_balance和unfrozen_balance |
| 2020-08-06 12:41 | 8.26.1.89 | 罗佳楠 | 增加字段money_type |
| 2019-02-13 17:08 | 8.26.1.55 | 彭立 | 增加字段sett_batch_no |
| 2018-09-20 14:50 | 8.26.1.43 | 蒋迪 | 增加字段busiflow_id |
| 2018-08-14 18:44 | 8.26.1.39 | 曾哲 | 增加sum_buy_amount，sum_buy_balance,sum_sell_amount，sum_sell_ba... |
| 2018-07-11 11:40 | 8.26.1.33 | 彭立 | uft_data_change_status改为必须 |
| 2022-10-27 15:10 | 8.26.2.38 | 张军 | 增加busiflow_id索引 |
| 2022-06-15 16:39 | 8.26.2.29 | 曾哲 | 增加bourse_amount,current_amount,correct_balance |
| 2022-03-27 14:36 | 8.26.2.22 | 周涛 | 索引增加字段stock_code_long |
| 2022-03-11 20:05 | 8.26.2.21 | 周涛 | 增加字段stock_code_long |
| 2021-09-08 17:23 | 8.26.2.11 | 徐开 | settnoaccountjour增加frozen_balance和unfrozen_balance |

> 共 20 条修改记录，仅显示最近15条

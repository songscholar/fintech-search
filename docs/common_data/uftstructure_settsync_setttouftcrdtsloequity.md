# setttouftcrdtsloequity - 清算融券股份权益信息表

**表对象ID**: 3067
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 70 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | serial_no | 是 |  |  |
| 3 | curr_date | 是 |  |  |
| 4 | curr_time | 是 |  |  |
| 5 | operator_no | 是 |  |  |
| 6 | op_branch_no | 是 |  |  |
| 7 | op_entrust_way | 是 |  |  |
| 8 | op_station | 是 |  |  |
| 9 | branch_no | 是 |  |  |
| 10 | fund_account | 是 |  |  |
| 11 | client_id | 是 |  |  |
| 12 | stock_account | 是 |  |  |
| 13 | exchange_type | 是 |  |  |
| 14 | stock_code | 是 |  |  |
| 15 | stock_type | 是 |  |  |
| 16 | money_type | 是 |  |  |
| 17 | equity_type | 是 |  |  |
| 18 | current_amount | 是 |  |  |
| 19 | recoup_amount | 是 |  |  |
| 20 | recoup_balance | 是 |  |  |
| 21 | recoup_type | 是 |  |  |
| 22 | register_date | 是 |  |  |
| 23 | compact_id | 是 |  |  |
| 24 | divid_date | 是 |  |  |
| 25 | cashgroup_no | 是 |  |  |
| 26 | equity_discount_ratio | 是 |  |  |
| 27 | equity_discount_flag | 是 |  |  |
| 28 | deal_status | 是 |  |  |
| 29 | date_clear | 是 |  |  |
| 30 | remark | 是 |  |  |
| 31 | position_str | 是 |  |  |
| 32 | recoup_amount_decimal | 是 |  |  |
| 33 | uft_data_change_status | 是 |  |  |
| 34 | compact_source | 是 |  |  |
| 35 | pre_recoup_balance | 是 |  |  |
| 36 | init_date | 是 |  |  |
| 37 | serial_no | 是 |  |  |
| 38 | curr_date | 是 |  |  |
| 39 | curr_time | 是 |  |  |
| 40 | operator_no | 是 |  |  |
| 41 | op_branch_no | 是 |  |  |
| 42 | op_entrust_way | 是 |  |  |
| 43 | op_station | 是 |  |  |
| 44 | branch_no | 是 |  |  |
| 45 | fund_account | 是 |  |  |
| 46 | client_id | 是 |  |  |
| 47 | stock_account | 是 |  |  |
| 48 | exchange_type | 是 |  |  |
| 49 | stock_code | 是 |  |  |
| 50 | stock_type | 是 |  |  |
| 51 | money_type | 是 |  |  |
| 52 | equity_type | 是 |  |  |
| 53 | current_amount | 是 |  |  |
| 54 | recoup_amount | 是 |  |  |
| 55 | recoup_balance | 是 |  |  |
| 56 | recoup_type | 是 |  |  |
| 57 | register_date | 是 |  |  |
| 58 | compact_id | 是 |  |  |
| 59 | divid_date | 是 |  |  |
| 60 | cashgroup_no | 是 |  |  |
| 61 | equity_discount_ratio | 是 |  |  |
| 62 | equity_discount_flag | 是 |  |  |
| 63 | deal_status | 是 |  |  |
| 64 | date_clear | 是 |  |  |
| 65 | remark | 是 |  |  |
| 66 | position_str | 是 |  |  |
| 67 | recoup_amount_decimal | 是 |  |  |
| 68 | uft_data_change_status | 是 |  |  |
| 69 | compact_source | 是 |  |  |
| 70 | pre_recoup_balance | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settcrdtsloequity_pos | 默认 | 是 | position_str, position_str |
| idx_settcrdtsloequity_exch | 默认 | 是 | stock_code, exchange_type, stock_account, stock_code, exchange_type, stock_account |
| idx_settcrdtsloequity_pos | 默认 | 是 | position_str, position_str |
| idx_settcrdtsloequity_exch | 默认 | 是 | stock_code, exchange_type, stock_account, stock_code, exchange_type, stock_account |

## 数据库索引（共 8 个）

| 索引名 | 字段 |
|--------|------|
| idx_idx_crdtsloequity_pos | position_str, position_str |
| idx_idx_crdtsloequity_acct | fund_account, fund_account |
| idx_idx_crdtsloequity_id | client_id, client_id |
| idx_crdtsloequity | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_idx_crdtsloequity_pos | position_str, position_str |
| idx_idx_crdtsloequity_acct | fund_account, fund_account |
| idx_idx_crdtsloequity_id | client_id, client_id |
| idx_crdtsloequity | serial_no, branch_no, init_date, serial_no, branch_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2022-05-25 19:33 | 8.26.2.20 | 徐开 | 新增pre_recoup_balance和compact_source字段 |
| 2021-04-21 11:13 | 8.26.1.91 | 罗佳楠 | 新增字段recoup_amount_decimal |
| 2018-04-10 16:40 | 8.26.1.8 | 曾哲 | 新增 |
| 2022-05-25 19:33 | 8.26.2.20 | 徐开 | 新增pre_recoup_balance和compact_source字段 |
| 2021-04-21 11:13 | 8.26.1.91 | 罗佳楠 | 新增字段recoup_amount_decimal |
| 2018-04-10 16:40 | 8.26.1.8 | 曾哲 | 新增 |

# uopt_hold_changeinfo - 期权交易持仓变更信息表

**表对象ID**: 9632
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | option_code | 否 |  |  |
| 10 | option_type | 否 |  |  |
| 11 | opthold_type | 否 |  |  |
| 12 | business_flag | 否 |  |  |
| 13 | occur_amount | 否 |  |  |
| 14 | current_amount | 否 |  |  |
| 15 | sum_open_amount | 否 |  |  |
| 16 | sum_buy_balance | 否 |  |  |
| 17 | sum_drop_amount | 否 |  |  |
| 18 | sum_sell_balance | 否 |  |  |
| 19 | opt_cost_price | 否 |  |  |
| 20 | remark | 否 |  |  |
| 21 | position_str | 否 |  |  |
| 22 | init_date | 否 |  |  |
| 23 | serial_no | 否 |  |  |
| 24 | curr_date | 否 |  |  |
| 25 | curr_time | 否 |  |  |
| 26 | fund_account | 否 |  |  |
| 27 | client_id | 否 |  |  |
| 28 | stock_account | 否 |  |  |
| 29 | exchange_type | 否 |  |  |
| 30 | option_code | 否 |  |  |
| 31 | option_type | 否 |  |  |
| 32 | opthold_type | 否 |  |  |
| 33 | business_flag | 否 |  |  |
| 34 | occur_amount | 否 |  |  |
| 35 | current_amount | 否 |  |  |
| 36 | sum_open_amount | 否 |  |  |
| 37 | sum_buy_balance | 否 |  |  |
| 38 | sum_drop_amount | 否 |  |  |
| 39 | sum_sell_balance | 否 |  |  |
| 40 | opt_cost_price | 否 |  |  |
| 41 | remark | 否 |  |  |
| 42 | position_str | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_hold_changeinfo | ART | 是 | init_date, serial_no, fund_account, exchange_type, stock_account, init_date, serial_no, fund_account, exchange_type, stock_account |
| idx_uopt_hold_changeinfo_pos | ART | 是 | position_str, position_str |
| idx_uopt_hold_changeinfo | ART | 是 | init_date, serial_no, fund_account, exchange_type, stock_account, init_date, serial_no, fund_account, exchange_type, stock_account |
| idx_uopt_hold_changeinfo_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_hold_changeinfo | init_date, serial_no, fund_account, exchange_type, stock_account, init_date, serial_no, fund_account, exchange_type, stock_account |
| idx_uopt_hold_changeinfo | init_date, serial_no, fund_account, exchange_type, stock_account, init_date, serial_no, fund_account, exchange_type, stock_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-03 13:35:34 | 3.0.2.20 | 黄佳为 | 新增 |
| 2025-12-03 13:35:34 | 3.0.2.20 | 黄佳为 | 新增 |

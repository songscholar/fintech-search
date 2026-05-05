# uopt_combholdreal_jour - 期权组合策略持仓实时交易流水表

**表对象ID**: 9617
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 48 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | trace_id | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_account | 否 |  |  |
| 10 | optcomb_code | 否 |  |  |
| 11 | optcomb_id | 否 |  |  |
| 12 | component_count | 否 |  |  |
| 13 | first_option_code | 否 |  |  |
| 14 | first_opthold_type | 否 |  |  |
| 15 | second_option_code | 否 |  |  |
| 16 | second_opthold_type | 否 |  |  |
| 17 | real_action | 否 |  |  |
| 18 | business_flag | 否 |  |  |
| 19 | occur_amount | 否 |  |  |
| 20 | post_amount | 否 |  |  |
| 21 | cancel_serial_no | 否 |  |  |
| 22 | position_str | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | modify_fields | 否 |  |  |
| 25 | init_date | 否 |  |  |
| 26 | serial_no | 否 |  |  |
| 27 | curr_date | 否 |  |  |
| 28 | curr_time | 否 |  |  |
| 29 | trace_id | 否 |  |  |
| 30 | client_id | 否 |  |  |
| 31 | fund_account | 否 |  |  |
| 32 | exchange_type | 否 |  |  |
| 33 | stock_account | 否 |  |  |
| 34 | optcomb_code | 否 |  |  |
| 35 | optcomb_id | 否 |  |  |
| 36 | component_count | 否 |  |  |
| 37 | first_option_code | 否 |  |  |
| 38 | first_opthold_type | 否 |  |  |
| 39 | second_option_code | 否 |  |  |
| 40 | second_opthold_type | 否 |  |  |
| 41 | real_action | 否 |  |  |
| 42 | business_flag | 否 |  |  |
| 43 | occur_amount | 否 |  |  |
| 44 | post_amount | 否 |  |  |
| 45 | cancel_serial_no | 否 |  |  |
| 46 | position_str | 否 |  |  |
| 47 | remark | 否 |  |  |
| 48 | modify_fields | 否 |  |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_combholdreal_jour_pos | 默认 | 否 | position_str, position_str |
| idx_uopt_combholdreal_jour | 默认 | 否 | init_date, serial_no, init_date, serial_no |
| idx_uopt_combholdreal_jour_acct | 默认 | 是 | fund_account, fund_account |
| idx_uopt_combholdreal_jour_pos | 默认 | 是 | position_str, position_str |
| idx_uopt_combholdreal_jour_temp | 默认 | 是 | init_date, serial_no, fund_account, exchange_type, stock_account, init_date, serial_no, fund_account, exchange_type, stock_account |
| idx_uopt_combholdreal_jour_pos | 默认 | 否 | position_str, position_str |
| idx_uopt_combholdreal_jour | 默认 | 否 | init_date, serial_no, init_date, serial_no |
| idx_uopt_combholdreal_jour_acct | 默认 | 是 | fund_account, fund_account |
| idx_uopt_combholdreal_jour_pos | 默认 | 是 | position_str, position_str |
| idx_uopt_combholdreal_jour_temp | 默认 | 是 | init_date, serial_no, fund_account, exchange_type, stock_account, init_date, serial_no, fund_account, exchange_type, stock_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_combholdreal_jour | init_date, serial_no, fund_account, exchange_type, stock_account, init_date, serial_no, fund_account, exchange_type, stock_account |
| idx_uopt_combholdreal_jour | init_date, serial_no, fund_account, exchange_type, stock_account, init_date, serial_no, fund_account, exchange_type, stock_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-07 13:30:18 | V3.0.2.3 |  | 内存索引字段新增init_date |
| 2025-07-25 16:58:56 | V3.0.2.1 | 汪迎 | 物理表uopt_combholdreal_jour，添加了表字段(position_str);
,物理表uopt_co... |
| 2025-08-07 13:30:18 | V3.0.2.3 |  | 内存索引字段新增init_date |
| 2025-07-25 16:58:56 | V3.0.2.1 | 汪迎 | 物理表uopt_combholdreal_jour，添加了表字段(position_str);
,物理表uopt_co... |

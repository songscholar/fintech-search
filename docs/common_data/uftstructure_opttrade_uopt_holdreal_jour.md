# uopt_holdreal_jour - 期权合约持仓实时交易流水表

**表对象ID**: 9614
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | trace_id | 否 |  |  |
| 3 | serial_no | 否 |  |  |
| 4 | curr_date | 否 |  |  |
| 5 | curr_time | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_account | 否 |  |  |
| 10 | option_code | 否 |  |  |
| 11 | option_type | 否 |  |  |
| 12 | opthold_type | 否 |  |  |
| 13 | real_action | 否 |  |  |
| 14 | business_flag | 否 |  |  |
| 15 | occur_amount | 否 |  |  |
| 16 | post_amount | 否 |  |  |
| 17 | cancel_serial_no | 否 |  |  |
| 18 | position_str | 否 |  |  |
| 19 | remark | 否 |  |  |
| 20 | modify_fields | 否 |  |  |
| 21 | init_date | 否 |  |  |
| 22 | trace_id | 否 |  |  |
| 23 | serial_no | 否 |  |  |
| 24 | curr_date | 否 |  |  |
| 25 | curr_time | 否 |  |  |
| 26 | client_id | 否 |  |  |
| 27 | fund_account | 否 |  |  |
| 28 | exchange_type | 否 |  |  |
| 29 | stock_account | 否 |  |  |
| 30 | option_code | 否 |  |  |
| 31 | option_type | 否 |  |  |
| 32 | opthold_type | 否 |  |  |
| 33 | real_action | 否 |  |  |
| 34 | business_flag | 否 |  |  |
| 35 | occur_amount | 否 |  |  |
| 36 | post_amount | 否 |  |  |
| 37 | cancel_serial_no | 否 |  |  |
| 38 | position_str | 否 |  |  |
| 39 | remark | 否 |  |  |
| 40 | modify_fields | 否 |  |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_holdreal_jour_pos | 默认 | 否 | position_str, position_str |
| idx_uopt_holdreal_jour | 默认 | 否 | init_date, serial_no, init_date, serial_no |
| idx_uopt_holdreal_jour_acct | 默认 | 是 | fund_account, fund_account |
| idx_uopt_holdreal_jour_pos | 默认 | 是 | position_str, position_str |
| idx_uopt_holdreal_jour_temp | 默认 | 是 | init_date, serial_no, fund_account, exchange_type, stock_account, init_date, serial_no, fund_account, exchange_type, stock_account |
| idx_uopt_holdreal_jour_pos | 默认 | 否 | position_str, position_str |
| idx_uopt_holdreal_jour | 默认 | 否 | init_date, serial_no, init_date, serial_no |
| idx_uopt_holdreal_jour_acct | 默认 | 是 | fund_account, fund_account |
| idx_uopt_holdreal_jour_pos | 默认 | 是 | position_str, position_str |
| idx_uopt_holdreal_jour_temp | 默认 | 是 | init_date, serial_no, fund_account, exchange_type, stock_account, init_date, serial_no, fund_account, exchange_type, stock_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_holdreal_jour | init_date, serial_no, fund_account, exchange_type, stock_account, init_date, serial_no, fund_account, exchange_type, stock_account |
| idx_uopt_holdreal_jour | init_date, serial_no, fund_account, exchange_type, stock_account, init_date, serial_no, fund_account, exchange_type, stock_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-07 13:31:02 | V3.0.2.3 |  | 内存表索引新增init_date |
| 2025-07-25 16:57:19 | V3.0.2.1 | 汪迎 | 物理表uopt_holdreal_jour，添加了表字段(position_str);
,物理表uopt_holdre... |
| 2025-06-11 14:34:31 | 3.0.2.2000 | 张明月 | 增加idx_uopt_holdreal_jour_acct索引 |
| 2025-08-07 13:31:02 | V3.0.2.3 |  | 内存表索引新增init_date |
| 2025-07-25 16:57:19 | V3.0.2.1 | 汪迎 | 物理表uopt_holdreal_jour，添加了表字段(position_str);
,物理表uopt_holdre... |
| 2025-06-11 14:34:31 | 3.0.2.2000 | 张明月 | 增加idx_uopt_holdreal_jour_acct索引 |

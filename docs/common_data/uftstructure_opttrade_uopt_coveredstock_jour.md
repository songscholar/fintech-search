# uopt_coveredstock_jour - 期权备兑证券持仓流水表

**表对象ID**: 9619
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | trace_id | 否 |  |  |
| 4 | curr_date | 否 |  |  |
| 5 | curr_time | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_account | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | real_action | 否 |  |  |
| 12 | business_flag | 否 |  |  |
| 13 | occur_amount | 否 |  |  |
| 14 | post_amount | 否 |  |  |
| 15 | cancel_serial_no | 否 |  |  |
| 16 | modify_fields | 否 |  |  |
| 17 | remark | 否 |  |  |
| 18 | init_date | 否 |  |  |
| 19 | serial_no | 否 |  |  |
| 20 | trace_id | 否 |  |  |
| 21 | curr_date | 否 |  |  |
| 22 | curr_time | 否 |  |  |
| 23 | client_id | 否 |  |  |
| 24 | fund_account | 否 |  |  |
| 25 | exchange_type | 否 |  |  |
| 26 | stock_account | 否 |  |  |
| 27 | stock_code | 否 |  |  |
| 28 | real_action | 否 |  |  |
| 29 | business_flag | 否 |  |  |
| 30 | occur_amount | 否 |  |  |
| 31 | post_amount | 否 |  |  |
| 32 | cancel_serial_no | 否 |  |  |
| 33 | modify_fields | 否 |  |  |
| 34 | remark | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_coveredstock_jour | 默认 | 否 | init_date, init_date |
| idx_uopt_coveredstock_jour | 默认 | 否 | init_date, serial_no, init_date, serial_no |
| idx_uopt_coveredstock_jour_acct | 默认 | 是 | fund_account, fund_account |
| idx_uopt_coveredstock_jour_temp | 默认 | 是 | init_date, serial_no, fund_account, exchange_type, stock_account, init_date, serial_no, fund_account, exchange_type, stock_account |
| idx_uopt_coveredstock_jour | 默认 | 否 | init_date, init_date |
| idx_uopt_coveredstock_jour | 默认 | 否 | init_date, serial_no, init_date, serial_no |
| idx_uopt_coveredstock_jour_acct | 默认 | 是 | fund_account, fund_account |
| idx_uopt_coveredstock_jour_temp | 默认 | 是 | init_date, serial_no, fund_account, exchange_type, stock_account, init_date, serial_no, fund_account, exchange_type, stock_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_coveredstock_jour | init_date, serial_no, fund_account, exchange_type, stock_account, init_date, serial_no, fund_account, exchange_type, stock_account |
| idx_uopt_coveredstock_jour | init_date, serial_no, fund_account, exchange_type, stock_account, init_date, serial_no, fund_account, exchange_type, stock_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-07 11:38:15 | V3.0.2.3 | 吴笑东 | 物理表uopt_coveredstock_jour，增加索引字段(索引idx_uopt_coveredstock_jou... |
| 2025-06-04 15:14:25 | V3.0.3.15 | 张明月 | 增加idx_uopt_coveredstock_jour_acct索引 |
| 2025-08-07 11:38:15 | V3.0.2.3 | 吴笑东 | 物理表uopt_coveredstock_jour，增加索引字段(索引idx_uopt_coveredstock_jou... |
| 2025-06-04 15:14:25 | V3.0.3.15 | 张明月 | 增加idx_uopt_coveredstock_jour_acct索引 |

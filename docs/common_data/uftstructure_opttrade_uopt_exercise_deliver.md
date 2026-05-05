# uopt_exercise_deliver - 期权行权交收信息表

**表对象ID**: 9020
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | opt_serial_no | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | money_type | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | stock_type | 否 |  |  |
| 10 | clear_amount | 否 |  |  |
| 11 | settle_amount | 否 |  |  |
| 12 | opt_cash_amount | 否 |  |  |
| 13 | short_amount | 否 |  |  |
| 14 | advance_amount | 否 |  |  |
| 15 | report_amount | 否 |  |  |
| 16 | clear_balance | 否 |  |  |
| 17 | opt_cash_balance | 否 |  |  |
| 18 | date_clear | 否 |  |  |
| 19 | init_date | 否 |  |  |
| 20 | opt_serial_no | 否 |  |  |
| 21 | exchange_type | 否 |  |  |
| 22 | money_type | 否 |  |  |
| 23 | client_id | 否 |  |  |
| 24 | fund_account | 否 |  |  |
| 25 | stock_account | 否 |  |  |
| 26 | stock_code | 否 |  |  |
| 27 | stock_type | 否 |  |  |
| 28 | clear_amount | 否 |  |  |
| 29 | settle_amount | 否 |  |  |
| 30 | opt_cash_amount | 否 |  |  |
| 31 | short_amount | 否 |  |  |
| 32 | advance_amount | 否 |  |  |
| 33 | report_amount | 否 |  |  |
| 34 | clear_balance | 否 |  |  |
| 35 | opt_cash_balance | 否 |  |  |
| 36 | date_clear | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_exercise_deliver | 默认 | 是 | client_id, opt_serial_no, client_id, opt_serial_no |
| idx_uopt_exercise_deliver | 默认 | 是 | client_id, opt_serial_no, client_id, opt_serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_exercise_deliver | client_id, opt_serial_no, client_id, opt_serial_no |
| idx_uopt_exercise_deliver | client_id, opt_serial_no, client_id, opt_serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-10-28 15:18:59 | V3.0.3.8 | 韦子晗 | serial_no字段替换成opt_serial_no字段 |
| 2024-10-28 15:18:59 | V3.0.3.8 | 韦子晗 | serial_no字段替换成opt_serial_no字段 |

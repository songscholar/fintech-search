# uopt_margin_float - 期权保证金浮动比例表

**表对象ID**: 9007
**所属模块**: optsms
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | option_type | 否 |  |  |
| 5 | option_code | 否 |  |  |
| 6 | margin_ratio | 否 |  |  |
| 7 | near_final_days | 否 |  |  |
| 8 | near_final_ratio | 否 |  |  |
| 9 | comb_upbail_balance | 否 |  |  |
| 10 | near_final_time | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | near_final_ratio_kind | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | remark | 否 |  |  |
| 17 | op_remark | 否 |  |  |
| 18 | company_no | 否 |  |  |
| 19 | exchange_type | 否 |  |  |
| 20 | stock_type | 否 |  |  |
| 21 | option_type | 否 |  |  |
| 22 | option_code | 否 |  |  |
| 23 | margin_ratio | 否 |  |  |
| 24 | near_final_days | 否 |  |  |
| 25 | near_final_ratio | 否 |  |  |
| 26 | comb_upbail_balance | 否 |  |  |
| 27 | near_final_time | 否 |  |  |
| 28 | update_date | 否 |  |  |
| 29 | update_time | 否 |  |  |
| 30 | stock_code | 否 |  |  |
| 31 | near_final_ratio_kind | 否 |  |  |
| 32 | transaction_no | 否 |  |  |
| 33 | remark | 否 |  |  |
| 34 | op_remark | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_margin_float | 默认 | 是 | company_no, exchange_type, stock_type, option_type, option_code, stock_code, company_no, exchange_type, stock_type, option_type, option_code, stock_code |
| idx_uopt_margin_float_qry | 默认 | 是 | company_no, exchange_type, option_type, stock_type, stock_code, option_code, company_no, exchange_type, option_type, stock_type, stock_code, option_code |
| idx_uopt_margin_float_qrycomb | 默认 | 是 | company_no, exchange_type, option_type, stock_type, option_code, stock_code, company_no, exchange_type, option_type, stock_type, option_code, stock_code |
| idx_uopt_margin_float | 默认 | 是 | company_no, exchange_type, stock_type, option_type, option_code, stock_code, company_no, exchange_type, stock_type, option_type, option_code, stock_code |
| idx_uopt_margin_float_qry | 默认 | 是 | company_no, exchange_type, option_type, stock_type, stock_code, option_code, company_no, exchange_type, option_type, stock_type, stock_code, option_code |
| idx_uopt_margin_float_qrycomb | 默认 | 是 | company_no, exchange_type, option_type, stock_type, option_code, stock_code, company_no, exchange_type, option_type, stock_type, option_code, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_margin_float | company_no, exchange_type, stock_type, option_type, option_code, stock_code, company_no, exchange_type, stock_type, option_type, option_code, stock_code |
| idx_uopt_margin_float | company_no, exchange_type, stock_type, option_type, option_code, stock_code, company_no, exchange_type, stock_type, option_type, option_code, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-12-16 17:28:37 | 3.0.0.0 | wuxd |  |
| 2023-12-16 17:28:37 | 3.0.0.0 | wuxd |  |

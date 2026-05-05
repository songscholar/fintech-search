# optmarginfloat - 期权保证金浮动比例导出表

**表对象ID**: 3214
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 是 |  |  |
| 2 | exchange_type | 是 |  |  |
| 3 | stock_type | 是 |  |  |
| 4 | option_type | 是 |  |  |
| 5 | option_code | 是 |  |  |
| 6 | margin_ratio | 是 |  |  |
| 7 | near_final_days | 是 |  |  |
| 8 | near_final_ratio | 是 |  |  |
| 9 | remark | 是 |  |  |
| 10 | near_final_ratio_kind | 是 |  |  |
| 11 | comb_upbail_balance | 是 |  |  |
| 12 | near_final_time | 是 |  |  |
| 13 | stock_code | 是 |  |  |
| 14 | company_no | 是 |  |  |
| 15 | exchange_type | 是 |  |  |
| 16 | stock_type | 是 |  |  |
| 17 | option_type | 是 |  |  |
| 18 | option_code | 是 |  |  |
| 19 | margin_ratio | 是 |  |  |
| 20 | near_final_days | 是 |  |  |
| 21 | near_final_ratio | 是 |  |  |
| 22 | remark | 是 |  |  |
| 23 | near_final_ratio_kind | 是 |  |  |
| 24 | comb_upbail_balance | 是 |  |  |
| 25 | near_final_time | 是 |  |  |
| 26 | stock_code | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optmarginfloat | 默认 | 是 | company_no, exchange_type, option_code, option_type, stock_code, stock_type, company_no, exchange_type, option_code, option_type, stock_code, stock_type |
| idx_optmarginfloat | 默认 | 是 | company_no, exchange_type, option_code, option_type, stock_code, stock_type, company_no, exchange_type, option_code, option_type, stock_code, stock_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optmarginfloat | company_no, exchange_type, option_code, option_type, stock_code, stock_type, company_no, exchange_type, option_code, option_type, stock_code, stock_type |
| idx_optmarginfloat | company_no, exchange_type, option_code, option_type, stock_code, stock_type, company_no, exchange_type, option_code, option_type, stock_code, stock_type |

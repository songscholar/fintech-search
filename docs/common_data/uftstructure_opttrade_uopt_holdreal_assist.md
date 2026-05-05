# uopt_holdreal_assist - 期权合约持仓辅助表

**表对象ID**: 9615
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | option_code | 否 |  |  |
| 5 | opthold_type | 否 |  |  |
| 6 | today_fd_amount | 否 |  |  |
| 7 | today_fdclose_amount | 否 |  |  |
| 8 | stock_account | 否 |  | this is uft2.0 |
| 9 | branch_no | 否 |  | this is uft2.0 |
| 10 | order_no | 否 |  | this is uft2.0 |
| 11 | client_id | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | option_code | 否 |  |  |
| 15 | opthold_type | 否 |  |  |
| 16 | today_fd_amount | 否 |  |  |
| 17 | today_fdclose_amount | 否 |  |  |
| 18 | stock_account | 否 |  | this is uft2.0 |
| 19 | branch_no | 否 |  | this is uft2.0 |
| 20 | order_no | 否 |  | this is uft2.0 |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_holdreal_assist | 默认 | 否 | option_code, opthold_type, option_code, opthold_type |
| idx_uopt_holdreal_assist_global | 默认 | 是 | fund_account, exchange_type, option_code, opthold_type, fund_account, exchange_type, option_code, opthold_type |
| idx_uopt_holdreal_assist_temp | 默认 | 是 | fund_account, exchange_type, option_code, opthold_type, stock_account, fund_account, exchange_type, option_code, opthold_type, stock_account |
| idx_uopt_holdreal_assist | 默认 | 否 | option_code, opthold_type, option_code, opthold_type |
| idx_uopt_holdreal_assist_global | 默认 | 是 | fund_account, exchange_type, option_code, opthold_type, fund_account, exchange_type, option_code, opthold_type |
| idx_uopt_holdreal_assist_temp | 默认 | 是 | fund_account, exchange_type, option_code, opthold_type, stock_account, fund_account, exchange_type, option_code, opthold_type, stock_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_holdreal_assist | fund_account, exchange_type, option_code, opthold_type, stock_account, fund_account, exchange_type, option_code, opthold_type, stock_account |
| idx_uopt_holdreal_assist | fund_account, exchange_type, option_code, opthold_type, stock_account, fund_account, exchange_type, option_code, opthold_type, stock_account |

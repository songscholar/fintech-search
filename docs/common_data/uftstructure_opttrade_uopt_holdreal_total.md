# uopt_holdreal_total - 期权合约持仓实时交易汇总表

**表对象ID**: 9627
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | sett_batch_no | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | stock_type | 否 |  |  |
| 9 | option_code | 否 |  |  |
| 10 | option_type | 否 |  |  |
| 11 | opthold_type | 否 |  |  |
| 12 | current_amount | 否 |  |  |
| 13 | frozen_amount | 否 |  |  |
| 14 | unfrozen_amount | 否 |  |  |
| 15 | enable_amount | 否 |  |  |
| 16 | optcomb_used_amount | 否 |  |  |
| 17 | opt_cost_price | 否 |  |  |
| 18 | sum_open_amount | 否 |  |  |
| 19 | sum_drop_amount | 否 |  |  |
| 20 | sum_buy_balance | 否 |  |  |
| 21 | sum_sell_balance | 否 |  |  |
| 22 | init_date | 否 |  |  |
| 23 | sett_batch_no | 否 |  |  |
| 24 | exchange_type | 否 |  |  |
| 25 | stock_account | 否 |  |  |
| 26 | client_id | 否 |  |  |
| 27 | fund_account | 否 |  |  |
| 28 | stock_code | 否 |  |  |
| 29 | stock_type | 否 |  |  |
| 30 | option_code | 否 |  |  |
| 31 | option_type | 否 |  |  |
| 32 | opthold_type | 否 |  |  |
| 33 | current_amount | 否 |  |  |
| 34 | frozen_amount | 否 |  |  |
| 35 | unfrozen_amount | 否 |  |  |
| 36 | enable_amount | 否 |  |  |
| 37 | optcomb_used_amount | 否 |  |  |
| 38 | opt_cost_price | 否 |  |  |
| 39 | sum_open_amount | 否 |  |  |
| 40 | sum_drop_amount | 否 |  |  |
| 41 | sum_buy_balance | 否 |  |  |
| 42 | sum_sell_balance | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_holdreal_total | 默认 | 是 | init_date, sett_batch_no, exchange_type, fund_account, stock_account, option_code, opthold_type, init_date, sett_batch_no, exchange_type, fund_account, stock_account, option_code, opthold_type |
| idx_uopt_holdreal_total | 默认 | 是 | init_date, sett_batch_no, exchange_type, fund_account, stock_account, option_code, opthold_type, init_date, sett_batch_no, exchange_type, fund_account, stock_account, option_code, opthold_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_holdreal_total | init_date, sett_batch_no, exchange_type, stock_account, fund_account, option_code, opthold_type, init_date, sett_batch_no, exchange_type, stock_account, fund_account, option_code, opthold_type |
| idx_uopt_holdreal_total | init_date, sett_batch_no, exchange_type, stock_account, fund_account, option_code, opthold_type, init_date, sett_batch_no, exchange_type, stock_account, fund_account, option_code, opthold_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-30 22:46:11 | V3.0.2.2 | 吴笑东 | 新增 |
| 2025-07-30 22:46:11 | V3.0.2.2 | 吴笑东 | 新增 |

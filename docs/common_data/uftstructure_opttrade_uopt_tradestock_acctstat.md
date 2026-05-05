# uopt_tradestock_acctstat - 期权交易同一账户统计表

**表对象ID**: 9620
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | short_occuped_balance | 否 |  |  |
| 5 | duty_used_bail | 否 |  |  |
| 6 | occuped_balance | 否 |  |  |
| 7 | prev_balance | 否 |  |  |
| 8 | cost_balance | 否 |  |  |
| 9 | all_occuped_amount | 否 |  |  |
| 10 | all_hold_amount | 否 |  |  |
| 11 | count | 否 |  |  |
| 12 | exch_entrust_margin | 否 |  |  |
| 13 | exch_hold_margin | 否 |  |  |
| 14 | order_no | 否 |  |  |
| 15 | partition_no | 否 |  |  |
| 16 | fund_account | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | stock_account | 否 |  |  |
| 19 | short_occuped_balance | 否 |  |  |
| 20 | duty_used_bail | 否 |  |  |
| 21 | occuped_balance | 否 |  |  |
| 22 | prev_balance | 否 |  |  |
| 23 | cost_balance | 否 |  |  |
| 24 | all_occuped_amount | 否 |  |  |
| 25 | all_hold_amount | 否 |  |  |
| 26 | count | 否 |  |  |
| 27 | exch_entrust_margin | 否 |  |  |
| 28 | exch_hold_margin | 否 |  |  |
| 29 | order_no | 否 |  |  |
| 30 | partition_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_tradestock_acctstat | ART | 是 | fund_account, exchange_type, stock_account, fund_account, exchange_type, stock_account |
| idx_uopt_tradestock_acctstat | ART | 是 | fund_account, exchange_type, stock_account, fund_account, exchange_type, stock_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_tradestock_acctstat | fund_account, exchange_type, stock_account, fund_account, exchange_type, stock_account |
| idx_uopt_tradestock_acctstat | fund_account, exchange_type, stock_account, fund_account, exchange_type, stock_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-05-09 09:36:15 | V3.0.3.8 | 韦子晗 | 新增partition_no字段 |
| 2024-05-09 09:36:15 | V3.0.3.8 | 韦子晗 | 新增partition_no字段 |

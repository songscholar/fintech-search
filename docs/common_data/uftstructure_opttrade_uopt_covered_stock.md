# uopt_covered_stock - 期权备兑证券持仓表

**表对象ID**: 9618
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | stock_type | 否 |  |  |
| 7 | current_amount | 否 |  |  |
| 8 | enable_amount | 否 |  |  |
| 9 | real_buy_amount | 否 |  |  |
| 10 | real_sell_amount | 否 |  |  |
| 11 | cir_covered_lock_amount | 否 |  |  |
| 12 | uncir_covered_lock_amount | 否 |  |  |
| 13 | covered_short_amount | 否 |  |  |
| 14 | order_no | 否 |  |  |
| 15 | entrust_sell_amount | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | fund_account | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | stock_account | 否 |  |  |
| 20 | stock_code | 否 |  |  |
| 21 | stock_type | 否 |  |  |
| 22 | current_amount | 否 |  |  |
| 23 | enable_amount | 否 |  |  |
| 24 | real_buy_amount | 否 |  |  |
| 25 | real_sell_amount | 否 |  |  |
| 26 | cir_covered_lock_amount | 否 |  |  |
| 27 | uncir_covered_lock_amount | 否 |  |  |
| 28 | covered_short_amount | 否 |  |  |
| 29 | order_no | 否 |  |  |
| 30 | entrust_sell_amount | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_covered_stock | 默认 | 否 | stock_code, stock_code |
| idx_uopt_covered_stock_global | 默认 | 是 | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |
| idx_uopt_covered_stock | 默认 | 否 | stock_code, stock_code |
| idx_uopt_covered_stock_global | 默认 | 是 | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_covered_stock | exchange_type, stock_code, fund_account, stock_account, exchange_type, stock_code, fund_account, stock_account |
| idx_uopt_covered_stock | exchange_type, stock_code, fund_account, stock_account, exchange_type, stock_code, fund_account, stock_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-11 10:13:14 | V3.0.3.18 | 舒来新 | uopt_covered_stock，添加了表字段(entrust_sell_amount);
 |
| 2025-10-09 13:49:06 | V3.0.2.14 | wuxd | 去除差量redo |
| 2026-03-11 10:13:14 | V3.0.3.18 | 舒来新 | uopt_covered_stock，添加了表字段(entrust_sell_amount);
 |
| 2025-10-09 13:49:06 | V3.0.2.14 | wuxd | 去除差量redo |

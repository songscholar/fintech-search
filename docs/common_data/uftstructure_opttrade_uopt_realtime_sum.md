# uopt_realtime_sum - 期权实时成交汇总表

**表对象ID**: 9624
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | option_code | 否 |  | this is uft2.0 |
| 2 | exchange_type | 否 |  | this is uft2.0 |
| 3 | fund_account | 否 |  | this is uft2.0 |
| 4 | stock_account | 否 |  | this is uft2.0 |
| 5 | opthold_type | 否 |  | this is uft2.0 |
| 6 | total_fare | 否 |  | this is uft2.0 |
| 7 | premium | 否 |  | this is uft2.0 |
| 8 | sum_open_balance | 否 |  | this is uft2.0 |
| 9 | sum_drop_balance | 否 |  | this is uft2.0 |
| 10 | order_no | 否 |  | this is uft2.0 |
| 11 | sum_real_buy_fare | 否 |  |  |
| 12 | sum_real_sell_fare | 否 |  |  |
| 13 | partition_no | 否 |  |  |
| 14 | option_code | 否 |  | this is uft2.0 |
| 15 | exchange_type | 否 |  | this is uft2.0 |
| 16 | fund_account | 否 |  | this is uft2.0 |
| 17 | stock_account | 否 |  | this is uft2.0 |
| 18 | opthold_type | 否 |  | this is uft2.0 |
| 19 | total_fare | 否 |  | this is uft2.0 |
| 20 | premium | 否 |  | this is uft2.0 |
| 21 | sum_open_balance | 否 |  | this is uft2.0 |
| 22 | sum_drop_balance | 否 |  | this is uft2.0 |
| 23 | order_no | 否 |  | this is uft2.0 |
| 24 | sum_real_buy_fare | 否 |  |  |
| 25 | sum_real_sell_fare | 否 |  |  |
| 26 | partition_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_realtime_sum | 默认 | 是 | option_code, exchange_type, fund_account, stock_account, opthold_type, option_code, exchange_type, fund_account, stock_account, opthold_type |
| idx_uopt_realtime_sum | 默认 | 是 | option_code, exchange_type, fund_account, stock_account, opthold_type, option_code, exchange_type, fund_account, stock_account, opthold_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_realtime_sum | option_code, exchange_type, fund_account, stock_account, opthold_type, option_code, exchange_type, fund_account, stock_account, opthold_type |
| idx_uopt_realtime_sum | option_code, exchange_type, fund_account, stock_account, opthold_type, option_code, exchange_type, fund_account, stock_account, opthold_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-09 13:49:06 | V3.0.2.14 | wuxd | 去除差量redo |
| 2024-05-09 11:08:14 | V3.0.3.10 | 韦子晗 | 增加partition_no字段 |
| 2025-10-09 13:49:06 | V3.0.2.14 | wuxd | 去除差量redo |
| 2024-05-09 11:08:14 | V3.0.3.10 | 韦子晗 | 增加partition_no字段 |

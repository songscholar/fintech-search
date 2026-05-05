# uopt_tradestock_codestat - 期权交易同一标的统计表

**表对象ID**: 9621
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  | this is uft2.0 |
| 2 | exchange_type | 否 |  | this is uft2.0 |
| 3 | stock_account | 否 |  | this is uft2.0 |
| 4 | stock_code | 否 |  | this is uft2.0 |
| 5 | right_hold_quota | 否 |  | this is uft2.0 |
| 6 | total_hold_quota | 否 |  | this is uft2.0 |
| 7 | today_buy_quota | 否 |  | this is uft2.0 |
| 8 | order_no | 否 |  | this is uft2.0 |
| 9 | partition_no | 否 |  |  |
| 10 | fund_account | 否 |  | this is uft2.0 |
| 11 | exchange_type | 否 |  | this is uft2.0 |
| 12 | stock_account | 否 |  | this is uft2.0 |
| 13 | stock_code | 否 |  | this is uft2.0 |
| 14 | right_hold_quota | 否 |  | this is uft2.0 |
| 15 | total_hold_quota | 否 |  | this is uft2.0 |
| 16 | today_buy_quota | 否 |  | this is uft2.0 |
| 17 | order_no | 否 |  | this is uft2.0 |
| 18 | partition_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_tradestock_codestat | ART | 是 | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |
| idx_uopt_tradestock_codestat | ART | 是 | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_tradestock_codestat | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |
| idx_uopt_tradestock_codestat | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-05-09 09:37:01 | V3.0.3.9 | 韦子晗 | 新增partition_no字段 |
| 2024-05-09 09:37:01 | V3.0.3.9 | 韦子晗 | 新增partition_no字段 |

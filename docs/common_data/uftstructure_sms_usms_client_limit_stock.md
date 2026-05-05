# usms_client_limit_stock - 客户限售股信息表(交易管理)

**表对象ID**: 2834
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 是 |  |  |
| 2 | fund_account | 是 |  |  |
| 3 | stock_account | 是 |  |  |
| 4 | exchange_type | 是 |  |  |
| 5 | stock_code | 是 |  |  |
| 6 | total_tax | 是 |  |  |
| 7 | tax_ratio | 是 |  |  |
| 8 | tax_balance | 是 |  |  |
| 9 | tax | 是 |  |  |
| 10 | baseprice_kind | 是 |  |  |
| 11 | cost_price | 是 |  |  |
| 12 | remark | 是 |  |  |
| 13 | modify_date | 是 |  |  |
| 14 | drawback_flag | 是 |  |  |
| 15 | client_id | 是 |  |  |
| 16 | fund_account | 是 |  |  |
| 17 | stock_account | 是 |  |  |
| 18 | exchange_type | 是 |  |  |
| 19 | stock_code | 是 |  |  |
| 20 | total_tax | 是 |  |  |
| 21 | tax_ratio | 是 |  |  |
| 22 | tax_balance | 是 |  |  |
| 23 | tax | 是 |  |  |
| 24 | baseprice_kind | 是 |  |  |
| 25 | cost_price | 是 |  |  |
| 26 | remark | 是 |  |  |
| 27 | modify_date | 是 |  |  |
| 28 | drawback_flag | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usms_client_limit_stock | 默认 | 否 | stock_account, fund_account, stock_code, exchange_type, stock_account, fund_account, stock_code, exchange_type |
| idx_usms_client_limit_stock | 默认 | 是 | stock_account, fund_account, stock_code, exchange_type, stock_account, fund_account, stock_code, exchange_type |
| idx_usms_client_limit_stock | 默认 | 否 | stock_account, fund_account, stock_code, exchange_type, stock_account, fund_account, stock_code, exchange_type |
| idx_usms_client_limit_stock | 默认 | 是 | stock_account, fund_account, stock_code, exchange_type, stock_account, fund_account, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usms_client_limit_stock | stock_account, fund_account, stock_code, exchange_type, stock_account, fund_account, stock_code, exchange_type |
| idx_usms_client_limit_stock | stock_account, fund_account, stock_code, exchange_type, stock_account, fund_account, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-05-08 15:58:41 | 3.0.6.87 |  | 物理表usms_client_limit_stock，增加索引(idx_usms_client_limit_stock:... |
| 2025-05-08 15:58:41 | 3.0.6.87 |  | 物理表usms_client_limit_stock，增加索引(idx_usms_client_limit_stock:... |

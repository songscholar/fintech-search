# client_limit_stock - 客户限售股信息表

**表对象ID**: 5531
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | total_tax | 否 |  |  |
| 7 | tax_ratio | 否 |  |  |
| 8 | tax_balance | 否 |  |  |
| 9 | tax | 否 |  |  |
| 10 | baseprice_kind | 否 |  |  |
| 11 | cost_price | 否 |  |  |
| 12 | remark | 否 |  |  |
| 13 | modify_date | 否 |  |  |
| 14 | drawback_flag | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | fund_account | 否 |  |  |
| 17 | stock_account | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | stock_code | 否 |  |  |
| 20 | total_tax | 否 |  |  |
| 21 | tax_ratio | 否 |  |  |
| 22 | tax_balance | 否 |  |  |
| 23 | tax | 否 |  |  |
| 24 | baseprice_kind | 否 |  |  |
| 25 | cost_price | 否 |  |  |
| 26 | remark | 否 |  |  |
| 27 | modify_date | 否 |  |  |
| 28 | drawback_flag | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_client_limit_stock | ART | 是 | stock_account, fund_account, stock_code, exchange_type, stock_account, fund_account, stock_code, exchange_type |
| idx_secuclt_limit_stock_acct | ART | 是 | fund_account, fund_account |
| idx_client_limit_stock | ART | 是 | stock_account, fund_account, stock_code, exchange_type, stock_account, fund_account, stock_code, exchange_type |
| idx_secuclt_limit_stock_acct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_client_limit_stock | stock_account, fund_account, stock_code, exchange_type, stock_account, fund_account, stock_code, exchange_type |
| idx_client_limit_stock | stock_account, fund_account, stock_code, exchange_type, stock_account, fund_account, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:49:41 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2026-03-09 13:49:41 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |

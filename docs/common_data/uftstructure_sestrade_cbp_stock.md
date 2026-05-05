# cbp_stock - 综合业务股份表

**表对象ID**: 5550
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | sum_buy_amount | 否 |  |  |
| 8 | sum_sell_amount | 否 |  |  |
| 9 | business_frozen_amount | 否 |  |  |
| 10 | cbp_frozen_amount | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | client_id | 否 |  |  |
| 13 | branch_no | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | stock_account | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | sum_buy_amount | 否 |  |  |
| 18 | sum_sell_amount | 否 |  |  |
| 19 | business_frozen_amount | 否 |  |  |
| 20 | cbp_frozen_amount | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_cbpstock | ART | 是 | stock_account, stock_code, branch_no, fund_account, exchange_type, stock_account, stock_code, branch_no, fund_account, exchange_type |
| idx_cbpstock | ART | 是 | stock_account, stock_code, branch_no, fund_account, exchange_type, stock_account, stock_code, branch_no, fund_account, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_cbpstock | stock_account, stock_code, branch_no, fund_account, exchange_type, stock_account, stock_code, branch_no, fund_account, exchange_type |
| idx_cbpstock | stock_account, stock_code, branch_no, fund_account, exchange_type, stock_account, stock_code, branch_no, fund_account, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:03:08 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-03-18 13:41:01 | 3.0.6.11 | 卢杰 | 新增 |
| 2025-03-07 10:28:55 | 3.0.2.62 | 洪略 | 新增 |
| 2026-03-09 14:03:08 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-03-18 13:41:01 | 3.0.6.11 | 卢杰 | 新增 |
| 2025-03-07 10:28:55 | 3.0.2.62 | 洪略 | 新增 |

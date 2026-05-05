# uft_etf_stock - UFTETF股份表

**表对象ID**: 5980
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_account | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | stock_type | 否 |  |  |
| 8 | begin_gap_amount | 否 |  |  |
| 9 | sell_frozen_amount1 | 否 |  |  |
| 10 | sell_real_amount1 | 否 |  |  |
| 11 | buy_real_amount1 | 否 |  |  |
| 12 | sell_frozen_amount2 | 否 |  |  |
| 13 | sell_real_amount2 | 否 |  |  |
| 14 | buy_real_amount2 | 否 |  |  |
| 15 | order_no | 否 |  |  |
| 16 | stock_account | 否 |  |  |
| 17 | stock_code | 否 |  |  |
| 18 | branch_no | 否 |  |  |
| 19 | exchange_type | 否 |  |  |
| 20 | fund_account | 否 |  |  |
| 21 | client_id | 否 |  |  |
| 22 | stock_type | 否 |  |  |
| 23 | begin_gap_amount | 否 |  |  |
| 24 | sell_frozen_amount1 | 否 |  |  |
| 25 | sell_real_amount1 | 否 |  |  |
| 26 | buy_real_amount1 | 否 |  |  |
| 27 | sell_frozen_amount2 | 否 |  |  |
| 28 | sell_real_amount2 | 否 |  |  |
| 29 | buy_real_amount2 | 否 |  |  |
| 30 | order_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uftetfstock | 默认 | 否 |  |
| idx_uftetfstock | ART | 是 | fund_account, stock_account, stock_code, branch_no, exchange_type, fund_account, stock_account, stock_code, branch_no, exchange_type |
| idx_uftetfstock | 默认 | 否 |  |
| idx_uftetfstock | ART | 是 | fund_account, stock_account, stock_code, branch_no, exchange_type, fund_account, stock_account, stock_code, branch_no, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uftetfstock | fund_account, stock_account, stock_code, branch_no, exchange_type, fund_account, stock_account, stock_code, branch_no, exchange_type |
| idx_uftetfstock | fund_account, stock_account, stock_code, branch_no, exchange_type, fund_account, stock_account, stock_code, branch_no, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:52:40 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:27:17 | 3.0.2.104 | taocong45644 | 当前表uft_etf_stock，修改了索引idx_uftetfstock,索引字段修改为：(fund_account,... |
| 2026-03-09 14:52:40 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:27:17 | 3.0.2.104 | taocong45644 | 当前表uft_etf_stock，修改了索引idx_uftetfstock,索引字段修改为：(fund_account,... |

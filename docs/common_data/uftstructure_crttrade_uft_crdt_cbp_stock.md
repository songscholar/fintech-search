# uft_crdt_cbp_stock - UFT信用综合业务股份表

**表对象ID**: 7989
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 22 个）

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
| 11 | order_no | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | client_id | 否 |  |  |
| 14 | branch_no | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_account | 否 |  |  |
| 17 | stock_code | 否 |  |  |
| 18 | sum_buy_amount | 否 |  |  |
| 19 | sum_sell_amount | 否 |  |  |
| 20 | business_frozen_amount | 否 |  |  |
| 21 | cbp_frozen_amount | 否 |  |  |
| 22 | order_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_crdt_cbp_stock | ART | 是 | stock_account, stock_code, branch_no, fund_account, exchange_type, stock_account, stock_code, branch_no, fund_account, exchange_type |
| idx_uft_crdt_cbp_stock_acct | ART | 是 | fund_account, fund_account |
| idx_uft_crdt_cbp_stock | ART | 是 | stock_account, stock_code, branch_no, fund_account, exchange_type, stock_account, stock_code, branch_no, fund_account, exchange_type |
| idx_uft_crdt_cbp_stock_acct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_crdt_cbp_stock | stock_account, stock_code, branch_no, fund_account, exchange_type, stock_account, stock_code, branch_no, fund_account, exchange_type |
| idx_uft_crdt_cbp_stock | stock_account, stock_code, branch_no, fund_account, exchange_type, stock_account, stock_code, branch_no, fund_account, exchange_type |

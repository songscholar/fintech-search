# ucrt_cbp_stock - 信用综合业务股份表

**表对象ID**: 7557
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

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

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdtcbpstock | ART | 是 | stock_account, stock_code, branch_no, fund_account, exchange_type, stock_account, stock_code, branch_no, fund_account, exchange_type |
| idx_crdtcbpstock_acct | ART | 是 | fund_account, fund_account |
| idx_crdtcbpstock | ART | 是 | stock_account, stock_code, branch_no, fund_account, exchange_type, stock_account, stock_code, branch_no, fund_account, exchange_type |
| idx_crdtcbpstock_acct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdtcbpstock | stock_account, stock_code, branch_no, fund_account, exchange_type, stock_account, stock_code, branch_no, fund_account, exchange_type |
| idx_crdtcbpstock | stock_account, stock_code, branch_no, fund_account, exchange_type, stock_account, stock_code, branch_no, fund_account, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-06-03 21:00:00 | 3.0.6.57 | 牟家乐 | 物理表ucrt_cbp_stock，添加了表字段(fund_account);
物理表ucrt_cbp_stock，添... |
| 2025-06-03 21:00:00 | 3.0.6.57 | 牟家乐 | 物理表ucrt_cbp_stock，添加了表字段(fund_account);
物理表ucrt_cbp_stock，添... |

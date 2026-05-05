# uft_cbp_stock - UFT综合业务股份表

**表对象ID**: 5979
**所属模块**: sestrade
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
| idx_uftcbpstock | 默认 | 否 |  |
| idx_uftcbpstock | ART | 是 | stock_account, stock_code, branch_no, fund_account, exchange_type, stock_account, stock_code, branch_no, fund_account, exchange_type |
| idx_uftcbpstock | 默认 | 否 |  |
| idx_uftcbpstock | ART | 是 | stock_account, stock_code, branch_no, fund_account, exchange_type, stock_account, stock_code, branch_no, fund_account, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uftcbpstock | stock_account, stock_code, branch_no, fund_account, exchange_type, stock_account, stock_code, branch_no, fund_account, exchange_type |
| idx_uftcbpstock | stock_account, stock_code, branch_no, fund_account, exchange_type, stock_account, stock_code, branch_no, fund_account, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:52:18 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:26:36 | 3.0.2.104 | taocong45644 | 当前表uft_cbp_stock，修改了索引idx_uftcbpstock,索引字段修改为：(stock_account... |
| 2025-06-03 10:26:44 | 3.0.2.62 | 杨新照 | 物理表uft_cbp_stock，添加了表字段(order_no);
 |
| 2025-03-07 10:28:55 | 3.0.2.62 | 杨新照 | 新增 |
| 2026-03-09 14:52:18 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:26:36 | 3.0.2.104 | taocong45644 | 当前表uft_cbp_stock，修改了索引idx_uftcbpstock,索引字段修改为：(stock_account... |
| 2025-06-03 10:26:44 | 3.0.2.62 | 杨新照 | 物理表uft_cbp_stock，添加了表字段(order_no);
 |
| 2025-03-07 10:28:55 | 3.0.2.62 | 杨新照 | 新增 |

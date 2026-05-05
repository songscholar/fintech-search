# uses_buy_promise - 要约业务表

**表对象ID**: 5516
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | amount | 否 |  |  |
| 2 | clear_date | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | frozen_balance | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | init_date | 否 |  |  |
| 8 | prev_amount | 否 |  |  |
| 9 | prev_status | 否 |  |  |
| 10 | purchase_id | 否 |  |  |
| 11 | status | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | stock_property | 否 |  |  |
| 15 | amount | 否 |  |  |
| 16 | clear_date | 否 |  |  |
| 17 | client_id | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | frozen_balance | 否 |  |  |
| 20 | fund_account | 否 |  |  |
| 21 | init_date | 否 |  |  |
| 22 | prev_amount | 否 |  |  |
| 23 | prev_status | 否 |  |  |
| 24 | purchase_id | 否 |  |  |
| 25 | status | 否 |  |  |
| 26 | stock_account | 否 |  |  |
| 27 | stock_code | 否 |  |  |
| 28 | stock_property | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_buy_promise | ART | 是 | fund_account, exchange_type, stock_account, stock_code, purchase_id, stock_property, fund_account, exchange_type, stock_account, stock_code, purchase_id, stock_property |
| idx_uses_buy_promise_stk | ART | 是 | exchange_type, fund_account, stock_account, stock_code, exchange_type, fund_account, stock_account, stock_code |
| idx_uses_buy_promise | ART | 是 | fund_account, exchange_type, stock_account, stock_code, purchase_id, stock_property, fund_account, exchange_type, stock_account, stock_code, purchase_id, stock_property |
| idx_uses_buy_promise_stk | ART | 是 | exchange_type, fund_account, stock_account, stock_code, exchange_type, fund_account, stock_account, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_buy_promise | fund_account, exchange_type, stock_account, stock_code, purchase_id, stock_property, fund_account, exchange_type, stock_account, stock_code, purchase_id, stock_property |
| idx_uses_buy_promise | fund_account, exchange_type, stock_account, stock_code, purchase_id, stock_property, fund_account, exchange_type, stock_account, stock_code, purchase_id, stock_property |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:42:36 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-29 15:33:33 | 3.0.2.49 | 卢杰 | 物理表uses_buy_promise，添加了表字段(purchase_id);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-09 13:42:36 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-29 15:33:33 | 3.0.2.49 | 卢杰 | 物理表uses_buy_promise，添加了表字段(purchase_id);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

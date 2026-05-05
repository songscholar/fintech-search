# settredo_stock_net - 清算重做股份轧差记录表

**表对象ID**: 5997
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_account | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | trustee_seat_no | 否 |  |  |
| 7 | stocknet_kind | 否 |  |  |
| 8 | prev_amount | 否 |  |  |
| 9 | sett_dml_type | 否 |  |  |
| 10 | sett_batch_no | 否 |  |  |
| 11 | begin_gap_amount | 否 |  |  |
| 12 | buy_real_amount1 | 否 |  |  |
| 13 | buy_real_amount2 | 否 |  |  |
| 14 | stock_account | 否 |  |  |
| 15 | stock_code | 否 |  |  |
| 16 | branch_no | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | fund_account | 否 |  |  |
| 19 | trustee_seat_no | 否 |  |  |
| 20 | stocknet_kind | 否 |  |  |
| 21 | prev_amount | 否 |  |  |
| 22 | sett_dml_type | 否 |  |  |
| 23 | sett_batch_no | 否 |  |  |
| 24 | begin_gap_amount | 否 |  |  |
| 25 | buy_real_amount1 | 否 |  |  |
| 26 | buy_real_amount2 | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_stock_net | ART | 是 | sett_batch_no, stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no, sett_batch_no, stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no |
| idx_settredo_stock_net | ART | 是 | sett_batch_no, stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no, sett_batch_no, stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_stock_net | sett_batch_no, stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no, sett_batch_no, stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no |
| idx_settredo_stock_net | sett_batch_no, stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no, sett_batch_no, stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:57:19 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-09-01 18:49:10 | 3.0.2.1006 | yangxz | 所有表settredo_stock_net，添加了表字段(begin_gap_amount);
所有表settredo... |
| 2025-07-24 09:42:19 | 3.0.2.1005 | yangxz |  |
| 2026-03-09 14:57:19 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-09-01 18:49:10 | 3.0.2.1006 | yangxz | 所有表settredo_stock_net，添加了表字段(begin_gap_amount);
所有表settredo... |
| 2025-07-24 09:42:19 | 3.0.2.1005 | yangxz |  |

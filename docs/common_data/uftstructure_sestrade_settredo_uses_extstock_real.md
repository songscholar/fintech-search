# settredo_uses_extstock_real - 清算重做证券股份交易信息扩展表

**表对象ID**: 5995
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | available_amount | 否 |  |  |
| 3 | frozen_amount | 否 |  |  |
| 4 | unfrozen_amount | 否 |  |  |
| 5 | tradable_amount | 否 |  |  |
| 6 | position_str | 否 |  | branch_no(5)+fund_account(18)+exchange_type(4)+stock_account |
| 7 | sett_dml_type | 否 |  |  |
| 8 | sett_batch_no | 否 |  |  |
| 9 | init_date | 否 |  |  |
| 10 | available_amount | 否 |  |  |
| 11 | frozen_amount | 否 |  |  |
| 12 | unfrozen_amount | 否 |  |  |
| 13 | tradable_amount | 否 |  |  |
| 14 | position_str | 否 |  | branch_no(5)+fund_account(18)+exchange_type(4)+stock_account |
| 15 | sett_dml_type | 否 |  |  |
| 16 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_extstock_pos | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_extstock_pos | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_extstock_pos | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_extstock_pos | sett_batch_no, position_str, sett_batch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:56:32 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-24 09:46:13 | 3.0.6.1008 | yangxz |  |
| 2026-03-09 14:56:32 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-24 09:46:13 | 3.0.6.1008 | yangxz |  |

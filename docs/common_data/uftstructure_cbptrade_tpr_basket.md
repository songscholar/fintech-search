# tpr_basket - 三方回购质押券篮子信息表

**表对象ID**: 2400
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | basket_id | 否 |  |  |
| 4 | basket_name | 否 |  |  |
| 5 | discount_rate | 否 |  |  |
| 6 | bond_end_date | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | stock_type | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | position_str | 否 |  | exchange_type(4)+stock_code(8) |
| 13 | init_date | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | basket_id | 否 |  |  |
| 16 | basket_name | 否 |  |  |
| 17 | discount_rate | 否 |  |  |
| 18 | bond_end_date | 否 |  |  |
| 19 | stock_code | 否 |  |  |
| 20 | stock_type | 否 |  |  |
| 21 | update_date | 否 |  |  |
| 22 | update_time | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | position_str | 否 |  | exchange_type(4)+stock_code(8) |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_tpr_basket_code | 默认 | 否 |  |
| idx_tpr_basket_id | 默认 | 否 |  |
| idx_tpr_basket_code | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_tpr_basket_id | ART | 是 | basket_id, basket_id |
| uk_rpt_tprbasket | ART | 是 | init_date, exchange_type, stock_code, init_date, exchange_type, stock_code |
| idx_tpr_basket_code | 默认 | 否 |  |
| idx_tpr_basket_id | 默认 | 否 |  |
| idx_tpr_basket_code | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_tpr_basket_id | ART | 是 | basket_id, basket_id |
| uk_rpt_tprbasket | ART | 是 | init_date, exchange_type, stock_code, init_date, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_tpr_basket_code | exchange_type, stock_code, exchange_type, stock_code |
| idx_tpr_basket_code | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:44:38 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-12-01 13:53:09 | 3.0.2.75 | taocong45644 | 当前表tpr_basket，修改了索引idx_tpr_basket_code,索引字段修改为：(exchange_typ... |
| 2025-02-20 11:31:34 | V3.0.5.1021 | 李想 | 新增表 |
| 2026-03-04 15:44:38 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-12-01 13:53:09 | 3.0.2.75 | taocong45644 | 当前表tpr_basket，修改了索引idx_tpr_basket_code,索引字段修改为：(exchange_typ... |
| 2025-02-20 11:31:34 | V3.0.5.1021 | 李想 | 新增表 |

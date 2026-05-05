# exch_boardacct_day_data - 转板账户每日全量关系表

**表对象ID**: 5968
**所属模块**: sestrade
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | csdc_stock_account_dest | 否 |  |  |
| 2 | csdc_stock_code | 否 |  |  |
| 3 | csdc_exch_board_type | 否 |  |  |
| 4 | init_date | 否 |  |  |
| 5 | csdc_stock_account_src | 否 |  |  |
| 6 | csdc_seat_no_out | 否 |  |  |
| 7 | position_str | 否 |  | init_date + csdc_exch_board_type + csdc_stock_code + csdc_st |
| 8 | transaction_no | 否 |  |  |
| 9 | csdc_stock_account_dest | 否 |  |  |
| 10 | csdc_stock_code | 否 |  |  |
| 11 | csdc_exch_board_type | 否 |  |  |
| 12 | init_date | 否 |  |  |
| 13 | csdc_stock_account_src | 否 |  |  |
| 14 | csdc_seat_no_out | 否 |  |  |
| 15 | position_str | 否 |  | init_date + csdc_exch_board_type + csdc_stock_code + csdc_st |
| 16 | transaction_no | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_exch_boardacct_day_data | 默认 | 否 |  |
| idx_exch_boardacct_day_data_id | 默认 | 否 | position_str, position_str |
| idx_exch_boardacct_day_data_id | ART | 是 | position_str, position_str |
| idx_rpt_exch_boardacct_day_data_id | ART | 是 | init_date, position_str, init_date, position_str |
| idx_exch_boardacct_day_data | 默认 | 否 |  |
| idx_exch_boardacct_day_data_id | 默认 | 否 | position_str, position_str |
| idx_exch_boardacct_day_data_id | ART | 是 | position_str, position_str |
| idx_rpt_exch_boardacct_day_data_id | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_exch_boardacct_day_data_id | position_str, position_str |
| idx_exch_boardacct_day_data_id | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:47:42 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:28:23 | V3.0.8.21 | 洪略 | 历史表索引加rpt前缀 |
| 2025-11-08 11:06:27 | 3.0.2.104 | 洪略 | 增加历史表 |
| 2025-09-25 11:43:01 | 3.0.2.62 | 洪略 | 添加了表字段(transaction_no)，同时调整表空间为usms，数据存储介质更改为DB+MDB的方式
 |
| 2025-07-24 17:23:44 | 3.0.6.13 | dongh | 物理表exch_boardacct_day_data，添加了表字段(init_date);
物理表exch_board... |
| 2025-02-27 11:20:38 | 3.0.2.61 | 杨森峰 | 表属性调整为不回库 |
| 2024-06-25 10:51:53 | 3.0.2.22 | 杨欣乐 | 新增表 |
| 2026-03-09 14:47:42 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:28:23 | V3.0.8.21 | 洪略 | 历史表索引加rpt前缀 |
| 2025-11-08 11:06:27 | 3.0.2.104 | 洪略 | 增加历史表 |
| 2025-09-25 11:43:01 | 3.0.2.62 | 洪略 | 添加了表字段(transaction_no)，同时调整表空间为usms，数据存储介质更改为DB+MDB的方式
 |
| 2025-07-24 17:23:44 | 3.0.6.13 | dongh | 物理表exch_boardacct_day_data，添加了表字段(init_date);
物理表exch_board... |
| 2025-02-27 11:20:38 | 3.0.2.61 | 杨森峰 | 表属性调整为不回库 |
| 2024-06-25 10:51:53 | 3.0.2.22 | 杨欣乐 | 新增表 |

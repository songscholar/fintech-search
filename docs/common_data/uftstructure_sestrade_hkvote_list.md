# hkvote_list - 港股投票议案详情表

**表对象ID**: 5566
**所属模块**: sestrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | distribute_rate | 否 |  |  |
| 4 | hkvote_ctrlstr | 否 |  |  |
| 5 | vote_group | 否 |  |  |
| 6 | placard_id | 否 |  |  |
| 7 | motion_id | 否 |  |  |
| 8 | sipf_remark | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | position_str | 否 |  | init_date(8)+exchange_type(4)+stock_code(8)+placard_id(20)+m |
| 12 | date_clear | 否 |  |  |
| 13 | vote_multiplier | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | update_date | 否 |  |  |
| 16 | update_time | 否 |  |  |
| 17 | stock_name | 否 | H |  |
| 18 | stock_type | 否 | H |  |
| 19 | sub_stock_type | 否 | H |  |
| 20 | init_date | 否 |  |  |
| 21 | stock_code | 否 |  |  |
| 22 | distribute_rate | 否 |  |  |
| 23 | hkvote_ctrlstr | 否 |  |  |
| 24 | vote_group | 否 |  |  |
| 25 | placard_id | 否 |  |  |
| 26 | motion_id | 否 |  |  |
| 27 | sipf_remark | 否 |  |  |
| 28 | remark | 否 |  |  |
| 29 | exchange_type | 否 |  |  |
| 30 | position_str | 否 |  | init_date(8)+exchange_type(4)+stock_code(8)+placard_id(20)+m |
| 31 | date_clear | 否 |  |  |
| 32 | vote_multiplier | 否 |  |  |
| 33 | transaction_no | 否 |  |  |
| 34 | update_date | 否 |  |  |
| 35 | update_time | 否 |  |  |
| 36 | stock_name | 否 | H |  |
| 37 | stock_type | 否 | H |  |
| 38 | sub_stock_type | 否 | H |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_hkvote_list | 默认 | 否 | exchange_type, stock_code, placard_id, exchange_type, stock_code, placard_id |
| idx_hkvote_list | ART | 是 | exchange_type, stock_code, placard_id, exchange_type, stock_code, placard_id |
| idx_hkvote_list_pos | ART | 是 | position_str, position_str |
| idx_rpt_hkvote_list_pos | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_hkvote_list_code | ART | 是 | exchange_type, stock_code, placard_id, exchange_type, stock_code, placard_id |
| idx_rpt_hkvotelist_tolast | ART | 是 | date_clear, date_clear |
| idx_hkvote_list | 默认 | 否 | exchange_type, stock_code, placard_id, exchange_type, stock_code, placard_id |
| idx_hkvote_list | ART | 是 | exchange_type, stock_code, placard_id, exchange_type, stock_code, placard_id |
| idx_hkvote_list_pos | ART | 是 | position_str, position_str |
| idx_rpt_hkvote_list_pos | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_hkvote_list_code | ART | 是 | exchange_type, stock_code, placard_id, exchange_type, stock_code, placard_id |
| idx_rpt_hkvotelist_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_hkvote_list_pos | position_str, position_str |
| idx_hkvote_list | exchange_type, stock_code, placard_id, exchange_type, stock_code, placard_id |
| idx_hkvote_list_pos | position_str, position_str |
| idx_hkvote_list | exchange_type, stock_code, placard_id, exchange_type, stock_code, placard_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:16:57 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:27:42 | V3.0.8.16 | 洪略 | 历史表索引加rpt前缀 |
| 2025-11-06 16:22:18 | V3.0.2.31 | 洪略 | 新增历史表 |
| 2025-07-17 15:25:27 | 3.0.6.1002 | 常行 | 物理表hkvote_list，增加索引(idx_hkvote_list:[exchange_type,stock_cod... |
| 2025-02-19 13:29:21 | 3.0.6.10 | 李想 | 物理表hkvote_list，添加了表字段(update_date);
物理表hkvote_list，添加了表字段(u... |
| 2024-11-13 14:27:28 | 3.0.5.1060 | 雷玄 | 修改idx_hkvote_list索引为分级索引 |
| 2024-07-26 14:40:03 | 3.0.2.30 | 余世泽 | 新增 |
| 2026-03-09 14:16:57 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:27:42 | V3.0.8.16 | 洪略 | 历史表索引加rpt前缀 |
| 2025-11-06 16:22:18 | V3.0.2.31 | 洪略 | 新增历史表 |
| 2025-07-17 15:25:27 | 3.0.6.1002 | 常行 | 物理表hkvote_list，增加索引(idx_hkvote_list:[exchange_type,stock_cod... |
| 2025-02-19 13:29:21 | 3.0.6.10 | 李想 | 物理表hkvote_list，添加了表字段(update_date);
物理表hkvote_list，添加了表字段(u... |
| 2024-11-13 14:27:28 | 3.0.5.1060 | 雷玄 | 修改idx_hkvote_list索引为分级索引 |
| 2024-07-26 14:40:03 | 3.0.2.30 | 余世泽 | 新增 |

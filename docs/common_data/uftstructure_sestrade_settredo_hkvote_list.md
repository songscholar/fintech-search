# settredo_hkvote_list - 清算重做港股投票议案详情表

**表对象ID**: 5802
**所属模块**: sestrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 30 个）

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
| 11 | position_str | 否 |  |  |
| 12 | date_clear | 否 |  |  |
| 13 | vote_multiplier | 否 |  |  |
| 14 | sett_dml_type | 否 |  |  |
| 15 | sett_batch_no | 否 |  |  |
| 16 | init_date | 否 |  |  |
| 17 | stock_code | 否 |  |  |
| 18 | distribute_rate | 否 |  |  |
| 19 | hkvote_ctrlstr | 否 |  |  |
| 20 | vote_group | 否 |  |  |
| 21 | placard_id | 否 |  |  |
| 22 | motion_id | 否 |  |  |
| 23 | sipf_remark | 否 |  |  |
| 24 | remark | 否 |  |  |
| 25 | exchange_type | 否 |  |  |
| 26 | position_str | 否 |  |  |
| 27 | date_clear | 否 |  |  |
| 28 | vote_multiplier | 否 |  |  |
| 29 | sett_dml_type | 否 |  |  |
| 30 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_hkvote_list_pos | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_hkvote_list_pos | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_hkvote_list_pos | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_hkvote_list_pos | sett_batch_no, position_str, sett_batch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-24 09:49:03 | 3.0.6.1013 | yangxz |  |
| 2025-07-24 09:49:03 | 3.0.6.1013 | yangxz |  |

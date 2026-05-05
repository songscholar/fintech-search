# setttoufthkvotelist - 清算港股投票议案详情表

**表对象ID**: 3037
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | exchange_type | 是 |  |  |
| 3 | stock_code | 是 |  |  |
| 4 | distribute_rate | 是 |  |  |
| 5 | hkvote_ctrlstr | 是 |  |  |
| 6 | vote_group | 是 |  |  |
| 7 | placard_id | 是 |  |  |
| 8 | motion_id | 是 |  |  |
| 9 | sipf_remark | 是 |  |  |
| 10 | remark | 是 |  |  |
| 11 | position_str | 是 |  |  |
| 12 | date_clear | 是 |  |  |
| 13 | vote_multiplier | 是 |  |  |
| 14 | uft_data_change_status | 是 |  |  |
| 15 | init_date | 是 |  |  |
| 16 | exchange_type | 是 |  |  |
| 17 | stock_code | 是 |  |  |
| 18 | distribute_rate | 是 |  |  |
| 19 | hkvote_ctrlstr | 是 |  |  |
| 20 | vote_group | 是 |  |  |
| 21 | placard_id | 是 |  |  |
| 22 | motion_id | 是 |  |  |
| 23 | sipf_remark | 是 |  |  |
| 24 | remark | 是 |  |  |
| 25 | position_str | 是 |  |  |
| 26 | date_clear | 是 |  |  |
| 27 | vote_multiplier | 是 |  |  |
| 28 | uft_data_change_status | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_setthkvotelist_pos | 默认 | 是 | position_str, position_str |
| idx_setthkvotelist_stock | 默认 | 是 | stock_code, exchange_type, placard_id, stock_code, exchange_type, placard_id |
| idx_setthkvotelist_pos | 默认 | 是 | position_str, position_str |
| idx_setthkvotelist_stock | 默认 | 是 | stock_code, exchange_type, placard_id, stock_code, exchange_type, placard_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_setthkvotelist_pos | position_str, position_str |
| idx_setthkvotelist_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2020-07-13 20:29 | 8.26.1.86 | 曾哲 | 增加vote_multiplier字段 |
| 2018-06-28 14:50 | 8.26.1.30 | 曾哲 | 新增 |
| 2020-07-13 20:29 | 8.26.1.86 | 曾哲 | 增加vote_multiplier字段 |
| 2018-06-28 14:50 | 8.26.1.30 | 曾哲 | 新增 |

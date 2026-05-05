# usps_cfare2seg - 融资融券后台费用分段表

**表对象ID**: 71
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | aim_value | 否 |  |  |
| 2 | balance_ratio | 否 |  |  |
| 3 | max_fare | 否 |  |  |
| 4 | min_fare | 否 |  |  |
| 5 | par_ratio | 否 |  |  |
| 6 | seg_order | 否 |  |  |
| 7 | segment_kind | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | position_str | 否 |  | segment_kind(10)+seg_order(10) |
| 12 | aim_value | 否 |  |  |
| 13 | balance_ratio | 否 |  |  |
| 14 | max_fare | 否 |  |  |
| 15 | min_fare | 否 |  |  |
| 16 | par_ratio | 否 |  |  |
| 17 | seg_order | 否 |  |  |
| 18 | segment_kind | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | position_str | 否 |  | segment_kind(10)+seg_order(10) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_cfare2seg | ART | 是 | segment_kind, seg_order, segment_kind, seg_order |
| idx_usps_cfare2seg_level | ART | 是 | segment_kind, aim_value, segment_kind, aim_value |
| idx_usps_cfare2seg | ART | 是 | segment_kind, seg_order, segment_kind, seg_order |
| idx_usps_cfare2seg_level | ART | 是 | segment_kind, aim_value, segment_kind, aim_value |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_cfare2seg | segment_kind, seg_order, segment_kind, seg_order |
| idx_usps_cfare2seg | segment_kind, seg_order, segment_kind, seg_order |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-14 09:56:52 | 3.0.6.20 | 李想 | 物理表usps_cfare2seg，添加了表字段(update_date);
物理表usps_cfare2seg，添加... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-06-13 19:00 | 0.0.0.7 | 汪林 | 新增usps_cfare2seg表 |
| 2025-02-14 09:56:52 | 3.0.6.20 | 李想 | 物理表usps_cfare2seg，添加了表字段(update_date);
物理表usps_cfare2seg，添加... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-06-13 19:00 | 0.0.0.7 | 汪林 | 新增usps_cfare2seg表 |

# usps_bfare2seg - 后台二级费用分段表

**表对象ID**: 8
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

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_bfare2seg_level | 默认 | 否 | segment_kind, aim_value, segment_kind, aim_value |
| idx_usps_bfare2seg | ART | 是 | segment_kind, seg_order, segment_kind, seg_order |
| idx_usps_bfare2seg_level | ART | 是 | segment_kind, aim_value, segment_kind, aim_value |
| idx_usps_bfare2seg_level | 默认 | 否 | segment_kind, aim_value, segment_kind, aim_value |
| idx_usps_bfare2seg | ART | 是 | segment_kind, seg_order, segment_kind, seg_order |
| idx_usps_bfare2seg_level | ART | 是 | segment_kind, aim_value, segment_kind, aim_value |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_bfare2seg | segment_kind, seg_order, segment_kind, seg_order |
| idx_usps_bfare2seg_level | segment_kind, aim_value, segment_kind, aim_value |
| idx_usps_bfare2seg | segment_kind, seg_order, segment_kind, seg_order |
| idx_usps_bfare2seg_level | segment_kind, aim_value, segment_kind, aim_value |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-17 11:10:59 | 3.0.6.1011 | 常行 | 物理表usps_bfare2seg，增加索引(idx_usps_bfare2seg_level:[segment_kin... |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-17 11:11:01 | 3.0.6.52 | 李想 | 物理表usps_bfare2seg，添加了表字段(update_date);
物理表usps_bfare2seg，添加... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 16:00 | 0.0.0.5 | 吴威 | 新增字段transaction_no |
| 2025-07-17 11:10:59 | 3.0.6.1011 | 常行 | 物理表usps_bfare2seg，增加索引(idx_usps_bfare2seg_level:[segment_kin... |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-17 11:11:01 | 3.0.6.52 | 李想 | 物理表usps_bfare2seg，添加了表字段(update_date);
物理表usps_bfare2seg，添加... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 16:00 | 0.0.0.5 | 吴威 | 新增字段transaction_no |

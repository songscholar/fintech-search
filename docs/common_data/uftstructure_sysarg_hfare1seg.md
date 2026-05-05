# hfare1seg - 一级回购费用分段表

**表对象ID**: 124
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | segment_kind | 否 |  |  |
| 2 | seg_order | 否 |  |  |
| 3 | aim_value | 否 |  |  |
| 4 | balance_ratio | 否 |  |  |
| 5 | par_ratio | 否 |  |  |
| 6 | min_fare | 否 |  |  |
| 7 | max_fare | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | position_str | 否 |  | seg_order(10)+segment_kind(10) |
| 12 | segment_kind | 否 |  |  |
| 13 | seg_order | 否 |  |  |
| 14 | aim_value | 否 |  |  |
| 15 | balance_ratio | 否 |  |  |
| 16 | par_ratio | 否 |  |  |
| 17 | min_fare | 否 |  |  |
| 18 | max_fare | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | position_str | 否 |  | seg_order(10)+segment_kind(10) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_hfare1seg | 默认 | 否 |  |
| idx_hfare1seg | ART | 是 | seg_order, segment_kind, seg_order, segment_kind |
| idx_hfare1seg | 默认 | 否 |  |
| idx_hfare1seg | ART | 是 | seg_order, segment_kind, seg_order, segment_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_hfare1seg | seg_order, segment_kind, seg_order, segment_kind |
| idx_hfare1seg | seg_order, segment_kind, seg_order, segment_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:40:27 | 3.0.2.103 | taocong45644 | 当前表hfare1seg，修改了索引idx_hfare1seg,索引字段修改为：(seg_order,segment_k... |
| 2025-02-17 11:01:02 | 3.0.6.50 | 李想 | 新增表 |
| 2025-12-01 14:40:27 | 3.0.2.103 | taocong45644 | 当前表hfare1seg，修改了索引idx_hfare1seg,索引字段修改为：(seg_order,segment_k... |
| 2025-02-17 11:01:02 | 3.0.6.50 | 李想 | 新增表 |

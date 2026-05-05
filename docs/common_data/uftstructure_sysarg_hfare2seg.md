# hfare2seg - 二级回购费用分段表

**表对象ID**: 300
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
| 8 | transaction_no | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | position_str | 否 |  | seg_order(10)+segment_kind(10) |
| 12 | segment_kind | 否 |  |  |
| 13 | seg_order | 否 |  |  |
| 14 | aim_value | 否 |  |  |
| 15 | balance_ratio | 否 |  |  |
| 16 | par_ratio | 否 |  |  |
| 17 | min_fare | 否 |  |  |
| 18 | max_fare | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | position_str | 否 |  | seg_order(10)+segment_kind(10) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_hfare2seg | ART | 是 | seg_order, segment_kind, seg_order, segment_kind |
| idx_hfare2seg | ART | 是 | seg_order, segment_kind, seg_order, segment_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_hfare2seg | seg_order, segment_kind, seg_order, segment_kind |
| idx_hfare2seg | seg_order, segment_kind, seg_order, segment_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-17 11:04:53 | 3.0.6.51 | 李想 | 物理表hfare2seg，添加了表字段(update_date);
物理表hfare2seg，添加了表字段(updat... |
| 2025-02-17 11:04:53 | 3.0.6.51 | 李想 | 物理表hfare2seg，添加了表字段(update_date);
物理表hfare2seg，添加了表字段(updat... |

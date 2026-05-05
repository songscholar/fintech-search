# commmodelseg - 二级佣金模板分段表

**表对象ID**: 332
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | segment_kind | 否 |  |  |
| 2 | seg_order | 否 |  |  |
| 3 | begin_value | 否 |  |  |
| 4 | end_value | 否 |  |  |
| 5 | commcalcu_mode | 否 |  |  |
| 6 | commission_rate | 否 |  |  |
| 7 | netfare0_flag | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | position_str | 否 |  | seg_order(10)+segment_kind(10) |
| 12 | segment_kind | 否 |  |  |
| 13 | seg_order | 否 |  |  |
| 14 | begin_value | 否 |  |  |
| 15 | end_value | 否 |  |  |
| 16 | commcalcu_mode | 否 |  |  |
| 17 | commission_rate | 否 |  |  |
| 18 | netfare0_flag | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | position_str | 否 |  | seg_order(10)+segment_kind(10) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_commmodelseg | ART | 是 | seg_order, segment_kind, seg_order, segment_kind |
| idx_commmodelseg | ART | 是 | seg_order, segment_kind, seg_order, segment_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_commmodelseg | seg_order, segment_kind, seg_order, segment_kind |
| idx_commmodelseg | seg_order, segment_kind, seg_order, segment_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-17 11:23:11 | 3.0.6.56 | 李想 | 物理表commmodelseg，添加了表字段(update_date);
物理表commmodelseg，添加了表字段... |
| 2024-09-26 19:45:00 | 3.0.3.14 |  | 物理表commmodelseg，添加了表字段(transaction_no);
 |
| 2024-09-23 17:18:37 | 3.0.2.15 | 张明月 | 新增 |
| 2025-02-17 11:23:11 | 3.0.6.56 | 李想 | 物理表commmodelseg，添加了表字段(update_date);
物理表commmodelseg，添加了表字段... |
| 2024-09-26 19:45:00 | 3.0.3.14 |  | 物理表commmodelseg，添加了表字段(transaction_no);
 |
| 2024-09-23 17:18:37 | 3.0.2.15 | 张明月 | 新增 |

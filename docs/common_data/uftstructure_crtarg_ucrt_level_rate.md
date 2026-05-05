# ucrt_level_rate - 信用等级保证金比例表

**表对象ID**: 7024
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | organ_flag | 否 |  |  |
| 2 | crdt_level | 否 |  |  |
| 3 | fin_ratio | 否 |  |  |
| 4 | slo_ratio | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | position_str | 否 |  | organ_flag(1)+crdt_level(10) |
| 9 | organ_flag | 否 |  |  |
| 10 | crdt_level | 否 |  |  |
| 11 | fin_ratio | 否 |  |  |
| 12 | slo_ratio | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | position_str | 否 |  | organ_flag(1)+crdt_level(10) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_level_rate | ART | 是 | organ_flag, crdt_level, organ_flag, crdt_level |
| idx_ucrt_level_rate | ART | 是 | organ_flag, crdt_level, organ_flag, crdt_level |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_level_rate | organ_flag, crdt_level, organ_flag, crdt_level |
| idx_ucrt_level_rate | organ_flag, crdt_level, organ_flag, crdt_level |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-17 15:26:37 | 3.0.6.43 | 李想 | 物理表ucrt_level_rate，添加了表字段(update_date);
物理表ucrt_level_rate，... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:19 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2025-02-17 15:26:37 | 3.0.6.43 | 李想 | 物理表ucrt_level_rate，添加了表字段(update_date);
物理表ucrt_level_rate，... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:19 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |

# uses_serial_counter - 证券流水号计数器

**表对象ID**: 5519
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | serial_counter_no | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | begin_serial_no | 否 |  |  |
| 4 | end_serial_no | 否 |  |  |
| 5 | serial_counter_value | 否 |  |  |
| 6 | active_status | 否 |  |  |
| 7 | partition_no | 否 |  |  |
| 8 | serial_counter_no | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | begin_serial_no | 否 |  |  |
| 11 | end_serial_no | 否 |  |  |
| 12 | serial_counter_value | 否 |  |  |
| 13 | active_status | 否 |  |  |
| 14 | partition_no | 否 |  |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_serial_counter_pn | ART | 是 | serial_counter_no, branch_no, begin_serial_no, partition_no, serial_counter_no, branch_no, begin_serial_no, partition_no |
| idx_uses_serial_counter | 默认 | 否 | partition_no, partition_no |
| idx_uses_serial_counter | ART | 是 | serial_counter_no, branch_no, begin_serial_no, serial_counter_no, branch_no, begin_serial_no |
| idx_uses_serial_counter_status | ART | 是 | serial_counter_no, branch_no, active_status, serial_counter_no, branch_no, active_status |
| idx_uses_serial_counter_pn | ART | 是 | serial_counter_no, branch_no, begin_serial_no, partition_no, serial_counter_no, branch_no, begin_serial_no, partition_no |
| idx_uses_serial_counter_pn | ART | 是 | serial_counter_no, branch_no, begin_serial_no, partition_no, serial_counter_no, branch_no, begin_serial_no, partition_no |
| idx_uses_serial_counter | 默认 | 否 | partition_no, partition_no |
| idx_uses_serial_counter | ART | 是 | serial_counter_no, branch_no, begin_serial_no, serial_counter_no, branch_no, begin_serial_no |
| idx_uses_serial_counter_status | ART | 是 | serial_counter_no, branch_no, active_status, serial_counter_no, branch_no, active_status |
| idx_uses_serial_counter_pn | ART | 是 | serial_counter_no, branch_no, begin_serial_no, partition_no, serial_counter_no, branch_no, begin_serial_no, partition_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_serial_counter | serial_counter_no, branch_no, begin_serial_no, partition_no, serial_counter_no, branch_no, begin_serial_no, partition_no |
| idx_uses_serial_counter | serial_counter_no, branch_no, begin_serial_no, partition_no, serial_counter_no, branch_no, begin_serial_no, partition_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:43:52 | V3.0.2.106 | taocong45644 | 当前表uses_serial_counter，增加索引（ idx_uses_serial_counter_pn:[ser... |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2024-06-25 13:48:42 | 3.0.2.22 | 张鹏飞 | 调整索引idx_uses_serial_counter为分级索引 |
| 2024-05-22 21:25:05 | 3.0.2.10 | 乐闽庭 | 物理表uses_serial_counter，增加索引字段(索引idx_uses_serial_counter:增加了索... |
| 2024-05-22 21:24:36 | 3.0.2.10 | 乐闽庭 | 物理表uses_serial_counter，添加了表字段(partition_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-09 13:43:52 | V3.0.2.106 | taocong45644 | 当前表uses_serial_counter，增加索引（ idx_uses_serial_counter_pn:[ser... |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2024-06-25 13:48:42 | 3.0.2.22 | 张鹏飞 | 调整索引idx_uses_serial_counter为分级索引 |
| 2024-05-22 21:25:05 | 3.0.2.10 | 乐闽庭 | 物理表uses_serial_counter，增加索引字段(索引idx_uses_serial_counter:增加了索... |
| 2024-05-22 21:24:36 | 3.0.2.10 | 乐闽庭 | 物理表uses_serial_counter，添加了表字段(partition_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

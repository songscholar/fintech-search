# uqms_serial_no_records - 申报流水号计数器流水表

**表对象ID**: 1610
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | serial_counter_no | 否 |  |  |
| 2 | partition_no | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | begin_serial_no | 否 |  |  |
| 5 | end_serial_no | 否 |  |  |
| 6 | seat_no | 否 |  |  |
| 7 | serial_counter_no | 否 |  |  |
| 8 | partition_no | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | begin_serial_no | 否 |  |  |
| 11 | end_serial_no | 否 |  |  |
| 12 | seat_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uqms_serial_no_records | ART | 是 | serial_counter_no, partition_no, branch_no, begin_serial_no, serial_counter_no, partition_no, branch_no, begin_serial_no |
| idx_uqms_serial_no_records | ART | 是 | serial_counter_no, partition_no, branch_no, begin_serial_no, serial_counter_no, partition_no, branch_no, begin_serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_serial_no_records | serial_counter_no, partition_no, branch_no, begin_serial_no, serial_counter_no, partition_no, branch_no, begin_serial_no |
| idx_uqms_serial_no_records | serial_counter_no, partition_no, branch_no, begin_serial_no, serial_counter_no, partition_no, branch_no, begin_serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:42:12 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-08-27 15:33:29 | 8.26.2.91 | 汪杰 | 物理表uqms_serial_no_records，添加了表字段(seat_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-29 20:43 | 0.3.3.116 | 杨森峰 | 修改表索引匹配类型 |
| 2026-03-05 16:42:12 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-08-27 15:33:29 | 8.26.2.91 | 汪杰 | 物理表uqms_serial_no_records，添加了表字段(seat_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-29 20:43 | 0.3.3.116 | 杨森峰 | 修改表索引匹配类型 |

# uqms_serial_config - 申报序列配置表

**表对象ID**: 1608
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 6 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | serial_counter_no | 否 |  |  |
| 2 | begin_serial_no | 否 |  |  |
| 3 | serial_assign_counts | 否 |  |  |
| 4 | serial_counter_no | 否 |  |  |
| 5 | begin_serial_no | 否 |  |  |
| 6 | serial_assign_counts | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uqms_serial_config | ART | 是 | serial_counter_no, serial_counter_no |
| idx_uqms_serial_config | ART | 是 | serial_counter_no, serial_counter_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_serial_config | serial_counter_no, serial_counter_no |
| idx_uqms_serial_config | serial_counter_no, serial_counter_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:40:42 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-05 16:40:42 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

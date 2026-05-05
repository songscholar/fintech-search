# usms_serial_counter_cp - 交易管理流水号计数器备份

**表对象ID**: 2851
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | serial_counter_no | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | begin_serial_no | 否 |  |  |
| 4 | end_serial_no | 否 |  |  |
| 5 | serial_counter_value | 否 |  |  |
| 6 | active_status | 否 |  |  |
| 7 | serial_counter_no | 否 |  |  |
| 8 | branch_no | 否 |  |  |
| 9 | begin_serial_no | 否 |  |  |
| 10 | end_serial_no | 否 |  |  |
| 11 | serial_counter_value | 否 |  |  |
| 12 | active_status | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usms_serial_counter_cp | ART | 是 | serial_counter_no, branch_no, serial_counter_no, branch_no |
| idx_usms_serial_counter_cp | ART | 是 | serial_counter_no, branch_no, serial_counter_no, branch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usms_serial_counter_cp | serial_counter_no, branch_no, serial_counter_no, branch_no |
| idx_usms_serial_counter_cp | serial_counter_no, branch_no, serial_counter_no, branch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 09:11:43 | V3.0.2.8 | taocong45644 | 数据存储介质修改为DB |
| 2025-09-16 17:38:53 | V3.0.2.2 | 李奕轩 | 表存储介质改为DB+MDB |
| 2025-08-02 13:42:09 | 3.0.2.1 | 乐闽庭 | 新增表 |
| 2026-03-06 09:11:43 | V3.0.2.8 | taocong45644 | 数据存储介质修改为DB |
| 2025-09-16 17:38:53 | V3.0.2.2 | 李奕轩 | 表存储介质改为DB+MDB |
| 2025-08-02 13:42:09 | 3.0.2.1 | 乐闽庭 | 新增表 |

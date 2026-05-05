# uarg_serial_counter - 参数流水号计数表

**表对象ID**: 105
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

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
| idx_uarg_serial_counter | 默认 | 否 |  |
| idx_uarg_serial_counter_status | 默认 | 否 |  |
| idx_uarg_serial_counter | 默认 | 否 | partition_no, partition_no |
| idx_uarg_serial_counter | ART | 是 | serial_counter_no, branch_no, begin_serial_no, serial_counter_no, branch_no, begin_serial_no |
| idx_uarg_serial_counter_status | ART | 是 | serial_counter_no, branch_no, active_status, serial_counter_no, branch_no, active_status |
| idx_uarg_serial_counter | 默认 | 否 |  |
| idx_uarg_serial_counter_status | 默认 | 否 |  |
| idx_uarg_serial_counter | 默认 | 否 | partition_no, partition_no |
| idx_uarg_serial_counter | ART | 是 | serial_counter_no, branch_no, begin_serial_no, serial_counter_no, branch_no, begin_serial_no |
| idx_uarg_serial_counter_status | ART | 是 | serial_counter_no, branch_no, active_status, serial_counter_no, branch_no, active_status |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_serial_counter | serial_counter_no, branch_no, begin_serial_no, serial_counter_no, branch_no, begin_serial_no |
| idx_uarg_serial_counter | serial_counter_no, branch_no, begin_serial_no, serial_counter_no, branch_no, begin_serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 15:20:30 | 3.0.2.103 | taocong45644 | 当前表uarg_serial_counter，修改了索引idx_uarg_serial_counter,索引字段修改为：... |
| 2025-07-17 14:04:41 | 3.0.6.1017 | 常行 | 物理表uarg_serial_counter，删除索引字段(索引idx_uarg_serial_counter:删除了索... |
| 2025-02-18 18:58:21 | 3.0.6.79 | 李想 | 新增表 |
| 2025-12-01 15:20:30 | 3.0.2.103 | taocong45644 | 当前表uarg_serial_counter，修改了索引idx_uarg_serial_counter,索引字段修改为：... |
| 2025-07-17 14:04:41 | 3.0.6.1017 | 常行 | 物理表uarg_serial_counter，删除索引字段(索引idx_uarg_serial_counter:删除了索... |
| 2025-02-18 18:58:21 | 3.0.6.79 | 李想 | 新增表 |

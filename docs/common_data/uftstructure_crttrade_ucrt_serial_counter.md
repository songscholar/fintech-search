# ucrt_serial_counter - 两融流水号计数器

**表对象ID**: 7549
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
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

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_serial_counter | ART | 是 | serial_counter_no, branch_no, begin_serial_no, serial_counter_no, branch_no, begin_serial_no |
| idx_ucrt_serial_counter_status | ART | 是 | serial_counter_no, branch_no, active_status, serial_counter_no, branch_no, active_status |
| idx_ucrt_serial_counter | ART | 是 | serial_counter_no, branch_no, begin_serial_no, serial_counter_no, branch_no, begin_serial_no |
| idx_ucrt_serial_counter_status | ART | 是 | serial_counter_no, branch_no, active_status, serial_counter_no, branch_no, active_status |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_serial_counter | serial_counter_no, branch_no, begin_serial_no, serial_counter_no, branch_no, begin_serial_no |
| idx_ucrt_serial_counter | serial_counter_no, branch_no, begin_serial_no, serial_counter_no, branch_no, begin_serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

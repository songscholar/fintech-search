# uref_serial_counter - 转融通子系统流水号计数器

**表对象ID**: 6000
**所属模块**: refarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | serial_counter_no | 否 |  |  |
| 3 | serial_counter_value | 否 |  |  |
| 4 | serial_counter_span | 否 |  |  |
| 5 | serial_counter_begin | 否 |  |  |
| 6 | serial_counter_end | 否 |  |  |
| 7 | append_number | 否 |  |  |
| 8 | length_need | 否 |  |  |
| 9 | init_serial_value | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | serial_counter_no | 否 |  |  |
| 12 | serial_counter_value | 否 |  |  |
| 13 | serial_counter_span | 否 |  |  |
| 14 | serial_counter_begin | 否 |  |  |
| 15 | serial_counter_end | 否 |  |  |
| 16 | append_number | 否 |  |  |
| 17 | length_need | 否 |  |  |
| 18 | init_serial_value | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refserialcounter | ART | 是 | serial_counter_no, branch_no, serial_counter_no, branch_no |
| idx_refserialcounter | ART | 是 | serial_counter_no, branch_no, serial_counter_no, branch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_refserialcounter | serial_counter_no, branch_no, serial_counter_no, branch_no |
| idx_refserialcounter | serial_counter_no, branch_no, serial_counter_no, branch_no |

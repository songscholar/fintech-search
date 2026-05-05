# secu_serial_counter - 证券流水号计数器2

**表对象ID**: 5765
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | node_id | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | serial_counter_no | 否 |  |  |
| 4 | serial_counter_value | 否 |  |  |
| 5 | serial_counter_span | 否 |  |  |
| 6 | serial_counter_begin | 否 |  |  |
| 7 | serial_counter_end | 否 |  |  |
| 8 | append_number | 否 |  |  |
| 9 | length_need | 否 |  |  |
| 10 | init_serial_value | 否 |  |  |
| 11 | modify_date | 否 |  |  |
| 12 | node_id | 否 |  |  |
| 13 | branch_no | 否 |  |  |
| 14 | serial_counter_no | 否 |  |  |
| 15 | serial_counter_value | 否 |  |  |
| 16 | serial_counter_span | 否 |  |  |
| 17 | serial_counter_begin | 否 |  |  |
| 18 | serial_counter_end | 否 |  |  |
| 19 | append_number | 否 |  |  |
| 20 | length_need | 否 |  |  |
| 21 | init_serial_value | 否 |  |  |
| 22 | modify_date | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_secu_serial_counter | ART | 是 | serial_counter_no, branch_no, node_id, serial_counter_no, branch_no, node_id |
| idx_secu_serial_counter | ART | 是 | serial_counter_no, branch_no, node_id, serial_counter_no, branch_no, node_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_secu_serial_counter | serial_counter_no, branch_no, node_id, serial_counter_no, branch_no, node_id |
| idx_secu_serial_counter | serial_counter_no, branch_no, node_id, serial_counter_no, branch_no, node_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:43:17 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2026-03-09 14:43:17 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |

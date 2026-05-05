# seq_config - 序列号配置表

**表对象ID**: 501
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | sequence_type | 否 |  |  |
| 2 | serial_counter_no | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | seat_no | 否 |  |  |
| 5 | sequence_increment_lpc | 否 |  |  |
| 6 | sequence_syncinterval_lpc | 否 |  |  |
| 7 | sequence_increment_rpc | 否 |  |  |
| 8 | sequence_syncinterval_rpc | 否 |  |  |
| 9 | sequence_min | 否 |  |  |
| 10 | sequence_max | 否 |  |  |
| 11 | sequence_next | 否 |  |  |
| 12 | join_table_name | 否 |  |  |
| 13 | sequence_type | 否 |  |  |
| 14 | serial_counter_no | 否 |  |  |
| 15 | branch_no | 否 |  |  |
| 16 | seat_no | 否 |  |  |
| 17 | sequence_increment_lpc | 否 |  |  |
| 18 | sequence_syncinterval_lpc | 否 |  |  |
| 19 | sequence_increment_rpc | 否 |  |  |
| 20 | sequence_syncinterval_rpc | 否 |  |  |
| 21 | sequence_min | 否 |  |  |
| 22 | sequence_max | 否 |  |  |
| 23 | sequence_next | 否 |  |  |
| 24 | join_table_name | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_seq_config | ART | 是 | sequence_type, serial_counter_no, branch_no, seat_no, sequence_type, serial_counter_no, branch_no, seat_no |
| idx_seq_config | ART | 是 | sequence_type, serial_counter_no, branch_no, seat_no, sequence_type, serial_counter_no, branch_no, seat_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_seq_config | sequence_type, serial_counter_no, branch_no, seat_no, sequence_type, serial_counter_no, branch_no, seat_no |
| idx_seq_config | sequence_type, serial_counter_no, branch_no, seat_no, sequence_type, serial_counter_no, branch_no, seat_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-03-25 16:52:25 | 3.0.2.81 | 王润雪 | 修改物理索引名 |
| 2025-03-20 18:29:19 | 3.0.2.80 | 程猛 | 新增 |
| 2025-03-25 16:52:25 | 3.0.2.81 | 王润雪 | 修改物理索引名 |
| 2025-03-20 18:29:19 | 3.0.2.80 | 程猛 | 新增 |

# usms_serial_counter - 交易管理流水号计数器

**表对象ID**: 2803
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 6 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | serial_counter_no | 是 |  |  |
| 2 | branch_no | 是 |  |  |
| 3 | serial_counter_value | 是 |  |  |
| 4 | serial_counter_no | 是 |  |  |
| 5 | branch_no | 是 |  |  |
| 6 | serial_counter_value | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usms_serial_counter | 默认 | 是 | serial_counter_no, branch_no, serial_counter_no, branch_no |
| idx_usms_serial_counter | 默认 | 是 | serial_counter_no, branch_no, serial_counter_no, branch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usms_serial_counter | serial_counter_no, branch_no, serial_counter_no, branch_no |
| idx_usms_serial_counter | serial_counter_no, branch_no, serial_counter_no, branch_no |

# transferfare - 非交易过户费用表2

**表对象ID**: 118
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | fare_sub_type | 否 |  |  |
| 3 | transfer_fare1 | 否 |  |  |
| 4 | transfer_fare2 | 否 |  |  |
| 5 | remark | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | position_str | 否 |  | fare_sub_type(1)+exchange_type(4) |
| 10 | exchange_type | 否 |  |  |
| 11 | fare_sub_type | 否 |  |  |
| 12 | transfer_fare1 | 否 |  |  |
| 13 | transfer_fare2 | 否 |  |  |
| 14 | remark | 否 |  |  |
| 15 | update_date | 否 |  |  |
| 16 | update_time | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | position_str | 否 |  | fare_sub_type(1)+exchange_type(4) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_transferfare | 默认 | 否 |  |
| idx_transferfare | ART | 是 | fare_sub_type, exchange_type, fare_sub_type, exchange_type |
| idx_transferfare | 默认 | 否 |  |
| idx_transferfare | ART | 是 | fare_sub_type, exchange_type, fare_sub_type, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_transferfare | fare_sub_type, exchange_type, fare_sub_type, exchange_type |
| idx_transferfare | fare_sub_type, exchange_type, fare_sub_type, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 15:14:36 | 3.0.2.103 | taocong45644 | 当前表transferfare，修改了索引idx_transferfare,索引字段修改为：(fare_sub_type... |
| 2025-02-14 16:11:22 | 3.0.6.36 | 李想 | 新增表 |
| 2025-12-01 15:14:36 | 3.0.2.103 | taocong45644 | 当前表transferfare，修改了索引idx_transferfare,索引字段修改为：(fare_sub_type... |
| 2025-02-14 16:11:22 | 3.0.6.36 | 李想 | 新增表 |

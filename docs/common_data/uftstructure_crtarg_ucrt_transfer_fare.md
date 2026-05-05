# ucrt_transfer_fare - 非交易过户费用表

**表对象ID**: 7034
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fare_sub_type | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | transfer_fare1 | 否 |  |  |
| 4 | transfer_fare2 | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | remark | 否 |  |  |
| 7 | update_date | 否 |  |  |
| 8 | update_time | 否 |  |  |
| 9 | position_str | 否 |  | fare_sub_type(1)+exchange_type(4) |
| 10 | fare_sub_type | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | transfer_fare1 | 否 |  |  |
| 13 | transfer_fare2 | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | remark | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | position_str | 否 |  | fare_sub_type(1)+exchange_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_transfer_fare | ART | 是 | fare_sub_type, exchange_type, fare_sub_type, exchange_type |
| idx_ucrt_transfer_fare | ART | 是 | fare_sub_type, exchange_type, fare_sub_type, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_transfer_fare | fare_sub_type, exchange_type, fare_sub_type, exchange_type |
| idx_ucrt_transfer_fare | fare_sub_type, exchange_type, fare_sub_type, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-24 10:01:15 | 3.0.6.115 |  | 物理表ucrt_transfer_fare，添加了表字段(remark);
物理表ucrt_transfer_fare... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 物理表ucrt_transfer_fare，添加了表字段(position_str);
 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-07-24 10:01:15 | 3.0.6.115 |  | 物理表ucrt_transfer_fare，添加了表字段(remark);
物理表ucrt_transfer_fare... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 物理表ucrt_transfer_fare，添加了表字段(position_str);
 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

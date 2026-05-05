# usps_transfer_fare - 证券非交易过户费用表

**表对象ID**: 93
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fare_sub_type | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | transfer_fare1 | 否 |  |  |
| 4 | transfer_fare2 | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | fare_sub_type | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | transfer_fare1 | 否 |  |  |
| 9 | transfer_fare2 | 否 |  |  |
| 10 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_transfer_fare | ART | 是 | fare_sub_type, exchange_type, fare_sub_type, exchange_type |
| idx_usps_transfer_fare | ART | 是 | fare_sub_type, exchange_type, fare_sub_type, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_transfer_fare | fare_sub_type, exchange_type, fare_sub_type, exchange_type |
| idx_usps_transfer_fare | fare_sub_type, exchange_type, fare_sub_type, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-02 14:48:01 | 3.0.2.81 | 张训华 | 不勾选[不落redo文件] |
| 2024-11-21 13:57:04 | 3.0.5.1005 | 杨涛 | 证券非交易过户费用表不回库 |
| 2024-09-12 16:35:22 | 3.0.3.10 | 沈勋 | 新增表结构 |
| 2025-04-02 14:48:01 | 3.0.2.81 | 张训华 | 不勾选[不落redo文件] |
| 2024-11-21 13:57:04 | 3.0.5.1005 | 杨涛 | 证券非交易过户费用表不回库 |
| 2024-09-12 16:35:22 | 3.0.3.10 | 沈勋 | 新增表结构 |

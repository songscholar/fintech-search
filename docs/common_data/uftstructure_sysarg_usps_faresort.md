# usps_faresort - 佣金类别表

**表对象ID**: 58
**所属模块**: sysarg
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fare_sort | 否 |  |  |
| 2 | en_fare_module | 否 |  |  |
| 3 | fare_deal_type | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | fare_sort | 否 |  |  |
| 6 | en_fare_module | 否 |  |  |
| 7 | fare_deal_type | 否 |  |  |
| 8 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_faresort | ART | 是 | fare_sort, fare_sort |
| idx_faresort | ART | 是 | fare_sort, fare_sort |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_faresort | fare_sort, fare_sort |
| idx_faresort | fare_sort, fare_sort |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

# usps_polling_status - 轮询信息表

**表对象ID**: 12
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | function_no | 否 |  | 对应触发轮询的功能号 |
| 2 | exchange_type | 否 |  |  |
| 3 | time_kind | 否 |  |  |
| 4 | last_check_date | 否 |  |  |
| 5 | last_check_time | 否 |  | 记录上次触发轮询的时间，用于判断加锁超时 |
| 6 | time_order | 否 |  | 记录当前正在执行的time_order |
| 7 | function_no | 否 |  | 对应触发轮询的功能号 |
| 8 | exchange_type | 否 |  |  |
| 9 | time_kind | 否 |  |  |
| 10 | last_check_date | 否 |  |  |
| 11 | last_check_time | 否 |  | 记录上次触发轮询的时间，用于判断加锁超时 |
| 12 | time_order | 否 |  | 记录当前正在执行的time_order |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_polling_status | ART | 是 | function_no, exchange_type, time_kind, function_no, exchange_type, time_kind |
| idx_usps_polling_status | ART | 是 | function_no, exchange_type, time_kind, function_no, exchange_type, time_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_polling_status | function_no, exchange_type, time_kind, function_no, exchange_type, time_kind |
| idx_usps_polling_status | function_no, exchange_type, time_kind, function_no, exchange_type, time_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-09-09 11:00:17 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2024-09-09 11:00:17 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

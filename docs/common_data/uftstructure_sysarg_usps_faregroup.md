# usps_faregroup - 群组佣金类别关系表

**表对象ID**: 57
**所属模块**: sysarg
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | groupfare_type | 否 |  |  |
| 2 | groupfare_object | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | fare_sort | 否 |  |  |
| 5 | begin_date | 否 |  |  |
| 6 | end_date | 否 |  |  |
| 7 | valid_date | 否 |  |  |
| 8 | unen_client_group | 否 |  |  |
| 9 | unen_room_code | 否 |  |  |
| 10 | consultative_flag | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | groupfare_type | 否 |  |  |
| 13 | groupfare_object | 否 |  |  |
| 14 | money_type | 否 |  |  |
| 15 | fare_sort | 否 |  |  |
| 16 | begin_date | 否 |  |  |
| 17 | end_date | 否 |  |  |
| 18 | valid_date | 否 |  |  |
| 19 | unen_client_group | 否 |  |  |
| 20 | unen_room_code | 否 |  |  |
| 21 | consultative_flag | 否 |  |  |
| 22 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_faregroup | ART | 是 | groupfare_type, groupfare_object, money_type, groupfare_type, groupfare_object, money_type |
| idx_usps_faregroup | ART | 是 | groupfare_type, groupfare_object, money_type, groupfare_type, groupfare_object, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_faregroup | groupfare_type, groupfare_object, money_type, groupfare_type, groupfare_object, money_type |
| idx_usps_faregroup | groupfare_type, groupfare_object, money_type, groupfare_type, groupfare_object, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

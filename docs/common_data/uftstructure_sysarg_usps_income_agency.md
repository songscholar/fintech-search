# usps_income_agency - 交易商代码表

**表对象ID**: 77
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | agency_no | 否 |  |  |
| 2 | agency_name | 否 |  |  |
| 3 | short_name | 否 |  |  |
| 4 | status | 否 |  |  |
| 5 | first_agency_flag | 否 |  |  |
| 6 | contact | 否 |  |  |
| 7 | fax | 否 |  |  |
| 8 | telphone | 否 |  |  |
| 9 | zipcode | 否 |  |  |
| 10 | address | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | update_date | 否 |  |  |
| 14 | update_time | 否 |  |  |
| 15 | position_str | 否 |  | agency_no(10)+exchange_type(4) |
| 16 | agency_no | 否 |  |  |
| 17 | agency_name | 否 |  |  |
| 18 | short_name | 否 |  |  |
| 19 | status | 否 |  |  |
| 20 | first_agency_flag | 否 |  |  |
| 21 | contact | 否 |  |  |
| 22 | fax | 否 |  |  |
| 23 | telphone | 否 |  |  |
| 24 | zipcode | 否 |  |  |
| 25 | address | 否 |  |  |
| 26 | exchange_type | 否 |  |  |
| 27 | transaction_no | 否 |  |  |
| 28 | update_date | 否 |  |  |
| 29 | update_time | 否 |  |  |
| 30 | position_str | 否 |  | agency_no(10)+exchange_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_income_agency | ART | 是 | agency_no, exchange_type, agency_no, exchange_type |
| idx_usps_income_agency | ART | 是 | agency_no, exchange_type, agency_no, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_income_agency | agency_no, exchange_type, agency_no, exchange_type |
| idx_usps_income_agency | agency_no, exchange_type, agency_no, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-19 16:32:51 | 3.0.6.102 | 李想 | 物理表usps_income_agency，添加了表字段(update_date);
物理表usps_income_a... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-07-12 17:29 | 0.3.3.13 | 徐世晗 | 新增 |
| 2025-02-19 16:32:51 | 3.0.6.102 | 李想 | 物理表usps_income_agency，添加了表字段(update_date);
物理表usps_income_a... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-07-12 17:29 | 0.3.3.13 | 徐世晗 | 新增 |

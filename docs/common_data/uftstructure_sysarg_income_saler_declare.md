# income_saler_declare - 交易员申报信息表

**表对象ID**: 138
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | serial_no | 否 |  |  |
| 2 | agency_no | 否 |  |  |
| 3 | trader_id | 否 |  |  |
| 4 | trader_name | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | id_kind | 否 |  |  |
| 7 | id_no | 否 |  |  |
| 8 | telphone | 否 |  |  |
| 9 | report_date | 否 |  |  |
| 10 | status | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | serial_no | 否 |  |  |
| 15 | agency_no | 否 |  |  |
| 16 | trader_id | 否 |  |  |
| 17 | trader_name | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | id_kind | 否 |  |  |
| 20 | id_no | 否 |  |  |
| 21 | telphone | 否 |  |  |
| 22 | report_date | 否 |  |  |
| 23 | status | 否 |  |  |
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_income_saler_declare | 默认 | 否 |  |
| idx_income_saler_declare | ART | 是 | serial_no, serial_no |
| idx_income_saler_declare | 默认 | 否 |  |
| idx_income_saler_declare | ART | 是 | serial_no, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_income_saler_declare | serial_no, serial_no |
| idx_income_saler_declare | serial_no, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:43:53 | 3.0.2.103 | taocong45644 | 当前表income_saler_declare，修改了索引idx_income_saler_declare,索引字段修改... |
| 2025-02-19 16:51:17 | 3.0.6.104 | 李想 | 新增表 |
| 2025-12-01 14:43:53 | 3.0.2.103 | taocong45644 | 当前表income_saler_declare，修改了索引idx_income_saler_declare,索引字段修改... |
| 2025-02-19 16:51:17 | 3.0.6.104 | 李想 | 新增表 |

# all_seats - 所有券商席位

**表对象ID**: 132
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | seat_no | 否 |  |  |
| 3 | company_name | 否 |  |  |
| 4 | update_date | 否 |  |  |
| 5 | update_time | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | position_str | 否 |  | exchange_type(4)+seat_no(8) |
| 8 | exchange_type | 否 |  |  |
| 9 | seat_no | 否 |  |  |
| 10 | company_name | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | position_str | 否 |  | exchange_type(4)+seat_no(8) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_all_seats | 默认 | 否 |  |
| idx_all_seats | ART | 是 | exchange_type, seat_no, exchange_type, seat_no |
| idx_all_seats | 默认 | 否 |  |
| idx_all_seats | ART | 是 | exchange_type, seat_no, exchange_type, seat_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_all_seats | exchange_type, seat_no, exchange_type, seat_no |
| idx_all_seats | exchange_type, seat_no, exchange_type, seat_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:36:02 | 3.0.2.103 | taocong45644 | 当前表all_seats，修改了索引idx_all_seats,索引字段修改为：(exchange_type,seat_... |
| 2025-02-19 13:36:02 | 3.0.6.83 | 李想 | 新增表 |
| 2025-12-01 14:36:02 | 3.0.2.103 | taocong45644 | 当前表all_seats，修改了索引idx_all_seats,索引字段修改为：(exchange_type,seat_... |
| 2025-02-19 13:36:02 | 3.0.6.83 | 李想 | 新增表 |

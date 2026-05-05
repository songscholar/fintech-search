# nosettle_date - 非交收日期表

**表对象ID**: 133
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | finance_type | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | init_date | 否 |  |  |
| 4 | update_date | 否 |  |  |
| 5 | update_time | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | position_str | 否 |  | init_date(8)+finance_type(1)+exchange_type(4) |
| 8 | finance_type | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | init_date | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | position_str | 否 |  | init_date(8)+finance_type(1)+exchange_type(4) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_nosettle_date | 默认 | 否 |  |
| idx_nosettle_date | ART | 是 | init_date, finance_type, exchange_type, init_date, finance_type, exchange_type |
| idx_nosettle_date | 默认 | 否 |  |
| idx_nosettle_date | ART | 是 | init_date, finance_type, exchange_type, init_date, finance_type, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_nosettle_date | init_date, finance_type, exchange_type, init_date, finance_type, exchange_type |
| idx_nosettle_date | init_date, finance_type, exchange_type, init_date, finance_type, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:46:58 | 3.0.2.103 | taocong45644 | 当前表nosettle_date，修改了索引idx_nosettle_date,索引字段修改为：(init_date,f... |
| 2025-02-19 13:37:44 | 3.0.6.84 | 李想 | 新增表 |
| 2025-12-01 14:46:58 | 3.0.2.103 | taocong45644 | 当前表nosettle_date，修改了索引idx_nosettle_date,索引字段修改为：(init_date,f... |
| 2025-02-19 13:37:44 | 3.0.6.84 | 李想 | 新增表 |

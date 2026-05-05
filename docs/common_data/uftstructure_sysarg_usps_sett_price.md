# usps_sett_price - 证券清算行情表

**表对象ID**: 385
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | init_date | 否 |  |  |
| 4 | last_price | 否 |  |  |
| 5 | closing_price | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | init_date | 否 |  |  |
| 9 | last_price | 否 |  |  |
| 10 | closing_price | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_sett_price | ART | 是 | stock_code, exchange_type, init_date, stock_code, exchange_type, init_date |
| idx_usps_sett_price_date | ART | 是 | init_date, init_date |
| idx_usps_sett_price | ART | 是 | stock_code, exchange_type, init_date, stock_code, exchange_type, init_date |
| idx_usps_sett_price_date | ART | 是 | init_date, init_date |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_sett_price | stock_code, exchange_type, init_date, stock_code, exchange_type, init_date |
| idx_usps_sett_price_date | init_date, init_date |
| idx_usps_sett_price | stock_code, exchange_type, init_date, stock_code, exchange_type, init_date |
| idx_usps_sett_price_date | init_date, init_date |

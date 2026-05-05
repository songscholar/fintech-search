# settredo_usps_sopt_code - 清算重做自主行权代码表

**表对象ID**: 12326
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | apply_price | 否 |  |  |
| 2 | update_time | 否 |  |  |
| 3 | update_date | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | sopt_code | 否 |  |  |
| 6 | sett_dml_type | 否 |  |  |
| 7 | sett_batch_no | 否 |  |  |
| 8 | apply_price | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | update_date | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | sopt_code | 否 |  |  |
| 13 | sett_dml_type | 否 |  |  |
| 14 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_soptcode | ART | 是 | sett_batch_no, exchange_type, sopt_code, sett_batch_no, exchange_type, sopt_code |
| idx_settredo_soptcode | ART | 是 | sett_batch_no, exchange_type, sopt_code, sett_batch_no, exchange_type, sopt_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_soptcode | sett_batch_no, exchange_type, sopt_code, sett_batch_no, exchange_type, sopt_code |
| idx_settredo_soptcode | sett_batch_no, exchange_type, sopt_code, sett_batch_no, exchange_type, sopt_code |

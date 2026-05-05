# settredo_pre_stock_info - 清算重做原持仓信息表

**表对象ID**: 2514
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | date_clear | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | sett_dml_type | 否 |  |  |
| 8 | sett_batch_no | 否 |  |  |
| 9 | init_date | 否 |  |  |
| 10 | client_id | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | date_clear | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | sett_dml_type | 否 |  |  |
| 16 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_prestockinfo | ART | 是 | sett_batch_no, client_id, exchange_type, stock_code, sett_batch_no, client_id, exchange_type, stock_code |
| idx_settredo_prestockinfo | ART | 是 | sett_batch_no, client_id, exchange_type, stock_code, sett_batch_no, client_id, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_prestockinfo | sett_batch_no, client_id, exchange_type, stock_code, sett_batch_no, client_id, exchange_type, stock_code |
| idx_settredo_prestockinfo | sett_batch_no, client_id, exchange_type, stock_code, sett_batch_no, client_id, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-11 15:13:01 | 8.26.2.94 | 马天宇 | 所有表settredo_pre_stock_info，添加了表字段(init_date);
所有表settredo_p... |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |
| 2025-11-11 15:13:01 | 8.26.2.94 | 马天宇 | 所有表settredo_pre_stock_info，添加了表字段(init_date);
所有表settredo_p... |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |

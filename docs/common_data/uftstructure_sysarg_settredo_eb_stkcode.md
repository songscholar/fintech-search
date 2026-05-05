# settredo_eb_stkcode - 清算重做转板代码信息表

**表对象ID**: 2515
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | eb_date | 否 |  |  |
| 5 | update_date | 否 |  |  |
| 6 | update_time | 否 |  |  |
| 7 | eb_exchange_type | 否 |  |  |
| 8 | eb_stock_code | 否 |  |  |
| 9 | sett_dml_type | 否 |  |  |
| 10 | sett_batch_no | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | position_str | 否 |  |  |
| 13 | init_date | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | stock_code | 否 |  |  |
| 16 | eb_date | 否 |  |  |
| 17 | update_date | 否 |  |  |
| 18 | update_time | 否 |  |  |
| 19 | eb_exchange_type | 否 |  |  |
| 20 | eb_stock_code | 否 |  |  |
| 21 | sett_dml_type | 否 |  |  |
| 22 | sett_batch_no | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | position_str | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_eb_stkcode | ART | 是 | sett_batch_no, eb_exchange_type, eb_stock_code, sett_batch_no, eb_exchange_type, eb_stock_code |
| idx_settredo_eb_stkcode | ART | 是 | sett_batch_no, eb_exchange_type, eb_stock_code, sett_batch_no, eb_exchange_type, eb_stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_eb_stkcode | sett_batch_no, eb_exchange_type, eb_stock_code, sett_batch_no, eb_exchange_type, eb_stock_code |
| idx_settredo_eb_stkcode | sett_batch_no, eb_exchange_type, eb_stock_code, sett_batch_no, eb_exchange_type, eb_stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-10 14:17:48 | 8.26.2.92 | yangxz | 所有表settredo_eb_stkcode，添加了表字段(transaction_no);
所有表settredo_... |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |
| 2025-11-10 14:17:48 | 8.26.2.92 | yangxz | 所有表settredo_eb_stkcode，添加了表字段(transaction_no);
所有表settredo_... |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |

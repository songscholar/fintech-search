# settredo_etb_bond_code - 清算重做互联互通债券代码表

**表对象ID**: 2516
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_name | 否 |  |  |
| 2 | stock_name_bank | 否 |  |  |
| 3 | update_date | 否 |  |  |
| 4 | update_time | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_code_long | 否 |  |  |
| 7 | sett_dml_type | 否 |  |  |
| 8 | sett_batch_no | 否 |  |  |
| 9 | stock_name | 否 |  |  |
| 10 | stock_name_bank | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_code_long | 否 |  |  |
| 15 | sett_dml_type | 否 |  |  |
| 16 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_etb_bond_code | ART | 是 | sett_batch_no, stock_code_long, exchange_type, sett_batch_no, stock_code_long, exchange_type |
| idx_settredo_etb_bond_code | ART | 是 | sett_batch_no, stock_code_long, exchange_type, sett_batch_no, stock_code_long, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_etb_bond_code | sett_batch_no, stock_code_long, exchange_type, sett_batch_no, stock_code_long, exchange_type |
| idx_settredo_etb_bond_code | sett_batch_no, stock_code_long, exchange_type, sett_batch_no, stock_code_long, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |

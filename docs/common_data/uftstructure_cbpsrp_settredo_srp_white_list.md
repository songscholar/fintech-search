# settredo_srp_white_list - 清算重做股票质押白名单表

**表对象ID**: 2656
**所属模块**: cbpsrp
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | sett_dml_type | 否 |  |  |
| 5 | sett_batch_no | 否 |  |  |
| 6 | branch_no | 否 |  |  |
| 7 | client_id | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | sett_dml_type | 否 |  |  |
| 10 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_srpwhitelist | ART | 是 | sett_batch_no, branch_no, client_id, exchange_type, sett_batch_no, branch_no, client_id, exchange_type |
| idx_settredo_srpwhitelist | ART | 是 | sett_batch_no, branch_no, client_id, exchange_type, sett_batch_no, branch_no, client_id, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_srpwhitelist | sett_batch_no, branch_no, client_id, exchange_type, sett_batch_no, branch_no, client_id, exchange_type |
| idx_settredo_srpwhitelist | sett_batch_no, branch_no, client_id, exchange_type, sett_batch_no, branch_no, client_id, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 17:02:56 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |
| 2026-03-06 17:02:56 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |

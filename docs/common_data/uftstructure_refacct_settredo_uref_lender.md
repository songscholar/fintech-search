# settredo_uref_lender - 清算重做转融通出借账户表

**表对象ID**: 6038
**所属模块**: refacct
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | reflender_status | 否 |  |  |
| 2 | position_str | 否 |  |  |
| 3 | sett_dml_type | 否 |  |  |
| 4 | sett_batch_no | 否 |  |  |
| 5 | reflender_status | 否 |  |  |
| 6 | position_str | 否 |  |  |
| 7 | sett_dml_type | 否 |  |  |
| 8 | sett_batch_no | 否 |  |  |
| 9 | reflender_status | 否 |  |  |
| 10 | position_str | 否 |  |  |
| 11 | sett_dml_type | 否 |  |  |
| 12 | sett_batch_no | 否 |  |  |
| 13 | reflender_status | 否 |  |  |
| 14 | position_str | 否 |  |  |
| 15 | sett_dml_type | 否 |  |  |
| 16 | sett_batch_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_reflender | 默认 | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_reflender | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_reflender | 默认 | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_reflender | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_reflender | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_reflender | sett_batch_no, position_str, sett_batch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-13 16:49:49 | 3.0.2.4 | 廖宏玮 | 调整uref_lender在usms做上下场 |
| 2025-08-20 09:33:37 | V3.0.2.1 | 廖宏玮 | 添加表 |
| 2025-08-20 09:33:37 | V3.0.2.1 |  |  |
| 2026-01-13 16:49:49 | 3.0.2.4 | 廖宏玮 | 调整uref_lender在usms做上下场 |
| 2025-08-20 09:33:37 | V3.0.2.1 | 廖宏玮 | 添加表 |
| 2025-08-20 09:33:37 | V3.0.2.1 |  |  |

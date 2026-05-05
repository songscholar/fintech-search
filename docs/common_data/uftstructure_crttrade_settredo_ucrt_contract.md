# settredo_ucrt_contract - 日终清算融资融券合同表

**表对象ID**: 7583
**所属模块**: crttrade
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | contract_id | 否 |  |  |
| 2 | contract_rights | 否 |  |  |
| 3 | contract_status | 否 |  |  |
| 4 | date_clear | 否 |  |  |
| 5 | sett_dml_type | 否 |  |  |
| 6 | sett_batch_no | 否 |  |  |
| 7 | contract_id | 否 |  |  |
| 8 | contract_rights | 否 |  |  |
| 9 | contract_status | 否 |  |  |
| 10 | date_clear | 否 |  |  |
| 11 | sett_dml_type | 否 |  |  |
| 12 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_ucrt_contract_id | ART | 是 | contract_id, sett_batch_no, contract_id, sett_batch_no |
| idx_strd_ucrt_contract_id | ART | 是 | contract_id, sett_batch_no, contract_id, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_ucrt_contract_id | contract_id, sett_batch_no, contract_id, sett_batch_no |
| idx_strd_ucrt_contract_id | contract_id, sett_batch_no, contract_id, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |

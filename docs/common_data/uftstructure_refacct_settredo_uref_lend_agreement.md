# settredo_uref_lend_agreement - 清算重做出借委托代理协议

**表对象ID**: 6039
**所属模块**: refacct
**数据空间**: HS_UFT_DATA

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | agreement_status | 否 |  |  |
| 2 | date_clear | 否 |  |  |
| 3 | used_amount | 否 |  |  |
| 4 | agreement_id | 否 |  |  |
| 5 | sett_dml_type | 否 |  |  |
| 6 | sett_batch_no | 否 |  |  |
| 7 | agreement_status | 否 |  |  |
| 8 | date_clear | 否 |  |  |
| 9 | used_amount | 否 |  |  |
| 10 | agreement_id | 否 |  |  |
| 11 | sett_dml_type | 否 |  |  |
| 12 | sett_batch_no | 否 |  |  |
| 13 | agreement_status | 否 |  |  |
| 14 | date_clear | 否 |  |  |
| 15 | used_amount | 否 |  |  |
| 16 | agreement_id | 否 |  |  |
| 17 | sett_dml_type | 否 |  |  |
| 18 | sett_batch_no | 否 |  |  |
| 19 | agreement_status | 否 |  |  |
| 20 | date_clear | 否 |  |  |
| 21 | used_amount | 否 |  |  |
| 22 | agreement_id | 否 |  |  |
| 23 | sett_dml_type | 否 |  |  |
| 24 | sett_batch_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_reflagreement | 默认 | 是 | sett_batch_no, agreement_id, sett_batch_no, agreement_id |
| idx_settredo_reflagreement | ART | 是 | sett_batch_no, agreement_id, sett_batch_no, agreement_id |
| idx_settredo_reflagreement | 默认 | 是 | sett_batch_no, agreement_id, sett_batch_no, agreement_id |
| idx_settredo_reflagreement | ART | 是 | sett_batch_no, agreement_id, sett_batch_no, agreement_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_reflagreement | sett_batch_no, agreement_id, sett_batch_no, agreement_id |
| idx_settredo_reflagreement | sett_batch_no, agreement_id, sett_batch_no, agreement_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-20 09:34:12 | V3.0.2.1 | 廖宏玮 | 添加表 |
| 2025-08-20 09:34:12 | V3.0.2.1 |  |  |
| 2025-08-20 09:34:12 | V3.0.2.1 | 廖宏玮 | 添加表 |
| 2025-08-20 09:34:12 | V3.0.2.1 |  |  |

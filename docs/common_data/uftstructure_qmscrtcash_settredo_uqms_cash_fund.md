# settredo_uqms_cash_fund - 日终清算头寸资金表

**表对象ID**: 1010
**所属模块**: qmscrtcash
**数据空间**: HS_UFT_DATA

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | cashgroup_no | 否 |  |  |
| 2 | money_type | 否 |  |  |
| 3 | fin_total_balance | 否 |  |  |
| 4 | fin_used_balance | 否 |  |  |
| 5 | ref_due_balance | 否 |  |  |
| 6 | sett_dml_type | 否 |  |  |
| 7 | sett_batch_no | 否 |  |  |
| 8 | enable_balance | 是 |  |  |
| 9 | cash_interest | 是 |  |  |
| 10 | cashgroup_no | 否 |  |  |
| 11 | money_type | 否 |  |  |
| 12 | fin_total_balance | 否 |  |  |
| 13 | fin_used_balance | 否 |  |  |
| 14 | ref_due_balance | 否 |  |  |
| 15 | sett_dml_type | 否 |  |  |
| 16 | sett_batch_no | 否 |  |  |
| 17 | enable_balance | 是 |  |  |
| 18 | cash_interest | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_uqms_cash_fund | ART | 是 | cashgroup_no, money_type, sett_batch_no, cashgroup_no, money_type, sett_batch_no |
| idx_strd_uqms_cash_fund | ART | 是 | cashgroup_no, money_type, sett_batch_no, cashgroup_no, money_type, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_uqms_cash_fund | cashgroup_no, money_type, sett_batch_no, cashgroup_no, money_type, sett_batch_no |
| idx_strd_uqms_cash_fund | cashgroup_no, money_type, sett_batch_no, cashgroup_no, money_type, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:55:28 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-10-11 10:55:27 | 3.0.6.23 | 沈勋 | 所有表settredo_uqms_cash_fund，添加了表字段(enable_balance);
所有表settr... |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2026-03-05 16:55:28 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-10-11 10:55:27 | 3.0.6.23 | 沈勋 | 所有表settredo_uqms_cash_fund，添加了表字段(enable_balance);
所有表settr... |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |

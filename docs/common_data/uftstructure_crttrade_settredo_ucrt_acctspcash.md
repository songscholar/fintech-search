# settredo_ucrt_acctspcash - 日终清算客户专项头寸账户表

**表对象ID**: 7601
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | cashgroup_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | crdt_fare_str | 否 |  |  |
| 5 | fare_main_flag | 否 |  |  |
| 6 | bonusalloc_flag | 否 |  |  |
| 7 | spcash_status | 否 |  |  |
| 8 | spcash_cost_fare | 否 |  |  |
| 9 | sett_batch_no | 否 |  |  |
| 10 | sett_dml_type | 否 |  |  |
| 11 | slo_refcost_fare | 是 |  |  |
| 12 | fin_refcost_fare | 是 |  |  |
| 13 | cashgroup_no | 否 |  |  |
| 14 | client_id | 否 |  |  |
| 15 | fund_account | 否 |  |  |
| 16 | crdt_fare_str | 否 |  |  |
| 17 | fare_main_flag | 否 |  |  |
| 18 | bonusalloc_flag | 否 |  |  |
| 19 | spcash_status | 否 |  |  |
| 20 | spcash_cost_fare | 否 |  |  |
| 21 | sett_batch_no | 否 |  |  |
| 22 | sett_dml_type | 否 |  |  |
| 23 | slo_refcost_fare | 是 |  |  |
| 24 | fin_refcost_fare | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_ucrt_acctspcash | ART | 是 | cashgroup_no, sett_batch_no, cashgroup_no, sett_batch_no |
| idx_strd_ucrt_acctspcash | ART | 是 | cashgroup_no, sett_batch_no, cashgroup_no, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_ucrt_acctspcash | cashgroup_no, sett_batch_no, cashgroup_no, sett_batch_no |
| idx_strd_ucrt_acctspcash | cashgroup_no, sett_batch_no, cashgroup_no, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-25 14:09:58 | 3.0.8.10 | 沈勋 | 所有表settredo_ucrt_acctspcash，添加了表字段(slo_refcost_fare);
所有表se... |
| 2025-09-03 10:21:01 | 3.0.6.1066 | 沈勋 | 新增 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2025-10-25 14:09:58 | 3.0.8.10 | 沈勋 | 所有表settredo_ucrt_acctspcash，添加了表字段(slo_refcost_fare);
所有表se... |
| 2025-09-03 10:21:01 | 3.0.6.1066 | 沈勋 | 新增 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |

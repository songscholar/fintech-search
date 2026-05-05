# settredo_ucrt_pend_fare - 日终清算待扣收表

**表对象ID**: 7603
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | pendfare_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | sett_dml_type | 否 |  |  |
| 4 | sett_batch_no | 否 |  |  |
| 5 | pend_fare | 否 |  |  |
| 6 | date_clear | 否 |  |  |
| 7 | satisfied_discount_flag | 否 |  |  |
| 8 | frozen_balance | 否 |  |  |
| 9 | orig_end_date | 否 |  |  |
| 10 | pend_trans_flag | 否 |  |  |
| 11 | pendfare_id | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | sett_dml_type | 否 |  |  |
| 14 | sett_batch_no | 否 |  |  |
| 15 | pend_fare | 否 |  |  |
| 16 | date_clear | 否 |  |  |
| 17 | satisfied_discount_flag | 否 |  |  |
| 18 | frozen_balance | 否 |  |  |
| 19 | orig_end_date | 否 |  |  |
| 20 | pend_trans_flag | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| strd_idx_ucrt_pend_fare | ART | 是 | fund_account, pendfare_id, sett_batch_no, fund_account, pendfare_id, sett_batch_no |
| strd_idx_ucrt_pend_fare | ART | 是 | fund_account, pendfare_id, sett_batch_no, fund_account, pendfare_id, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| strd_idx_ucrt_pend_fare | fund_account, pendfare_id, sett_batch_no, fund_account, pendfare_id, sett_batch_no |
| strd_idx_ucrt_pend_fare | fund_account, pendfare_id, sett_batch_no, fund_account, pendfare_id, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-22 11:24:21 | 3.0.2.1 | 沈勋 | 新增 |
| 2025-10-22 11:24:21 | 3.0.2.1 | 沈勋 | 新增 |

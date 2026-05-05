# settredo_ucrt_pend_fare_jour - 日终清算待扣收流水表

**表对象ID**: 7589
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | prefer_balance | 否 |  |  |
| 4 | sett_dml_type | 否 |  |  |
| 5 | sett_batch_no | 否 |  |  |
| 6 | fund_account | 是 |  |  |
| 7 | pendfare_id | 是 |  |  |
| 8 | init_date | 否 |  |  |
| 9 | serial_no | 否 |  |  |
| 10 | prefer_balance | 否 |  |  |
| 11 | sett_dml_type | 否 |  |  |
| 12 | sett_batch_no | 否 |  |  |
| 13 | fund_account | 是 |  |  |
| 14 | pendfare_id | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_ucrt_pendfarejour | 默认 | 否 | init_date, serial_no, sett_batch_no, fund_account, pendfare_id, init_date, serial_no, sett_batch_no, fund_account, pendfare_id |
| idx_strd_ucrt_pendfarejour | ART | 是 | init_date, serial_no, sett_batch_no, fund_account, pendfare_id, init_date, serial_no, sett_batch_no, fund_account, pendfare_id |
| idx_strd_ucrt_pendfarejour | 默认 | 否 | init_date, serial_no, sett_batch_no, fund_account, pendfare_id, init_date, serial_no, sett_batch_no, fund_account, pendfare_id |
| idx_strd_ucrt_pendfarejour | ART | 是 | init_date, serial_no, sett_batch_no, fund_account, pendfare_id, init_date, serial_no, sett_batch_no, fund_account, pendfare_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_ucrt_pendfarejour | init_date, serial_no, sett_batch_no, fund_account, pendfare_id, init_date, serial_no, sett_batch_no, fund_account, pendfare_id |
| idx_strd_ucrt_pendfarejour | init_date, serial_no, sett_batch_no, fund_account, pendfare_id, init_date, serial_no, sett_batch_no, fund_account, pendfare_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2025-09-26 11:25:14 | 3.0.6.1072 | 沈勋 | 当前表settredo_ucrt_pend_fare_jour，增加索引(idx_strd_ucrt_pendfarej... |
| 2025-09-26 11:24:20 | 3.0.6.1071 | 沈勋 | 所有表settredo_ucrt_pend_fare_jour，添加了表字段(fund_account);
所有表se... |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2025-09-26 11:25:14 | 3.0.6.1072 | 沈勋 | 当前表settredo_ucrt_pend_fare_jour，增加索引(idx_strd_ucrt_pendfarej... |
| 2025-09-26 11:24:20 | 3.0.6.1071 | 沈勋 | 所有表settredo_ucrt_pend_fare_jour，添加了表字段(fund_account);
所有表se... |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |

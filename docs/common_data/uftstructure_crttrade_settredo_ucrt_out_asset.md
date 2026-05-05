# settredo_ucrt_out_asset - 日终清算信用场外资产信息表

**表对象ID**: 7598
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | out_asset_type | 否 |  |  |
| 5 | out_assure_value | 否 |  |  |
| 6 | begin_out_assure_value | 否 |  |  |
| 7 | valid_date | 否 |  |  |
| 8 | date_clear | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | current_amount | 否 |  |  |
| 12 | assure_ratio | 否 |  |  |
| 13 | sett_dml_type | 否 |  |  |
| 14 | sett_batch_no | 否 |  |  |
| 15 | init_date | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | fund_account | 否 |  |  |
| 18 | out_asset_type | 否 |  |  |
| 19 | out_assure_value | 否 |  |  |
| 20 | begin_out_assure_value | 否 |  |  |
| 21 | valid_date | 否 |  |  |
| 22 | date_clear | 否 |  |  |
| 23 | exchange_type | 否 |  |  |
| 24 | stock_code | 否 |  |  |
| 25 | current_amount | 否 |  |  |
| 26 | assure_ratio | 否 |  |  |
| 27 | sett_dml_type | 否 |  |  |
| 28 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_ucrt_out_asset | ART | 是 | fund_account, out_asset_type, exchange_type, stock_code, sett_batch_no, fund_account, out_asset_type, exchange_type, stock_code, sett_batch_no |
| idx_strd_ucrt_out_asset | ART | 是 | fund_account, out_asset_type, exchange_type, stock_code, sett_batch_no, fund_account, out_asset_type, exchange_type, stock_code, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_ucrt_out_asset | fund_account, out_asset_type, exchange_type, stock_code, sett_batch_no, fund_account, out_asset_type, exchange_type, stock_code, sett_batch_no |
| idx_strd_ucrt_out_asset | fund_account, out_asset_type, exchange_type, stock_code, sett_batch_no, fund_account, out_asset_type, exchange_type, stock_code, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |

# settredo_ucrt_stock_holder - 日终清算融资融券证券账户控制表

**表对象ID**: 7591
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | regflag | 否 |  |  |
| 5 | seat_no | 否 |  |  |
| 6 | stkholder_ctrlstr | 否 |  |  |
| 7 | sett_dml_type | 否 |  |  |
| 8 | sett_batch_no | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | stock_account | 否 |  |  |
| 12 | regflag | 否 |  |  |
| 13 | seat_no | 否 |  |  |
| 14 | stkholder_ctrlstr | 否 |  |  |
| 15 | sett_dml_type | 否 |  |  |
| 16 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_ucrt_stock_holder | ART | 是 | stock_account, exchange_type, fund_account, sett_batch_no, stock_account, exchange_type, fund_account, sett_batch_no |
| idx_strd_ucrt_stock_holder | ART | 是 | stock_account, exchange_type, fund_account, sett_batch_no, stock_account, exchange_type, fund_account, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_ucrt_stock_holder | stock_account, exchange_type, fund_account, sett_batch_no, stock_account, exchange_type, fund_account, sett_batch_no |
| idx_strd_ucrt_stock_holder | stock_account, exchange_type, fund_account, sett_batch_no, stock_account, exchange_type, fund_account, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |

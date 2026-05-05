# settredo_ucrt_surplus_stock - 日终清算余券信息表

**表对象ID**: 7586
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | cashgroup_no | 否 |  |  |
| 5 | current_amount | 否 |  |  |
| 6 | sett_dml_type | 否 |  |  |
| 7 | sett_batch_no | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | cashgroup_no | 否 |  |  |
| 12 | current_amount | 否 |  |  |
| 13 | sett_dml_type | 否 |  |  |
| 14 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_ucrt_surplus_stock | ART | 是 | stock_code, exchange_type, cashgroup_no, fund_account, sett_batch_no, stock_code, exchange_type, cashgroup_no, fund_account, sett_batch_no |
| idx_strd_ucrt_surplus_stock | ART | 是 | stock_code, exchange_type, cashgroup_no, fund_account, sett_batch_no, stock_code, exchange_type, cashgroup_no, fund_account, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_ucrt_surplus_stock | stock_code, exchange_type, cashgroup_no, fund_account, sett_batch_no, stock_code, exchange_type, cashgroup_no, fund_account, sett_batch_no |
| idx_strd_ucrt_surplus_stock | stock_code, exchange_type, cashgroup_no, fund_account, sett_batch_no, stock_code, exchange_type, cashgroup_no, fund_account, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |

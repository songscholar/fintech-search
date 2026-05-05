# settredo_reits_alloc_quota - 清算重做基础设施基金配售额度表

**表对象ID**: 509
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | used_quota | 否 |  |  |
| 6 | sett_batch_no | 否 |  |  |
| 7 | sett_dml_type | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | stock_account | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | used_quota | 否 |  |  |
| 13 | sett_batch_no | 否 |  |  |
| 14 | sett_dml_type | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_sett_reits_alloc_quota | ART | 是 | sett_batch_no, fund_account, stock_account, exchange_type, stock_code, sett_batch_no, fund_account, stock_account, exchange_type, stock_code |
| idx_sett_reits_alloc_quota | ART | 是 | sett_batch_no, fund_account, stock_account, exchange_type, stock_code, sett_batch_no, fund_account, stock_account, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_sett_reits_alloc_quota | sett_batch_no, fund_account, stock_account, exchange_type, stock_code, sett_batch_no, fund_account, stock_account, exchange_type, stock_code |
| idx_sett_reits_alloc_quota | sett_batch_no, fund_account, stock_account, exchange_type, stock_code, sett_batch_no, fund_account, stock_account, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 14:03:00 | V3.0.2.101 | zhangxh | 新增表结构 |
| 2025-11-21 14:03:00 | V3.0.2.101 | zhangxh | 新增表结构 |

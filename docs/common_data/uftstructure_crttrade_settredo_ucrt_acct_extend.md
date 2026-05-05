# settredo_ucrt_acct_extend - 日终清算信用账户扩展信息表

**表对象ID**: 7593
**所属模块**: crttrade
**数据空间**: HS_USMS_DATA
**运行模式**: DB

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | riskcrdt_flag | 否 |  |  |
| 3 | payoff_flag | 否 |  |  |
| 4 | break_times | 否 |  |  |
| 5 | payoff_count | 否 |  |  |
| 6 | black_times | 否 |  |  |
| 7 | sett_dml_type | 否 |  |  |
| 8 | sett_batch_no | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | riskcrdt_flag | 否 |  |  |
| 11 | payoff_flag | 否 |  |  |
| 12 | break_times | 否 |  |  |
| 13 | payoff_count | 否 |  |  |
| 14 | black_times | 否 |  |  |
| 15 | sett_dml_type | 否 |  |  |
| 16 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_ucrt_acct_extend | ART | 是 | fund_account, sett_batch_no, fund_account, sett_batch_no |
| idx_strd_ucrt_acct_extend | ART | 是 | fund_account, sett_batch_no, fund_account, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_ucrt_acct_extend | fund_account, sett_batch_no, fund_account, sett_batch_no |
| idx_strd_ucrt_acct_extend | fund_account, sett_batch_no, fund_account, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |

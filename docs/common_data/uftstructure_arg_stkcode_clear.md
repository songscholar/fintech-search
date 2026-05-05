# stkcode_clear - 过期证券代码清理表

**表对象ID**: 607
**所属模块**: arg
**数据空间**: HS_UARG_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_name | 否 |  |  |
| 5 | stock_type | 否 |  |  |
| 6 | relative_code | 否 |  |  |
| 7 | market_date | 否 |  |  |
| 8 | init_date | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | stock_name | 否 |  |  |
| 12 | stock_type | 否 |  |  |
| 13 | relative_code | 否 |  |  |
| 14 | market_date | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_reloadfundacct | 默认 | 否 | fund_account, fund_account |
| idx_stkcodeclear | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_rpt_stkcodeclear | ART | 是 | init_date, exchange_type, stock_code, init_date, exchange_type, stock_code |
| idx_reloadfundacct | 默认 | 否 | fund_account, fund_account |
| idx_stkcodeclear | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_rpt_stkcodeclear | ART | 是 | init_date, exchange_type, stock_code, init_date, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-03-07 14:21:00 | 3.0.2.77 | 洪略 | 新增 |
| 2025-03-07 14:21:00 | 3.0.2.77 | 洪略 | 新增 |

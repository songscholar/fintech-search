# acct_stkrisk_ratio - 个人流动性风险控制参数表

**表对象ID**: 7097
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | stock_type | 否 |  |  |
| 6 | market_value | 否 |  |  |
| 7 | stock_assets_ratio | 否 |  |  |
| 8 | assurescale_value | 否 |  |  |
| 9 | risk_restriction | 否 |  |  |
| 10 | assure_close_balance | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | position_str | 否 |  | fund_account(18)+stock_code(8)+stock_type(4)+exchange_type(4 |
| 15 | fund_account | 否 |  |  |
| 16 | branch_no | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | stock_type | 否 |  |  |
| 20 | market_value | 否 |  |  |
| 21 | stock_assets_ratio | 否 |  |  |
| 22 | assurescale_value | 否 |  |  |
| 23 | risk_restriction | 否 |  |  |
| 24 | assure_close_balance | 否 |  |  |
| 25 | update_date | 否 |  |  |
| 26 | update_time | 否 |  |  |
| 27 | transaction_no | 否 |  |  |
| 28 | position_str | 否 |  | fund_account(18)+stock_code(8)+stock_type(4)+exchange_type(4 |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_acct_stkrisk_ratio | ART | 是 | fund_account, stock_code, stock_type, exchange_type, fund_account, stock_code, stock_type, exchange_type |
| idx_acct_stkrisk_ratio | ART | 是 | fund_account, stock_code, stock_type, exchange_type, fund_account, stock_code, stock_type, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_acct_stkrisk_ratio | fund_account, stock_code, stock_type, exchange_type, fund_account, stock_code, stock_type, exchange_type |
| idx_acct_stkrisk_ratio | fund_account, stock_code, stock_type, exchange_type, fund_account, stock_code, stock_type, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 13:47:48 | 3.0.6.82 | 李想 | 新增表 |
| 2025-02-18 13:47:48 | 3.0.6.82 | 李想 | 新增表 |

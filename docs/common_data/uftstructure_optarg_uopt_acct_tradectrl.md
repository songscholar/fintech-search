# uopt_acct_tradectrl - 期权客户交易控制参数表

**表对象ID**: 9016
**所属模块**: optarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 是 |  |  |
| 2 | fund_account | 是 |  |  |
| 3 | market_selftrade_flag | 是 |  |  |
| 4 | limit_selftrade_flag | 是 |  |  |
| 5 | update_date | 是 |  |  |
| 6 | update_time | 是 |  |  |
| 7 | remark | 是 |  |  |
| 8 | client_id | 是 |  |  |
| 9 | fund_account | 是 |  |  |
| 10 | market_selftrade_flag | 是 |  |  |
| 11 | limit_selftrade_flag | 是 |  |  |
| 12 | update_date | 是 |  |  |
| 13 | update_time | 是 |  |  |
| 14 | remark | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_acct_tradectrl | 默认 | 是 | fund_account, fund_account |
| idx_uopt_acct_tradectrl | 默认 | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_acct_tradectrl | fund_account, fund_account |
| idx_uopt_acct_tradectrl | fund_account, fund_account |

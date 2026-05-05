# uref_bail_equity_detail - 保证金权益信息明细表

**表对象ID**: 6161
**所属模块**: refsett
**数据空间**: HS_UFT_DATA

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | equity_type | 否 |  |  |
| 5 | recoup_balance | 否 |  |  |
| 6 | recoup_amount | 否 |  |  |
| 7 | register_date | 否 |  |  |
| 8 | dr_date | 否 |  |  |
| 9 | settle_date | 否 |  |  |
| 10 | date_clear | 否 |  |  |
| 11 | stock_account | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | equity_type | 否 |  |  |
| 16 | recoup_balance | 否 |  |  |
| 17 | recoup_amount | 否 |  |  |
| 18 | register_date | 否 |  |  |
| 19 | dr_date | 否 |  |  |
| 20 | settle_date | 否 |  |  |
| 21 | date_clear | 否 |  |  |
| 22 | stock_account | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refbailequitydetail | ART | 是 | fund_account, exchange_type, stock_code, equity_type, fund_account, exchange_type, stock_code, equity_type |
| idx_refbailequitydetail | ART | 是 | fund_account, exchange_type, stock_code, equity_type, fund_account, exchange_type, stock_code, equity_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_refbailequitydetail | fund_account, exchange_type, stock_code, equity_type, fund_account, exchange_type, stock_code, equity_type |
| idx_refbailequitydetail | fund_account, exchange_type, stock_code, equity_type, fund_account, exchange_type, stock_code, equity_type |

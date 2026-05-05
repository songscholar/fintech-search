# ucrt_ipoinfo - 融资融券新股申购信息表

**表对象ID**: 7556
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | lucky_balance | 否 |  |  |
| 7 | unfrozen_balance | 否 |  |  |
| 8 | frozen_balance | 否 |  |  |
| 9 | date_clear | 否 |  |  |
| 10 | frozen_balance_t1 | 否 |  |  |
| 11 | init_date | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | lucky_balance | 否 |  |  |
| 17 | unfrozen_balance | 否 |  |  |
| 18 | frozen_balance | 否 |  |  |
| 19 | date_clear | 否 |  |  |
| 20 | frozen_balance_t1 | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_ipoinfo | ART | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_ucrt_ipoinfo_stock_account | ART | 是 | stock_account, stock_code, stock_account, stock_code |
| idx_ucrt_ipoinfo | ART | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_ucrt_ipoinfo_stock_account | ART | 是 | stock_account, stock_code, stock_account, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_ipoinfo | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_ucrt_ipoinfo | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-01-06 14:58:10 | 3.0.6.28 | 刘景锋 | 新增，数据同步自ucbp_ipoinfo表 |
| 2025-01-06 14:58:10 | 3.0.6.28 | 刘景锋 | 新增，数据同步自ucbp_ipoinfo表 |

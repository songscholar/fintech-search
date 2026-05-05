# settopttradestockacctstat - 清算期权交易同一账户统计表

**表对象ID**: 3227
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 是 |  |  |
| 2 | fund_account | 是 |  |  |
| 3 | exchange_type | 是 |  |  |
| 4 | stock_account | 是 |  |  |
| 5 | duty_used_bail | 是 |  |  |
| 6 | cost_balance | 是 |  |  |
| 7 | exch_hold_margin | 是 |  |  |
| 8 | client_id | 是 |  |  |
| 9 | fund_account | 是 |  |  |
| 10 | exchange_type | 是 |  |  |
| 11 | stock_account | 是 |  |  |
| 12 | duty_used_bail | 是 |  |  |
| 13 | cost_balance | 是 |  |  |
| 14 | exch_hold_margin | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_opttradestockacctstat | 默认 | 是 | client_id, fund_account, exchange_type, client_id, fund_account, exchange_type |
| uk_opttradestockacctstat | 默认 | 是 | client_id, fund_account, exchange_type, client_id, fund_account, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| uk_opttradestockacctstat | client_id, fund_account, exchange_type, client_id, fund_account, exchange_type |
| uk_opttradestockacctstat | client_id, fund_account, exchange_type, client_id, fund_account, exchange_type |

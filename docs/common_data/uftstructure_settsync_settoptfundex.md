# settoptfundex - 清算期权资金拓展信息

**表对象ID**: 3226
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 是 |  |  |
| 2 | fund_account | 是 |  |  |
| 3 | money_type | 是 |  |  |
| 4 | static_margin | 是 |  |  |
| 5 | max_static_margin | 是 |  |  |
| 6 | client_id | 是 |  |  |
| 7 | fund_account | 是 |  |  |
| 8 | money_type | 是 |  |  |
| 9 | static_margin | 是 |  |  |
| 10 | max_static_margin | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settoptfundex | 默认 | 是 | client_id, fund_account, money_type, client_id, fund_account, money_type |
| idx_settoptfundex | 默认 | 是 | client_id, fund_account, money_type, client_id, fund_account, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optsettfundex | client_id, fund_account, money_type, client_id, fund_account, money_type |
| idx_optsettfundex | client_id, fund_account, money_type, client_id, fund_account, money_type |

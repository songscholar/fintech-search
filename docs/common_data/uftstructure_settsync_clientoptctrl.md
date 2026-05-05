# clientoptctrl - 期权适当性导出表

**表对象ID**: 3207
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 是 |  |  |
| 2 | exchange_type | 是 |  |  |
| 3 | fund_account | 是 |  |  |
| 4 | branch_no | 是 |  |  |
| 5 | opt_level | 是 |  |  |
| 6 | en_opt_busi | 是 |  |  |
| 7 | money_type | 是 |  |  |
| 8 | pur_quota | 是 |  |  |
| 9 | begin_date | 是 |  |  |
| 10 | end_date | 是 |  |  |
| 11 | modify_date | 是 |  |  |
| 12 | pre_pur_quota | 是 |  |  |
| 13 | organ_flag | 是 |  |  |
| 14 | client_id | 是 |  |  |
| 15 | exchange_type | 是 |  |  |
| 16 | fund_account | 是 |  |  |
| 17 | branch_no | 是 |  |  |
| 18 | opt_level | 是 |  |  |
| 19 | en_opt_busi | 是 |  |  |
| 20 | money_type | 是 |  |  |
| 21 | pur_quota | 是 |  |  |
| 22 | begin_date | 是 |  |  |
| 23 | end_date | 是 |  |  |
| 24 | modify_date | 是 |  |  |
| 25 | pre_pur_quota | 是 |  |  |
| 26 | organ_flag | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_clientoptctrl | 默认 | 是 | exchange_type, client_id, exchange_type, client_id |
| idx_clientoptctrl | 默认 | 是 | exchange_type, client_id, exchange_type, client_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_clientoptctrl | exchange_type, client_id, exchange_type, client_id |
| idx_clientoptctrl | exchange_type, client_id, exchange_type, client_id |

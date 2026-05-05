# settclientoptctrl - 清算期权客户控制表

**表对象ID**: 3223
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 是 |  |  |
| 2 | node_id | 是 |  |  |
| 3 | sysnode_version | 是 |  |  |
| 4 | exchange_type | 是 |  |  |
| 5 | fund_account | 是 |  |  |
| 6 | branch_no | 是 |  |  |
| 7 | opt_level | 是 |  |  |
| 8 | en_opt_busi | 是 |  |  |
| 9 | money_type | 是 |  |  |
| 10 | pur_quota | 是 |  |  |
| 11 | begin_date | 是 |  |  |
| 12 | end_date | 是 |  |  |
| 13 | modify_date | 是 |  |  |
| 14 | pre_pur_quota | 是 |  |  |
| 15 | organ_flag | 是 |  |  |
| 16 | modify_flag | 是 |  |  |
| 17 | client_id | 是 |  |  |
| 18 | node_id | 是 |  |  |
| 19 | sysnode_version | 是 |  |  |
| 20 | exchange_type | 是 |  |  |
| 21 | fund_account | 是 |  |  |
| 22 | branch_no | 是 |  |  |
| 23 | opt_level | 是 |  |  |
| 24 | en_opt_busi | 是 |  |  |
| 25 | money_type | 是 |  |  |
| 26 | pur_quota | 是 |  |  |
| 27 | begin_date | 是 |  |  |
| 28 | end_date | 是 |  |  |
| 29 | modify_date | 是 |  |  |
| 30 | pre_pur_quota | 是 |  |  |
| 31 | organ_flag | 是 |  |  |
| 32 | modify_flag | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settclientoptctrl | 默认 | 是 | exchange_type, client_id, exchange_type, client_id |
| idx_settclientoptctrl | 默认 | 是 | exchange_type, client_id, exchange_type, client_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settclientoptctrl | exchange_type, client_id, exchange_type, client_id |
| idx_settclientoptctrl | exchange_type, client_id, exchange_type, client_id |

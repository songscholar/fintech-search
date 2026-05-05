# settoptcombhold - 清算期权组合持仓表

**表对象ID**: 3220
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | node_id | 是 |  |  |
| 2 | sysnode_version | 是 |  |  |
| 3 | optcomb_id | 是 |  |  |
| 4 | branch_no | 是 |  |  |
| 5 | fund_account | 是 |  |  |
| 6 | client_id | 是 |  |  |
| 7 | stock_account | 是 |  |  |
| 8 | exchange_type | 是 |  |  |
| 9 | optcomb_code | 是 |  |  |
| 10 | component_count | 是 |  |  |
| 11 | first_option_code | 是 |  |  |
| 12 | first_opthold_type | 是 |  |  |
| 13 | second_option_code | 是 |  |  |
| 14 | second_opthold_type | 是 |  |  |
| 15 | current_amount | 是 |  |  |
| 16 | enable_amount | 是 |  |  |
| 17 | real_comb_amount | 是 |  |  |
| 18 | real_split_amount | 是 |  |  |
| 19 | position_str | 是 |  |  |
| 20 | begin_amount | 是 |  |  |
| 21 | post_current_amount | 是 |  |  |
| 22 | node_id | 是 |  |  |
| 23 | sysnode_version | 是 |  |  |
| 24 | optcomb_id | 是 |  |  |
| 25 | branch_no | 是 |  |  |
| 26 | fund_account | 是 |  |  |
| 27 | client_id | 是 |  |  |
| 28 | stock_account | 是 |  |  |
| 29 | exchange_type | 是 |  |  |
| 30 | optcomb_code | 是 |  |  |
| 31 | component_count | 是 |  |  |
| 32 | first_option_code | 是 |  |  |
| 33 | first_opthold_type | 是 |  |  |
| 34 | second_option_code | 是 |  |  |
| 35 | second_opthold_type | 是 |  |  |
| 36 | current_amount | 是 |  |  |
| 37 | enable_amount | 是 |  |  |
| 38 | real_comb_amount | 是 |  |  |
| 39 | real_split_amount | 是 |  |  |
| 40 | position_str | 是 |  |  |
| 41 | begin_amount | 是 |  |  |
| 42 | post_current_amount | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settoptcombhold | 默认 | 是 | optcomb_id, exchange_type, optcomb_id, exchange_type |
| idx_settoptcombhold | 默认 | 是 | optcomb_id, exchange_type, optcomb_id, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settoptcombhold | optcomb_id, exchange_type, optcomb_id, exchange_type |
| idx_settoptcombhold | optcomb_id, exchange_type, optcomb_id, exchange_type |

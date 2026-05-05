# settoptcoverstock - 清算期权备兑证券持仓表

**表对象ID**: 3222
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | node_id | 是 |  |  |
| 2 | sysnode_version | 是 |  |  |
| 3 | init_date | 是 |  |  |
| 4 | file_type | 是 |  |  |
| 5 | company_no | 是 |  |  |
| 6 | exchange_type | 是 |  |  |
| 7 | branch_no | 是 |  |  |
| 8 | fund_account | 是 |  |  |
| 9 | client_id | 是 |  |  |
| 10 | stock_account | 是 |  |  |
| 11 | stock_code | 是 |  |  |
| 12 | stock_type | 是 |  |  |
| 13 | cir_covered_lock_amount | 是 |  |  |
| 14 | uncir_covered_lock_amount | 是 |  |  |
| 15 | covered_short_amount | 是 |  |  |
| 16 | covered_preshort_amount | 是 |  |  |
| 17 | current_amount | 是 |  |  |
| 18 | enable_amount | 是 |  |  |
| 19 | node_id | 是 |  |  |
| 20 | sysnode_version | 是 |  |  |
| 21 | init_date | 是 |  |  |
| 22 | file_type | 是 |  |  |
| 23 | company_no | 是 |  |  |
| 24 | exchange_type | 是 |  |  |
| 25 | branch_no | 是 |  |  |
| 26 | fund_account | 是 |  |  |
| 27 | client_id | 是 |  |  |
| 28 | stock_account | 是 |  |  |
| 29 | stock_code | 是 |  |  |
| 30 | stock_type | 是 |  |  |
| 31 | cir_covered_lock_amount | 是 |  |  |
| 32 | uncir_covered_lock_amount | 是 |  |  |
| 33 | covered_short_amount | 是 |  |  |
| 34 | covered_preshort_amount | 是 |  |  |
| 35 | current_amount | 是 |  |  |
| 36 | enable_amount | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optsettcoverstock | 默认 | 是 | exchange_type, branch_no, fund_account, stock_account, stock_code, exchange_type, branch_no, fund_account, stock_account, stock_code |
| idx_optsettcoverstock | 默认 | 是 | exchange_type, branch_no, fund_account, stock_account, stock_code, exchange_type, branch_no, fund_account, stock_account, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optsettcoverstock | exchange_type, branch_no, fund_account, stock_account, stock_code, exchange_type, branch_no, fund_account, stock_account, stock_code |
| idx_optsettcoverstock | exchange_type, branch_no, fund_account, stock_account, stock_code, exchange_type, branch_no, fund_account, stock_account, stock_code |

# optstockholder - 期权账户控制导出表

**表对象ID**: 3206
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 是 |  |  |
| 2 | stock_account | 是 |  |  |
| 3 | exchange_type | 是 |  |  |
| 4 | internal_account | 是 |  |  |
| 5 | fund_account | 是 |  |  |
| 6 | client_id | 是 |  |  |
| 7 | main_flag | 是 |  |  |
| 8 | ordinal | 是 |  |  |
| 9 | holder_kind | 是 |  |  |
| 10 | holder_level | 是 |  |  |
| 11 | report_level | 是 |  |  |
| 12 | holder_status | 是 |  |  |
| 13 | holder_rights | 是 |  |  |
| 14 | holder_restriction | 是 |  |  |
| 15 | regflag | 是 |  |  |
| 16 | seat_no | 是 |  |  |
| 17 | bondreg | 是 |  |  |
| 18 | open_date | 是 |  |  |
| 19 | stkholder_ctrlstr | 是 |  |  |
| 20 | branch_no | 是 |  |  |
| 21 | stock_account | 是 |  |  |
| 22 | exchange_type | 是 |  |  |
| 23 | internal_account | 是 |  |  |
| 24 | fund_account | 是 |  |  |
| 25 | client_id | 是 |  |  |
| 26 | main_flag | 是 |  |  |
| 27 | ordinal | 是 |  |  |
| 28 | holder_kind | 是 |  |  |
| 29 | holder_level | 是 |  |  |
| 30 | report_level | 是 |  |  |
| 31 | holder_status | 是 |  |  |
| 32 | holder_rights | 是 |  |  |
| 33 | holder_restriction | 是 |  |  |
| 34 | regflag | 是 |  |  |
| 35 | seat_no | 是 |  |  |
| 36 | bondreg | 是 |  |  |
| 37 | open_date | 是 |  |  |
| 38 | stkholder_ctrlstr | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optstockholder | 默认 | 是 | stock_account, exchange_type, fund_account, branch_no, stock_account, exchange_type, fund_account, branch_no |
| idx_optstockholder | 默认 | 是 | stock_account, exchange_type, fund_account, branch_no, stock_account, exchange_type, fund_account, branch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optstockholder | stock_account, exchange_type, fund_account, branch_no, stock_account, exchange_type, fund_account, branch_no |
| idx_optstockholder | stock_account, exchange_type, fund_account, branch_no, stock_account, exchange_type, fund_account, branch_no |

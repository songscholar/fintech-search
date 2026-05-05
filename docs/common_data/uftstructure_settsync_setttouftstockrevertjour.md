# setttouftstockrevertjour - 清算证券反向操作流水表

**表对象ID**: 3098
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 48 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | serial_no | 是 |  |  |
| 3 | stock_account | 是 |  |  |
| 4 | stock_code | 是 |  |  |
| 5 | branch_no | 是 |  |  |
| 6 | exchange_type | 是 |  |  |
| 7 | curr_date | 是 |  |  |
| 8 | curr_time | 是 |  |  |
| 9 | business_flag | 是 |  |  |
| 10 | op_branch_no | 是 |  |  |
| 11 | operator_no | 是 |  |  |
| 12 | op_station | 是 |  |  |
| 13 | fund_account | 是 |  |  |
| 14 | client_id | 是 |  |  |
| 15 | occur_amount | 是 |  |  |
| 16 | treat_status | 是 |  |  |
| 17 | valid_date | 是 |  |  |
| 18 | position_str | 是 |  |  |
| 19 | client_group | 是 |  |  |
| 20 | room_code | 是 |  |  |
| 21 | money_type | 是 |  |  |
| 22 | stock_type | 是 |  |  |
| 23 | cancel_serialno | 是 |  |  |
| 24 | frozen_reason | 是 |  |  |
| 25 | init_date | 是 |  |  |
| 26 | serial_no | 是 |  |  |
| 27 | stock_account | 是 |  |  |
| 28 | stock_code | 是 |  |  |
| 29 | branch_no | 是 |  |  |
| 30 | exchange_type | 是 |  |  |
| 31 | curr_date | 是 |  |  |
| 32 | curr_time | 是 |  |  |
| 33 | business_flag | 是 |  |  |
| 34 | op_branch_no | 是 |  |  |
| 35 | operator_no | 是 |  |  |
| 36 | op_station | 是 |  |  |
| 37 | fund_account | 是 |  |  |
| 38 | client_id | 是 |  |  |
| 39 | occur_amount | 是 |  |  |
| 40 | treat_status | 是 |  |  |
| 41 | valid_date | 是 |  |  |
| 42 | position_str | 是 |  |  |
| 43 | client_group | 是 |  |  |
| 44 | room_code | 是 |  |  |
| 45 | money_type | 是 |  |  |
| 46 | stock_type | 是 |  |  |
| 47 | cancel_serialno | 是 |  |  |
| 48 | frozen_reason | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settstockrevertjour | 默认 | 是 | serial_no, init_date, serial_no, init_date |
| idx_settstockrevertjour_acct | 默认 | 是 | fund_account, fund_account |
| idx_settstockrevertjour | 默认 | 是 | serial_no, init_date, serial_no, init_date |
| idx_settstockrevertjour_acct | 默认 | 是 | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2020-10-10 10:20 | 8.26.1.97 | 罗佳楠 | 新增 |
| 2020-10-10 10:20 | 8.26.1.97 | 罗佳楠 | 新增 |

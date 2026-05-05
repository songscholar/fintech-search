# setttouftfundrevertjour - 清算资金反向操作流水表

**表对象ID**: 3057
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | serial_no | 是 |  |  |
| 3 | client_id | 是 |  |  |
| 4 | fund_account | 是 |  |  |
| 5 | money_type | 是 |  |  |
| 6 | curr_date | 是 |  |  |
| 7 | curr_time | 是 |  |  |
| 8 | business_flag | 是 |  |  |
| 9 | op_branch_no | 是 |  |  |
| 10 | operator_no | 是 |  |  |
| 11 | op_station | 是 |  |  |
| 12 | branch_no | 是 |  |  |
| 13 | occur_balance | 是 |  |  |
| 14 | post_balance | 是 |  |  |
| 15 | treat_status | 是 |  |  |
| 16 | valid_date | 是 |  |  |
| 17 | frozen_reason | 是 |  |  |
| 18 | remark | 是 |  |  |
| 19 | position_str | 是 |  |  |
| 20 | uft_data_change_status | 是 |  |  |
| 21 | init_date | 是 |  |  |
| 22 | serial_no | 是 |  |  |
| 23 | client_id | 是 |  |  |
| 24 | fund_account | 是 |  |  |
| 25 | money_type | 是 |  |  |
| 26 | curr_date | 是 |  |  |
| 27 | curr_time | 是 |  |  |
| 28 | business_flag | 是 |  |  |
| 29 | op_branch_no | 是 |  |  |
| 30 | operator_no | 是 |  |  |
| 31 | op_station | 是 |  |  |
| 32 | branch_no | 是 |  |  |
| 33 | occur_balance | 是 |  |  |
| 34 | post_balance | 是 |  |  |
| 35 | treat_status | 是 |  |  |
| 36 | valid_date | 是 |  |  |
| 37 | frozen_reason | 是 |  |  |
| 38 | remark | 是 |  |  |
| 39 | position_str | 是 |  |  |
| 40 | uft_data_change_status | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_settfundrevertjour_pos | 默认 | 是 | position_str, position_str |
| idx_settfundrevertjour_fk | 默认 | 是 | fund_account, money_type, fund_account, money_type |
| uk_settfundrevertjour_pos | 默认 | 是 | position_str, position_str |
| idx_settfundrevertjour_fk | 默认 | 是 | fund_account, money_type, fund_account, money_type |

## 数据库索引（共 8 个）

| 索引名 | 字段 |
|--------|------|
| idx_fundrevertjour_pos | position_str, position_str |
| idx_fundrevertjour | init_date, branch_no, serial_no, init_date, branch_no, serial_no |
| idx_fundrevertjour_id | client_id, client_id |
| idx_fundrevertjour_fk | fund_account, money_type, fund_account, money_type |
| idx_fundrevertjour_pos | position_str, position_str |
| idx_fundrevertjour | init_date, branch_no, serial_no, init_date, branch_no, serial_no |
| idx_fundrevertjour_id | client_id, client_id |
| idx_fundrevertjour_fk | fund_account, money_type, fund_account, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2021-05-17 19:24 | 8.26.1.25 | 郑天翔 | 增加settfundrevertjour |
| 2021-05-17 19:24 | 8.26.1.25 | 郑天翔 | 增加settfundrevertjour |

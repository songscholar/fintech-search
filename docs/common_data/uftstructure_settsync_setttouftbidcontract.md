# setttouftbidcontract - 清算分销认购合同表

**表对象ID**: 3042
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 58 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | curr_date | 是 |  |  |
| 3 | curr_time | 是 |  |  |
| 4 | op_entrust_way | 是 |  |  |
| 5 | branch_no | 是 |  |  |
| 6 | fund_account | 是 |  |  |
| 7 | client_id | 是 |  |  |
| 8 | stock_account | 是 |  |  |
| 9 | exchange_type | 是 |  |  |
| 10 | stock_code | 是 |  |  |
| 11 | relative_code | 是 |  |  |
| 12 | money_type | 是 |  |  |
| 13 | contract_id | 是 |  |  |
| 14 | bid_contract_status | 是 |  |  |
| 15 | bid_type | 是 |  |  |
| 16 | bid_rate | 是 |  |  |
| 17 | entrust_amount | 是 |  |  |
| 18 | entrust_balance | 是 |  |  |
| 19 | bid_balance | 是 |  |  |
| 20 | distribute_type | 是 |  |  |
| 21 | winning_rate | 是 |  |  |
| 22 | winning_balance | 是 |  |  |
| 23 | execute_stage | 是 |  |  |
| 24 | date_clear | 是 |  |  |
| 25 | remark | 是 |  |  |
| 26 | position_str | 是 |  |  |
| 27 | bid_frozen_balance | 是 |  |  |
| 28 | uft_data_change_status | 是 |  |  |
| 29 | sett_id | 是 |  |  |
| 30 | init_date | 是 |  |  |
| 31 | curr_date | 是 |  |  |
| 32 | curr_time | 是 |  |  |
| 33 | op_entrust_way | 是 |  |  |
| 34 | branch_no | 是 |  |  |
| 35 | fund_account | 是 |  |  |
| 36 | client_id | 是 |  |  |
| 37 | stock_account | 是 |  |  |
| 38 | exchange_type | 是 |  |  |
| 39 | stock_code | 是 |  |  |
| 40 | relative_code | 是 |  |  |
| 41 | money_type | 是 |  |  |
| 42 | contract_id | 是 |  |  |
| 43 | bid_contract_status | 是 |  |  |
| 44 | bid_type | 是 |  |  |
| 45 | bid_rate | 是 |  |  |
| 46 | entrust_amount | 是 |  |  |
| 47 | entrust_balance | 是 |  |  |
| 48 | bid_balance | 是 |  |  |
| 49 | distribute_type | 是 |  |  |
| 50 | winning_rate | 是 |  |  |
| 51 | winning_balance | 是 |  |  |
| 52 | execute_stage | 是 |  |  |
| 53 | date_clear | 是 |  |  |
| 54 | remark | 是 |  |  |
| 55 | position_str | 是 |  |  |
| 56 | bid_frozen_balance | 是 |  |  |
| 57 | uft_data_change_status | 是 |  |  |
| 58 | sett_id | 是 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settbidcontract | 默认 | 是 | contract_id, contract_id |
| idx_settbidcontract_acct | 默认 | 是 | fund_account, fund_account |
| idx_settbidcontract_exch | 默认 | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_settbidcontract | 默认 | 是 | contract_id, contract_id |
| idx_settbidcontract_acct | 默认 | 是 | fund_account, fund_account |
| idx_settbidcontract_exch | 默认 | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settbidcontract | contract_id, contract_id |
| idx_settbidcontract | contract_id, contract_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2018-09-21 10:15 | 8.26.1.44 | 俞亚君 | 新增 |
| 2018-09-21 10:15 | 8.26.1.44 | 俞亚君 | 新增 |

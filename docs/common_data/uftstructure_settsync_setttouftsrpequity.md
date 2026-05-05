# setttouftsrpequity - 清算股票质押权益表

**表对象ID**: 3024
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 50 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | sett_id | 是 |  |  |
| 3 | contract_id | 是 |  |  |
| 4 | srp_equity_type | 是 |  |  |
| 5 | branch_no | 是 |  |  |
| 6 | fund_account | 是 |  |  |
| 7 | client_id | 是 |  |  |
| 8 | stock_account | 是 |  |  |
| 9 | exchange_type | 是 |  |  |
| 10 | stock_code | 是 |  |  |
| 11 | stock_type | 是 |  |  |
| 12 | money_type | 是 |  |  |
| 13 | register_amount | 是 |  |  |
| 14 | bonus_amount | 是 |  |  |
| 15 | bonus_balance | 是 |  |  |
| 16 | orig_entrust_date | 是 |  |  |
| 17 | orig_entrust_no | 是 |  |  |
| 18 | entrust_date | 是 |  |  |
| 19 | entrust_no | 是 |  |  |
| 20 | deal_status | 是 |  |  |
| 21 | date_clear | 是 |  |  |
| 22 | date_back | 是 |  |  |
| 23 | remark | 是 |  |  |
| 24 | position_str | 是 |  |  |
| 25 | uft_data_change_status | 是 |  |  |
| 26 | init_date | 是 |  |  |
| 27 | sett_id | 是 |  |  |
| 28 | contract_id | 是 |  |  |
| 29 | srp_equity_type | 是 |  |  |
| 30 | branch_no | 是 |  |  |
| 31 | fund_account | 是 |  |  |
| 32 | client_id | 是 |  |  |
| 33 | stock_account | 是 |  |  |
| 34 | exchange_type | 是 |  |  |
| 35 | stock_code | 是 |  |  |
| 36 | stock_type | 是 |  |  |
| 37 | money_type | 是 |  |  |
| 38 | register_amount | 是 |  |  |
| 39 | bonus_amount | 是 |  |  |
| 40 | bonus_balance | 是 |  |  |
| 41 | orig_entrust_date | 是 |  |  |
| 42 | orig_entrust_no | 是 |  |  |
| 43 | entrust_date | 是 |  |  |
| 44 | entrust_no | 是 |  |  |
| 45 | deal_status | 是 |  |  |
| 46 | date_clear | 是 |  |  |
| 47 | date_back | 是 |  |  |
| 48 | remark | 是 |  |  |
| 49 | position_str | 是 |  |  |
| 50 | uft_data_change_status | 是 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settsrpequity_pos | 默认 | 是 | position_str, position_str |
| idx_settsrpequity_id | 默认 | 是 | contract_id, contract_id |
| idx_settsrpequity_orig | 默认 | 是 | orig_entrust_no, orig_entrust_date, orig_entrust_no, orig_entrust_date |
| idx_settsrpequity_pos | 默认 | 是 | position_str, position_str |
| idx_settsrpequity_id | 默认 | 是 | contract_id, contract_id |
| idx_settsrpequity_orig | 默认 | 是 | orig_entrust_no, orig_entrust_date, orig_entrust_no, orig_entrust_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settsrpequity_pos | position_str, position_str |
| idx_settsrpequity_pos | position_str, position_str |

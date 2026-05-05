# setttouftsrpfpreclear - 清算股票质押融出方预入账表

**表对象ID**: 3053
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | serial_no | 是 |  |  |
| 3 | curr_date | 是 |  |  |
| 4 | curr_time | 是 |  |  |
| 5 | branch_no | 是 |  |  |
| 6 | fund_account | 是 |  |  |
| 7 | client_id | 是 |  |  |
| 8 | exchange_type | 是 |  |  |
| 9 | funder_no | 是 |  |  |
| 10 | funder_name | 是 |  |  |
| 11 | contract_id | 是 |  |  |
| 12 | clear_balance | 是 |  |  |
| 13 | business_flag | 是 |  |  |
| 14 | deal_flag | 是 |  |  |
| 15 | date_clear | 是 |  |  |
| 16 | position_str | 是 |  |  |
| 17 | init_date | 是 |  |  |
| 18 | serial_no | 是 |  |  |
| 19 | curr_date | 是 |  |  |
| 20 | curr_time | 是 |  |  |
| 21 | branch_no | 是 |  |  |
| 22 | fund_account | 是 |  |  |
| 23 | client_id | 是 |  |  |
| 24 | exchange_type | 是 |  |  |
| 25 | funder_no | 是 |  |  |
| 26 | funder_name | 是 |  |  |
| 27 | contract_id | 是 |  |  |
| 28 | clear_balance | 是 |  |  |
| 29 | business_flag | 是 |  |  |
| 30 | deal_flag | 是 |  |  |
| 31 | date_clear | 是 |  |  |
| 32 | position_str | 是 |  |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settsrpfpreclear_pos | 默认 | 是 | position_str, position_str |
| idx_settsrpfpreclear_acct | 默认 | 是 | fund_account, fund_account |
| idx_settsrpfpreclear_id | 默认 | 是 | client_id, client_id |
| idx_settsrpfpreclear_con | 默认 | 是 | contract_id, contract_id |
| idx_settsrpfpreclear | 默认 | 是 | serial_no, init_date, serial_no, init_date |
| idx_settsrpfpreclear_pos | 默认 | 是 | position_str, position_str |
| idx_settsrpfpreclear_acct | 默认 | 是 | fund_account, fund_account |
| idx_settsrpfpreclear_id | 默认 | 是 | client_id, client_id |
| idx_settsrpfpreclear_con | 默认 | 是 | contract_id, contract_id |
| idx_settsrpfpreclear | 默认 | 是 | serial_no, init_date, serial_no, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpfpreclear_acct | fund_account, fund_account |
| idx_srpfpreclear_acct | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2022-10-18 17:22 | 8.26.2.37 | 徐世晗 | 新增 |
| 2022-10-18 17:22 | 8.26.2.37 | 徐世晗 | 新增 |

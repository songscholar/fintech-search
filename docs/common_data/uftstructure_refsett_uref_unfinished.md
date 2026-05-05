# uref_unfinished - 转融通在途业务表

**表对象ID**: 6165
**所属模块**: refsett
**数据空间**: HS_UFT_DATA

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | company_no | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | stock_account | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | relative_code | 否 |  |  |
| 11 | equity_type | 否 |  |  |
| 12 | entrust_no | 否 |  |  |
| 13 | cbp_business_id | 否 |  |  |
| 14 | refbusi_code | 否 |  |  |
| 15 | entrust_amount | 否 |  |  |
| 16 | entrust_balance | 否 |  |  |
| 17 | correct_balance | 否 |  |  |
| 18 | date_clear | 否 |  |  |
| 19 | remark | 否 |  |  |
| 20 | position_str | 否 |  |  |
| 21 | csfc_borrow_accttype | 否 |  |  |
| 22 | init_date | 否 |  |  |
| 23 | serial_no | 否 |  |  |
| 24 | company_no | 否 |  |  |
| 25 | exchange_type | 否 |  |  |
| 26 | branch_no | 否 |  |  |
| 27 | client_id | 否 |  |  |
| 28 | fund_account | 否 |  |  |
| 29 | stock_account | 否 |  |  |
| 30 | stock_code | 否 |  |  |
| 31 | relative_code | 否 |  |  |
| 32 | equity_type | 否 |  |  |
| 33 | entrust_no | 否 |  |  |
| 34 | cbp_business_id | 否 |  |  |
| 35 | refbusi_code | 否 |  |  |
| 36 | entrust_amount | 否 |  |  |
| 37 | entrust_balance | 否 |  |  |
| 38 | correct_balance | 否 |  |  |
| 39 | date_clear | 否 |  |  |
| 40 | remark | 否 |  |  |
| 41 | position_str | 否 |  |  |
| 42 | csfc_borrow_accttype | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refunfinished | ART | 是 | serial_no, refbusi_code, init_date, serial_no, refbusi_code, init_date |
| idx_refunfinished_id | ART | 是 | client_id, client_id |
| idx_refunfinished_acct | ART | 是 | fund_account, fund_account |
| idx_refunfinished_pos | ART | 是 | position_str, position_str |
| idx_refunfinished | ART | 是 | serial_no, refbusi_code, init_date, serial_no, refbusi_code, init_date |
| idx_refunfinished_id | ART | 是 | client_id, client_id |
| idx_refunfinished_acct | ART | 是 | fund_account, fund_account |
| idx_refunfinished_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 8 个）

| 索引名 | 字段 |
|--------|------|
| idx_refunfinished | serial_no, refbusi_code, init_date, serial_no, refbusi_code, init_date |
| idx_refunfinished_id | client_id, client_id |
| idx_refunfinished_acct | fund_account, fund_account |
| idx_refunfinished_pos | position_str, position_str |
| idx_refunfinished | serial_no, refbusi_code, init_date, serial_no, refbusi_code, init_date |
| idx_refunfinished_id | client_id, client_id |
| idx_refunfinished_acct | fund_account, fund_account |
| idx_refunfinished_pos | position_str, position_str |

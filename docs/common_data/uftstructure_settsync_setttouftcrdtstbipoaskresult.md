# setttouftcrdtstbipoaskresult - 清算融资融券股转IPO询价结果表

**表对象ID**: 3062
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | branch_no | 是 |  |  |
| 3 | fund_account | 是 |  |  |
| 4 | exchange_type | 是 |  |  |
| 5 | stock_account | 是 |  |  |
| 6 | stock_code | 是 |  |  |
| 7 | business_id | 是 |  |  |
| 8 | contract_id | 是 |  |  |
| 9 | confirm_amount | 是 |  |  |
| 10 | business_price | 是 |  |  |
| 11 | business_date | 是 |  |  |
| 12 | business_time | 是 |  |  |
| 13 | withdraw_cause | 是 |  |  |
| 14 | returnbusin_kind | 是 |  |  |
| 15 | date_clear | 是 |  |  |
| 16 | business_amount2 | 是 |  |  |
| 17 | uft_data_change_status | 是 |  |  |
| 18 | init_date | 是 |  |  |
| 19 | branch_no | 是 |  |  |
| 20 | fund_account | 是 |  |  |
| 21 | exchange_type | 是 |  |  |
| 22 | stock_account | 是 |  |  |
| 23 | stock_code | 是 |  |  |
| 24 | business_id | 是 |  |  |
| 25 | contract_id | 是 |  |  |
| 26 | confirm_amount | 是 |  |  |
| 27 | business_price | 是 |  |  |
| 28 | business_date | 是 |  |  |
| 29 | business_time | 是 |  |  |
| 30 | withdraw_cause | 是 |  |  |
| 31 | returnbusin_kind | 是 |  |  |
| 32 | date_clear | 是 |  |  |
| 33 | business_amount2 | 是 |  |  |
| 34 | uft_data_change_status | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settcrdtstbipoaskresult | 默认 | 是 | stock_code, exchange_type, stock_account, fund_account, init_date, contract_id, stock_code, exchange_type, stock_account, fund_account, init_date, contract_id |
| idx_settcrdtstbipoaskresult | 默认 | 是 | stock_code, exchange_type, stock_account, fund_account, init_date, contract_id, stock_code, exchange_type, stock_account, fund_account, init_date, contract_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdtstbipoaskresult | stock_account, stock_code, fund_account, exchange_type, init_date, contract_id, stock_account, stock_code, fund_account, exchange_type, init_date, contract_id |
| idx_crdtstbipoaskresult | stock_account, stock_code, fund_account, exchange_type, init_date, contract_id, stock_account, stock_code, fund_account, exchange_type, init_date, contract_id |

# setttoufttprcontractext - 清算三方回购合约扩展表

**表对象ID**: 3040
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | sett_id | 是 |  |  |
| 2 | init_date | 是 |  |  |
| 3 | branch_no | 是 |  |  |
| 4 | fund_account | 是 |  |  |
| 5 | stock_account | 是 |  |  |
| 6 | exchange_type | 是 |  |  |
| 7 | contract_id | 是 |  |  |
| 8 | report_id | 是 |  |  |
| 9 | stock_code | 是 |  |  |
| 10 | impawn_amount | 是 |  |  |
| 11 | exch_in_amount | 是 |  |  |
| 12 | exch_out_amount | 是 |  |  |
| 13 | uft_data_change_status | 是 |  |  |
| 14 | sett_id | 是 |  |  |
| 15 | init_date | 是 |  |  |
| 16 | branch_no | 是 |  |  |
| 17 | fund_account | 是 |  |  |
| 18 | stock_account | 是 |  |  |
| 19 | exchange_type | 是 |  |  |
| 20 | contract_id | 是 |  |  |
| 21 | report_id | 是 |  |  |
| 22 | stock_code | 是 |  |  |
| 23 | impawn_amount | 是 |  |  |
| 24 | exch_in_amount | 是 |  |  |
| 25 | exch_out_amount | 是 |  |  |
| 26 | uft_data_change_status | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_setttprcontractext | 默认 | 是 | contract_id, stock_code, exchange_type, contract_id, stock_code, exchange_type |
| idx_setttprcontractext | 默认 | 是 | contract_id, stock_code, exchange_type, contract_id, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_setttprcontractext | contract_id, stock_account, exchange_type, contract_id, stock_account, exchange_type |
| idx_setttprcontractext | contract_id, stock_account, exchange_type, contract_id, stock_account, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2018-09-21 10:15 | 8.26.1.44 | 俞亚君 | 新增 |
| 2018-09-21 10:15 | 8.26.1.44 | 俞亚君 | 新增 |

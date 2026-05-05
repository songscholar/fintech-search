# setttouftimpawnstock - 清算质押国债表

**表对象ID**: 3029
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | sett_id | 是 |  |  |
| 2 | branch_no | 是 |  |  |
| 3 | client_id | 是 |  |  |
| 4 | fund_account | 是 |  |  |
| 5 | exchange_type | 是 |  |  |
| 6 | stock_account | 是 |  |  |
| 7 | stock_code | 是 |  |  |
| 8 | pre_out_amount | 是 |  |  |
| 9 | pre_in_amount | 是 |  |  |
| 10 | store_amount | 是 |  |  |
| 11 | uft_data_change_status | 是 |  |  |
| 12 | sett_id | 是 |  |  |
| 13 | branch_no | 是 |  |  |
| 14 | client_id | 是 |  |  |
| 15 | fund_account | 是 |  |  |
| 16 | exchange_type | 是 |  |  |
| 17 | stock_account | 是 |  |  |
| 18 | stock_code | 是 |  |  |
| 19 | pre_out_amount | 是 |  |  |
| 20 | pre_in_amount | 是 |  |  |
| 21 | store_amount | 是 |  |  |
| 22 | uft_data_change_status | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settimpawnstock | 默认 | 是 | stock_account, exchange_type, fund_account, stock_code, stock_account, exchange_type, fund_account, stock_code |
| idx_settimpawnstock_f | 默认 | 是 | fund_account, fund_account |
| idx_settimpawnstock | 默认 | 是 | stock_account, exchange_type, fund_account, stock_code, stock_account, exchange_type, fund_account, stock_code |
| idx_settimpawnstock_f | 默认 | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settimpawnstock | stock_account, exchange_type, fund_account, stock_code, stock_account, exchange_type, fund_account, stock_code |
| idx_settimpawnstock | stock_account, exchange_type, fund_account, stock_code, stock_account, exchange_type, fund_account, stock_code |

# setttoufttprimpawnstock - 清算三方回购质押券信息表

**表对象ID**: 3041
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | sett_id | 是 |  |  |
| 2 | branch_no | 是 |  |  |
| 3 | client_id | 是 |  |  |
| 4 | fund_account | 是 |  |  |
| 5 | exchange_type | 是 |  |  |
| 6 | stock_account | 是 |  |  |
| 7 | basket_id | 是 |  |  |
| 8 | stock_code | 是 |  |  |
| 9 | bond_end_date | 是 |  |  |
| 10 | store_amount | 是 |  |  |
| 11 | reg_impawn_amount | 是 |  |  |
| 12 | pre_out_amount | 是 |  |  |
| 13 | used_amount | 是 |  |  |
| 14 | fruits | 是 |  |  |
| 15 | uft_data_change_status | 是 |  |  |
| 16 | sett_id | 是 |  |  |
| 17 | branch_no | 是 |  |  |
| 18 | client_id | 是 |  |  |
| 19 | fund_account | 是 |  |  |
| 20 | exchange_type | 是 |  |  |
| 21 | stock_account | 是 |  |  |
| 22 | basket_id | 是 |  |  |
| 23 | stock_code | 是 |  |  |
| 24 | bond_end_date | 是 |  |  |
| 25 | store_amount | 是 |  |  |
| 26 | reg_impawn_amount | 是 |  |  |
| 27 | pre_out_amount | 是 |  |  |
| 28 | used_amount | 是 |  |  |
| 29 | fruits | 是 |  |  |
| 30 | uft_data_change_status | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_setttprimpawnstock | 默认 | 是 | stock_code, exchange_type, fund_account, stock_account, stock_code, exchange_type, fund_account, stock_account |
| idx_setttprimpawnstock | 默认 | 是 | stock_code, exchange_type, fund_account, stock_account, stock_code, exchange_type, fund_account, stock_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_setttprimpawnstock | stock_code, exchange_type, fund_account, stock_account, stock_code, exchange_type, fund_account, stock_account |
| idx_setttprimpawnstock | stock_code, exchange_type, fund_account, stock_account, stock_code, exchange_type, fund_account, stock_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2018-09-21 10:15 | 8.26.1.44 | 俞亚君 | 新增 |
| 2018-09-21 10:15 | 8.26.1.44 | 俞亚君 | 新增 |

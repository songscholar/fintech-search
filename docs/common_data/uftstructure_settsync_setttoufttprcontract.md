# setttoufttprcontract - 清算三方回购合约表

**表对象ID**: 3039
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 62 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | sett_id | 是 |  |  |
| 2 | init_date | 是 |  |  |
| 3 | branch_no | 是 |  |  |
| 4 | fund_account | 是 |  |  |
| 5 | client_id | 是 |  |  |
| 6 | stock_account | 是 |  |  |
| 7 | exchange_type | 是 |  |  |
| 8 | contract_id | 是 |  |  |
| 9 | tpr_source_type | 是 |  |  |
| 10 | prop_fund_acco | 是 |  |  |
| 11 | prop_stock_account | 是 |  |  |
| 12 | prop_seat_no | 是 |  |  |
| 13 | entrust_date | 是 |  |  |
| 14 | entrust_balance | 是 |  |  |
| 15 | expire_year_rate | 是 |  |  |
| 16 | back_balance | 是 |  |  |
| 17 | date_back | 是 |  |  |
| 18 | real_year_rate | 是 |  |  |
| 19 | real_back_balance | 是 |  |  |
| 20 | real_date_back | 是 |  |  |
| 21 | fruits | 是 |  |  |
| 22 | current_assure_value | 是 |  |  |
| 23 | report_id | 是 |  |  |
| 24 | szdc_business_no | 是 |  |  |
| 25 | tpr_contract_status | 是 |  |  |
| 26 | date_clear | 是 |  |  |
| 27 | remark | 是 |  |  |
| 28 | position_str | 是 |  |  |
| 29 | en_basket_id | 是 |  |  |
| 30 | exch_out_fruits | 是 |  |  |
| 31 | uft_data_change_status | 是 |  |  |
| 32 | sett_id | 是 |  |  |
| 33 | init_date | 是 |  |  |
| 34 | branch_no | 是 |  |  |
| 35 | fund_account | 是 |  |  |
| 36 | client_id | 是 |  |  |
| 37 | stock_account | 是 |  |  |
| 38 | exchange_type | 是 |  |  |
| 39 | contract_id | 是 |  |  |
| 40 | tpr_source_type | 是 |  |  |
| 41 | prop_fund_acco | 是 |  |  |
| 42 | prop_stock_account | 是 |  |  |
| 43 | prop_seat_no | 是 |  |  |
| 44 | entrust_date | 是 |  |  |
| 45 | entrust_balance | 是 |  |  |
| 46 | expire_year_rate | 是 |  |  |
| 47 | back_balance | 是 |  |  |
| 48 | date_back | 是 |  |  |
| 49 | real_year_rate | 是 |  |  |
| 50 | real_back_balance | 是 |  |  |
| 51 | real_date_back | 是 |  |  |
| 52 | fruits | 是 |  |  |
| 53 | current_assure_value | 是 |  |  |
| 54 | report_id | 是 |  |  |
| 55 | szdc_business_no | 是 |  |  |
| 56 | tpr_contract_status | 是 |  |  |
| 57 | date_clear | 是 |  |  |
| 58 | remark | 是 |  |  |
| 59 | position_str | 是 |  |  |
| 60 | en_basket_id | 是 |  |  |
| 61 | exch_out_fruits | 是 |  |  |
| 62 | uft_data_change_status | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_setttprcontract | 默认 | 是 | contract_id, contract_id |
| idx_setttprcontract_fund | 默认 | 是 | fund_account, fund_account |
| idx_setttprcontract | 默认 | 是 | contract_id, contract_id |
| idx_setttprcontract_fund | 默认 | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_setttprcontract | contract_id, contract_id |
| idx_setttprcontract | contract_id, contract_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2018-09-21 10:15 | 8.26.1.44 | 俞亚君 | 新增 |
| 2018-09-21 10:15 | 8.26.1.44 | 俞亚君 | 新增 |

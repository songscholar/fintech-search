# setttouftetfustockinfo - 清算网下股份认购信息表

**表对象ID**: 3020
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 62 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | sett_id | 是 |  |  |
| 3 | branch_no | 是 |  |  |
| 4 | fund_account | 是 |  |  |
| 5 | stock_account | 是 |  |  |
| 6 | client_id | 是 |  |  |
| 7 | exchange_type | 是 |  |  |
| 8 | stock_code | 是 |  |  |
| 9 | stock_name | 是 |  |  |
| 10 | component_code | 是 |  |  |
| 11 | component_name | 是 |  |  |
| 12 | money_type | 是 |  |  |
| 13 | operator_no | 是 |  |  |
| 14 | entrust_amount | 是 |  |  |
| 15 | entrust_status | 是 |  |  |
| 16 | prev_status | 是 |  |  |
| 17 | confirm_amount | 是 |  |  |
| 18 | seat_no | 是 |  |  |
| 19 | fare_rate | 是 |  |  |
| 20 | entrust_date | 是 |  |  |
| 21 | entrust_time | 是 |  |  |
| 22 | entrust_no | 是 |  |  |
| 23 | entrust_operator | 是 |  |  |
| 24 | remark | 是 |  |  |
| 25 | report_date | 是 |  |  |
| 26 | unfrozen_amount | 是 |  |  |
| 27 | join_stock_account | 是 |  |  |
| 28 | join_report_account | 是 |  |  |
| 29 | join_seat_no | 是 |  |  |
| 30 | position_str | 是 |  |  |
| 31 | uft_data_change_status | 是 |  |  |
| 32 | init_date | 是 |  |  |
| 33 | sett_id | 是 |  |  |
| 34 | branch_no | 是 |  |  |
| 35 | fund_account | 是 |  |  |
| 36 | stock_account | 是 |  |  |
| 37 | client_id | 是 |  |  |
| 38 | exchange_type | 是 |  |  |
| 39 | stock_code | 是 |  |  |
| 40 | stock_name | 是 |  |  |
| 41 | component_code | 是 |  |  |
| 42 | component_name | 是 |  |  |
| 43 | money_type | 是 |  |  |
| 44 | operator_no | 是 |  |  |
| 45 | entrust_amount | 是 |  |  |
| 46 | entrust_status | 是 |  |  |
| 47 | prev_status | 是 |  |  |
| 48 | confirm_amount | 是 |  |  |
| 49 | seat_no | 是 |  |  |
| 50 | fare_rate | 是 |  |  |
| 51 | entrust_date | 是 |  |  |
| 52 | entrust_time | 是 |  |  |
| 53 | entrust_no | 是 |  |  |
| 54 | entrust_operator | 是 |  |  |
| 55 | remark | 是 |  |  |
| 56 | report_date | 是 |  |  |
| 57 | unfrozen_amount | 是 |  |  |
| 58 | join_stock_account | 是 |  |  |
| 59 | join_report_account | 是 |  |  |
| 60 | join_seat_no | 是 |  |  |
| 61 | position_str | 是 |  |  |
| 62 | uft_data_change_status | 是 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settetfustockinfo | 默认 | 是 | fund_account, stock_account, stock_code, component_code, fund_account, stock_account, stock_code, component_code |
| idx_settetfustockinfo_code | 默认 | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_settetfustockinfo_exch | 默认 | 是 | stock_account, exchange_type, stock_account, exchange_type |
| idx_settetfustockinfo | 默认 | 是 | fund_account, stock_account, stock_code, component_code, fund_account, stock_account, stock_code, component_code |
| idx_settetfustockinfo_code | 默认 | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_settetfustockinfo_exch | 默认 | 是 | stock_account, exchange_type, stock_account, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settetfustockinfo_exch | stock_account, exchange_type, stock_account, exchange_type |
| idx_settetfustockinfo_exch | stock_account, exchange_type, stock_account, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2018-04-03 11:00 | 8.26.1.7 | 彭立 | 增加索引idx_settetfustockinfo_exch |
| 2018-04-03 11:00 | 8.26.1.7 | 彭立 | 增加索引idx_settetfustockinfo_exch |

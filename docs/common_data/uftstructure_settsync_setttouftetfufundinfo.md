# setttouftetfufundinfo - 清算网下现金认购信息表

**表对象ID**: 3019
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 56 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | sett_id | 是 |  |  |
| 3 | branch_no | 是 |  |  |
| 4 | fund_account | 是 |  |  |
| 5 | stock_account | 是 |  |  |
| 6 | stock_code | 是 |  |  |
| 7 | client_id | 是 |  |  |
| 8 | exchange_type | 是 |  |  |
| 9 | stock_name | 是 |  |  |
| 10 | money_type | 是 |  |  |
| 11 | operator_no | 是 |  |  |
| 12 | entrust_amount | 是 |  |  |
| 13 | entrust_price | 是 |  |  |
| 14 | entrust_status | 是 |  |  |
| 15 | prev_status | 是 |  |  |
| 16 | frozen_balance | 是 |  |  |
| 17 | frozen_fare | 是 |  |  |
| 18 | entrust_date | 是 |  |  |
| 19 | entrust_time | 是 |  |  |
| 20 | entrust_no | 是 |  |  |
| 21 | entrust_operator | 是 |  |  |
| 22 | remark | 是 |  |  |
| 23 | report_amount | 是 |  |  |
| 24 | report_balance | 是 |  |  |
| 25 | entrustno_str | 是 |  |  |
| 26 | report_date | 是 |  |  |
| 27 | position_str | 是 |  |  |
| 28 | uft_data_change_status | 是 |  |  |
| 29 | init_date | 是 |  |  |
| 30 | sett_id | 是 |  |  |
| 31 | branch_no | 是 |  |  |
| 32 | fund_account | 是 |  |  |
| 33 | stock_account | 是 |  |  |
| 34 | stock_code | 是 |  |  |
| 35 | client_id | 是 |  |  |
| 36 | exchange_type | 是 |  |  |
| 37 | stock_name | 是 |  |  |
| 38 | money_type | 是 |  |  |
| 39 | operator_no | 是 |  |  |
| 40 | entrust_amount | 是 |  |  |
| 41 | entrust_price | 是 |  |  |
| 42 | entrust_status | 是 |  |  |
| 43 | prev_status | 是 |  |  |
| 44 | frozen_balance | 是 |  |  |
| 45 | frozen_fare | 是 |  |  |
| 46 | entrust_date | 是 |  |  |
| 47 | entrust_time | 是 |  |  |
| 48 | entrust_no | 是 |  |  |
| 49 | entrust_operator | 是 |  |  |
| 50 | remark | 是 |  |  |
| 51 | report_amount | 是 |  |  |
| 52 | report_balance | 是 |  |  |
| 53 | entrustno_str | 是 |  |  |
| 54 | report_date | 是 |  |  |
| 55 | position_str | 是 |  |  |
| 56 | uft_data_change_status | 是 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settetfufundinfo | 默认 | 是 | position_str, position_str |
| idx_settetfufundinfo_acct | 默认 | 是 | fund_account, fund_account |
| idx_settetfufundinfo_exch | 默认 | 是 | stock_account, exchange_type, stock_account, exchange_type |
| idx_settetfufundinfo_code | 默认 | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_settetfufundinfo | 默认 | 是 | position_str, position_str |
| idx_settetfufundinfo_acct | 默认 | 是 | fund_account, fund_account |
| idx_settetfufundinfo_exch | 默认 | 是 | stock_account, exchange_type, stock_account, exchange_type |
| idx_settetfufundinfo_code | 默认 | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settetfufundinfo_acct | fund_account, fund_account |
| idx_settetfufundinfo_acct | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2021-01-19 11:15 | 8.26.1.109 | 郑宇 | 增加索引idx_settetfufundinfo_code |
| 2018-04-03 11:01 | 8.26.1.7 | 彭立 | 增加索引idx_settetfufundinfo_exch |
| 2021-01-19 11:15 | 8.26.1.109 | 郑宇 | 增加索引idx_settetfufundinfo_code |
| 2018-04-03 11:01 | 8.26.1.7 | 彭立 | 增加索引idx_settetfufundinfo_exch |

# setttouftuncompact - 清算未完成合约汇总表

**表对象ID**: 3071
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 62 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | compact_id | 是 |  |  |
| 3 | compact_type | 是 |  |  |
| 4 | exchange_type | 是 |  |  |
| 5 | stock_code | 是 |  |  |
| 6 | money_type | 是 |  |  |
| 7 | fund_account | 是 |  |  |
| 8 | cashgroup_no | 是 |  |  |
| 9 | uncompact_type | 是 |  |  |
| 10 | interest_date | 是 |  |  |
| 11 | deal_date | 是 |  |  |
| 12 | compact_integral | 是 |  |  |
| 13 | fine_integral | 是 |  |  |
| 14 | compact_interest | 是 |  |  |
| 15 | repaid_interest | 是 |  |  |
| 16 | year_rate | 是 |  |  |
| 17 | occur_interest | 是 |  |  |
| 18 | occur_frozen_interest | 是 |  |  |
| 19 | ret_end_date | 是 |  |  |
| 20 | compact_postpone_status | 是 |  |  |
| 21 | compact_postpone_times | 是 |  |  |
| 22 | crdt_fare_str | 是 |  |  |
| 23 | compact_status | 是 |  |  |
| 24 | real_status | 是 |  |  |
| 25 | date_clear | 是 |  |  |
| 26 | uft_data_change_status | 是 |  |  |
| 27 | compact_fine_settlement | 是 |  |  |
| 28 | occur_fine_interest | 是 |  |  |
| 29 | fine_rate | 是 |  |  |
| 30 | primerate_flag | 是 |  |  |
| 31 | followdate_flag | 是 |  |  |
| 32 | init_date | 是 |  |  |
| 33 | compact_id | 是 |  |  |
| 34 | compact_type | 是 |  |  |
| 35 | exchange_type | 是 |  |  |
| 36 | stock_code | 是 |  |  |
| 37 | money_type | 是 |  |  |
| 38 | fund_account | 是 |  |  |
| 39 | cashgroup_no | 是 |  |  |
| 40 | uncompact_type | 是 |  |  |
| 41 | interest_date | 是 |  |  |
| 42 | deal_date | 是 |  |  |
| 43 | compact_integral | 是 |  |  |
| 44 | fine_integral | 是 |  |  |
| 45 | compact_interest | 是 |  |  |
| 46 | repaid_interest | 是 |  |  |
| 47 | year_rate | 是 |  |  |
| 48 | occur_interest | 是 |  |  |
| 49 | occur_frozen_interest | 是 |  |  |
| 50 | ret_end_date | 是 |  |  |
| 51 | compact_postpone_status | 是 |  |  |
| 52 | compact_postpone_times | 是 |  |  |
| 53 | crdt_fare_str | 是 |  |  |
| 54 | compact_status | 是 |  |  |
| 55 | real_status | 是 |  |  |
| 56 | date_clear | 是 |  |  |
| 57 | uft_data_change_status | 是 |  |  |
| 58 | compact_fine_settlement | 是 |  |  |
| 59 | occur_fine_interest | 是 |  |  |
| 60 | fine_rate | 是 |  |  |
| 61 | primerate_flag | 是 |  |  |
| 62 | followdate_flag | 是 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settuncompacttotal | 默认 | 是 | compact_id, uncompact_type, deal_date, compact_id, uncompact_type, deal_date |
| idx_settuncompacttotal_comp | 默认 | 是 | compact_id, compact_id |
| idx_settuncompacttotal_acct | 默认 | 是 | fund_account, fund_account |
| idx_settuncompacttotal | 默认 | 是 | compact_id, uncompact_type, deal_date, compact_id, uncompact_type, deal_date |
| idx_settuncompacttotal_comp | 默认 | 是 | compact_id, compact_id |
| idx_settuncompacttotal_acct | 默认 | 是 | fund_account, fund_account |

## 数据库索引（共 6 个）

| 索引名 | 字段 |
|--------|------|
| idx_uncompact | deal_date, compact_id, uncompact_type, deal_date, compact_id, uncompact_type |
| idx_uncompact_comp | compact_id, compact_id |
| idx_uncompact_acct | fund_account, fund_account |
| idx_uncompact | deal_date, compact_id, uncompact_type, deal_date, compact_id, uncompact_type |
| idx_uncompact_comp | compact_id, compact_id |
| idx_uncompact_acct | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2020-05-03 09:36 | 8.26.1.66 | 曾哲 | 补充字段，与UF20保持一致 |
| 2018-09-21 10:15 | 8.26.1.33 | 俞亚君 | 新增 |
| 2020-05-03 09:36 | 8.26.1.66 | 曾哲 | 补充字段，与UF20保持一致 |
| 2018-09-21 10:15 | 8.26.1.33 | 俞亚君 | 新增 |

# ucrt_total_compact - 实时合约汇总表

**表对象ID**: 7504
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_account | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | money_type | 否 |  |  |
| 8 | compact_type | 否 |  |  |
| 9 | compact_source | 否 |  |  |
| 10 | stock_type | 否 |  |  |
| 11 | begin_compact_balance | 否 |  |  |
| 12 | real_occuped_balance | 否 |  |  |
| 13 | real_occuped_amount | 否 |  |  |
| 14 | real_compact_balance | 否 |  |  |
| 15 | real_compact_amount | 否 |  |  |
| 16 | real_compact_fare | 否 |  |  |
| 17 | real_compact_interest | 否 |  |  |
| 18 | slo_uncome_amount | 否 |  |  |
| 19 | slo_sell_amount | 否 |  |  |
| 20 | slo_totalused_bail_amount | 否 |  |  |
| 21 | fin_totalused_bail_balance | 否 |  |  |
| 22 | check_date | 否 |  |  |
| 23 | real_occuped_fare | 否 |  |  |
| 24 | business_fare | 否 |  |  |
| 25 | real_repaycost_balance | 否 |  |  |
| 26 | business_balance | 否 |  |  |
| 27 | business_amount | 否 |  |  |
| 28 | stock_account | 否 |  |  |
| 29 | stock_code | 否 |  |  |
| 30 | branch_no | 否 |  |  |
| 31 | exchange_type | 否 |  |  |
| 32 | fund_account | 否 |  |  |
| 33 | client_id | 否 |  |  |
| 34 | money_type | 否 |  |  |
| 35 | compact_type | 否 |  |  |
| 36 | compact_source | 否 |  |  |
| 37 | stock_type | 否 |  |  |
| 38 | begin_compact_balance | 否 |  |  |
| 39 | real_occuped_balance | 否 |  |  |
| 40 | real_occuped_amount | 否 |  |  |
| 41 | real_compact_balance | 否 |  |  |
| 42 | real_compact_amount | 否 |  |  |
| 43 | real_compact_fare | 否 |  |  |
| 44 | real_compact_interest | 否 |  |  |
| 45 | slo_uncome_amount | 否 |  |  |
| 46 | slo_sell_amount | 否 |  |  |
| 47 | slo_totalused_bail_amount | 否 |  |  |
| 48 | fin_totalused_bail_balance | 否 |  |  |
| 49 | check_date | 否 |  |  |
| 50 | real_occuped_fare | 否 |  |  |
| 51 | business_fare | 否 |  |  |
| 52 | real_repaycost_balance | 否 |  |  |
| 53 | business_balance | 否 |  |  |
| 54 | business_amount | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_total_compact | ART | 是 | fund_account, exchange_type, stock_code, compact_type, compact_source, fund_account, exchange_type, stock_code, compact_type, compact_source |
| idx_ucrt_total_compact | ART | 是 | fund_account, exchange_type, stock_code, compact_type, compact_source, fund_account, exchange_type, stock_code, compact_type, compact_source |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_total_compact | fund_account, stock_code, exchange_type, compact_type, compact_source, fund_account, stock_code, exchange_type, compact_type, compact_source |
| idx_ucrt_total_compact | fund_account, stock_code, exchange_type, compact_type, compact_source, fund_account, stock_code, exchange_type, compact_type, compact_source |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-03-24 18:57:42 | 3.0.6.50 | 徐世晗 | 重新编译 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-03-24 18:57:42 | 3.0.6.50 | 徐世晗 | 重新编译 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

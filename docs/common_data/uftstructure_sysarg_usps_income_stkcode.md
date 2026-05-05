# usps_income_stkcode - 固收证券代码表

**表对象ID**: 66
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 70 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | stock_name | 否 |  |  |
| 4 | trade_product | 否 |  |  |
| 5 | stock_type | 否 |  |  |
| 6 | stkcode_status | 否 |  |  |
| 7 | impawn_code | 否 |  |  |
| 8 | begin_time | 否 |  |  |
| 9 | end_time | 否 |  |  |
| 10 | wit_type | 否 |  |  |
| 11 | par_value | 否 |  |  |
| 12 | issue_price | 否 |  |  |
| 13 | interest_rate_type | 否 |  |  |
| 14 | interest_freq | 否 |  |  |
| 15 | bottom_rate | 否 |  |  |
| 16 | basic_rate | 否 |  |  |
| 17 | basic_ratediff | 否 |  |  |
| 18 | deriv_term | 否 |  |  |
| 19 | total_amount | 否 |  |  |
| 20 | issue_date | 否 |  |  |
| 21 | issue_end_date | 否 |  |  |
| 22 | market_date | 否 |  |  |
| 23 | end_date | 否 |  |  |
| 24 | bond_stktype | 否 |  |  |
| 25 | issue_way | 否 |  |  |
| 26 | cross_market_flag | 否 |  |  |
| 27 | short_flag | 否 |  |  |
| 28 | bears_amount | 否 |  |  |
| 29 | trader_short_amount | 否 |  |  |
| 30 | close_price | 否 |  |  |
| 31 | weightavg_price | 否 |  |  |
| 32 | transaction_no | 否 |  |  |
| 33 | update_date | 否 |  |  |
| 34 | update_time | 否 |  |  |
| 35 | position_str | 否 |  | exchange_type(4)+stock_code(8) |
| 36 | exchange_type | 否 |  |  |
| 37 | stock_code | 否 |  |  |
| 38 | stock_name | 否 |  |  |
| 39 | trade_product | 否 |  |  |
| 40 | stock_type | 否 |  |  |
| 41 | stkcode_status | 否 |  |  |
| 42 | impawn_code | 否 |  |  |
| 43 | begin_time | 否 |  |  |
| 44 | end_time | 否 |  |  |
| 45 | wit_type | 否 |  |  |
| 46 | par_value | 否 |  |  |
| 47 | issue_price | 否 |  |  |
| 48 | interest_rate_type | 否 |  |  |
| 49 | interest_freq | 否 |  |  |
| 50 | bottom_rate | 否 |  |  |
| 51 | basic_rate | 否 |  |  |
| 52 | basic_ratediff | 否 |  |  |
| 53 | deriv_term | 否 |  |  |
| 54 | total_amount | 否 |  |  |
| 55 | issue_date | 否 |  |  |
| 56 | issue_end_date | 否 |  |  |
| 57 | market_date | 否 |  |  |
| 58 | end_date | 否 |  |  |
| 59 | bond_stktype | 否 |  |  |
| 60 | issue_way | 否 |  |  |
| 61 | cross_market_flag | 否 |  |  |
| 62 | short_flag | 否 |  |  |
| 63 | bears_amount | 否 |  |  |
| 64 | trader_short_amount | 否 |  |  |
| 65 | close_price | 否 |  |  |
| 66 | weightavg_price | 否 |  |  |
| 67 | transaction_no | 否 |  |  |
| 68 | update_date | 否 |  |  |
| 69 | update_time | 否 |  |  |
| 70 | position_str | 否 |  | exchange_type(4)+stock_code(8) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_income_stkcode | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_usps_income_stkcode | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_income_stkcode | exchange_type, stock_code, exchange_type, stock_code |
| idx_usps_income_stkcode | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 17:08:29 | 3.0.6.70 | 李想 | 物理表usps_income_stkcode，添加了表字段(update_date);
物理表usps_income_... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-02-18 17:08:29 | 3.0.6.70 | 李想 | 物理表usps_income_stkcode，添加了表字段(update_date);
物理表usps_income_... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

# usps_etf_code - ETF代码表

**表对象ID**: 50
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 84 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_code_etf0 | 否 |  |  |
| 5 | stock_code_etf2 | 否 |  |  |
| 6 | stock_code_etf3 | 否 |  |  |
| 7 | stock_code_etf4 | 否 |  |  |
| 8 | exchange_unit | 否 |  |  |
| 9 | cash_balance | 否 |  |  |
| 10 | max_cash_ratio | 否 |  |  |
| 11 | etfcode_status | 否 |  |  |
| 12 | component_num | 否 |  |  |
| 13 | publish | 否 |  |  |
| 14 | tradingday | 否 |  |  |
| 15 | pretradingday | 否 |  |  |
| 16 | cashcomponent | 否 |  |  |
| 17 | navpercu | 否 |  |  |
| 18 | nav | 否 |  |  |
| 19 | cash_unit | 否 |  |  |
| 20 | cash_min | 否 |  |  |
| 21 | cash_max | 否 |  |  |
| 22 | stock_unit | 否 |  |  |
| 23 | stock_min | 否 |  |  |
| 24 | stock_max | 否 |  |  |
| 25 | etfcode_type | 否 |  |  |
| 26 | priv_component_num | 否 |  |  |
| 27 | allot_max | 否 |  |  |
| 28 | redeem_max | 否 |  |  |
| 29 | rept_cash_per | 否 |  |  |
| 30 | channel_type | 否 |  |  |
| 31 | pd_secu_flag | 否 |  |  |
| 32 | en_company_no | 否 |  |  |
| 33 | cash_ratio_mode | 否 |  |  |
| 34 | transaction_no | 否 |  |  |
| 35 | update_date | 否 |  |  |
| 36 | update_time | 否 |  |  |
| 37 | position_str | 否 |  | stock_code(8)+channel_type(1)+exchange_type(4)+init_date(8) |
| 38 | appredeem_type | 否 |  |  |
| 39 | acct_net_allot_max | 否 |  |  |
| 40 | acct_net_redeem_max | 否 |  |  |
| 41 | acct_sum_allot_max | 否 |  |  |
| 42 | acct_sum_redeem_max | 否 |  |  |
| 43 | init_date | 否 |  |  |
| 44 | exchange_type | 否 |  |  |
| 45 | stock_code | 否 |  |  |
| 46 | stock_code_etf0 | 否 |  |  |
| 47 | stock_code_etf2 | 否 |  |  |
| 48 | stock_code_etf3 | 否 |  |  |
| 49 | stock_code_etf4 | 否 |  |  |
| 50 | exchange_unit | 否 |  |  |
| 51 | cash_balance | 否 |  |  |
| 52 | max_cash_ratio | 否 |  |  |
| 53 | etfcode_status | 否 |  |  |
| 54 | component_num | 否 |  |  |
| 55 | publish | 否 |  |  |
| 56 | tradingday | 否 |  |  |
| 57 | pretradingday | 否 |  |  |
| 58 | cashcomponent | 否 |  |  |
| 59 | navpercu | 否 |  |  |
| 60 | nav | 否 |  |  |
| 61 | cash_unit | 否 |  |  |
| 62 | cash_min | 否 |  |  |
| 63 | cash_max | 否 |  |  |
| 64 | stock_unit | 否 |  |  |
| 65 | stock_min | 否 |  |  |
| 66 | stock_max | 否 |  |  |
| 67 | etfcode_type | 否 |  |  |
| 68 | priv_component_num | 否 |  |  |
| 69 | allot_max | 否 |  |  |
| 70 | redeem_max | 否 |  |  |
| 71 | rept_cash_per | 否 |  |  |
| 72 | channel_type | 否 |  |  |
| 73 | pd_secu_flag | 否 |  |  |
| 74 | en_company_no | 否 |  |  |
| 75 | cash_ratio_mode | 否 |  |  |
| 76 | transaction_no | 否 |  |  |
| 77 | update_date | 否 |  |  |
| 78 | update_time | 否 |  |  |
| 79 | position_str | 否 |  | stock_code(8)+channel_type(1)+exchange_type(4)+init_date(8) |
| 80 | appredeem_type | 否 |  |  |
| 81 | acct_net_allot_max | 否 |  |  |
| 82 | acct_net_redeem_max | 否 |  |  |
| 83 | acct_sum_allot_max | 否 |  |  |
| 84 | acct_sum_redeem_max | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_etf_code | ART | 是 | stock_code, channel_type, exchange_type, init_date, stock_code, channel_type, exchange_type, init_date |
| uk_rpt_uspsetfcode | ART | 是 | init_date, stock_code, channel_type, exchange_type, init_date, stock_code, channel_type, exchange_type |
| idx_usps_etf_code | ART | 是 | stock_code, channel_type, exchange_type, init_date, stock_code, channel_type, exchange_type, init_date |
| uk_rpt_uspsetfcode | ART | 是 | init_date, stock_code, channel_type, exchange_type, init_date, stock_code, channel_type, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_etf_code | stock_code, channel_type, exchange_type, init_date, stock_code, channel_type, exchange_type, init_date |
| idx_usps_etf_code | stock_code, channel_type, exchange_type, init_date, stock_code, channel_type, exchange_type, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-26 20:57:56 | 3.0.6.122 | 李想 | 物理表usps_etf_code，添加了表字段(appredeem_type);
物理表usps_etf_code，添... |
| 2025-02-18 17:43:15 | 3.0.6.76 | 李想 | 物理表usps_etf_code，添加了表字段(update_date);
物理表usps_etf_code，添加了表... |
| 2023-11-21 14:17:25 | V3.0.1.18 | 徐志坚 | 为了提升行情转入性能修改索引为分级索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-26 20:57:56 | 3.0.6.122 | 李想 | 物理表usps_etf_code，添加了表字段(appredeem_type);
物理表usps_etf_code，添... |
| 2025-02-18 17:43:15 | 3.0.6.76 | 李想 | 物理表usps_etf_code，添加了表字段(update_date);
物理表usps_etf_code，添加了表... |
| 2023-11-21 14:17:25 | V3.0.1.18 | 徐志坚 | 为了提升行情转入性能修改索引为分级索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

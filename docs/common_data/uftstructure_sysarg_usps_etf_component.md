# usps_etf_component - ETF成份股份信息表

**表对象ID**: 51
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 44 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | component_code | 否 |  |  |
| 5 | component_name | 否 |  |  |
| 6 | component_amount | 否 |  |  |
| 7 | replace_flag | 否 |  |  |
| 8 | replace_ratio | 否 |  |  |
| 9 | replace_balance | 否 |  |  |
| 10 | redeem_replace_balance | 否 |  |  |
| 11 | secu_market_code | 否 |  |  |
| 12 | modify_date | 否 |  |  |
| 13 | channel_type | 否 |  |  |
| 14 | discount_rate | 否 |  |  |
| 15 | redeem_replace_ratio | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | mapping_code | 否 |  |  |
| 18 | phycreredemption_flag | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | position_str | 否 |  | stock_code(8)+channel_type(1)+component_code(20)+exchange_ty |
| 22 | tradingday | 否 |  |  |
| 23 | init_date | 否 |  |  |
| 24 | exchange_type | 否 |  |  |
| 25 | stock_code | 否 |  |  |
| 26 | component_code | 否 |  |  |
| 27 | component_name | 否 |  |  |
| 28 | component_amount | 否 |  |  |
| 29 | replace_flag | 否 |  |  |
| 30 | replace_ratio | 否 |  |  |
| 31 | replace_balance | 否 |  |  |
| 32 | redeem_replace_balance | 否 |  |  |
| 33 | secu_market_code | 否 |  |  |
| 34 | modify_date | 否 |  |  |
| 35 | channel_type | 否 |  |  |
| 36 | discount_rate | 否 |  |  |
| 37 | redeem_replace_ratio | 否 |  |  |
| 38 | transaction_no | 否 |  |  |
| 39 | mapping_code | 否 |  |  |
| 40 | phycreredemption_flag | 否 |  |  |
| 41 | update_date | 否 |  |  |
| 42 | update_time | 否 |  |  |
| 43 | position_str | 否 |  | stock_code(8)+channel_type(1)+component_code(20)+exchange_ty |
| 44 | tradingday | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_etf_component | ART | 是 | stock_code, exchange_type, channel_type, component_code, init_date, stock_code, exchange_type, channel_type, component_code, init_date |
| idx_usps_etf_component | ART | 是 | stock_code, exchange_type, channel_type, component_code, init_date, stock_code, exchange_type, channel_type, component_code, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_etf_component | stock_code, channel_type, component_code, exchange_type, init_date, stock_code, channel_type, component_code, exchange_type, init_date |
| idx_usps_etf_component | stock_code, channel_type, component_code, exchange_type, init_date, stock_code, channel_type, component_code, exchange_type, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 18:28:43 | 3.0.6.77 | 李想 | 物理表usps_etf_component，添加了表字段(update_date);
物理表usps_etf_comp... |
| 2025-07-16 15:19:45 | 3.0.2.89 | 张华佳 | 物理表usps_etf_component，添加了表字段(tradingday);
 |
| 2024-07-08 17:20:42 | 3.0.2.14 | 阮善宏 | 物理表usps_etf_component，添加了表字段(mapping_code);
物理表usps_etf_com... |
| 2023-11-21 14:18:31 | V3.0.1.18 | 徐志坚 | 为了提升行情转入性能修改索引为分级索引 |
| 2023-09-23 16:01:01 | V3.0.1.9 | 汪林 | 调整idx_usps_etf_component索引为分级索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-06-20 17:14 | 0.0.0.10 | 侯璇 | 修改表中文名，"分"改为"份" |
| 2025-02-18 18:28:43 | 3.0.6.77 | 李想 | 物理表usps_etf_component，添加了表字段(update_date);
物理表usps_etf_comp... |
| 2025-07-16 15:19:45 | 3.0.2.89 | 张华佳 | 物理表usps_etf_component，添加了表字段(tradingday);
 |
| 2024-07-08 17:20:42 | 3.0.2.14 | 阮善宏 | 物理表usps_etf_component，添加了表字段(mapping_code);
物理表usps_etf_com... |
| 2023-11-21 14:18:31 | V3.0.1.18 | 徐志坚 | 为了提升行情转入性能修改索引为分级索引 |
| 2023-09-23 16:01:01 | V3.0.1.9 | 汪林 | 调整idx_usps_etf_component索引为分级索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

> 共 16 条修改记录，仅显示最近15条

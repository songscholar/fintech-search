# usps_nsrisk_info - 新股风险信息表

**表对象ID**: 47
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | market_date | 否 |  |  |
| 4 | end_date | 否 |  |  |
| 5 | circulate_amount | 否 |  |  |
| 6 | acum_buy_percent | 否 |  |  |
| 7 | acum_buy_amount | 否 |  |  |
| 8 | single_buy_percent | 否 |  |  |
| 9 | single_buy_amount | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | position_str | 否 |  | exchange_type(4)+stock_code(8) |
| 14 | exchange_type | 否 |  |  |
| 15 | stock_code | 否 |  |  |
| 16 | market_date | 否 |  |  |
| 17 | end_date | 否 |  |  |
| 18 | circulate_amount | 否 |  |  |
| 19 | acum_buy_percent | 否 |  |  |
| 20 | acum_buy_amount | 否 |  |  |
| 21 | single_buy_percent | 否 |  |  |
| 22 | single_buy_amount | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | position_str | 否 |  | exchange_type(4)+stock_code(8) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_nsrisk_info | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_usps_nsrisk_info | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_nsrisk_info | exchange_type, stock_code, exchange_type, stock_code |
| idx_usps_nsrisk_info | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-19 16:22:04 | 3.0.6.100 | 李想 | 物理表usps_nsrisk_info，添加了表字段(update_date);
物理表usps_nsrisk_inf... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-02-19 16:22:04 | 3.0.6.100 | 李想 | 物理表usps_nsrisk_info，添加了表字段(update_date);
物理表usps_nsrisk_inf... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

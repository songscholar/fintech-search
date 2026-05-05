# usps_price - 证券行情表

**表对象ID**: 38
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 60 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | init_date | 否 |  |  |
| 4 | asset_price | 否 |  |  |
| 5 | last_price | 否 |  |  |
| 6 | money_type | 否 |  |  |
| 7 | rate_price | 否 |  |  |
| 8 | business_balance | 否 |  |  |
| 9 | close_flag | 否 |  |  |
| 10 | low_price | 否 |  |  |
| 11 | high_price | 否 |  |  |
| 12 | closing_price | 否 |  |  |
| 13 | weightavg_price | 否 |  |  |
| 14 | dr_price | 否 |  |  |
| 15 | last_price_consult | 否 |  |  |
| 16 | last_price_click | 否 |  |  |
| 17 | last_price_inquiry | 否 |  |  |
| 18 | last_price_compete | 否 |  |  |
| 19 | pre_dr_price | 否 |  |  |
| 20 | business_amount | 否 |  |  |
| 21 | hq_date | 否 |  |  |
| 22 | cs_value_price | 否 |  |  |
| 23 | cb_value_price | 否 |  |  |
| 24 | cs_value_price_date | 否 |  |  |
| 25 | cb_value_price_date | 否 |  |  |
| 26 | transaction_no | 否 |  |  |
| 27 | position_str | 否 |  | init_date(8)+exchange_type(4)+stock_code(8) |
| 28 | stock_name | 否 | H |  |
| 29 | stock_type | 否 | H |  |
| 30 | sub_stock_type | 否 | H |  |
| 31 | exchange_type | 否 |  |  |
| 32 | stock_code | 否 |  |  |
| 33 | init_date | 否 |  |  |
| 34 | asset_price | 否 |  |  |
| 35 | last_price | 否 |  |  |
| 36 | money_type | 否 |  |  |
| 37 | rate_price | 否 |  |  |
| 38 | business_balance | 否 |  |  |
| 39 | close_flag | 否 |  |  |
| 40 | low_price | 否 |  |  |
| 41 | high_price | 否 |  |  |
| 42 | closing_price | 否 |  |  |
| 43 | weightavg_price | 否 |  |  |
| 44 | dr_price | 否 |  |  |
| 45 | last_price_consult | 否 |  |  |
| 46 | last_price_click | 否 |  |  |
| 47 | last_price_inquiry | 否 |  |  |
| 48 | last_price_compete | 否 |  |  |
| 49 | pre_dr_price | 否 |  |  |
| 50 | business_amount | 否 |  |  |
| 51 | hq_date | 否 |  |  |
| 52 | cs_value_price | 否 |  |  |
| 53 | cb_value_price | 否 |  |  |
| 54 | cs_value_price_date | 否 |  |  |
| 55 | cb_value_price_date | 否 |  |  |
| 56 | transaction_no | 否 |  |  |
| 57 | position_str | 否 |  | init_date(8)+exchange_type(4)+stock_code(8) |
| 58 | stock_name | 否 | H |  |
| 59 | stock_type | 否 | H |  |
| 60 | sub_stock_type | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_price | ART | 是 | stock_code, exchange_type, init_date, stock_code, exchange_type, init_date |
| idx_rpt_usps_price | ART | 是 | stock_code, exchange_type, init_date, stock_code, exchange_type, init_date |
| idx_price | ART | 是 | stock_code, exchange_type, init_date, stock_code, exchange_type, init_date |
| idx_rpt_usps_price | ART | 是 | stock_code, exchange_type, init_date, stock_code, exchange_type, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_price | stock_code, exchange_type, init_date, stock_code, exchange_type, init_date |
| idx_price | stock_code, exchange_type, init_date, stock_code, exchange_type, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-26 18:07:43 | 8.26.2.94 | 刘珊珊 | 所有表usps_price，添加了表字段(position_str);
 |
| 2025-11-10 13:25:22 | 3.0.2.87 | 洪略 | 补齐历史表信息 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-27 10:26:48 | 3.0.2.56 | 洪略 | 新增 |
| 2025-11-26 18:07:43 | 8.26.2.94 | 刘珊珊 | 所有表usps_price，添加了表字段(position_str);
 |
| 2025-11-10 13:25:22 | 3.0.2.87 | 洪略 | 补齐历史表信息 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-27 10:26:48 | 3.0.2.56 | 洪略 | 新增 |

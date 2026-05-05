# usps_bt_bookinginfo - 债券现券竞买预约信息表

**表对象ID**: 69
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | init_date | 否 |  |  |
| 4 | bid_id | 否 |  |  |
| 5 | bid_trade_date | 否 |  |  |
| 6 | bid_pre_amount | 否 |  |  |
| 7 | min_deal_amount | 否 |  |  |
| 8 | bid_deal_way | 否 |  |  |
| 9 | anonymous_flag | 否 |  |  |
| 10 | agency_no | 否 |  |  |
| 11 | bond_investor_type | 否 |  |  |
| 12 | up_price | 否 |  |  |
| 13 | down_price | 否 |  |  |
| 14 | settle_type | 否 |  |  |
| 15 | settle_period | 否 |  |  |
| 16 | bid_hq_status | 否 |  |  |
| 17 | modify_date | 否 |  |  |
| 18 | transaction_no | 否 |  |  |
| 19 | exchange_type | 否 |  |  |
| 20 | stock_code | 否 |  |  |
| 21 | init_date | 否 |  |  |
| 22 | bid_id | 否 |  |  |
| 23 | bid_trade_date | 否 |  |  |
| 24 | bid_pre_amount | 否 |  |  |
| 25 | min_deal_amount | 否 |  |  |
| 26 | bid_deal_way | 否 |  |  |
| 27 | anonymous_flag | 否 |  |  |
| 28 | agency_no | 否 |  |  |
| 29 | bond_investor_type | 否 |  |  |
| 30 | up_price | 否 |  |  |
| 31 | down_price | 否 |  |  |
| 32 | settle_type | 否 |  |  |
| 33 | settle_period | 否 |  |  |
| 34 | bid_hq_status | 否 |  |  |
| 35 | modify_date | 否 |  |  |
| 36 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_bt_bookinginfo | ART | 是 | bid_id, bid_trade_date, exchange_type, bid_id, bid_trade_date, exchange_type |
| idx_usps_bt_bookinginfo | ART | 是 | bid_id, bid_trade_date, exchange_type, bid_id, bid_trade_date, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_bt_bookinginfo | bid_id, bid_trade_date, exchange_type, bid_id, bid_trade_date, exchange_type |
| idx_usps_bt_bookinginfo | bid_id, bid_trade_date, exchange_type, bid_id, bid_trade_date, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-05 17:07:00 | 3.0.2.2001 | 蒋浩宇 | 物理表usps_bt_bookinginfo，添加了表字段(transaction_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 18:58 | 0.0.0.7 | 汪林 | 新增usps_bt_bookinginfo表 |
| 2025-04-05 17:07:00 | 3.0.2.2001 | 蒋浩宇 | 物理表usps_bt_bookinginfo，添加了表字段(transaction_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 18:58 | 0.0.0.7 | 汪林 | 新增usps_bt_bookinginfo表 |

# usps_cbpprice - 综合业务行情表

**表对象ID**: 68
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 76 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | order_no | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | seat_no | 否 |  |  |
| 5 | cbptrans_type | 否 |  |  |
| 6 | cbphq_type | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | stock_name | 否 |  |  |
| 9 | entrust_price | 否 |  |  |
| 10 | entrust_amount | 否 |  |  |
| 11 | business_amount | 否 |  |  |
| 12 | compact_term | 否 |  |  |
| 13 | relation_name | 否 |  |  |
| 14 | relation_tel | 否 |  |  |
| 15 | cbpconfer_id | 否 |  |  |
| 16 | report_time | 否 |  |  |
| 17 | busin_type_id | 否 |  |  |
| 18 | entrust_hq_type | 否 |  |  |
| 19 | entrust_bs | 否 |  |  |
| 20 | agency_no | 否 |  |  |
| 21 | bond_investor_type | 否 |  |  |
| 22 | bond_investor_id | 否 |  |  |
| 23 | brp_investor_name | 否 |  |  |
| 24 | trader_id | 否 |  |  |
| 25 | settle_type | 否 |  |  |
| 26 | settle_period | 否 |  |  |
| 27 | bid_id | 否 |  |  |
| 28 | bid_transtype | 否 |  |  |
| 29 | bid_deal_way | 否 |  |  |
| 30 | up_price | 否 |  |  |
| 31 | down_price | 否 |  |  |
| 32 | min_deal_amount | 否 |  |  |
| 33 | bid_trade_date | 否 |  |  |
| 34 | bid_hq_status | 否 |  |  |
| 35 | channel_no | 否 |  |  |
| 36 | update_date | 否 |  |  |
| 37 | update_time | 否 |  |  |
| 38 | position_str | 否 |  | init_date(8)+exchange_type(4)+order_no(10)+channel_no(16) |
| 39 | init_date | 否 |  |  |
| 40 | order_no | 否 |  |  |
| 41 | exchange_type | 否 |  |  |
| 42 | seat_no | 否 |  |  |
| 43 | cbptrans_type | 否 |  |  |
| 44 | cbphq_type | 否 |  |  |
| 45 | stock_code | 否 |  |  |
| 46 | stock_name | 否 |  |  |
| 47 | entrust_price | 否 |  |  |
| 48 | entrust_amount | 否 |  |  |
| 49 | business_amount | 否 |  |  |
| 50 | compact_term | 否 |  |  |
| 51 | relation_name | 否 |  |  |
| 52 | relation_tel | 否 |  |  |
| 53 | cbpconfer_id | 否 |  |  |
| 54 | report_time | 否 |  |  |
| 55 | busin_type_id | 否 |  |  |
| 56 | entrust_hq_type | 否 |  |  |
| 57 | entrust_bs | 否 |  |  |
| 58 | agency_no | 否 |  |  |
| 59 | bond_investor_type | 否 |  |  |
| 60 | bond_investor_id | 否 |  |  |
| 61 | brp_investor_name | 否 |  |  |
| 62 | trader_id | 否 |  |  |
| 63 | settle_type | 否 |  |  |
| 64 | settle_period | 否 |  |  |
| 65 | bid_id | 否 |  |  |
| 66 | bid_transtype | 否 |  |  |
| 67 | bid_deal_way | 否 |  |  |
| 68 | up_price | 否 |  |  |
| 69 | down_price | 否 |  |  |
| 70 | min_deal_amount | 否 |  |  |
| 71 | bid_trade_date | 否 |  |  |
| 72 | bid_hq_status | 否 |  |  |
| 73 | channel_no | 否 |  |  |
| 74 | update_date | 否 |  |  |
| 75 | update_time | 否 |  |  |
| 76 | position_str | 否 |  | init_date(8)+exchange_type(4)+order_no(10)+channel_no(16) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_cbpprice | ART | 是 | init_date, exchange_type, order_no, channel_no, init_date, exchange_type, order_no, channel_no |
| uk_rpt_uspscbpprice | ART | 是 | init_date, exchange_type, order_no, channel_no, init_date, exchange_type, order_no, channel_no |
| idx_usps_cbpprice | ART | 是 | init_date, exchange_type, order_no, channel_no, init_date, exchange_type, order_no, channel_no |
| uk_rpt_uspscbpprice | ART | 是 | init_date, exchange_type, order_no, channel_no, init_date, exchange_type, order_no, channel_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_cbpprice | init_date, exchange_type, order_no, channel_no, init_date, exchange_type, order_no, channel_no |
| idx_usps_cbpprice | init_date, exchange_type, order_no, channel_no, init_date, exchange_type, order_no, channel_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-02-19 11:24:00 | 3.0.6.80 | 李想 | 物理表usps_cbpprice，添加了表字段(update_date);
物理表usps_cbpprice，添加了表... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 18:58 | 0.0.0.7 | 汪林 | 新增usps_cbpprice表 |
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-02-19 11:24:00 | 3.0.6.80 | 李想 | 物理表usps_cbpprice，添加了表字段(update_date);
物理表usps_cbpprice，添加了表... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 18:58 | 0.0.0.7 | 汪林 | 新增usps_cbpprice表 |

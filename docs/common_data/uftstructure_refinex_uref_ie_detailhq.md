# uref_ie_detailhq - 信息交互平台明细行情表

**表对象ID**: 6228
**所属模块**: refinex
**数据空间**: HS_UFT_DATA

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | ie_hq_kind | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | ref_term | 否 |  |  |
| 6 | reflend_rate | 否 |  |  |
| 7 | refborrow_rate | 否 |  |  |
| 8 | lend_report_amount | 否 |  |  |
| 9 | borrow_report_amount | 否 |  |  |
| 10 | business_amount | 否 |  |  |
| 11 | business_balance | 否 |  |  |
| 12 | match_business_amount | 否 |  |  |
| 13 | match_business_balance | 否 |  |  |
| 14 | high_rate | 否 |  |  |
| 15 | low_rate | 否 |  |  |
| 16 | last_rate | 否 |  |  |
| 17 | weightavg_rate | 否 |  |  |
| 18 | reflend_gear_str | 否 |  |  |
| 19 | refborrow_gear_str | 否 |  |  |
| 20 | modify_time | 否 |  |  |
| 21 | position_str | 否 |  |  |
| 22 | init_date | 否 |  |  |
| 23 | ie_hq_kind | 否 |  |  |
| 24 | stock_code | 否 |  |  |
| 25 | exchange_type | 否 |  |  |
| 26 | ref_term | 否 |  |  |
| 27 | reflend_rate | 否 |  |  |
| 28 | refborrow_rate | 否 |  |  |
| 29 | lend_report_amount | 否 |  |  |
| 30 | borrow_report_amount | 否 |  |  |
| 31 | business_amount | 否 |  |  |
| 32 | business_balance | 否 |  |  |
| 33 | match_business_amount | 否 |  |  |
| 34 | match_business_balance | 否 |  |  |
| 35 | high_rate | 否 |  |  |
| 36 | low_rate | 否 |  |  |
| 37 | last_rate | 否 |  |  |
| 38 | weightavg_rate | 否 |  |  |
| 39 | reflend_gear_str | 否 |  |  |
| 40 | refborrow_gear_str | 否 |  |  |
| 41 | modify_time | 否 |  |  |
| 42 | position_str | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_iedetailhq | ART | 是 | ie_hq_kind, stock_code, exchange_type, ref_term, reflend_rate, ie_hq_kind, stock_code, exchange_type, ref_term, reflend_rate |
| idx_iedetailhq | ART | 是 | ie_hq_kind, stock_code, exchange_type, ref_term, reflend_rate, ie_hq_kind, stock_code, exchange_type, ref_term, reflend_rate |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_iedetailhq | ie_hq_kind, stock_code, exchange_type, ref_term, reflend_rate, ie_hq_kind, stock_code, exchange_type, ref_term, reflend_rate |
| idx_iedetailhq | ie_hq_kind, stock_code, exchange_type, ref_term, reflend_rate, ie_hq_kind, stock_code, exchange_type, ref_term, reflend_rate |

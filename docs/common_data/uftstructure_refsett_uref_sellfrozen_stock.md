# uref_sellfrozen_stock - 可售冻结股份表

**表对象ID**: 6171
**所属模块**: refsett
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_type | 否 |  |  |
| 6 | available_amount | 否 |  |  |
| 7 | seat_no | 否 |  |  |
| 8 | stock_property | 否 |  |  |
| 9 | hkdc_circulate_type | 否 |  |  |
| 10 | date_clear | 否 |  |  |
| 11 | position_str | 否 |  |  |
| 12 | tohis_date | 否 | H |  |
| 13 | stock_name | 否 | H |  |
| 14 | sub_stock_type | 否 | H |  |
| 15 | init_date | 否 |  |  |
| 16 | stock_account | 否 |  |  |
| 17 | stock_code | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | stock_type | 否 |  |  |
| 20 | available_amount | 否 |  |  |
| 21 | seat_no | 否 |  |  |
| 22 | stock_property | 否 |  |  |
| 23 | hkdc_circulate_type | 否 |  |  |
| 24 | date_clear | 否 |  |  |
| 25 | position_str | 否 |  |  |
| 26 | tohis_date | 否 | H |  |
| 27 | stock_name | 否 | H |  |
| 28 | sub_stock_type | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_sellfrozenstock | ART | 是 | stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type, stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type |
| idx_sellfrozenstock_pos | ART | 是 | position_str, position_str |
| idx_sellfrozenstock | ART | 是 | stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type, stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type |
| idx_sellfrozenstock_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_sellfrozenstock | stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type, stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type |
| rpt_uk_sellfrozenstock | tohis_date, position_str, tohis_date, position_str |
| idx_sellfrozenstock | stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type, stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type |
| rpt_uk_sellfrozenstock | tohis_date, position_str, tohis_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-16 10:40:12 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-10-16 10:40:12 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

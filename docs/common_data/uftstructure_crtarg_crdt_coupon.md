# crdt_coupon - 融资融券优惠券表

**表对象ID**: 7121
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 76 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | money_type | 否 |  |  |
| 5 | perfer_no | 否 |  |  |
| 6 | coupon_type | 否 |  |  |
| 7 | coupon_status | 否 |  |  |
| 8 | en_exchange_type | 否 |  |  |
| 9 | en_stock_type | 否 |  |  |
| 10 | en_compact_type | 否 |  |  |
| 11 | total_prefer_balance | 否 |  |  |
| 12 | prefer_balance | 否 |  |  |
| 13 | begin_date | 否 |  |  |
| 14 | end_date | 否 |  |  |
| 15 | remark | 否 |  |  |
| 16 | date_clear | 否 |  |  |
| 17 | begin_discount_balance | 否 |  |  |
| 18 | min_compact_rate | 否 |  |  |
| 19 | satisfied_balance | 否 |  |  |
| 20 | stock_code | 否 |  |  |
| 21 | exchange_type | 否 |  |  |
| 22 | crdt_source | 否 |  |  |
| 23 | discount_rate | 否 |  |  |
| 24 | coupongrp_no | 否 |  |  |
| 25 | update_date | 否 |  |  |
| 26 | update_time | 否 |  |  |
| 27 | transaction_no | 否 |  |  |
| 28 | position_str | 否 |  | fund_account(18)+end_date(10)+begin_date(10)+money_type(3)+p |
| 29 | client_group | 否 | H |  |
| 30 | room_code | 否 | H |  |
| 31 | asset_prop | 否 | H |  |
| 32 | limit_flag | 否 | H |  |
| 33 | risk_level | 否 | H |  |
| 34 | corp_client_group | 否 | H |  |
| 35 | corp_risk_level | 否 | H |  |
| 36 | asset_level | 否 | H |  |
| 37 | client_name | 否 | H |  |
| 38 | client_prop | 否 | H |  |
| 39 | branch_no | 否 |  |  |
| 40 | fund_account | 否 |  |  |
| 41 | client_id | 否 |  |  |
| 42 | money_type | 否 |  |  |
| 43 | perfer_no | 否 |  |  |
| 44 | coupon_type | 否 |  |  |
| 45 | coupon_status | 否 |  |  |
| 46 | en_exchange_type | 否 |  |  |
| 47 | en_stock_type | 否 |  |  |
| 48 | en_compact_type | 否 |  |  |
| 49 | total_prefer_balance | 否 |  |  |
| 50 | prefer_balance | 否 |  |  |
| 51 | begin_date | 否 |  |  |
| 52 | end_date | 否 |  |  |
| 53 | remark | 否 |  |  |
| 54 | date_clear | 否 |  |  |
| 55 | begin_discount_balance | 否 |  |  |
| 56 | min_compact_rate | 否 |  |  |
| 57 | satisfied_balance | 否 |  |  |
| 58 | stock_code | 否 |  |  |
| 59 | exchange_type | 否 |  |  |
| 60 | crdt_source | 否 |  |  |
| 61 | discount_rate | 否 |  |  |
| 62 | coupongrp_no | 否 |  |  |
| 63 | update_date | 否 |  |  |
| 64 | update_time | 否 |  |  |
| 65 | transaction_no | 否 |  |  |
| 66 | position_str | 否 |  | fund_account(18)+end_date(10)+begin_date(10)+money_type(3)+p |
| 67 | client_group | 否 | H |  |
| 68 | room_code | 否 | H |  |
| 69 | asset_prop | 否 | H |  |
| 70 | limit_flag | 否 | H |  |
| 71 | risk_level | 否 | H |  |
| 72 | corp_client_group | 否 | H |  |
| 73 | corp_risk_level | 否 | H |  |
| 74 | asset_level | 否 | H |  |
| 75 | client_name | 否 | H |  |
| 76 | client_prop | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdtcoupon | ART | 是 | fund_account, end_date, begin_date, money_type, perfer_no, fund_account, end_date, begin_date, money_type, perfer_no |
| idx_crdtcoupon_id | ART | 是 | client_id, client_id |
| uk_rpt_crdtcoupon | ART | 是 | date_clear, branch_no, position_str, date_clear, branch_no, position_str |
| idx_rpt_crdtcoupon_cid | ART | 是 | date_clear, client_id, fund_account, position_str, date_clear, client_id, fund_account, position_str |
| idx_crdtcoupon | ART | 是 | fund_account, end_date, begin_date, money_type, perfer_no, fund_account, end_date, begin_date, money_type, perfer_no |
| idx_crdtcoupon_id | ART | 是 | client_id, client_id |
| uk_rpt_crdtcoupon | ART | 是 | date_clear, branch_no, position_str, date_clear, branch_no, position_str |
| idx_rpt_crdtcoupon_cid | ART | 是 | date_clear, client_id, fund_account, position_str, date_clear, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdtcoupon | fund_account, end_date, begin_date, money_type, perfer_no, fund_account, end_date, begin_date, money_type, perfer_no |
| idx_crdtcoupon | fund_account, end_date, begin_date, money_type, perfer_no, fund_account, end_date, begin_date, money_type, perfer_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-16 19:02:30 | 3.0.6.1066 | 周兆军 | 表空间调整为HS_UFT_DATA |
| 2025-05-06 20:33:58 | 3.0.6.109 | 常行 | 新增表 |
| 2025-09-16 19:02:30 | 3.0.6.1066 | 周兆军 | 表空间调整为HS_UFT_DATA |
| 2025-05-06 20:33:58 | 3.0.6.109 | 常行 | 新增表 |

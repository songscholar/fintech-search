# crdt_coupon_jour - 融资融券优惠券流水表

**表对象ID**: 7122
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 78 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | operator_no | 否 |  |  |
| 4 | op_branch_no | 否 |  |  |
| 5 | curr_date | 否 |  |  |
| 6 | curr_time | 否 |  |  |
| 7 | branch_no | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | client_id | 否 |  |  |
| 10 | money_type | 否 |  |  |
| 11 | perfer_no | 否 |  |  |
| 12 | coupon_type | 否 |  |  |
| 13 | coupon_status | 否 |  |  |
| 14 | en_exchange_type | 否 |  |  |
| 15 | en_stock_type | 否 |  |  |
| 16 | en_compact_type | 否 |  |  |
| 17 | business_flag | 否 |  |  |
| 18 | occur_balance | 否 |  |  |
| 19 | post_balance | 否 |  |  |
| 20 | begin_date | 否 |  |  |
| 21 | end_date | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | compact_id | 否 |  |  |
| 24 | pendfare_id | 否 |  |  |
| 25 | position_str | 否 |  |  |
| 26 | stock_code | 否 |  |  |
| 27 | exchange_type | 否 |  |  |
| 28 | crdt_source | 否 |  |  |
| 29 | coupongrp_no | 否 |  |  |
| 30 | client_group | 否 | H |  |
| 31 | room_code | 否 | H |  |
| 32 | asset_prop | 否 | H |  |
| 33 | limit_flag | 否 | H |  |
| 34 | risk_level | 否 | H |  |
| 35 | corp_client_group | 否 | H |  |
| 36 | corp_risk_level | 否 | H |  |
| 37 | asset_level | 否 | H |  |
| 38 | client_name | 否 | H |  |
| 39 | client_prop | 否 | H |  |
| 40 | init_date | 否 |  |  |
| 41 | serial_no | 否 |  |  |
| 42 | operator_no | 否 |  |  |
| 43 | op_branch_no | 否 |  |  |
| 44 | curr_date | 否 |  |  |
| 45 | curr_time | 否 |  |  |
| 46 | branch_no | 否 |  |  |
| 47 | fund_account | 否 |  |  |
| 48 | client_id | 否 |  |  |
| 49 | money_type | 否 |  |  |
| 50 | perfer_no | 否 |  |  |
| 51 | coupon_type | 否 |  |  |
| 52 | coupon_status | 否 |  |  |
| 53 | en_exchange_type | 否 |  |  |
| 54 | en_stock_type | 否 |  |  |
| 55 | en_compact_type | 否 |  |  |
| 56 | business_flag | 否 |  |  |
| 57 | occur_balance | 否 |  |  |
| 58 | post_balance | 否 |  |  |
| 59 | begin_date | 否 |  |  |
| 60 | end_date | 否 |  |  |
| 61 | remark | 否 |  |  |
| 62 | compact_id | 否 |  |  |
| 63 | pendfare_id | 否 |  |  |
| 64 | position_str | 否 |  |  |
| 65 | stock_code | 否 |  |  |
| 66 | exchange_type | 否 |  |  |
| 67 | crdt_source | 否 |  |  |
| 68 | coupongrp_no | 否 |  |  |
| 69 | client_group | 否 | H |  |
| 70 | room_code | 否 | H |  |
| 71 | asset_prop | 否 | H |  |
| 72 | limit_flag | 否 | H |  |
| 73 | risk_level | 否 | H |  |
| 74 | corp_client_group | 否 | H |  |
| 75 | corp_risk_level | 否 | H |  |
| 76 | asset_level | 否 | H |  |
| 77 | client_name | 否 | H |  |
| 78 | client_prop | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdtcouponjour | ART | 是 | position_str, position_str |
| idx_crdtcouponjour_acct | ART | 是 | fund_account, fund_account |
| idx_crdtcouponjour_id | ART | 是 | client_id, client_id |
| uk_rpt_crdtcouponjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_crdtcouponjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_crdtcouponjour | ART | 是 | position_str, position_str |
| idx_crdtcouponjour_acct | ART | 是 | fund_account, fund_account |
| idx_crdtcouponjour_id | ART | 是 | client_id, client_id |
| uk_rpt_crdtcouponjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_crdtcouponjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdtcouponjour | position_str, position_str |
| idx_crdtcouponjour | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-16 19:02:30 | 3.0.6.1066 | 周兆军 | 表空间调整为HS_UFT_DATA |
| 2025-05-06 20:34:17 | 3.0.6.109 | 常行 | 新增表 |
| 2025-09-16 19:02:30 | 3.0.6.1066 | 周兆军 | 表空间调整为HS_UFT_DATA |
| 2025-05-06 20:34:17 | 3.0.6.109 | 常行 | 新增表 |

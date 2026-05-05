# qrp_quota_jour - 报价回购额度控制流水表

**表对象ID**: 1599
**所属模块**: qmsquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | company_no | 否 |  |  |
| 8 | cancel_serialno | 否 |  |  |
| 9 | entrust_type | 否 |  |  |
| 10 | entrust_prop | 否 |  |  |
| 11 | occur_balance | 否 |  |  |
| 12 | qrp_approv_quota | 否 |  |  |
| 13 | qrp_actual_quota | 否 |  |  |
| 14 | qrp_impawn_balance | 否 |  |  |
| 15 | qrp_buy_quota | 否 |  |  |
| 16 | qrp_term_quota | 否 |  |  |
| 17 | qrp_huge_ratio | 否 |  |  |
| 18 | qrp_buy_balance | 否 |  |  |
| 19 | qrp_term_balance | 否 |  |  |
| 20 | qrp_undue_balance | 否 |  |  |
| 21 | qrp_due_balance | 否 |  |  |
| 22 | cash_balance | 否 |  |  |
| 23 | qrp_day_orderup_quota | 否 |  |  |
| 24 | qrp_sum_uncomebalance_limit | 否 |  |  |
| 25 | exclusive_quota_flag | 否 |  |  |
| 26 | exclusive_quota_endtime | 否 |  |  |
| 27 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 28 | init_date | 否 |  |  |
| 29 | serial_no | 否 |  |  |
| 30 | curr_date | 否 |  |  |
| 31 | curr_time | 否 |  |  |
| 32 | exchange_type | 否 |  |  |
| 33 | stock_code | 否 |  |  |
| 34 | company_no | 否 |  |  |
| 35 | cancel_serialno | 否 |  |  |
| 36 | entrust_type | 否 |  |  |
| 37 | entrust_prop | 否 |  |  |
| 38 | occur_balance | 否 |  |  |
| 39 | qrp_approv_quota | 否 |  |  |
| 40 | qrp_actual_quota | 否 |  |  |
| 41 | qrp_impawn_balance | 否 |  |  |
| 42 | qrp_buy_quota | 否 |  |  |
| 43 | qrp_term_quota | 否 |  |  |
| 44 | qrp_huge_ratio | 否 |  |  |
| 45 | qrp_buy_balance | 否 |  |  |
| 46 | qrp_term_balance | 否 |  |  |
| 47 | qrp_undue_balance | 否 |  |  |
| 48 | qrp_due_balance | 否 |  |  |
| 49 | cash_balance | 否 |  |  |
| 50 | qrp_day_orderup_quota | 否 |  |  |
| 51 | qrp_sum_uncomebalance_limit | 否 |  |  |
| 52 | exclusive_quota_flag | 否 |  |  |
| 53 | exclusive_quota_endtime | 否 |  |  |
| 54 | position_str | 否 |  | init_date(8)+serial_no(10) |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_qrpquotajour | 默认 | 否 |  |
| idx_qrpquotajour_cancel | 默认 | 否 |  |
| uk_qrpquotajour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_qrpquotajour_cancel | ART | 是 | cancel_serialno, cancel_serialno |
| uk_qrpquotajour | 默认 | 否 |  |
| idx_qrpquotajour_cancel | 默认 | 否 |  |
| uk_qrpquotajour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_qrpquotajour_cancel | ART | 是 | cancel_serialno, cancel_serialno |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| uk_qrp_quota_jour | init_date, serial_no, init_date, serial_no |
| uk_qrp_quota_jour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 17:03:48 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:57:44 | 3.0.2.5 | taocong45644 | 当前表qrp_quota_jour，修改了索引uk_qrpquotajour,索引字段修改为：(init_date,se... |
| 2025-04-03 12:01:56 | V3.0.2.2002 | 王云乾 | 新增 |
| 2026-03-05 17:03:48 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:57:44 | 3.0.2.5 | taocong45644 | 当前表qrp_quota_jour，修改了索引uk_qrpquotajour,索引字段修改为：(init_date,se... |
| 2025-04-03 12:01:56 | V3.0.2.2002 | 王云乾 | 新增 |

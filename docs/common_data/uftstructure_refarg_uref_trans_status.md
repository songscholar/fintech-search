# uref_trans_status - 转融通报盘状态表

**表对象ID**: 6018
**所属模块**: refarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | reftrans_type | 否 |  |  |
| 3 | login_pbu | 否 |  |  |
| 4 | target_ar | 否 |  |  |
| 5 | trans_name | 否 |  |  |
| 6 | report_status | 否 |  |  |
| 7 | login_times | 否 |  |  |
| 8 | opening_status | 否 |  |  |
| 9 | transplat_type | 否 |  |  |
| 10 | seat_no | 否 |  |  |
| 11 | csfc_organ_code | 否 |  |  |
| 12 | csfc_borrower_code | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | reftrans_type | 否 |  |  |
| 15 | login_pbu | 否 |  |  |
| 16 | target_ar | 否 |  |  |
| 17 | trans_name | 否 |  |  |
| 18 | report_status | 否 |  |  |
| 19 | login_times | 否 |  |  |
| 20 | opening_status | 否 |  |  |
| 21 | transplat_type | 否 |  |  |
| 22 | seat_no | 否 |  |  |
| 23 | csfc_organ_code | 否 |  |  |
| 24 | csfc_borrower_code | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_reftransstatus | ART | 是 | trans_name, exchange_type, seat_no, trans_name, exchange_type, seat_no |
| idx_reftransstatus | ART | 是 | trans_name, exchange_type, seat_no, trans_name, exchange_type, seat_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_reftransstatus | trans_name, exchange_type, seat_no, trans_name, exchange_type, seat_no |
| idx_reftransstatus | trans_name, exchange_type, seat_no, trans_name, exchange_type, seat_no |

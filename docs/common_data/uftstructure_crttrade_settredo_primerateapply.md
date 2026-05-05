# settredo_primerateapply - 日终清算优惠利率申请表

**表对象ID**: 7600
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 72 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | op_station | 否 |  |  |
| 5 | serial_no | 否 |  |  |
| 6 | branch_no | 否 |  |  |
| 7 | client_id | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | compact_type | 否 |  |  |
| 10 | avg_fin_balance | 否 |  |  |
| 11 | crdt_buy_ratio | 否 |  |  |
| 12 | crdt_sell_ratio | 否 |  |  |
| 13 | fin_buy_ratio | 否 |  |  |
| 14 | stock_sell_ratio | 否 |  |  |
| 15 | primerate_apply_status | 否 |  |  |
| 16 | audit_primerate | 否 |  |  |
| 17 | apply_primerate | 否 |  |  |
| 18 | primerate_kind | 否 |  |  |
| 19 | date_clear | 否 |  |  |
| 20 | remark | 否 |  |  |
| 21 | position_str | 否 |  |  |
| 22 | op_branch_no | 否 |  |  |
| 23 | operator_no | 否 |  |  |
| 24 | min_buy_ratio | 否 |  |  |
| 25 | min_sell_ratio | 否 |  |  |
| 26 | assure_close_balance | 否 |  |  |
| 27 | net_asset | 否 |  |  |
| 28 | fin_close_balance | 否 |  |  |
| 29 | apply_slo_primerate | 否 |  |  |
| 30 | audit_slo_primerate | 否 |  |  |
| 31 | valid_date | 否 |  |  |
| 32 | primerate_apply_type | 否 |  |  |
| 33 | primerate_reset_mode | 否 |  |  |
| 34 | credit_quota | 是 |  |  |
| 35 | sett_batch_no | 否 |  |  |
| 36 | sett_dml_type | 否 |  |  |
| 37 | init_date | 否 |  |  |
| 38 | curr_date | 否 |  |  |
| 39 | curr_time | 否 |  |  |
| 40 | op_station | 否 |  |  |
| 41 | serial_no | 否 |  |  |
| 42 | branch_no | 否 |  |  |
| 43 | client_id | 否 |  |  |
| 44 | fund_account | 否 |  |  |
| 45 | compact_type | 否 |  |  |
| 46 | avg_fin_balance | 否 |  |  |
| 47 | crdt_buy_ratio | 否 |  |  |
| 48 | crdt_sell_ratio | 否 |  |  |
| 49 | fin_buy_ratio | 否 |  |  |
| 50 | stock_sell_ratio | 否 |  |  |
| 51 | primerate_apply_status | 否 |  |  |
| 52 | audit_primerate | 否 |  |  |
| 53 | apply_primerate | 否 |  |  |
| 54 | primerate_kind | 否 |  |  |
| 55 | date_clear | 否 |  |  |
| 56 | remark | 否 |  |  |
| 57 | position_str | 否 |  |  |
| 58 | op_branch_no | 否 |  |  |
| 59 | operator_no | 否 |  |  |
| 60 | min_buy_ratio | 否 |  |  |
| 61 | min_sell_ratio | 否 |  |  |
| 62 | assure_close_balance | 否 |  |  |
| 63 | net_asset | 否 |  |  |
| 64 | fin_close_balance | 否 |  |  |
| 65 | apply_slo_primerate | 否 |  |  |
| 66 | audit_slo_primerate | 否 |  |  |
| 67 | valid_date | 否 |  |  |
| 68 | primerate_apply_type | 否 |  |  |
| 69 | primerate_reset_mode | 否 |  |  |
| 70 | credit_quota | 是 |  |  |
| 71 | sett_batch_no | 否 |  |  |
| 72 | sett_dml_type | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_primerateapply | ART | 是 | init_date, serial_no, branch_no, sett_batch_no, init_date, serial_no, branch_no, sett_batch_no |
| idx_strd_primerateapply | ART | 是 | init_date, serial_no, branch_no, sett_batch_no, init_date, serial_no, branch_no, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_primerateapply | init_date, serial_no, branch_no, sett_batch_no, init_date, serial_no, branch_no, sett_batch_no |
| idx_strd_primerateapply | init_date, serial_no, branch_no, sett_batch_no, init_date, serial_no, branch_no, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-03 10:21:01 | 3.0.6.1066 | 沈勋 | 新增 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2025-09-03 10:21:01 | 3.0.6.1066 | 沈勋 | 新增 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |

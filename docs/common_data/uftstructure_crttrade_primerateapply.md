# primerateapply - 优惠利率申请表

**表对象ID**: 7575
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 90 个）

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
| 35 | client_name | 否 | H |  |
| 36 | corp_client_group | 否 | H |  |
| 37 | client_group | 否 | H |  |
| 38 | room_code | 否 | H |  |
| 39 | asset_prop | 否 | H |  |
| 40 | limit_flag | 否 | H |  |
| 41 | client_prop | 否 | H |  |
| 42 | asset_level | 否 | H |  |
| 43 | risk_level | 否 | H |  |
| 44 | corp_risk_level | 否 | H |  |
| 45 | tohis_date | 否 | H |  |
| 46 | init_date | 否 |  |  |
| 47 | curr_date | 否 |  |  |
| 48 | curr_time | 否 |  |  |
| 49 | op_station | 否 |  |  |
| 50 | serial_no | 否 |  |  |
| 51 | branch_no | 否 |  |  |
| 52 | client_id | 否 |  |  |
| 53 | fund_account | 否 |  |  |
| 54 | compact_type | 否 |  |  |
| 55 | avg_fin_balance | 否 |  |  |
| 56 | crdt_buy_ratio | 否 |  |  |
| 57 | crdt_sell_ratio | 否 |  |  |
| 58 | fin_buy_ratio | 否 |  |  |
| 59 | stock_sell_ratio | 否 |  |  |
| 60 | primerate_apply_status | 否 |  |  |
| 61 | audit_primerate | 否 |  |  |
| 62 | apply_primerate | 否 |  |  |
| 63 | primerate_kind | 否 |  |  |
| 64 | date_clear | 否 |  |  |
| 65 | remark | 否 |  |  |
| 66 | position_str | 否 |  |  |
| 67 | op_branch_no | 否 |  |  |
| 68 | operator_no | 否 |  |  |
| 69 | min_buy_ratio | 否 |  |  |
| 70 | min_sell_ratio | 否 |  |  |
| 71 | assure_close_balance | 否 |  |  |
| 72 | net_asset | 否 |  |  |
| 73 | fin_close_balance | 否 |  |  |
| 74 | apply_slo_primerate | 否 |  |  |
| 75 | audit_slo_primerate | 否 |  |  |
| 76 | valid_date | 否 |  |  |
| 77 | primerate_apply_type | 否 |  |  |
| 78 | primerate_reset_mode | 否 |  |  |
| 79 | credit_quota | 是 |  |  |
| 80 | client_name | 否 | H |  |
| 81 | corp_client_group | 否 | H |  |
| 82 | client_group | 否 | H |  |
| 83 | room_code | 否 | H |  |
| 84 | asset_prop | 否 | H |  |
| 85 | limit_flag | 否 | H |  |
| 86 | client_prop | 否 | H |  |
| 87 | asset_level | 否 | H |  |
| 88 | risk_level | 否 | H |  |
| 89 | corp_risk_level | 否 | H |  |
| 90 | tohis_date | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_primerateapply | ART | 是 | init_date, serial_no, branch_no, init_date, serial_no, branch_no |
| idx_primerateapply_pos | ART | 是 | position_str, position_str |
| uk_rpt_primerateapply | ART | 是 | tohis_date, branch_no, position_str, tohis_date, branch_no, position_str |
| idx_rpt_primerateapply_cid | ART | 是 | tohis_date, client_id, fund_account, position_str, tohis_date, client_id, fund_account, position_str |
| idx_primerateapply | ART | 是 | init_date, serial_no, branch_no, init_date, serial_no, branch_no |
| idx_primerateapply_pos | ART | 是 | position_str, position_str |
| uk_rpt_primerateapply | ART | 是 | tohis_date, branch_no, position_str, tohis_date, branch_no, position_str |
| idx_rpt_primerateapply_cid | ART | 是 | tohis_date, client_id, fund_account, position_str, tohis_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_primerateapply | init_date, serial_no, branch_no, init_date, serial_no, branch_no |
| idx_primerateapply | init_date, serial_no, branch_no, init_date, serial_no, branch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-11 19:01:43 | 3.0.8.11 | 沈勋 | 新增idx_primerateapply_pos索引 |
| 2025-08-29 10:05:42 | 3.0.2.2015 | huangzh | 所有表primerateapply，添加了表字段(credit_quota);
 |
| 2025-08-29 10:05:06 | 3.0.2.2015 | huangzh | 所有表primerateapply，删除了表字段（client_quota）；
 |
| 2025-07-14 10:16:22 | 3.0.2.2009 | huangzh | 物理表primerateapply，添加了表字段(init_date);
物理表primerateapply，添加了表... |
| 2025-11-11 19:01:43 | 3.0.8.11 | 沈勋 | 新增idx_primerateapply_pos索引 |
| 2025-08-29 10:05:42 | 3.0.2.2015 | huangzh | 所有表primerateapply，添加了表字段(credit_quota);
 |
| 2025-08-29 10:05:06 | 3.0.2.2015 | huangzh | 所有表primerateapply，删除了表字段（client_quota）；
 |
| 2025-07-14 10:16:22 | 3.0.2.2009 | huangzh | 物理表primerateapply，添加了表字段(init_date);
物理表primerateapply，添加了表... |

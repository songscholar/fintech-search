# primerateapplyjour - 优惠利率申请流水表

**表对象ID**: 7576
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 66 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | operator_no | 否 |  |  |
| 6 | op_branch_no | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | op_station | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | client_id | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | compact_type | 否 |  |  |
| 13 | primerate_apply_status | 否 |  |  |
| 14 | apply_primerate | 否 |  |  |
| 15 | audit_primerate | 否 |  |  |
| 16 | apply_slo_primerate | 否 |  |  |
| 17 | audit_slo_primerate | 否 |  |  |
| 18 | primerate_apply_type | 否 |  |  |
| 19 | primerate_kind | 否 |  |  |
| 20 | primerate_reset_mode | 否 |  |  |
| 21 | remark | 否 |  |  |
| 22 | join_position_str | 否 |  |  |
| 23 | position_str | 否 |  |  |
| 24 | client_name | 否 | H |  |
| 25 | corp_client_group | 否 | H |  |
| 26 | client_group | 否 | H |  |
| 27 | room_code | 否 | H |  |
| 28 | asset_prop | 否 | H |  |
| 29 | limit_flag | 否 | H |  |
| 30 | client_prop | 否 | H |  |
| 31 | asset_level | 否 | H |  |
| 32 | risk_level | 否 | H |  |
| 33 | corp_risk_level | 否 | H |  |
| 34 | init_date | 否 |  |  |
| 35 | serial_no | 否 |  |  |
| 36 | curr_date | 否 |  |  |
| 37 | curr_time | 否 |  |  |
| 38 | operator_no | 否 |  |  |
| 39 | op_branch_no | 否 |  |  |
| 40 | op_entrust_way | 否 |  |  |
| 41 | op_station | 否 |  |  |
| 42 | branch_no | 否 |  |  |
| 43 | client_id | 否 |  |  |
| 44 | fund_account | 否 |  |  |
| 45 | compact_type | 否 |  |  |
| 46 | primerate_apply_status | 否 |  |  |
| 47 | apply_primerate | 否 |  |  |
| 48 | audit_primerate | 否 |  |  |
| 49 | apply_slo_primerate | 否 |  |  |
| 50 | audit_slo_primerate | 否 |  |  |
| 51 | primerate_apply_type | 否 |  |  |
| 52 | primerate_kind | 否 |  |  |
| 53 | primerate_reset_mode | 否 |  |  |
| 54 | remark | 否 |  |  |
| 55 | join_position_str | 否 |  |  |
| 56 | position_str | 否 |  |  |
| 57 | client_name | 否 | H |  |
| 58 | corp_client_group | 否 | H |  |
| 59 | client_group | 否 | H |  |
| 60 | room_code | 否 | H |  |
| 61 | asset_prop | 否 | H |  |
| 62 | limit_flag | 否 | H |  |
| 63 | client_prop | 否 | H |  |
| 64 | asset_level | 否 | H |  |
| 65 | risk_level | 否 | H |  |
| 66 | corp_risk_level | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_primerateapplyjour | ART | 是 | position_str, position_str |
| uk_rpt_primerateapplyjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_primerateapplyjour | ART | 是 | position_str, position_str |
| uk_rpt_primerateapplyjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_primerateapplyjour | position_str, position_str |
| idx_primerateapplyjour | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-15 11:05:57 | 3.0.2.2012 | huangzh |  |
| 2025-07-15 11:05:57 | 3.0.2.2012 | huangzh |  |

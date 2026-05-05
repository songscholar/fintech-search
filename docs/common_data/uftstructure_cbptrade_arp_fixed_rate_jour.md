# arp_fixed_rate_jour - 约定购回固定利率流水表

**表对象ID**: 2537
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | op_branch_no | 否 |  |  |
| 6 | operator_no | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | op_station | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | money_type | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | client_id | 否 |  |  |
| 13 | fixed_ratio | 否 |  |  |
| 14 | valid_date | 否 |  |  |
| 15 | rate_mode | 否 |  |  |
| 16 | cbpacct_type | 否 |  |  |
| 17 | remark | 否 |  |  |
| 18 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 19 | init_date | 否 |  |  |
| 20 | serial_no | 否 |  |  |
| 21 | curr_date | 否 |  |  |
| 22 | curr_time | 否 |  |  |
| 23 | op_branch_no | 否 |  |  |
| 24 | operator_no | 否 |  |  |
| 25 | op_entrust_way | 否 |  |  |
| 26 | op_station | 否 |  |  |
| 27 | branch_no | 否 |  |  |
| 28 | money_type | 否 |  |  |
| 29 | fund_account | 否 |  |  |
| 30 | client_id | 否 |  |  |
| 31 | fixed_ratio | 否 |  |  |
| 32 | valid_date | 否 |  |  |
| 33 | rate_mode | 否 |  |  |
| 34 | cbpacct_type | 否 |  |  |
| 35 | remark | 否 |  |  |
| 36 | position_str | 否 |  | init_date(8)+serial_no(10) |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arpfixedratejour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_arpfixedratejour_acct | ART | 是 | fund_account, fund_account |
| idx_arpfixedratejour_id | ART | 是 | client_id, client_id |
| idx_arpfixedratejour_pos | ART | 是 | position_str, position_str |
| idx_arpfixedratejour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_arpfixedratejour_acct | ART | 是 | fund_account, fund_account |
| idx_arpfixedratejour_id | ART | 是 | client_id, client_id |
| idx_arpfixedratejour_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_arpfixedratejour | serial_no, init_date, serial_no, init_date |
| idx_arpfixedratejour | serial_no, init_date, serial_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:23:55 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2026-03-04 16:23:55 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |

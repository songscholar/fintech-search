# setttouftjudifrozenjour - 清算司法冻结流水表

**表对象ID**: 3094
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 60 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | serial_no | 是 |  |  |
| 3 | curr_date | 是 |  |  |
| 4 | curr_time | 是 |  |  |
| 5 | operator_no | 是 |  |  |
| 6 | op_branch_no | 是 |  |  |
| 7 | op_entrust_way | 是 |  |  |
| 8 | op_station | 是 |  |  |
| 9 | branch_no | 是 |  |  |
| 10 | fund_account | 是 |  |  |
| 11 | client_id | 是 |  |  |
| 12 | stock_account | 是 |  |  |
| 13 | exchange_type | 是 |  |  |
| 14 | stock_code | 是 |  |  |
| 15 | seat_no | 是 |  |  |
| 16 | frozen_amount | 是 |  |  |
| 17 | stbcontain_flag | 是 |  |  |
| 18 | csdc_sellfro_flag | 是 |  |  |
| 19 | begin_date | 是 |  |  |
| 20 | end_date | 是 |  |  |
| 21 | juti_type | 是 |  |  |
| 22 | judiorgan_name | 是 |  |  |
| 23 | judiorgan_kind | 是 |  |  |
| 24 | judireport_id | 是 |  |  |
| 25 | judifrozen_id | 是 |  |  |
| 26 | judiwait_id | 是 |  |  |
| 27 | judi_status | 是 |  |  |
| 28 | sz_frozen_organname | 是 |  |  |
| 29 | remark | 是 |  |  |
| 30 | position_str | 是 |  |  |
| 31 | init_date | 是 |  |  |
| 32 | serial_no | 是 |  |  |
| 33 | curr_date | 是 |  |  |
| 34 | curr_time | 是 |  |  |
| 35 | operator_no | 是 |  |  |
| 36 | op_branch_no | 是 |  |  |
| 37 | op_entrust_way | 是 |  |  |
| 38 | op_station | 是 |  |  |
| 39 | branch_no | 是 |  |  |
| 40 | fund_account | 是 |  |  |
| 41 | client_id | 是 |  |  |
| 42 | stock_account | 是 |  |  |
| 43 | exchange_type | 是 |  |  |
| 44 | stock_code | 是 |  |  |
| 45 | seat_no | 是 |  |  |
| 46 | frozen_amount | 是 |  |  |
| 47 | stbcontain_flag | 是 |  |  |
| 48 | csdc_sellfro_flag | 是 |  |  |
| 49 | begin_date | 是 |  |  |
| 50 | end_date | 是 |  |  |
| 51 | juti_type | 是 |  |  |
| 52 | judiorgan_name | 是 |  |  |
| 53 | judiorgan_kind | 是 |  |  |
| 54 | judireport_id | 是 |  |  |
| 55 | judifrozen_id | 是 |  |  |
| 56 | judiwait_id | 是 |  |  |
| 57 | judi_status | 是 |  |  |
| 58 | sz_frozen_organname | 是 |  |  |
| 59 | remark | 是 |  |  |
| 60 | position_str | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_judifrozenj | 默认 | 否 | init_date, serial_no, branch_no, init_date, serial_no, branch_no |
| idx_settjudifrozenj | 默认 | 否 | init_date, serial_no, branch_no, init_date, serial_no, branch_no |
| idx_judifrozenj | 默认 | 否 | init_date, serial_no, branch_no, init_date, serial_no, branch_no |
| idx_settjudifrozenj | 默认 | 否 | init_date, serial_no, branch_no, init_date, serial_no, branch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_judifrozenj | init_date, serial_no, branch_no, init_date, serial_no, branch_no |
| idx_judifrozenj | init_date, serial_no, branch_no, init_date, serial_no, branch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-21 14:10:56 | 8.26.2.86 |  | 物理表setttouftjudifrozenjour，增加索引(idx_judifrozenj:[init_date,s... |
| 2025-04-21 14:10:56 | 8.26.2.86 |  | 物理表setttouftjudifrozenjour，增加索引(idx_judifrozenj:[init_date,s... |

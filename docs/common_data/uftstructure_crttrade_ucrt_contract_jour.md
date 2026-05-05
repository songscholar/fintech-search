# ucrt_contract_jour - 融资融券合同流水表

**表对象ID**: 7577
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 58 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | contract_id | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | crdtint_mode | 否 |  |  |
| 6 | crdt_fare_str | 否 |  |  |
| 7 | contract_rights | 否 |  |  |
| 8 | fin_max_quota | 否 |  |  |
| 9 | slo_max_quota | 否 |  |  |
| 10 | total_max_quota | 否 |  |  |
| 11 | papercont_id | 否 |  |  |
| 12 | compact_term | 否 |  |  |
| 13 | crdt_level | 否 |  |  |
| 14 | build_date | 否 |  |  |
| 15 | begin_date | 否 |  |  |
| 16 | end_date | 否 |  |  |
| 17 | fin_cashgroup_no | 否 |  |  |
| 18 | slo_cashgroup_no | 否 |  |  |
| 19 | contract_status | 否 |  |  |
| 20 | date_clear | 否 |  |  |
| 21 | personalization_mode | 否 |  |  |
| 22 | package_kind_str | 否 |  |  |
| 23 | package_begin_date | 否 |  |  |
| 24 | package_end_date | 否 |  |  |
| 25 | primerate_end_date | 否 |  |  |
| 26 | primerate_begin_date | 否 |  |  |
| 27 | remark | 否 |  |  |
| 28 | position_str | 否 |  |  |
| 29 | serial_no | 否 |  |  |
| 30 | init_date | 否 |  |  |
| 31 | contract_id | 否 |  |  |
| 32 | client_id | 否 |  |  |
| 33 | fund_account | 否 |  |  |
| 34 | crdtint_mode | 否 |  |  |
| 35 | crdt_fare_str | 否 |  |  |
| 36 | contract_rights | 否 |  |  |
| 37 | fin_max_quota | 否 |  |  |
| 38 | slo_max_quota | 否 |  |  |
| 39 | total_max_quota | 否 |  |  |
| 40 | papercont_id | 否 |  |  |
| 41 | compact_term | 否 |  |  |
| 42 | crdt_level | 否 |  |  |
| 43 | build_date | 否 |  |  |
| 44 | begin_date | 否 |  |  |
| 45 | end_date | 否 |  |  |
| 46 | fin_cashgroup_no | 否 |  |  |
| 47 | slo_cashgroup_no | 否 |  |  |
| 48 | contract_status | 否 |  |  |
| 49 | date_clear | 否 |  |  |
| 50 | personalization_mode | 否 |  |  |
| 51 | package_kind_str | 否 |  |  |
| 52 | package_begin_date | 否 |  |  |
| 53 | package_end_date | 否 |  |  |
| 54 | primerate_end_date | 否 |  |  |
| 55 | primerate_begin_date | 否 |  |  |
| 56 | remark | 否 |  |  |
| 57 | position_str | 否 |  |  |
| 58 | serial_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_contractjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_contractjour | ART | 是 | serial_no, init_date, serial_no, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_contractjour | serial_no, init_date, serial_no, init_date |
| idx_contractjour | serial_no, init_date, serial_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-16 16:20:39 | 3.0.2.2014 | huangzh | 新增合同流水表 |
| 2025-07-16 16:20:39 | 3.0.2.2014 | huangzh | 新增合同流水表 |

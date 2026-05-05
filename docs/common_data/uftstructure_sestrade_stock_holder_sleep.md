# stock_holder_sleep - 证券账户休眠表

**表对象ID**: 5564
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 56 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | internal_account | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | main_flag | 否 |  |  |
| 8 | asset_prop | 否 |  |  |
| 9 | ordinal | 否 |  |  |
| 10 | id_kind | 否 |  |  |
| 11 | id_no | 否 |  |  |
| 12 | holder_name | 否 |  |  |
| 13 | full_name | 否 |  |  |
| 14 | holder_kind | 否 |  |  |
| 15 | holder_level | 否 |  |  |
| 16 | report_level | 否 |  |  |
| 17 | holder_status | 否 |  |  |
| 18 | holder_rights | 否 |  |  |
| 19 | holder_restriction | 否 |  |  |
| 20 | regflag | 否 |  |  |
| 21 | seat_no | 否 |  |  |
| 22 | bondreg | 否 |  |  |
| 23 | open_date | 否 |  |  |
| 24 | acode_account | 否 |  |  |
| 25 | open_type | 否 |  |  |
| 26 | position_str | 否 |  |  |
| 27 | csdc_optacct_useage | 否 |  |  |
| 28 | en_ext_holder_rights | 否 |  |  |
| 29 | branch_no | 否 |  |  |
| 30 | stock_account | 否 |  |  |
| 31 | exchange_type | 否 |  |  |
| 32 | internal_account | 否 |  |  |
| 33 | fund_account | 否 |  |  |
| 34 | client_id | 否 |  |  |
| 35 | main_flag | 否 |  |  |
| 36 | asset_prop | 否 |  |  |
| 37 | ordinal | 否 |  |  |
| 38 | id_kind | 否 |  |  |
| 39 | id_no | 否 |  |  |
| 40 | holder_name | 否 |  |  |
| 41 | full_name | 否 |  |  |
| 42 | holder_kind | 否 |  |  |
| 43 | holder_level | 否 |  |  |
| 44 | report_level | 否 |  |  |
| 45 | holder_status | 否 |  |  |
| 46 | holder_rights | 否 |  |  |
| 47 | holder_restriction | 否 |  |  |
| 48 | regflag | 否 |  |  |
| 49 | seat_no | 否 |  |  |
| 50 | bondreg | 否 |  |  |
| 51 | open_date | 否 |  |  |
| 52 | acode_account | 否 |  |  |
| 53 | open_type | 否 |  |  |
| 54 | position_str | 否 |  |  |
| 55 | csdc_optacct_useage | 否 |  |  |
| 56 | en_ext_holder_rights | 否 |  |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stkholder_sleep | ART | 是 | position_str, position_str |
| idx_stkholder_sleep_stk | ART | 是 | stock_account, branch_no, exchange_type, stock_account, branch_no, exchange_type |
| idx_stkholder_sleep_id | ART | 是 | client_id, client_id |
| idx_stkholder_sleep_fa | ART | 是 | fund_account, fund_account |
| idx_stkholder_sleep_internal | ART | 是 | internal_account, internal_account |
| idx_stkholder_sleep | ART | 是 | position_str, position_str |
| idx_stkholder_sleep_stk | ART | 是 | stock_account, branch_no, exchange_type, stock_account, branch_no, exchange_type |
| idx_stkholder_sleep_id | ART | 是 | client_id, client_id |
| idx_stkholder_sleep_fa | ART | 是 | fund_account, fund_account |
| idx_stkholder_sleep_internal | ART | 是 | internal_account, internal_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stkholder_sleep | position_str, position_str |
| idx_stkholder_sleep | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:14:20 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-09 11:16:40 | 3.0.2.43 | 杨森峰 | 表属性调整为不回库 |
| 2024-07-23 14:50:22 | 3.0.2.30 | 杨涛 | 新增 |
| 2026-03-09 14:14:20 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-09 11:16:40 | 3.0.2.43 | 杨森峰 | 表属性调整为不回库 |
| 2024-07-23 14:50:22 | 3.0.2.30 | 杨涛 | 新增 |

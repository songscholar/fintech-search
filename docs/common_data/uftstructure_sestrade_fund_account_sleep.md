# fund_account_sleep - 资产账号休眠户表

**表对象ID**: 5563
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 60 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | fund_card | 否 |  |  |
| 5 | main_flag | 否 |  |  |
| 6 | risk_level | 否 |  |  |
| 7 | risk_enddate | 否 |  |  |
| 8 | inter_account | 否 |  |  |
| 9 | client_group | 否 |  |  |
| 10 | room_code | 否 |  |  |
| 11 | asset_prop | 否 |  |  |
| 12 | fare_kind_str | 否 |  |  |
| 13 | discount_model | 否 |  |  |
| 14 | en_entrust_way | 否 |  |  |
| 15 | client_rights | 否 |  |  |
| 16 | restriction | 否 |  |  |
| 17 | profit_flag | 否 |  |  |
| 18 | open_date | 否 |  |  |
| 19 | cancel_date | 否 |  |  |
| 20 | product_flag | 否 |  |  |
| 21 | fundacct_status | 否 |  |  |
| 22 | limit_flag | 否 |  |  |
| 23 | position_str | 否 |  |  |
| 24 | remark | 否 |  |  |
| 25 | en_ext_rights | 否 |  |  |
| 26 | open_type | 否 |  |  |
| 27 | finstat_settle_id | 否 |  |  |
| 28 | cost_center | 否 |  |  |
| 29 | fund_account_type | 否 |  |  |
| 30 | en_ext_restriction | 否 |  |  |
| 31 | branch_no | 否 |  |  |
| 32 | client_id | 否 |  |  |
| 33 | fund_account | 否 |  |  |
| 34 | fund_card | 否 |  |  |
| 35 | main_flag | 否 |  |  |
| 36 | risk_level | 否 |  |  |
| 37 | risk_enddate | 否 |  |  |
| 38 | inter_account | 否 |  |  |
| 39 | client_group | 否 |  |  |
| 40 | room_code | 否 |  |  |
| 41 | asset_prop | 否 |  |  |
| 42 | fare_kind_str | 否 |  |  |
| 43 | discount_model | 否 |  |  |
| 44 | en_entrust_way | 否 |  |  |
| 45 | client_rights | 否 |  |  |
| 46 | restriction | 否 |  |  |
| 47 | profit_flag | 否 |  |  |
| 48 | open_date | 否 |  |  |
| 49 | cancel_date | 否 |  |  |
| 50 | product_flag | 否 |  |  |
| 51 | fundacct_status | 否 |  |  |
| 52 | limit_flag | 否 |  |  |
| 53 | position_str | 否 |  |  |
| 54 | remark | 否 |  |  |
| 55 | en_ext_rights | 否 |  |  |
| 56 | open_type | 否 |  |  |
| 57 | finstat_settle_id | 否 |  |  |
| 58 | cost_center | 否 |  |  |
| 59 | fund_account_type | 否 |  |  |
| 60 | en_ext_restriction | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_fund_account_sleep | ART | 是 | fund_account, fund_account |
| idx_fund_account_sleep_client | ART | 是 | client_id, client_id |
| idx_fund_account_sleep_card | ART | 是 | fund_card, fund_card |
| idx_fundaccounts_pos | ART | 是 | position_str, position_str |
| idx_fund_account_sleep | ART | 是 | fund_account, fund_account |
| idx_fund_account_sleep_client | ART | 是 | client_id, client_id |
| idx_fund_account_sleep_card | ART | 是 | fund_card, fund_card |
| idx_fundaccounts_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_fund_account_sleep | fund_account, fund_account |
| idx_fund_account_sleep | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:11:59 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-09 11:15:59 | 3.0.2.43 | 杨森峰 | 表属性调整为不回库 |
| 2024-07-23 14:50:22 | 3.0.2.30 | 杨涛 | 对象号改为5563 |
| 2026-03-09 14:11:59 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-09 11:15:59 | 3.0.2.43 | 杨森峰 | 表属性调整为不回库 |
| 2024-07-23 14:50:22 | 3.0.2.30 | 杨涛 | 对象号改为5563 |

# uref_fund_account - 转融通资产账号表

**表对象ID**: 6036
**所属模块**: refacct
**数据空间**: HS_UFT_DATA

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | asset_prop | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | client_group | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | client_rights | 否 |  |  |
| 6 | discount_model | 否 |  |  |
| 7 | en_entrust_way | 否 |  |  |
| 8 | fare_kind_str | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | fundacct_status | 否 |  |  |
| 11 | main_flag | 否 |  |  |
| 12 | organ_flag | 否 |  |  |
| 13 | trade_password | 否 |  |  |
| 14 | profit_flag | 否 |  |  |
| 15 | restriction | 否 |  |  |
| 16 | room_code | 否 |  |  |
| 17 | fundacct_ctrlstr | 否 |  |  |
| 18 | partition_no | 否 |  |  |
| 19 | fund_password | 否 |  |  |
| 20 | query_password | 否 |  |  |
| 21 | asset_prop | 否 |  |  |
| 22 | branch_no | 否 |  |  |
| 23 | client_group | 否 |  |  |
| 24 | client_id | 否 |  |  |
| 25 | client_rights | 否 |  |  |
| 26 | discount_model | 否 |  |  |
| 27 | en_entrust_way | 否 |  |  |
| 28 | fare_kind_str | 否 |  |  |
| 29 | fund_account | 否 |  |  |
| 30 | fundacct_status | 否 |  |  |
| 31 | main_flag | 否 |  |  |
| 32 | organ_flag | 否 |  |  |
| 33 | trade_password | 否 |  |  |
| 34 | profit_flag | 否 |  |  |
| 35 | restriction | 否 |  |  |
| 36 | room_code | 否 |  |  |
| 37 | fundacct_ctrlstr | 否 |  |  |
| 38 | partition_no | 否 |  |  |
| 39 | fund_password | 否 |  |  |
| 40 | query_password | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uref_fund_account | ART | 是 | fund_account, fund_account |
| idx_uref_fund_account_id | ART | 是 | client_id, client_id |
| idx_uref_fund_account | ART | 是 | fund_account, fund_account |
| idx_uref_fund_account_id | ART | 是 | client_id, client_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uref_fund_account | fund_account, fund_account |
| idx_uref_fund_account | fund_account, fund_account |

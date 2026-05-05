# usms_fund_account - 资产账号表

**表对象ID**: 2801
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 62 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | asset_prop | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | client_group | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | discount_model | 否 |  |  |
| 6 | en_entrust_way | 否 |  |  |
| 7 | fare_kind_str | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | fundacct_status | 否 |  |  |
| 10 | main_flag | 否 |  |  |
| 11 | organ_flag | 否 |  |  |
| 12 | trade_password | 否 |  |  |
| 13 | profit_flag | 否 |  |  |
| 14 | room_code | 否 |  |  |
| 15 | partition_no | 否 |  |  |
| 16 | query_password | 否 |  |  |
| 17 | organ_prod_kind | 否 |  |  |
| 18 | product_flag | 否 |  |  |
| 19 | en_ext_rights | 否 |  |  |
| 20 | fund_account_type | 否 |  |  |
| 21 | en_ext_restriction | 否 |  |  |
| 22 | position_str | 否 |  |  |
| 23 | fund_password | 否 |  |  |
| 24 | fundacct_ctrlstr | 否 |  |  |
| 25 | open_date | 否 |  |  |
| 26 | fund_card | 否 |  |  |
| 27 | cancel_date | 否 |  |  |
| 28 | limit_flag | 否 |  |  |
| 29 | remark | 否 |  |  |
| 30 | client_rights | 否 |  |  |
| 31 | restriction | 否 |  |  |
| 32 | asset_prop | 否 |  |  |
| 33 | branch_no | 否 |  |  |
| 34 | client_group | 否 |  |  |
| 35 | client_id | 否 |  |  |
| 36 | discount_model | 否 |  |  |
| 37 | en_entrust_way | 否 |  |  |
| 38 | fare_kind_str | 否 |  |  |
| 39 | fund_account | 否 |  |  |
| 40 | fundacct_status | 否 |  |  |
| 41 | main_flag | 否 |  |  |
| 42 | organ_flag | 否 |  |  |
| 43 | trade_password | 否 |  |  |
| 44 | profit_flag | 否 |  |  |
| 45 | room_code | 否 |  |  |
| 46 | partition_no | 否 |  |  |
| 47 | query_password | 否 |  |  |
| 48 | organ_prod_kind | 否 |  |  |
| 49 | product_flag | 否 |  |  |
| 50 | en_ext_rights | 否 |  |  |
| 51 | fund_account_type | 否 |  |  |
| 52 | en_ext_restriction | 否 |  |  |
| 53 | position_str | 否 |  |  |
| 54 | fund_password | 否 |  |  |
| 55 | fundacct_ctrlstr | 否 |  |  |
| 56 | open_date | 否 |  |  |
| 57 | fund_card | 否 |  |  |
| 58 | cancel_date | 否 |  |  |
| 59 | limit_flag | 否 |  |  |
| 60 | remark | 否 |  |  |
| 61 | client_rights | 否 |  |  |
| 62 | restriction | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usms_fund_account | 默认 | 是 | fund_account, fund_account |
| idx_usms_fund_account_id | 默认 | 是 | client_id, client_id |
| idx_usms_fund_account | 默认 | 是 | fund_account, fund_account |
| idx_usms_fund_account_id | 默认 | 是 | client_id, client_id |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_usms_fund_account | fund_account, fund_account |
| idx_usms_fund_account_id | client_id, client_id |
| idx_usms_fund_account | fund_account, fund_account |
| idx_usms_fund_account_id | client_id, client_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-25 09:54:11 | 8.26.2.93 | 刘大为 | 所有表usms_fund_account，添加了表字段(fundacct_ctrlstr);
所有表usms_fund... |
| 2025-11-25 09:54:11 | 8.26.2.93 | 刘大为 | 所有表usms_fund_account，添加了表字段(fundacct_ctrlstr);
所有表usms_fund... |

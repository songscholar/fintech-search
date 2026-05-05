# usms_stock_holder - 证券账户表

**表对象ID**: 2802
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 50 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | acode_account | 是 |  |  |
| 2 | exchange_type | 是 |  |  |
| 3 | fund_account | 是 |  |  |
| 4 | holder_kind | 是 |  |  |
| 5 | holder_level | 是 |  |  |
| 6 | holder_status | 是 |  |  |
| 7 | main_flag | 是 |  |  |
| 8 | regflag | 是 |  |  |
| 9 | report_level | 是 |  |  |
| 10 | seat_no | 是 |  |  |
| 11 | stkholder_ctrlstr | 是 |  |  |
| 12 | stock_account | 是 |  |  |
| 13 | szdc_use_flag | 是 |  |  |
| 14 | partition_no | 是 |  |  |
| 15 | branch_no | 是 |  |  |
| 16 | transaction_no | 是 |  |  |
| 17 | internal_account | 是 |  |  |
| 18 | client_id | 是 |  |  |
| 19 | ordinal | 是 |  |  |
| 20 | bondreg | 是 |  |  |
| 21 | open_date | 是 |  |  |
| 22 | en_ext_holder_rights | 是 |  |  |
| 23 | asset_prop | 是 |  |  |
| 24 | holder_rights | 是 |  |  |
| 25 | holder_restriction | 是 |  |  |
| 26 | acode_account | 是 |  |  |
| 27 | exchange_type | 是 |  |  |
| 28 | fund_account | 是 |  |  |
| 29 | holder_kind | 是 |  |  |
| 30 | holder_level | 是 |  |  |
| 31 | holder_status | 是 |  |  |
| 32 | main_flag | 是 |  |  |
| 33 | regflag | 是 |  |  |
| 34 | report_level | 是 |  |  |
| 35 | seat_no | 是 |  |  |
| 36 | stkholder_ctrlstr | 是 |  |  |
| 37 | stock_account | 是 |  |  |
| 38 | szdc_use_flag | 是 |  |  |
| 39 | partition_no | 是 |  |  |
| 40 | branch_no | 是 |  |  |
| 41 | transaction_no | 是 |  |  |
| 42 | internal_account | 是 |  |  |
| 43 | client_id | 是 |  |  |
| 44 | ordinal | 是 |  |  |
| 45 | bondreg | 是 |  |  |
| 46 | open_date | 是 |  |  |
| 47 | en_ext_holder_rights | 是 |  |  |
| 48 | asset_prop | 是 |  |  |
| 49 | holder_rights | 是 |  |  |
| 50 | holder_restriction | 是 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usms_stock_holder_uk | 默认 | 是 | stock_account, exchange_type, fund_account, stock_account, exchange_type, fund_account |
| idx_usms_stock_holder_acode | 默认 | 是 | acode_account, acode_account |
| idx_usms_stock_holder_fund_acct | 默认 | 是 | fund_account, exchange_type, fund_account, exchange_type |
| idx_usms_stock_holder_uk | 默认 | 是 | stock_account, exchange_type, fund_account, stock_account, exchange_type, fund_account |
| idx_usms_stock_holder_acode | 默认 | 是 | acode_account, acode_account |
| idx_usms_stock_holder_fund_acct | 默认 | 是 | fund_account, exchange_type, fund_account, exchange_type |

## 数据库索引（共 6 个）

| 索引名 | 字段 |
|--------|------|
| idx_usms_stock_holder_uk | stock_account, exchange_type, fund_account, stock_account, exchange_type, fund_account |
| idx_usms_stock_holder_acode | acode_account, acode_account |
| idx_usms_stock_holder_fund_acct | fund_account, exchange_type, fund_account, exchange_type |
| idx_usms_stock_holder_uk | stock_account, exchange_type, fund_account, stock_account, exchange_type, fund_account |
| idx_usms_stock_holder_acode | acode_account, acode_account |
| idx_usms_stock_holder_fund_acct | fund_account, exchange_type, fund_account, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-03-14 09:41:59 | 3.0.6.81 |  | 物理表usms_stock_holder，添加了表字段(asset_prop);
 |
| 2025-03-14 09:41:59 | 3.0.6.81 |  | 物理表usms_stock_holder，添加了表字段(asset_prop);
 |

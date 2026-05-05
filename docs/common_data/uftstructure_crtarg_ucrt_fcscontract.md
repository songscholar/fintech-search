# ucrt_fcscontract - 融资融券计费签约账户信息表

**表对象ID**: 7055
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 56 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fcs_product_id | 否 |  |  |
| 4 | fare_mode | 否 |  |  |
| 5 | fare_kind | 否 |  |  |
| 6 | sign_date | 否 |  |  |
| 7 | sign_time | 否 |  |  |
| 8 | unsign_date | 否 |  |  |
| 9 | unsign_time | 否 |  |  |
| 10 | busiwhite_transin_date | 否 |  |  |
| 11 | busiwhite_transin_time | 否 |  |  |
| 12 | busiwhite_transout_date | 否 |  |  |
| 13 | busiwhite_transout_time | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | fund_account | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | fcs_product_id | 否 |  |  |
| 18 | fare_mode | 否 |  |  |
| 19 | fare_kind | 否 |  |  |
| 20 | sign_date | 否 |  |  |
| 21 | sign_time | 否 |  |  |
| 22 | unsign_date | 否 |  |  |
| 23 | unsign_time | 否 |  |  |
| 24 | busiwhite_transin_date | 否 |  |  |
| 25 | busiwhite_transin_time | 否 |  |  |
| 26 | busiwhite_transout_date | 否 |  |  |
| 27 | busiwhite_transout_time | 否 |  |  |
| 28 | transaction_no | 否 |  |  |
| 29 | fund_account | 否 |  |  |
| 30 | client_id | 否 |  |  |
| 31 | fcs_product_id | 否 |  |  |
| 32 | fare_mode | 否 |  |  |
| 33 | fare_kind | 否 |  |  |
| 34 | sign_date | 否 |  |  |
| 35 | sign_time | 否 |  |  |
| 36 | unsign_date | 否 |  |  |
| 37 | unsign_time | 否 |  |  |
| 38 | busiwhite_transin_date | 否 |  |  |
| 39 | busiwhite_transin_time | 否 |  |  |
| 40 | busiwhite_transout_date | 否 |  |  |
| 41 | busiwhite_transout_time | 否 |  |  |
| 42 | transaction_no | 否 |  |  |
| 43 | fund_account | 否 |  |  |
| 44 | client_id | 否 |  |  |
| 45 | fcs_product_id | 否 |  |  |
| 46 | fare_mode | 否 |  |  |
| 47 | fare_kind | 否 |  |  |
| 48 | sign_date | 否 |  |  |
| 49 | sign_time | 否 |  |  |
| 50 | unsign_date | 否 |  |  |
| 51 | unsign_time | 否 |  |  |
| 52 | busiwhite_transin_date | 否 |  |  |
| 53 | busiwhite_transin_time | 否 |  |  |
| 54 | busiwhite_transout_date | 否 |  |  |
| 55 | busiwhite_transout_time | 否 |  |  |
| 56 | transaction_no | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_fcscontract | ART | 是 | fund_account, client_id, fcs_product_id, fund_account, client_id, fcs_product_id |
| idx_fcscontract | ART | 是 | fund_account, client_id, fcs_product_id, fund_account, client_id, fcs_product_id |
| idx_fcscontract_mode | ART | 是 | fund_account, fare_mode, fund_account, fare_mode |
| idx_fcscontract | ART | 是 | fund_account, client_id, fcs_product_id, fund_account, client_id, fcs_product_id |
| idx_fcscontract | ART | 是 | fund_account, client_id, fcs_product_id, fund_account, client_id, fcs_product_id |
| idx_fcscontract_mode | ART | 是 | fund_account, fare_mode, fund_account, fare_mode |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_fcscontract | fund_account, client_id, fcs_product_id, fund_account, client_id, fcs_product_id |
| idx_fcscontract | fund_account, client_id, fcs_product_id, fund_account, client_id, fcs_product_id |
| idx_fcscontract | fund_account, client_id, fcs_product_id, fund_account, client_id, fcs_product_id |
| idx_fcscontract | fund_account, client_id, fcs_product_id, fund_account, client_id, fcs_product_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-10 15:04:31 | 3.0.6.1066 | 徐世晗 | 添加表 |
| 2025-09-10 15:04:31 | 3.0.6.1066 |  |  |
| 2025-09-10 15:04:31 | 3.0.6.1066 | 徐世晗 | 添加表 |
| 2025-09-10 15:04:31 | 3.0.6.1066 |  |  |

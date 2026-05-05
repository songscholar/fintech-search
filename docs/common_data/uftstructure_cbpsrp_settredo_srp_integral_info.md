# settredo_srp_integral_info - 清算重做股票质押结息日期信息表

**表对象ID**: 12609
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | branch_no | 否 |  |  |
| 5 | contract_id | 否 |  |  |
| 6 | funder_no | 否 |  |  |
| 7 | interest_date | 否 |  |  |
| 8 | agreed_interest | 否 |  |  |
| 9 | repaid_interest | 否 |  |  |
| 10 | auto_type | 否 |  |  |
| 11 | date_clear | 否 |  |  |
| 12 | position_str | 否 |  |  |
| 13 | payinterest_deal_flag | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | sett_dml_type | 否 |  |  |
| 17 | sett_batch_no | 否 |  |  |
| 18 | init_date | 否 |  |  |
| 19 | fund_account | 否 |  |  |
| 20 | client_id | 否 |  |  |
| 21 | branch_no | 否 |  |  |
| 22 | contract_id | 否 |  |  |
| 23 | funder_no | 否 |  |  |
| 24 | interest_date | 否 |  |  |
| 25 | agreed_interest | 否 |  |  |
| 26 | repaid_interest | 否 |  |  |
| 27 | auto_type | 否 |  |  |
| 28 | date_clear | 否 |  |  |
| 29 | position_str | 否 |  |  |
| 30 | payinterest_deal_flag | 否 |  |  |
| 31 | update_date | 否 |  |  |
| 32 | update_time | 否 |  |  |
| 33 | sett_dml_type | 否 |  |  |
| 34 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_srpintegralinfo | ART | 是 | sett_batch_no, contract_id, interest_date, sett_batch_no, contract_id, interest_date |
| idx_settredo_srpintegralinfo | ART | 是 | sett_batch_no, contract_id, interest_date, sett_batch_no, contract_id, interest_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_srpintegralinfo | sett_batch_no, contract_id, interest_date, sett_batch_no, contract_id, interest_date |
| idx_settredo_srpintegralinfo | sett_batch_no, contract_id, interest_date, sett_batch_no, contract_id, interest_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 17:04:03 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2026-03-06 17:04:03 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |

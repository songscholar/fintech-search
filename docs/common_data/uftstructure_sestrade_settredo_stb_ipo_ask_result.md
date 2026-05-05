# settredo_stb_ipo_ask_result - 清算重做证券股转IPO询价结果表

**表对象ID**: 5756
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | business_id | 否 |  |  |
| 2 | confirm_amount | 否 |  |  |
| 3 | business_amount2 | 否 |  |  |
| 4 | business_price | 否 |  |  |
| 5 | business_date | 否 |  |  |
| 6 | business_time | 否 |  |  |
| 7 | withdraw_cause | 否 |  |  |
| 8 | returnbusin_kind | 否 |  |  |
| 9 | date_clear | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | contract_id | 否 |  |  |
| 15 | init_date | 否 |  |  |
| 16 | sett_dml_type | 否 |  |  |
| 17 | sett_batch_no | 否 |  |  |
| 18 | business_id | 否 |  |  |
| 19 | confirm_amount | 否 |  |  |
| 20 | business_amount2 | 否 |  |  |
| 21 | business_price | 否 |  |  |
| 22 | business_date | 否 |  |  |
| 23 | business_time | 否 |  |  |
| 24 | withdraw_cause | 否 |  |  |
| 25 | returnbusin_kind | 否 |  |  |
| 26 | date_clear | 否 |  |  |
| 27 | exchange_type | 否 |  |  |
| 28 | fund_account | 否 |  |  |
| 29 | stock_code | 否 |  |  |
| 30 | stock_account | 否 |  |  |
| 31 | contract_id | 否 |  |  |
| 32 | init_date | 否 |  |  |
| 33 | sett_dml_type | 否 |  |  |
| 34 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stb_settredo_ipo_ask_result | ART | 是 | sett_batch_no, exchange_type, fund_account, stock_code, stock_account, contract_id, init_date, sett_batch_no, exchange_type, fund_account, stock_code, stock_account, contract_id, init_date |
| idx_stb_settredo_ipo_ask_result | ART | 是 | sett_batch_no, exchange_type, fund_account, stock_code, stock_account, contract_id, init_date, sett_batch_no, exchange_type, fund_account, stock_code, stock_account, contract_id, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stb_settredo_ipo_ask_result | sett_batch_no, exchange_type, fund_account, stock_code, stock_account, contract_id, init_date, sett_batch_no, exchange_type, fund_account, stock_code, stock_account, contract_id, init_date |
| idx_stb_settredo_ipo_ask_result | sett_batch_no, exchange_type, fund_account, stock_code, stock_account, contract_id, init_date, sett_batch_no, exchange_type, fund_account, stock_code, stock_account, contract_id, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:42:11 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2026-03-09 14:42:11 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |

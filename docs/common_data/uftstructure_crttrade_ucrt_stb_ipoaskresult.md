# ucrt_stb_ipoaskresult - 股转IPO询价结果表

**表对象ID**: 7524
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 60 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | business_id | 否 |  |  |
| 8 | contract_id | 否 |  |  |
| 9 | confirm_amount | 否 |  |  |
| 10 | business_price | 否 |  |  |
| 11 | business_date | 否 |  |  |
| 12 | business_time | 否 |  |  |
| 13 | withdraw_cause | 否 |  |  |
| 14 | date_clear | 否 |  |  |
| 15 | business_amount2 | 否 |  |  |
| 16 | returnbusin_kind | 否 |  |  |
| 17 | client_id | 否 | H |  |
| 18 | stock_name | 否 | H |  |
| 19 | sub_stock_type | 否 | H |  |
| 20 | stock_type | 否 | H |  |
| 21 | client_group | 否 | H |  |
| 22 | room_code | 否 | H |  |
| 23 | asset_prop | 否 | H |  |
| 24 | limit_flag | 否 | H |  |
| 25 | risk_level | 否 | H |  |
| 26 | corp_client_group | 否 | H |  |
| 27 | corp_risk_level | 否 | H |  |
| 28 | asset_level | 否 | H |  |
| 29 | client_name | 否 | H |  |
| 30 | client_prop | 否 | H |  |
| 31 | init_date | 否 |  |  |
| 32 | branch_no | 否 |  |  |
| 33 | fund_account | 否 |  |  |
| 34 | exchange_type | 否 |  |  |
| 35 | stock_account | 否 |  |  |
| 36 | stock_code | 否 |  |  |
| 37 | business_id | 否 |  |  |
| 38 | contract_id | 否 |  |  |
| 39 | confirm_amount | 否 |  |  |
| 40 | business_price | 否 |  |  |
| 41 | business_date | 否 |  |  |
| 42 | business_time | 否 |  |  |
| 43 | withdraw_cause | 否 |  |  |
| 44 | date_clear | 否 |  |  |
| 45 | business_amount2 | 否 |  |  |
| 46 | returnbusin_kind | 否 |  |  |
| 47 | client_id | 否 | H |  |
| 48 | stock_name | 否 | H |  |
| 49 | sub_stock_type | 否 | H |  |
| 50 | stock_type | 否 | H |  |
| 51 | client_group | 否 | H |  |
| 52 | room_code | 否 | H |  |
| 53 | asset_prop | 否 | H |  |
| 54 | limit_flag | 否 | H |  |
| 55 | risk_level | 否 | H |  |
| 56 | corp_client_group | 否 | H |  |
| 57 | corp_risk_level | 否 | H |  |
| 58 | asset_level | 否 | H |  |
| 59 | client_name | 否 | H |  |
| 60 | client_prop | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_stb_ipoaskresult | ART | 是 | fund_account, exchange_type, stock_account, stock_code, returnbusin_kind, fund_account, exchange_type, stock_account, stock_code, returnbusin_kind |
| idx_ucrt_stb_ipoaskresult_unique | ART | 是 | fund_account, exchange_type, stock_account, stock_code, init_date, contract_id, fund_account, exchange_type, stock_account, stock_code, init_date, contract_id |
| uk_rpt_ucrtstbipoaskresult | ART | 是 | init_date, client_id, fund_account, stock_account, stock_code, exchange_type, contract_id, init_date, client_id, fund_account, stock_account, stock_code, exchange_type, contract_id |
| idx_rpt_ucrtstbipoaskresult_tolast | ART | 是 | date_clear, date_clear |
| idx_ucrt_stb_ipoaskresult | ART | 是 | fund_account, exchange_type, stock_account, stock_code, returnbusin_kind, fund_account, exchange_type, stock_account, stock_code, returnbusin_kind |
| idx_ucrt_stb_ipoaskresult_unique | ART | 是 | fund_account, exchange_type, stock_account, stock_code, init_date, contract_id, fund_account, exchange_type, stock_account, stock_code, init_date, contract_id |
| uk_rpt_ucrtstbipoaskresult | ART | 是 | init_date, client_id, fund_account, stock_account, stock_code, exchange_type, contract_id, init_date, client_id, fund_account, stock_account, stock_code, exchange_type, contract_id |
| idx_rpt_ucrtstbipoaskresult_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_stb_ipoaskresult | fund_account, exchange_type, stock_account, stock_code, init_date, contract_id, fund_account, exchange_type, stock_account, stock_code, init_date, contract_id |
| idx_ucrt_stb_ipoaskresult | fund_account, exchange_type, stock_account, stock_code, init_date, contract_id, fund_account, exchange_type, stock_account, stock_code, init_date, contract_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-02 15:26:26 | 3.0.2.1 | 曾阳璞 | 内存表新增全局唯一索引idx_ucrt_stb_ipoaskresult_unique |
| 2024-07-22 13:24:12 | 3.0.3.4 | 袁文龙 | 修复关联字段和关联索引字段重复 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-08-02 15:26:26 | 3.0.2.1 | 曾阳璞 | 内存表新增全局唯一索引idx_ucrt_stb_ipoaskresult_unique |
| 2024-07-22 13:24:12 | 3.0.3.4 | 袁文龙 | 修复关联字段和关联索引字段重复 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

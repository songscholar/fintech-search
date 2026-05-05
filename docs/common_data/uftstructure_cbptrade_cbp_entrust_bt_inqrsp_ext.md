# cbp_entrust_bt_inqrsp_ext - 债券现券询价报价回复委托扩展表

**表对象ID**: 2545
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 76 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | order_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | quotereq_id | 否 |  |  |
| 8 | quoteresp_id | 否 |  |  |
| 9 | quote_id | 否 |  |  |
| 10 | entrust_prop | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | entrust_bs | 否 |  |  |
| 13 | entrust_amount | 否 |  |  |
| 14 | entrust_balance | 否 |  |  |
| 15 | entrust_price | 否 |  |  |
| 16 | cbp_business_id | 否 |  |  |
| 17 | business_price | 否 |  |  |
| 18 | business_amount | 否 |  |  |
| 19 | business_balance | 否 |  |  |
| 20 | oppo_agency | 否 |  |  |
| 21 | oppo_bond_investor_type | 否 |  |  |
| 22 | oppo_bond_investor_id | 否 |  |  |
| 23 | oppo_brp_investor_name | 否 |  |  |
| 24 | oppo_trader_id | 否 |  |  |
| 25 | client_id | 否 | H |  |
| 26 | client_name | 否 | H |  |
| 27 | corp_client_group | 否 | H |  |
| 28 | client_group | 否 | H |  |
| 29 | room_code | 否 | H |  |
| 30 | asset_prop | 否 | H |  |
| 31 | limit_flag | 否 | H |  |
| 32 | client_prop | 否 | H |  |
| 33 | asset_level | 否 | H |  |
| 34 | risk_level | 否 | H |  |
| 35 | corp_risk_level | 否 | H |  |
| 36 | stock_name | 否 | H |  |
| 37 | stock_type | 否 | H |  |
| 38 | sub_stock_type | 否 | H |  |
| 39 | init_date | 否 |  |  |
| 40 | order_id | 否 |  |  |
| 41 | branch_no | 否 |  |  |
| 42 | fund_account | 否 |  |  |
| 43 | stock_account | 否 |  |  |
| 44 | exchange_type | 否 |  |  |
| 45 | quotereq_id | 否 |  |  |
| 46 | quoteresp_id | 否 |  |  |
| 47 | quote_id | 否 |  |  |
| 48 | entrust_prop | 否 |  |  |
| 49 | stock_code | 否 |  |  |
| 50 | entrust_bs | 否 |  |  |
| 51 | entrust_amount | 否 |  |  |
| 52 | entrust_balance | 否 |  |  |
| 53 | entrust_price | 否 |  |  |
| 54 | cbp_business_id | 否 |  |  |
| 55 | business_price | 否 |  |  |
| 56 | business_amount | 否 |  |  |
| 57 | business_balance | 否 |  |  |
| 58 | oppo_agency | 否 |  |  |
| 59 | oppo_bond_investor_type | 否 |  |  |
| 60 | oppo_bond_investor_id | 否 |  |  |
| 61 | oppo_brp_investor_name | 否 |  |  |
| 62 | oppo_trader_id | 否 |  |  |
| 63 | client_id | 否 | H |  |
| 64 | client_name | 否 | H |  |
| 65 | corp_client_group | 否 | H |  |
| 66 | client_group | 否 | H |  |
| 67 | room_code | 否 | H |  |
| 68 | asset_prop | 否 | H |  |
| 69 | limit_flag | 否 | H |  |
| 70 | client_prop | 否 | H |  |
| 71 | asset_level | 否 | H |  |
| 72 | risk_level | 否 | H |  |
| 73 | corp_risk_level | 否 | H |  |
| 74 | stock_name | 否 | H |  |
| 75 | stock_type | 否 | H |  |
| 76 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_cbpbtinqrspext | ART | 是 | init_date, order_id, quote_id, init_date, order_id, quote_id |
| idx_cbpbtinqrspext_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_cbpentrustbtinqrspext | ART | 是 | init_date, order_id, quote_id, init_date, order_id, quote_id |
| idx_rpt_cbpentrustbtinqrspext_acct | ART | 是 | fund_account, fund_account |
| idx_cbpbtinqrspext | ART | 是 | init_date, order_id, quote_id, init_date, order_id, quote_id |
| idx_cbpbtinqrspext_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_cbpentrustbtinqrspext | ART | 是 | init_date, order_id, quote_id, init_date, order_id, quote_id |
| idx_rpt_cbpentrustbtinqrspext_acct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_cbpbtinqrspext | init_date, order_id, quote_id, init_date, order_id, quote_id |
| idx_cbpbtinqrspext | init_date, order_id, quote_id, init_date, order_id, quote_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:27:11 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-03-18 13:47:09 | V3.0.6.12 | 卢杰 | 新增 |
| 2025-02-19 16:12:49 | V3.0.2.1010 | 华曌 | ucbp_entrust_bt_inqrsp_ext调整表对象为2545，表名变更为cbp_entrust_bt_inq... |
| 2026-03-04 16:27:11 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-03-18 13:47:09 | V3.0.6.12 | 卢杰 | 新增 |
| 2025-02-19 16:12:49 | V3.0.2.1010 | 华曌 | ucbp_entrust_bt_inqrsp_ext调整表对象为2545，表名变更为cbp_entrust_bt_inq... |

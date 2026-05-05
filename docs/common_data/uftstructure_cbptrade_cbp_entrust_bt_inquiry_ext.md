# cbp_entrust_bt_inquiry_ext - 债券现券询价委托扩展表

**表对象ID**: 2544
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | order_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | entrust_prop | 否 |  |  |
| 8 | quotereq_id | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | entrust_amount | 否 |  |  |
| 11 | entrust_bs | 否 |  |  |
| 12 | oppo_agency | 否 |  |  |
| 13 | oppo_bond_investor_type | 否 |  |  |
| 14 | client_id | 否 | H |  |
| 15 | client_name | 否 | H |  |
| 16 | corp_client_group | 否 | H |  |
| 17 | client_group | 否 | H |  |
| 18 | room_code | 否 | H |  |
| 19 | asset_prop | 否 | H |  |
| 20 | limit_flag | 否 | H |  |
| 21 | client_prop | 否 | H |  |
| 22 | asset_level | 否 | H |  |
| 23 | risk_level | 否 | H |  |
| 24 | corp_risk_level | 否 | H |  |
| 25 | stock_name | 否 | H |  |
| 26 | stock_type | 否 | H |  |
| 27 | sub_stock_type | 否 | H |  |
| 28 | init_date | 否 |  |  |
| 29 | order_id | 否 |  |  |
| 30 | branch_no | 否 |  |  |
| 31 | fund_account | 否 |  |  |
| 32 | stock_account | 否 |  |  |
| 33 | exchange_type | 否 |  |  |
| 34 | entrust_prop | 否 |  |  |
| 35 | quotereq_id | 否 |  |  |
| 36 | stock_code | 否 |  |  |
| 37 | entrust_amount | 否 |  |  |
| 38 | entrust_bs | 否 |  |  |
| 39 | oppo_agency | 否 |  |  |
| 40 | oppo_bond_investor_type | 否 |  |  |
| 41 | client_id | 否 | H |  |
| 42 | client_name | 否 | H |  |
| 43 | corp_client_group | 否 | H |  |
| 44 | client_group | 否 | H |  |
| 45 | room_code | 否 | H |  |
| 46 | asset_prop | 否 | H |  |
| 47 | limit_flag | 否 | H |  |
| 48 | client_prop | 否 | H |  |
| 49 | asset_level | 否 | H |  |
| 50 | risk_level | 否 | H |  |
| 51 | corp_risk_level | 否 | H |  |
| 52 | stock_name | 否 | H |  |
| 53 | stock_type | 否 | H |  |
| 54 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_cbpbtinquiryext | ART | 是 | init_date, order_id, oppo_agency, oppo_bond_investor_type, init_date, order_id, oppo_agency, oppo_bond_investor_type |
| idx_cbpentrustbtext_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_cbpentrustbtinquiryext | ART | 是 | init_date, order_id, oppo_agency, oppo_bond_investor_type, init_date, order_id, oppo_agency, oppo_bond_investor_type |
| idx_rpt_cbpentrustbtinquiryext_acct | ART | 是 | fund_account, fund_account |
| idx_cbpbtinquiryext | ART | 是 | init_date, order_id, oppo_agency, oppo_bond_investor_type, init_date, order_id, oppo_agency, oppo_bond_investor_type |
| idx_cbpentrustbtext_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_cbpentrustbtinquiryext | ART | 是 | init_date, order_id, oppo_agency, oppo_bond_investor_type, init_date, order_id, oppo_agency, oppo_bond_investor_type |
| idx_rpt_cbpentrustbtinquiryext_acct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_cbpbtinquiryext | init_date, order_id, oppo_agency, oppo_bond_investor_type, init_date, order_id, oppo_agency, oppo_bond_investor_type |
| idx_cbpbtinquiryext | init_date, order_id, oppo_agency, oppo_bond_investor_type, init_date, order_id, oppo_agency, oppo_bond_investor_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:26:44 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-03-18 13:46:49 | V3.0.6.12 | 卢杰 | 新增 |
| 2025-02-19 16:09:37 | V3.0.2.1010 | 华曌 | ucbp_entrust_bt_inquiry_ext调整表对象为2544，表名变更为cbp_entrust_bt_in... |
| 2026-03-04 16:26:44 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-03-18 13:46:49 | V3.0.6.12 | 卢杰 | 新增 |
| 2025-02-19 16:09:37 | V3.0.2.1010 | 华曌 | ucbp_entrust_bt_inquiry_ext调整表对象为2544，表名变更为cbp_entrust_bt_in... |

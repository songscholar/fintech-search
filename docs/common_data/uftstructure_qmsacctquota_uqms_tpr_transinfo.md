# uqms_tpr_transinfo - 额度管理转发申报信息表

**表对象ID**: 1621
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 118 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | exec_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | prop_fund_acco | 否 |  |  |
| 8 | prop_stock_account | 否 |  |  |
| 9 | prop_seat_no | 否 |  |  |
| 10 | entrust_date | 否 |  |  |
| 11 | entrust_prop | 否 |  |  |
| 12 | entrust_balance | 否 |  |  |
| 13 | expire_year_rate | 否 |  |  |
| 14 | back_balance | 否 |  |  |
| 15 | date_back | 否 |  |  |
| 16 | report_id | 否 |  |  |
| 17 | tprtrans_status | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | position_str | 否 |  |  |
| 20 | order_id | 否 |  |  |
| 21 | orig_order_id | 否 |  |  |
| 22 | seat_no | 否 |  |  |
| 23 | en_basket_id | 否 |  |  |
| 24 | trade_id | 否 |  |  |
| 25 | agency_no | 否 |  |  |
| 26 | bond_investor_type | 否 |  |  |
| 27 | bond_investor_id | 否 |  |  |
| 28 | brp_investor_name | 否 |  |  |
| 29 | trader_id | 否 |  |  |
| 30 | oppo_agency | 否 |  |  |
| 31 | oppo_bond_investor_type | 否 |  |  |
| 32 | oppo_bond_investor_id | 否 |  |  |
| 33 | oppo_brp_investor_name | 否 |  |  |
| 34 | oppo_trader_id | 否 |  |  |
| 35 | trdsubtype | 否 |  |  |
| 36 | entrust_amount | 否 |  |  |
| 37 | stock_parvalue | 否 |  |  |
| 38 | compact_term | 否 |  |  |
| 39 | alloc_settl_curr_amt | 否 |  |  |
| 40 | settl_curr_amt | 否 |  |  |
| 41 | cbpconfer_id | 否 |  |  |
| 42 | stock_code | 否 |  |  |
| 43 | entrust_price | 否 |  |  |
| 44 | disposal_flag | 否 |  |  |
| 45 | grace_days | 否 |  |  |
| 46 | client_id | 否 | H |  |
| 47 | client_name | 否 | H |  |
| 48 | corp_client_group | 否 | H |  |
| 49 | client_group | 否 | H |  |
| 50 | room_code | 否 | H |  |
| 51 | asset_prop | 否 | H |  |
| 52 | limit_flag | 否 | H |  |
| 53 | client_prop | 否 | H |  |
| 54 | asset_level | 否 | H |  |
| 55 | risk_level | 否 | H |  |
| 56 | corp_risk_level | 否 | H |  |
| 57 | stock_type | 否 | H |  |
| 58 | stock_name | 否 | H |  |
| 59 | sub_stock_type | 否 | H |  |
| 60 | init_date | 否 |  |  |
| 61 | branch_no | 否 |  |  |
| 62 | exec_id | 否 |  |  |
| 63 | fund_account | 否 |  |  |
| 64 | stock_account | 否 |  |  |
| 65 | exchange_type | 否 |  |  |
| 66 | prop_fund_acco | 否 |  |  |
| 67 | prop_stock_account | 否 |  |  |
| 68 | prop_seat_no | 否 |  |  |
| 69 | entrust_date | 否 |  |  |
| 70 | entrust_prop | 否 |  |  |
| 71 | entrust_balance | 否 |  |  |
| 72 | expire_year_rate | 否 |  |  |
| 73 | back_balance | 否 |  |  |
| 74 | date_back | 否 |  |  |
| 75 | report_id | 否 |  |  |
| 76 | tprtrans_status | 否 |  |  |
| 77 | remark | 否 |  |  |
| 78 | position_str | 否 |  |  |
| 79 | order_id | 否 |  |  |
| 80 | orig_order_id | 否 |  |  |
| 81 | seat_no | 否 |  |  |
| 82 | en_basket_id | 否 |  |  |
| 83 | trade_id | 否 |  |  |
| 84 | agency_no | 否 |  |  |
| 85 | bond_investor_type | 否 |  |  |
| 86 | bond_investor_id | 否 |  |  |
| 87 | brp_investor_name | 否 |  |  |
| 88 | trader_id | 否 |  |  |
| 89 | oppo_agency | 否 |  |  |
| 90 | oppo_bond_investor_type | 否 |  |  |
| 91 | oppo_bond_investor_id | 否 |  |  |
| 92 | oppo_brp_investor_name | 否 |  |  |
| 93 | oppo_trader_id | 否 |  |  |
| 94 | trdsubtype | 否 |  |  |
| 95 | entrust_amount | 否 |  |  |
| 96 | stock_parvalue | 否 |  |  |
| 97 | compact_term | 否 |  |  |
| 98 | alloc_settl_curr_amt | 否 |  |  |
| 99 | settl_curr_amt | 否 |  |  |
| 100 | cbpconfer_id | 否 |  |  |
| 101 | stock_code | 否 |  |  |
| 102 | entrust_price | 否 |  |  |
| 103 | disposal_flag | 否 |  |  |
| 104 | grace_days | 否 |  |  |
| 105 | client_id | 否 | H |  |
| 106 | client_name | 否 | H |  |
| 107 | corp_client_group | 否 | H |  |
| 108 | client_group | 否 | H |  |
| 109 | room_code | 否 | H |  |
| 110 | asset_prop | 否 | H |  |
| 111 | limit_flag | 否 | H |  |
| 112 | client_prop | 否 | H |  |
| 113 | asset_level | 否 | H |  |
| 114 | risk_level | 否 | H |  |
| 115 | corp_risk_level | 否 | H |  |
| 116 | stock_type | 否 | H |  |
| 117 | stock_name | 否 | H |  |
| 118 | sub_stock_type | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uqms_tprtransinfo_id | ART | 是 | init_date, exec_id, init_date, exec_id |
| idx_uqms_tprtransinfo_acct | ART | 是 | fund_account, fund_account |
| idx_uqms_tprtransinfo_pos | ART | 是 | position_str, position_str |
| uk_rpt_uqmstprtransinfo | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_uqmstprtransinfo_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_uqms_tprtransinfo_id | ART | 是 | init_date, exec_id, init_date, exec_id |
| idx_uqms_tprtransinfo_acct | ART | 是 | fund_account, fund_account |
| idx_uqms_tprtransinfo_pos | ART | 是 | position_str, position_str |
| uk_rpt_uqmstprtransinfo | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_uqmstprtransinfo_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_tprtransinfo_id | init_date, exec_id, init_date, exec_id |
| idx_uqms_tprtransinfo_id | init_date, exec_id, init_date, exec_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:47:34 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-05-06 16:54:14 | 3.0.2.13 | 周富安 | 新增 |
| 2026-03-05 16:47:34 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-05-06 16:54:14 | 3.0.2.13 | 周富安 | 新增 |

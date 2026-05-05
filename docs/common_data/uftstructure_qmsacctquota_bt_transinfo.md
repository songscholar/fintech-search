# bt_transinfo - 额度管理债券现券转发申报信息表

**表对象ID**: 1618
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 104 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exec_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | entrust_prop | 否 |  |  |
| 7 | entrust_amount | 否 |  |  |
| 8 | entrust_price | 否 |  |  |
| 9 | entrust_balance | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | entrust_bs | 否 |  |  |
| 12 | bondtrade_trans_status | 否 |  |  |
| 13 | remark | 否 |  |  |
| 14 | order_id | 否 |  |  |
| 15 | orig_order_id | 否 |  |  |
| 16 | trade_id | 否 |  |  |
| 17 | agency_no | 否 |  |  |
| 18 | bond_investor_type | 否 |  |  |
| 19 | bond_investor_id | 否 |  |  |
| 20 | brp_investor_name | 否 |  |  |
| 21 | trader_id | 否 |  |  |
| 22 | oppo_agency | 否 |  |  |
| 23 | oppo_bond_investor_type | 否 |  |  |
| 24 | oppo_bond_investor_id | 否 |  |  |
| 25 | oppo_brp_investor_name | 否 |  |  |
| 26 | oppo_trader_id | 否 |  |  |
| 27 | cbpconfer_id | 否 |  |  |
| 28 | settle_type | 否 |  |  |
| 29 | settle_period | 否 |  |  |
| 30 | entrust_crdt_flag | 否 |  |  |
| 31 | invalid_time | 否 |  |  |
| 32 | quote_id | 否 |  |  |
| 33 | trade_handling_instr | 否 |  |  |
| 34 | orig_business_date | 否 |  |  |
| 35 | business_id | 否 |  |  |
| 36 | quotereq_id | 否 |  |  |
| 37 | branch_no | 否 |  |  |
| 38 | position_str | 否 |  | init_date(8)+exec_id(32) |
| 39 | client_id | 否 | H |  |
| 40 | stock_name | 否 | H |  |
| 41 | sub_stock_type | 否 | H |  |
| 42 | stock_type | 否 | H |  |
| 43 | client_group | 否 | H |  |
| 44 | room_code | 否 | H |  |
| 45 | asset_prop | 否 | H |  |
| 46 | limit_flag | 否 | H |  |
| 47 | risk_level | 否 | H |  |
| 48 | corp_client_group | 否 | H |  |
| 49 | corp_risk_level | 否 | H |  |
| 50 | asset_level | 否 | H |  |
| 51 | client_name | 否 | H |  |
| 52 | client_prop | 否 | H |  |
| 53 | init_date | 否 |  |  |
| 54 | exec_id | 否 |  |  |
| 55 | fund_account | 否 |  |  |
| 56 | stock_account | 否 |  |  |
| 57 | exchange_type | 否 |  |  |
| 58 | entrust_prop | 否 |  |  |
| 59 | entrust_amount | 否 |  |  |
| 60 | entrust_price | 否 |  |  |
| 61 | entrust_balance | 否 |  |  |
| 62 | stock_code | 否 |  |  |
| 63 | entrust_bs | 否 |  |  |
| 64 | bondtrade_trans_status | 否 |  |  |
| 65 | remark | 否 |  |  |
| 66 | order_id | 否 |  |  |
| 67 | orig_order_id | 否 |  |  |
| 68 | trade_id | 否 |  |  |
| 69 | agency_no | 否 |  |  |
| 70 | bond_investor_type | 否 |  |  |
| 71 | bond_investor_id | 否 |  |  |
| 72 | brp_investor_name | 否 |  |  |
| 73 | trader_id | 否 |  |  |
| 74 | oppo_agency | 否 |  |  |
| 75 | oppo_bond_investor_type | 否 |  |  |
| 76 | oppo_bond_investor_id | 否 |  |  |
| 77 | oppo_brp_investor_name | 否 |  |  |
| 78 | oppo_trader_id | 否 |  |  |
| 79 | cbpconfer_id | 否 |  |  |
| 80 | settle_type | 否 |  |  |
| 81 | settle_period | 否 |  |  |
| 82 | entrust_crdt_flag | 否 |  |  |
| 83 | invalid_time | 否 |  |  |
| 84 | quote_id | 否 |  |  |
| 85 | trade_handling_instr | 否 |  |  |
| 86 | orig_business_date | 否 |  |  |
| 87 | business_id | 否 |  |  |
| 88 | quotereq_id | 否 |  |  |
| 89 | branch_no | 否 |  |  |
| 90 | position_str | 否 |  | init_date(8)+exec_id(32) |
| 91 | client_id | 否 | H |  |
| 92 | stock_name | 否 | H |  |
| 93 | sub_stock_type | 否 | H |  |
| 94 | stock_type | 否 | H |  |
| 95 | client_group | 否 | H |  |
| 96 | room_code | 否 | H |  |
| 97 | asset_prop | 否 | H |  |
| 98 | limit_flag | 否 | H |  |
| 99 | risk_level | 否 | H |  |
| 100 | corp_client_group | 否 | H |  |
| 101 | corp_risk_level | 否 | H |  |
| 102 | asset_level | 否 | H |  |
| 103 | client_name | 否 | H |  |
| 104 | client_prop | 否 | H |  |

## 索引（共 16 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_bt_transinfo | ART | 是 | init_date, exec_id, init_date, exec_id |
| idx_bt_transinfo_quote | ART | 是 | quote_id, quote_id |
| idx_bt_transinfo_order | ART | 是 | order_id, order_id |
| idx_bt_transinfo_quotereq | ART | 是 | quotereq_id, quotereq_id |
| idx_bt_transinfo_origorderid | ART | 是 | orig_order_id, orig_order_id |
| idx_bt_transinfo_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_bttransinfo | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_bttransinfo_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_bt_transinfo | ART | 是 | init_date, exec_id, init_date, exec_id |
| idx_bt_transinfo_quote | ART | 是 | quote_id, quote_id |
| idx_bt_transinfo_order | ART | 是 | order_id, order_id |
| idx_bt_transinfo_quotereq | ART | 是 | quotereq_id, quotereq_id |
| idx_bt_transinfo_origorderid | ART | 是 | orig_order_id, orig_order_id |
| idx_bt_transinfo_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_bttransinfo | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_bttransinfo_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_bt_transinfo | init_date, exec_id, init_date, exec_id |
| idx_bt_transinfo | init_date, exec_id, init_date, exec_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:46:12 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-11-21 19:56:55 | V3.0.6.14 | 周兆军 | 维护历史表 |
| 2025-03-18 13:40:28 | 3.0.6.11 | 卢杰 | 新增 |
| 2025-02-25 09:36:57 | 3.0.2.10 | 马天宇 | 修改索引名称，新增branch_no、position_str字段 |
| 2025-02-18 14:45:32 | 3.0.2.9 | 於达 | 新增 |
| 2026-03-05 16:46:12 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-11-21 19:56:55 | V3.0.6.14 | 周兆军 | 维护历史表 |
| 2025-03-18 13:40:28 | 3.0.6.11 | 卢杰 | 新增 |
| 2025-02-25 09:36:57 | 3.0.2.10 | 马天宇 | 修改索引名称，新增branch_no、position_str字段 |
| 2025-02-18 14:45:32 | 3.0.2.9 | 於达 | 新增 |

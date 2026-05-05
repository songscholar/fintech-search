# trpt_transinfo - 成交申报转发信息表

**表对象ID**: 1619
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 86 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exch_order_id | 否 |  |  |
| 2 | entrust_prop | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | entrust_bs | 否 |  |  |
| 5 | init_date | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | order_id | 否 |  |  |
| 8 | entrust_price | 否 |  |  |
| 9 | settle_type | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | entrust_amount | 否 |  |  |
| 12 | entrust_balance | 否 |  |  |
| 13 | full_deal_flag | 否 |  |  |
| 14 | quotereq_id | 否 |  |  |
| 15 | orig_order_id | 否 |  |  |
| 16 | exec_id | 否 |  |  |
| 17 | ext_order_id | 否 |  |  |
| 18 | trader_id_src | 否 |  |  |
| 19 | seat_no_src | 否 |  |  |
| 20 | branch_no_src | 否 |  |  |
| 21 | stock_account_src | 否 |  |  |
| 22 | brp_investor_name | 否 |  |  |
| 23 | trader_id_dest | 否 |  |  |
| 24 | cbpconfer_id | 否 |  |  |
| 25 | trade_report_trans_status | 否 |  |  |
| 26 | remark | 否 |  |  |
| 27 | agency_no_dest | 否 |  |  |
| 28 | position_str | 否 |  | init_date(8)+entrust_prop(3)+exch_order_id(18)+entrust_bs(1) |
| 29 | client_id | 否 | H |  |
| 30 | client_name | 否 | H |  |
| 31 | branch_no | 否 | H |  |
| 32 | corp_client_group | 否 | H |  |
| 33 | client_group | 否 | H |  |
| 34 | room_code | 否 | H |  |
| 35 | asset_prop | 否 | H |  |
| 36 | limit_flag | 否 | H |  |
| 37 | client_prop | 否 | H |  |
| 38 | asset_level | 否 | H |  |
| 39 | risk_level | 否 | H |  |
| 40 | corp_risk_level | 否 | H |  |
| 41 | stock_name | 否 | H |  |
| 42 | stock_type | 否 | H |  |
| 43 | sub_stock_type | 否 | H |  |
| 44 | exch_order_id | 否 |  |  |
| 45 | entrust_prop | 否 |  |  |
| 46 | exchange_type | 否 |  |  |
| 47 | entrust_bs | 否 |  |  |
| 48 | init_date | 否 |  |  |
| 49 | fund_account | 否 |  |  |
| 50 | order_id | 否 |  |  |
| 51 | entrust_price | 否 |  |  |
| 52 | settle_type | 否 |  |  |
| 53 | stock_code | 否 |  |  |
| 54 | entrust_amount | 否 |  |  |
| 55 | entrust_balance | 否 |  |  |
| 56 | full_deal_flag | 否 |  |  |
| 57 | quotereq_id | 否 |  |  |
| 58 | orig_order_id | 否 |  |  |
| 59 | exec_id | 否 |  |  |
| 60 | ext_order_id | 否 |  |  |
| 61 | trader_id_src | 否 |  |  |
| 62 | seat_no_src | 否 |  |  |
| 63 | branch_no_src | 否 |  |  |
| 64 | stock_account_src | 否 |  |  |
| 65 | brp_investor_name | 否 |  |  |
| 66 | trader_id_dest | 否 |  |  |
| 67 | cbpconfer_id | 否 |  |  |
| 68 | trade_report_trans_status | 否 |  |  |
| 69 | remark | 否 |  |  |
| 70 | agency_no_dest | 否 |  |  |
| 71 | position_str | 否 |  | init_date(8)+entrust_prop(3)+exch_order_id(18)+entrust_bs(1) |
| 72 | client_id | 否 | H |  |
| 73 | client_name | 否 | H |  |
| 74 | branch_no | 否 | H |  |
| 75 | corp_client_group | 否 | H |  |
| 76 | client_group | 否 | H |  |
| 77 | room_code | 否 | H |  |
| 78 | asset_prop | 否 | H |  |
| 79 | limit_flag | 否 | H |  |
| 80 | client_prop | 否 | H |  |
| 81 | asset_level | 否 | H |  |
| 82 | risk_level | 否 | H |  |
| 83 | corp_risk_level | 否 | H |  |
| 84 | stock_name | 否 | H |  |
| 85 | stock_type | 否 | H |  |
| 86 | sub_stock_type | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_trpttransinfo | ART | 是 | position_str, position_str |
| idx_trpttransinfo_id | ART | 是 | exch_order_id, entrust_prop, exch_order_id, entrust_prop |
| idx_trpttransinfo_trader | ART | 是 | trader_id_dest, entrust_prop, trader_id_dest, entrust_prop |
| uk_rpt_trpttransinfo | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_trpttransinfo_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_trpttransinfo | ART | 是 | position_str, position_str |
| idx_trpttransinfo_id | ART | 是 | exch_order_id, entrust_prop, exch_order_id, entrust_prop |
| idx_trpttransinfo_trader | ART | 是 | trader_id_dest, entrust_prop, trader_id_dest, entrust_prop |
| uk_rpt_trpttransinfo | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_trpttransinfo_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_trpttransinfo | position_str, position_str |
| idx_trpttransinfo | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:46:38 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-03-19 11:25:49 | 3.0.6.12 | 卢杰 | 新增 |
| 2025-02-19 00:14:59 | 3.0.2.9 | 乐闽庭 | 新增trpt_transinfo表 |
| 2026-03-05 16:46:38 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-03-19 11:25:49 | 3.0.6.12 | 卢杰 | 新增 |
| 2025-02-19 00:14:59 | 3.0.2.9 | 乐闽庭 | 新增trpt_transinfo表 |

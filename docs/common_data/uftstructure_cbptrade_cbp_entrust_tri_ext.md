# cbp_entrust_tri_ext - 三方回购委托扩展表

**表对象ID**: 2489
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 56 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | cbpcontract_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | business_id | 否 |  |  |
| 8 | basket_id | 否 |  |  |
| 9 | basket_name | 否 |  |  |
| 10 | discount_rate | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | impawn_amount | 否 |  |  |
| 13 | impawn_bs | 否 |  |  |
| 14 | order_id | 否 |  |  |
| 15 | client_id | 否 | H |  |
| 16 | client_name | 否 | H |  |
| 17 | corp_client_group | 否 | H |  |
| 18 | client_group | 否 | H |  |
| 19 | room_code | 否 | H |  |
| 20 | asset_prop | 否 | H |  |
| 21 | limit_flag | 否 | H |  |
| 22 | client_prop | 否 | H |  |
| 23 | asset_level | 否 | H |  |
| 24 | risk_level | 否 | H |  |
| 25 | corp_risk_level | 否 | H |  |
| 26 | stock_name | 否 | H |  |
| 27 | stock_type | 否 | H |  |
| 28 | sub_stock_type | 否 | H |  |
| 29 | init_date | 否 |  |  |
| 30 | cbpcontract_id | 否 |  |  |
| 31 | branch_no | 否 |  |  |
| 32 | fund_account | 否 |  |  |
| 33 | stock_account | 否 |  |  |
| 34 | exchange_type | 否 |  |  |
| 35 | business_id | 否 |  |  |
| 36 | basket_id | 否 |  |  |
| 37 | basket_name | 否 |  |  |
| 38 | discount_rate | 否 |  |  |
| 39 | stock_code | 否 |  |  |
| 40 | impawn_amount | 否 |  |  |
| 41 | impawn_bs | 否 |  |  |
| 42 | order_id | 否 |  |  |
| 43 | client_id | 否 | H |  |
| 44 | client_name | 否 | H |  |
| 45 | corp_client_group | 否 | H |  |
| 46 | client_group | 否 | H |  |
| 47 | room_code | 否 | H |  |
| 48 | asset_prop | 否 | H |  |
| 49 | limit_flag | 否 | H |  |
| 50 | client_prop | 否 | H |  |
| 51 | asset_level | 否 | H |  |
| 52 | risk_level | 否 | H |  |
| 53 | corp_risk_level | 否 | H |  |
| 54 | stock_name | 否 | H |  |
| 55 | stock_type | 否 | H |  |
| 56 | sub_stock_type | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_cbpentrusttriext_code | 默认 | 否 |  |
| idx_cbpentrusttriext_code | ART | 是 | order_id, init_date, impawn_bs, exchange_type, stock_code, order_id, init_date, impawn_bs, exchange_type, stock_code |
| uk_rpt_cbpentrusttriext | ART | 是 | init_date, order_id, impawn_bs, exchange_type, stock_code, init_date, order_id, impawn_bs, exchange_type, stock_code |
| idx_cbpentrusttriext_code | 默认 | 否 |  |
| idx_cbpentrusttriext_code | ART | 是 | order_id, init_date, impawn_bs, exchange_type, stock_code, order_id, init_date, impawn_bs, exchange_type, stock_code |
| uk_rpt_cbpentrusttriext | ART | 是 | init_date, order_id, impawn_bs, exchange_type, stock_code, init_date, order_id, impawn_bs, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_cbpentrusttriext_code | order_id, init_date, impawn_bs, exchange_type, stock_code, order_id, init_date, impawn_bs, exchange_type, stock_code |
| idx_cbpentrusttriext_code | order_id, init_date, impawn_bs, exchange_type, stock_code, order_id, init_date, impawn_bs, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:48:31 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-12-01 13:46:49 | 3.0.2.75 | taocong45644 | 当前表cbp_entrust_tri_ext，修改了索引idx_cbpentrusttriext_code,索引字段修改... |
| 2026-03-04 15:48:31 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-12-01 13:46:49 | 3.0.2.75 | taocong45644 | 当前表cbp_entrust_tri_ext，修改了索引idx_cbpentrusttriext_code,索引字段修改... |

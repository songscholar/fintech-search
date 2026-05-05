# ucrt_asset_bd_stock - 波段宝投顾产品持仓表

**表对象ID**: 7053
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 104 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | adviser_id | 否 |  |  |
| 3 | bdproduct_id | 否 |  |  |
| 4 | adviser_flag | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | branch_no | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | stock_account | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | money_type | 否 |  |  |
| 11 | business_amount | 否 |  |  |
| 12 | business_price | 否 |  |  |
| 13 | date_clear | 否 |  |  |
| 14 | position_str | 否 |  | init_date + adviser_id + adviser_flag + serial_no + join_ini |
| 15 | join_entrust_no | 否 |  |  |
| 16 | join_serial_no | 否 |  |  |
| 17 | store_unit | 否 |  |  |
| 18 | modify_date | 否 |  |  |
| 19 | entrust_bs | 否 |  |  |
| 20 | serial_no | 否 |  |  |
| 21 | join_init_date | 否 |  |  |
| 22 | file_type | 否 |  |  |
| 23 | file_kind | 否 |  |  |
| 24 | set_seat_no | 否 |  |  |
| 25 | original_fare0 | 否 |  |  |
| 26 | fare0 | 否 |  |  |
| 27 | fare1 | 否 |  |  |
| 28 | fare2 | 否 |  |  |
| 29 | fare3 | 否 |  |  |
| 30 | farex | 否 |  |  |
| 31 | entrust_curr_date | 否 |  |  |
| 32 | entrust_curr_time | 否 |  |  |
| 33 | business_time | 否 |  |  |
| 34 | actually_rate | 否 |  |  |
| 35 | adviser_fare | 否 |  |  |
| 36 | adviser_fare_actually | 否 |  |  |
| 37 | remark | 否 |  |  |
| 38 | business_type | 否 |  |  |
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
| 54 | adviser_id | 否 |  |  |
| 55 | bdproduct_id | 否 |  |  |
| 56 | adviser_flag | 否 |  |  |
| 57 | exchange_type | 否 |  |  |
| 58 | branch_no | 否 |  |  |
| 59 | fund_account | 否 |  |  |
| 60 | stock_account | 否 |  |  |
| 61 | stock_code | 否 |  |  |
| 62 | money_type | 否 |  |  |
| 63 | business_amount | 否 |  |  |
| 64 | business_price | 否 |  |  |
| 65 | date_clear | 否 |  |  |
| 66 | position_str | 否 |  | init_date + adviser_id + adviser_flag + serial_no + join_ini |
| 67 | join_entrust_no | 否 |  |  |
| 68 | join_serial_no | 否 |  |  |
| 69 | store_unit | 否 |  |  |
| 70 | modify_date | 否 |  |  |
| 71 | entrust_bs | 否 |  |  |
| 72 | serial_no | 否 |  |  |
| 73 | join_init_date | 否 |  |  |
| 74 | file_type | 否 |  |  |
| 75 | file_kind | 否 |  |  |
| 76 | set_seat_no | 否 |  |  |
| 77 | original_fare0 | 否 |  |  |
| 78 | fare0 | 否 |  |  |
| 79 | fare1 | 否 |  |  |
| 80 | fare2 | 否 |  |  |
| 81 | fare3 | 否 |  |  |
| 82 | farex | 否 |  |  |
| 83 | entrust_curr_date | 否 |  |  |
| 84 | entrust_curr_time | 否 |  |  |
| 85 | business_time | 否 |  |  |
| 86 | actually_rate | 否 |  |  |
| 87 | adviser_fare | 否 |  |  |
| 88 | adviser_fare_actually | 否 |  |  |
| 89 | remark | 否 |  |  |
| 90 | business_type | 否 |  |  |
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

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_bd_stock | ART | 是 | exchange_type, position_str, exchange_type, position_str |
| idx_ucrt_bd_stock_acct | ART | 是 | fund_account, exchange_type, stock_code, stock_account, fund_account, exchange_type, stock_code, stock_account |
| idx_ucrt_bd_stock | ART | 是 | exchange_type, position_str, exchange_type, position_str |
| uk_rpt_ucrtassetbdstock | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtassetbdstock_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_ucrtassetbdstock_tolast | ART | 是 | date_clear, date_clear |
| idx_ucrt_bd_stock | ART | 是 | exchange_type, position_str, exchange_type, position_str |
| idx_ucrt_bd_stock_acct | ART | 是 | fund_account, exchange_type, stock_code, stock_account, fund_account, exchange_type, stock_code, stock_account |
| idx_ucrt_bd_stock | ART | 是 | exchange_type, position_str, exchange_type, position_str |
| uk_rpt_ucrtassetbdstock | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtassetbdstock_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_ucrtassetbdstock_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_bd_stock | exchange_type, position_str, exchange_type, position_str |
| idx_ucrt_bd_stock | exchange_type, position_str, exchange_type, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-15 15:15:10 | V3.0.6.1072 | 袁文龙 | 物理表ucrt_asset_bd_stock，增加索引（ idx_ucrt_bd_stock:[exchange_typ... |
| 2025-04-24 15:14:12 | 3.0.6.54 | 袁文龙 | 对象号7051修改为7053 |
| 2025-01-01 09:29:16 | 3.0.6.24 | 牟家乐 | 新增表结构 |
| 2026-01-15 15:15:10 | V3.0.6.1072 | 袁文龙 | 物理表ucrt_asset_bd_stock，增加索引（ idx_ucrt_bd_stock:[exchange_typ... |
| 2025-04-24 15:14:12 | 3.0.6.54 | 袁文龙 | 对象号7051修改为7053 |
| 2025-01-01 09:29:16 | 3.0.6.24 | 牟家乐 | 新增表结构 |

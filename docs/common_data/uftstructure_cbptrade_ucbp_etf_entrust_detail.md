# ucbp_etf_entrust_detail - 综合ETF申赎委托明细表

**表对象ID**: 2317
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 62 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | entrust_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_account | 否 |  |  |
| 7 | report_account | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | component_code | 否 |  |  |
| 10 | money_type | 否 |  |  |
| 11 | occur_amount | 否 |  |  |
| 12 | occur_balance | 否 |  |  |
| 13 | date_clear | 否 |  |  |
| 14 | prev_status | 否 |  |  |
| 15 | deal_status | 否 |  |  |
| 16 | cancel_serial_no | 否 |  |  |
| 17 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+entrust_no(10)+com |
| 18 | branch_no | 否 |  |  |
| 19 | client_name | 否 | H |  |
| 20 | corp_client_group | 否 | H |  |
| 21 | client_group | 否 | H |  |
| 22 | room_code | 否 | H |  |
| 23 | asset_prop | 否 | H |  |
| 24 | limit_flag | 否 | H |  |
| 25 | client_prop | 否 | H |  |
| 26 | asset_level | 否 | H |  |
| 27 | risk_level | 否 | H |  |
| 28 | corp_risk_level | 否 | H |  |
| 29 | stock_name | 否 | H |  |
| 30 | stock_type | 否 | H |  |
| 31 | sub_stock_type | 否 | H |  |
| 32 | init_date | 否 |  |  |
| 33 | entrust_no | 否 |  |  |
| 34 | fund_account | 否 |  |  |
| 35 | client_id | 否 |  |  |
| 36 | exchange_type | 否 |  |  |
| 37 | stock_account | 否 |  |  |
| 38 | report_account | 否 |  |  |
| 39 | stock_code | 否 |  |  |
| 40 | component_code | 否 |  |  |
| 41 | money_type | 否 |  |  |
| 42 | occur_amount | 否 |  |  |
| 43 | occur_balance | 否 |  |  |
| 44 | date_clear | 否 |  |  |
| 45 | prev_status | 否 |  |  |
| 46 | deal_status | 否 |  |  |
| 47 | cancel_serial_no | 否 |  |  |
| 48 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+entrust_no(10)+com |
| 49 | branch_no | 否 |  |  |
| 50 | client_name | 否 | H |  |
| 51 | corp_client_group | 否 | H |  |
| 52 | client_group | 否 | H |  |
| 53 | room_code | 否 | H |  |
| 54 | asset_prop | 否 | H |  |
| 55 | limit_flag | 否 | H |  |
| 56 | client_prop | 否 | H |  |
| 57 | asset_level | 否 | H |  |
| 58 | risk_level | 否 | H |  |
| 59 | corp_risk_level | 否 | H |  |
| 60 | stock_name | 否 | H |  |
| 61 | stock_type | 否 | H |  |
| 62 | sub_stock_type | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucbp_etf_entrust_detail_pos | ART | 是 | stock_code, component_code, position_str, stock_code, component_code, position_str |
| idx_ucbp_etf_entrust_detail | ART | 是 | init_date, exchange_type, entrust_no, stock_code, component_code, init_date, exchange_type, entrust_no, stock_code, component_code |
| idx_ucbp_etf_entrust_detail_pos | ART | 是 | stock_code, component_code, position_str, stock_code, component_code, position_str |
| uk_rpt_ucbpetfentrustdetail | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucbpetfentrustdetail_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_ucbp_etf_entrust_detail_pos | ART | 是 | stock_code, component_code, position_str, stock_code, component_code, position_str |
| idx_ucbp_etf_entrust_detail | ART | 是 | init_date, exchange_type, entrust_no, stock_code, component_code, init_date, exchange_type, entrust_no, stock_code, component_code |
| idx_ucbp_etf_entrust_detail_pos | ART | 是 | stock_code, component_code, position_str, stock_code, component_code, position_str |
| uk_rpt_ucbpetfentrustdetail | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucbpetfentrustdetail_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucbp_etf_entrust_detail | stock_code, component_code, position_str, stock_code, component_code, position_str |
| idx_ucbp_etf_entrust_detail | stock_code, component_code, position_str, stock_code, component_code, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 19:19:20 | V3.0.2.78 | taocong45644 | 当前表ucbp_etf_entrust_detail，增加索引（ idx_ucbp_etf_entrust_detail... |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-01-22 10:54:47 | 3.0.2.2 | 李江霖 | 将position_str中的sysnode_id调整为partition_no |
| 2024-12-27 14:28:13 | V3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-07-27 15:34:31 | V3.0.1.14 | 董乾坤 | 新增 |
| 2026-03-09 19:19:20 | V3.0.2.78 | taocong45644 | 当前表ucbp_etf_entrust_detail，增加索引（ idx_ucbp_etf_entrust_detail... |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-01-22 10:54:47 | 3.0.2.2 | 李江霖 | 将position_str中的sysnode_id调整为partition_no |
| 2024-12-27 14:28:13 | V3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-07-27 15:34:31 | V3.0.1.14 | 董乾坤 | 新增 |

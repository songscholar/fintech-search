# etf_entrust_detail - ETF申赎委托明细表

**表对象ID**: 5572
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 70 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | entrust_no | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | report_account | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | component_code | 否 |  |  |
| 11 | money_type | 否 |  |  |
| 12 | occur_amount | 否 |  |  |
| 13 | occur_balance | 否 |  |  |
| 14 | clear_date | 否 |  |  |
| 15 | component_market | 否 |  |  |
| 16 | prev_status | 否 |  |  |
| 17 | deal_status | 否 |  |  |
| 18 | cancel_serial_no | 否 |  |  |
| 19 | channel_type | 否 |  |  |
| 20 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+entrust_no(10)+com |
| 21 | begin_gap_amount | 否 |  |  |
| 22 | buy_real_amount2 | 否 |  |  |
| 23 | client_name | 否 | H |  |
| 24 | corp_client_group | 否 | H |  |
| 25 | client_group | 否 | H |  |
| 26 | room_code | 否 | H |  |
| 27 | asset_prop | 否 | H |  |
| 28 | limit_flag | 否 | H |  |
| 29 | client_prop | 否 | H |  |
| 30 | asset_level | 否 | H |  |
| 31 | risk_level | 否 | H |  |
| 32 | corp_risk_level | 否 | H |  |
| 33 | stock_name | 否 | H |  |
| 34 | stock_type | 否 | H |  |
| 35 | sub_stock_type | 否 | H |  |
| 36 | init_date | 否 |  |  |
| 37 | branch_no | 否 |  |  |
| 38 | entrust_no | 否 |  |  |
| 39 | fund_account | 否 |  |  |
| 40 | client_id | 否 |  |  |
| 41 | exchange_type | 否 |  |  |
| 42 | stock_account | 否 |  |  |
| 43 | report_account | 否 |  |  |
| 44 | stock_code | 否 |  |  |
| 45 | component_code | 否 |  |  |
| 46 | money_type | 否 |  |  |
| 47 | occur_amount | 否 |  |  |
| 48 | occur_balance | 否 |  |  |
| 49 | clear_date | 否 |  |  |
| 50 | component_market | 否 |  |  |
| 51 | prev_status | 否 |  |  |
| 52 | deal_status | 否 |  |  |
| 53 | cancel_serial_no | 否 |  |  |
| 54 | channel_type | 否 |  |  |
| 55 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+entrust_no(10)+com |
| 56 | begin_gap_amount | 否 |  |  |
| 57 | buy_real_amount2 | 否 |  |  |
| 58 | client_name | 否 | H |  |
| 59 | corp_client_group | 否 | H |  |
| 60 | client_group | 否 | H |  |
| 61 | room_code | 否 | H |  |
| 62 | asset_prop | 否 | H |  |
| 63 | limit_flag | 否 | H |  |
| 64 | client_prop | 否 | H |  |
| 65 | asset_level | 否 | H |  |
| 66 | risk_level | 否 | H |  |
| 67 | corp_risk_level | 否 | H |  |
| 68 | stock_name | 否 | H |  |
| 69 | stock_type | 否 | H |  |
| 70 | sub_stock_type | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_etf_entrust_detail | ART | 是 | position_str, stock_code, component_code, position_str, stock_code, component_code |
| idx_etfentrustd_entrust_no | ART | 是 | fund_account, entrust_no, component_code, fund_account, entrust_no, component_code |
| idx_etfentrustd_date_no | ART | 是 | init_date, entrust_no, init_date, entrust_no |
| uk_rpt_etfentrustdetail | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_etfentrustdetail_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_etf_entrust_detail | ART | 是 | position_str, stock_code, component_code, position_str, stock_code, component_code |
| idx_etfentrustd_entrust_no | ART | 是 | fund_account, entrust_no, component_code, fund_account, entrust_no, component_code |
| idx_etfentrustd_date_no | ART | 是 | init_date, entrust_no, init_date, entrust_no |
| uk_rpt_etfentrustdetail | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_etfentrustdetail_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_etf_entrust_detail | position_str, stock_code, component_code, position_str, stock_code, component_code |
| idx_etf_entrust_detail | position_str, stock_code, component_code, position_str, stock_code, component_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:21:27 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-01-22 10:54:47 | 3.0.2.37 | 李江霖 | 将position_str中的sysnode_id调整为partition_no |
| 2024-12-27 14:28:13 | 3.0.2.36 | 李江霖 | 增加position_str的备注 |
| 2024-08-12 11:08:55 | 3.0.2.35 | 程猛 | 删除bank_no字段，调整cancel_serialno为cancel_serial_no；新增全局非唯一索引idx_... |
| 2026-03-09 14:21:27 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-01-22 10:54:47 | 3.0.2.37 | 李江霖 | 将position_str中的sysnode_id调整为partition_no |
| 2024-12-27 14:28:13 | 3.0.2.36 | 李江霖 | 增加position_str的备注 |
| 2024-08-12 11:08:55 | 3.0.2.35 | 程猛 | 删除bank_no字段，调整cancel_serialno为cancel_serial_no；新增全局非唯一索引idx_... |

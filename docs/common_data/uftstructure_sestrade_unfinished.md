# unfinished - 在途业务表

**表对象ID**: 5526
**所属模块**: sestrade
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 94 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | unfinished_type | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | report_account | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | frozen_code | 否 |  |  |
| 11 | entrust_bs | 否 |  |  |
| 12 | seat_no | 否 |  |  |
| 13 | entrust_no | 否 |  |  |
| 14 | entrust_date | 否 |  |  |
| 15 | business_price | 否 |  |  |
| 16 | business_balance | 否 |  |  |
| 17 | business_amount | 否 |  |  |
| 18 | occur_amount | 否 |  |  |
| 19 | clear_balance | 否 |  |  |
| 20 | sub_balance | 否 |  |  |
| 21 | sub_amount | 否 |  |  |
| 22 | deli_status | 否 |  |  |
| 23 | date_back | 否 |  |  |
| 24 | date_clear | 否 |  |  |
| 25 | remark | 否 |  |  |
| 26 | position_str | 否 |  |  |
| 27 | business_type | 否 |  |  |
| 28 | branch_no | 否 |  |  |
| 29 | transaction_no | 否 |  |  |
| 30 | stock_type | 是 |  |  |
| 31 | business_no | 是 |  |  |
| 32 | business_id | 是 |  |  |
| 33 | stock_interestx | 是 |  |  |
| 34 | report_no | 否 |  |  |
| 35 | order_id | 否 |  |  |
| 36 | client_name | 否 | H |  |
| 37 | corp_client_group | 否 | H |  |
| 38 | client_group | 否 | H |  |
| 39 | room_code | 否 | H |  |
| 40 | limit_flag | 否 | H |  |
| 41 | client_prop | 否 | H |  |
| 42 | asset_level | 否 | H |  |
| 43 | risk_level | 否 | H |  |
| 44 | corp_risk_level | 否 | H |  |
| 45 | stock_name | 否 | H |  |
| 46 | sub_stock_type | 否 | H |  |
| 47 | asset_prop | 是 |  |  |
| 48 | init_date | 否 |  |  |
| 49 | serial_no | 否 |  |  |
| 50 | unfinished_type | 否 |  |  |
| 51 | exchange_type | 否 |  |  |
| 52 | client_id | 否 |  |  |
| 53 | fund_account | 否 |  |  |
| 54 | stock_account | 否 |  |  |
| 55 | report_account | 否 |  |  |
| 56 | stock_code | 否 |  |  |
| 57 | frozen_code | 否 |  |  |
| 58 | entrust_bs | 否 |  |  |
| 59 | seat_no | 否 |  |  |
| 60 | entrust_no | 否 |  |  |
| 61 | entrust_date | 否 |  |  |
| 62 | business_price | 否 |  |  |
| 63 | business_balance | 否 |  |  |
| 64 | business_amount | 否 |  |  |
| 65 | occur_amount | 否 |  |  |
| 66 | clear_balance | 否 |  |  |
| 67 | sub_balance | 否 |  |  |
| 68 | sub_amount | 否 |  |  |
| 69 | deli_status | 否 |  |  |
| 70 | date_back | 否 |  |  |
| 71 | date_clear | 否 |  |  |
| 72 | remark | 否 |  |  |
| 73 | position_str | 否 |  |  |
| 74 | business_type | 否 |  |  |
| 75 | branch_no | 否 |  |  |
| 76 | transaction_no | 否 |  |  |
| 77 | stock_type | 是 |  |  |
| 78 | business_no | 是 |  |  |
| 79 | business_id | 是 |  |  |
| 80 | stock_interestx | 是 |  |  |
| 81 | report_no | 否 |  |  |
| 82 | order_id | 否 |  |  |
| 83 | client_name | 否 | H |  |
| 84 | corp_client_group | 否 | H |  |
| 85 | client_group | 否 | H |  |
| 86 | room_code | 否 | H |  |
| 87 | limit_flag | 否 | H |  |
| 88 | client_prop | 否 | H |  |
| 89 | asset_level | 否 | H |  |
| 90 | risk_level | 否 | H |  |
| 91 | corp_risk_level | 否 | H |  |
| 92 | stock_name | 否 | H |  |
| 93 | sub_stock_type | 否 | H |  |
| 94 | asset_prop | 是 |  |  |

## 索引（共 22 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_unfinished_id | 默认 | 否 |  |
| idx_unfinished_pos | 默认 | 是 | position_str, position_str |
| idx_unfinished | ART | 是 | serial_no, unfinished_type, init_date, serial_no, unfinished_type, init_date |
| idx_unfinished_id | ART | 是 | client_id, position_str, client_id, position_str |
| idx_unfinished_acct | ART | 是 | fund_account, fund_account |
| idx_unfinished_pos | ART | 是 | position_str, position_str |
| idx_unfinished_stk | ART | 是 | stock_account, unfinished_type, stock_account, unfinished_type |
| idx_unfinished_deli | ART | 是 | deli_status, deli_status |
| uk_rpt_unfinished | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_unfinished_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_unfinished_tolast | ART | 是 | date_clear, date_clear |
| idx_unfinished_id | 默认 | 否 |  |
| idx_unfinished_pos | 默认 | 是 | position_str, position_str |
| idx_unfinished | ART | 是 | serial_no, unfinished_type, init_date, serial_no, unfinished_type, init_date |
| idx_unfinished_id | ART | 是 | client_id, position_str, client_id, position_str |
| idx_unfinished_acct | ART | 是 | fund_account, fund_account |
| idx_unfinished_pos | ART | 是 | position_str, position_str |
| idx_unfinished_stk | ART | 是 | stock_account, unfinished_type, stock_account, unfinished_type |
| idx_unfinished_deli | ART | 是 | deli_status, deli_status |
| uk_rpt_unfinished | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_unfinished_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_unfinished_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_unfinished | serial_no, unfinished_type, init_date, serial_no, unfinished_type, init_date |
| idx_unfinished_pos | position_str, position_str |
| idx_unfinished | serial_no, unfinished_type, init_date, serial_no, unfinished_type, init_date |
| idx_unfinished_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:47:03 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2026-01-15 20:37:40 | V3.0.8.32 | 沈勋 | 所有表unfinished，添加了表字段(asset_prop);
 |
| 2025-12-19 10:55:36 | V3.0.8.31 | yusz | 当前表unfinished，修改了索引idx_unfinished_id,索引字段修改为：(client_id,posi... |
| 2025-12-18 14:42:50 | 3.0.2.80 | 洪略 | 支持分区存储 |
| 2025-11-08 12:32:45 | 3.0.2.79 | 洪略 | 补齐资源 |
| 2025-10-29 15:17:24 | 3.0.2.78 |  | 所有表unfinished，添加了表字段(report_no);
所有表unfinished，添加了表字段(order... |
| 2025-09-24 10:54:55 | 3.0.2.77 | yangxz | 当前表unfinished，增加索引（ idx_unfinished_pos:[position_str]）;
 |
| 2025-08-14 10:04:03 | 3.0.2.76 | 高志强 | 增加DB模式,避免写表失败 |
| 2025-08-05 14:17:23 | 3.0.2.73 | 张训华 | 物理表unfinished，添加了表字段(transaction_no);
 |
| 2025-07-18 11:12:18 | 3.0.2.72 | dongh | 物理表unfinished，添加了表字段(business_id);
 |
| 2025-09-25 18:52:57 | V3.0.8.7 | luofan | 物理表unfinished，添加了表字段(stock_type);
物理表unfinished，添加了表字段(busi... |
| 2024-09-25 21:44:36 | 3.0.2.48 | 张明月 | 物理表unfinished，添加了表字段(branch_no);
 |
| 2024-09-09 11:13:25 | 3.0.2.43 | 杨森峰 | 表属性调整为不回库 |
| 2024-06-27 20:20:07 | 3.0.2.23 | 董乾坤 | 物理表unfinished，添加了表字段(business_type);
 |
| 2024-06-17 14:04:06 | 3.0.2.20 | yusz | 物理表unfinished，删除了表字段(stock_type);
物理表unfinished，删除了表字段(busi... |

> 共 30 条修改记录，仅显示最近15条

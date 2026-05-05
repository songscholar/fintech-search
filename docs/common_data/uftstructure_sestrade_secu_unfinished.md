# secu_unfinished - 证券在途业务表

**表对象ID**: 5577
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 72 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | unfinished_type | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | stock_account | 否 |  |  |
| 9 | report_account | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | stock_type | 否 |  |  |
| 12 | frozen_code | 否 |  |  |
| 13 | entrust_bs | 否 |  |  |
| 14 | seat_no | 否 |  |  |
| 15 | entrust_no | 否 |  |  |
| 16 | entrust_date | 否 |  |  |
| 17 | business_no | 否 |  |  |
| 18 | business_id | 否 |  |  |
| 19 | business_type | 否 |  |  |
| 20 | business_price | 否 |  |  |
| 21 | business_balance | 否 |  |  |
| 22 | business_amount | 否 |  |  |
| 23 | occur_amount | 否 |  |  |
| 24 | clear_balance | 否 |  |  |
| 25 | stock_interestx | 否 |  |  |
| 26 | sub_balance | 否 |  |  |
| 27 | sub_amount | 否 |  |  |
| 28 | deli_status | 否 |  |  |
| 29 | date_back | 否 |  |  |
| 30 | date_clear | 否 |  |  |
| 31 | remark | 否 |  |  |
| 32 | position_str | 否 |  |  |
| 33 | report_no | 否 |  |  |
| 34 | order_id | 否 |  |  |
| 35 | branch_no_b | 否 |  |  |
| 36 | transaction_no | 否 |  |  |
| 37 | init_date | 否 |  |  |
| 38 | serial_no | 否 |  |  |
| 39 | unfinished_type | 否 |  |  |
| 40 | exchange_type | 否 |  |  |
| 41 | branch_no | 否 |  |  |
| 42 | client_id | 否 |  |  |
| 43 | fund_account | 否 |  |  |
| 44 | stock_account | 否 |  |  |
| 45 | report_account | 否 |  |  |
| 46 | stock_code | 否 |  |  |
| 47 | stock_type | 否 |  |  |
| 48 | frozen_code | 否 |  |  |
| 49 | entrust_bs | 否 |  |  |
| 50 | seat_no | 否 |  |  |
| 51 | entrust_no | 否 |  |  |
| 52 | entrust_date | 否 |  |  |
| 53 | business_no | 否 |  |  |
| 54 | business_id | 否 |  |  |
| 55 | business_type | 否 |  |  |
| 56 | business_price | 否 |  |  |
| 57 | business_balance | 否 |  |  |
| 58 | business_amount | 否 |  |  |
| 59 | occur_amount | 否 |  |  |
| 60 | clear_balance | 否 |  |  |
| 61 | stock_interestx | 否 |  |  |
| 62 | sub_balance | 否 |  |  |
| 63 | sub_amount | 否 |  |  |
| 64 | deli_status | 否 |  |  |
| 65 | date_back | 否 |  |  |
| 66 | date_clear | 否 |  |  |
| 67 | remark | 否 |  |  |
| 68 | position_str | 否 |  |  |
| 69 | report_no | 否 |  |  |
| 70 | order_id | 否 |  |  |
| 71 | branch_no_b | 否 |  |  |
| 72 | transaction_no | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_secuunfinished_pos | ART | 是 | position_str, position_str |
| idx_secuunfinished_acct | ART | 是 | fund_account, fund_account |
| idx_secuunfinished_id | ART | 是 | client_id, client_id |
| idx_secuunfinished | ART | 是 | serial_no, unfinished_type, init_date, serial_no, unfinished_type, init_date |
| idx_secuunfinished_pos | ART | 是 | position_str, position_str |
| idx_secuunfinished_acct | ART | 是 | fund_account, fund_account |
| idx_secuunfinished_id | ART | 是 | client_id, client_id |
| idx_secuunfinished | ART | 是 | serial_no, unfinished_type, init_date, serial_no, unfinished_type, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_secuunfinished_pos | position_str, position_str |
| idx_secuunfinished_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:26:45 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-08-14 10:03:53 | 3.0.2.76 | 高志强 | 增加DB模式,避免写表失败 |
| 2025-08-05 14:18:54 | 3.0.2.74 | 张训华 | 物理表secu_unfinished，添加了表字段(transaction_no);
 |
| 2024-10-30 10:39:21 | 3.0.5.1055 | 张训华 | 新增表 |
| 2026-03-09 14:26:45 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-08-14 10:03:53 | 3.0.2.76 | 高志强 | 增加DB模式,避免写表失败 |
| 2025-08-05 14:18:54 | 3.0.2.74 | 张训华 | 物理表secu_unfinished，添加了表字段(transaction_no);
 |
| 2024-10-30 10:39:21 | 3.0.5.1055 | 张训华 | 新增表 |

# ucrt_unfinished - 融资融券在途业务表

**表对象ID**: 7546
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 72 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | unfinished_type | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | business_type | 否 |  |  |
| 8 | deli_status | 否 |  |  |
| 9 | serial_no | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | report_account | 否 |  |  |
| 13 | stock_type | 否 |  |  |
| 14 | entrust_bs | 否 |  |  |
| 15 | seat_no | 否 |  |  |
| 16 | entrust_date | 否 |  |  |
| 17 | business_id | 否 |  |  |
| 18 | business_balance | 否 |  |  |
| 19 | occur_amount | 否 |  |  |
| 20 | clear_balance | 否 |  |  |
| 21 | stock_interestx | 否 |  |  |
| 22 | sub_balance | 否 |  |  |
| 23 | sub_amount | 否 |  |  |
| 24 | date_back | 否 |  |  |
| 25 | remark | 否 |  |  |
| 26 | position_str | 否 |  | fund_account(18)+init_date(8)+serial_no(10)+unfinished_type( |
| 27 | report_no | 否 |  |  |
| 28 | order_id | 否 |  |  |
| 29 | frozen_code | 否 |  |  |
| 30 | entrust_no | 否 |  |  |
| 31 | business_no | 否 |  |  |
| 32 | business_price | 否 |  |  |
| 33 | business_amount | 否 |  |  |
| 34 | date_clear | 否 |  |  |
| 35 | entrust_way | 否 |  |  |
| 36 | entrust_type | 否 |  |  |
| 37 | init_date | 否 |  |  |
| 38 | unfinished_type | 否 |  |  |
| 39 | exchange_type | 否 |  |  |
| 40 | fund_account | 否 |  |  |
| 41 | stock_account | 否 |  |  |
| 42 | stock_code | 否 |  |  |
| 43 | business_type | 否 |  |  |
| 44 | deli_status | 否 |  |  |
| 45 | serial_no | 否 |  |  |
| 46 | branch_no | 否 |  |  |
| 47 | client_id | 否 |  |  |
| 48 | report_account | 否 |  |  |
| 49 | stock_type | 否 |  |  |
| 50 | entrust_bs | 否 |  |  |
| 51 | seat_no | 否 |  |  |
| 52 | entrust_date | 否 |  |  |
| 53 | business_id | 否 |  |  |
| 54 | business_balance | 否 |  |  |
| 55 | occur_amount | 否 |  |  |
| 56 | clear_balance | 否 |  |  |
| 57 | stock_interestx | 否 |  |  |
| 58 | sub_balance | 否 |  |  |
| 59 | sub_amount | 否 |  |  |
| 60 | date_back | 否 |  |  |
| 61 | remark | 否 |  |  |
| 62 | position_str | 否 |  | fund_account(18)+init_date(8)+serial_no(10)+unfinished_type( |
| 63 | report_no | 否 |  |  |
| 64 | order_id | 否 |  |  |
| 65 | frozen_code | 否 |  |  |
| 66 | entrust_no | 否 |  |  |
| 67 | business_no | 否 |  |  |
| 68 | business_price | 否 |  |  |
| 69 | business_amount | 否 |  |  |
| 70 | date_clear | 否 |  |  |
| 71 | entrust_way | 否 |  |  |
| 72 | entrust_type | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_unfinished | 默认 | 否 | fund_account, init_date, serial_no, unfinished_type, stock_code, exchange_type, fund_account, init_date, serial_no, unfinished_type, stock_code, exchange_type |
| idx_ucrt_unfinished | 默认 | 否 |  |
| idx_ucrt_unfinished | ART | 是 | fund_account, exchange_type, stock_account, unfinished_type, stock_code, fund_account, exchange_type, stock_account, unfinished_type, stock_code |
| idx_ucrt_unfinished_serial_no | ART | 是 | fund_account, init_date, serial_no, unfinished_type, stock_code, exchange_type, fund_account, init_date, serial_no, unfinished_type, stock_code, exchange_type |
| idx_ucrt_unfinished | 默认 | 否 | fund_account, init_date, serial_no, unfinished_type, stock_code, exchange_type, fund_account, init_date, serial_no, unfinished_type, stock_code, exchange_type |
| idx_ucrt_unfinished | 默认 | 否 |  |
| idx_ucrt_unfinished | ART | 是 | fund_account, exchange_type, stock_account, unfinished_type, stock_code, fund_account, exchange_type, stock_account, unfinished_type, stock_code |
| idx_ucrt_unfinished_serial_no | ART | 是 | fund_account, init_date, serial_no, unfinished_type, stock_code, exchange_type, fund_account, init_date, serial_no, unfinished_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_unfinished | fund_account, init_date, serial_no, unfinished_type, stock_code, exchange_type, fund_account, init_date, serial_no, unfinished_type, stock_code, exchange_type |
| idx_ucrt_unfinished | fund_account, init_date, serial_no, unfinished_type, stock_code, exchange_type, fund_account, init_date, serial_no, unfinished_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-15 15:26:37 | 3.0.8.13 | 袁文龙 | 物理表ucrt_unfinished，新增索引（idx_ucrt_unfinished_serial_no） |
| 2025-09-11 11:30:55 | 3.0.6.1070 | 袁文龙 | ses合入dev，版本+1 |
| 2025-09-02 11:14:30 | 3.0.6.1067 | 许琮擎 | 索引中增加字段stock_code |
| 2025-08-02 15:59:09 | 3.0.2.1 | 曾阳璞 | 物理表ucrt_unfinished，添加了表字段(branch_no);
物理表ucrt_unfinished，添加... |
| 2024-10-12 13:55:42 | 3.0.6.4 | 汪杰 | 物理表ucrt_unfinished，增加索引(idx_ucrt_unfinished:[fund_account,in... |
| 2024-10-12 13:54:03 | 3.0.6.4 | 汪杰 | 物理表ucrt_unfinished，删除了表索引(idx_ucrt_unfinished);
 |
| 2024-10-12 13:53:36 | 3.0.6.4 | 汪杰 | 物理表ucrt_unfinished，添加了表字段(serial_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-01-15 15:26:37 | 3.0.8.13 | 袁文龙 | 物理表ucrt_unfinished，新增索引（idx_ucrt_unfinished_serial_no） |
| 2025-09-11 11:30:55 | 3.0.6.1070 | 袁文龙 | ses合入dev，版本+1 |
| 2025-09-02 11:14:30 | 3.0.6.1067 | 许琮擎 | 索引中增加字段stock_code |
| 2025-08-02 15:59:09 | 3.0.2.1 | 曾阳璞 | 物理表ucrt_unfinished，添加了表字段(branch_no);
物理表ucrt_unfinished，添加... |
| 2024-10-12 13:55:42 | 3.0.6.4 | 汪杰 | 物理表ucrt_unfinished，增加索引(idx_ucrt_unfinished:[fund_account,in... |
| 2024-10-12 13:54:03 | 3.0.6.4 | 汪杰 | 物理表ucrt_unfinished，删除了表索引(idx_ucrt_unfinished);
 |
| 2024-10-12 13:53:36 | 3.0.6.4 | 汪杰 | 物理表ucrt_unfinished，添加了表字段(serial_no);
 |

> 共 16 条修改记录，仅显示最近15条

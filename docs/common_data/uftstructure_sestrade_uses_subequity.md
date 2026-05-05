# uses_subequity - 市值申购权益

**表对象ID**: 5515
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | enable_amount | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | init_date | 否 |  |  |
| 5 | register_date | 否 |  |  |
| 6 | seat_no | 否 |  |  |
| 7 | stib_enable_quota | 否 |  |  |
| 8 | stock_account | 否 |  |  |
| 9 | partition_no | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | branch_no | 否 |  |  |
| 12 | update_date | 否 |  |  |
| 13 | update_time | 否 |  |  |
| 14 | position_str | 否 |  |  |
| 15 | client_id | 否 | H |  |
| 16 | client_name | 否 | H |  |
| 17 | enable_amount | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | fund_account | 否 |  |  |
| 20 | init_date | 否 |  |  |
| 21 | register_date | 否 |  |  |
| 22 | seat_no | 否 |  |  |
| 23 | stib_enable_quota | 否 |  |  |
| 24 | stock_account | 否 |  |  |
| 25 | partition_no | 否 |  |  |
| 26 | transaction_no | 否 |  |  |
| 27 | branch_no | 否 |  |  |
| 28 | update_date | 否 |  |  |
| 29 | update_time | 否 |  |  |
| 30 | position_str | 否 |  |  |
| 31 | client_id | 否 | H |  |
| 32 | client_name | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_subequity_fund_account | 默认 | 否 | fund_account, fund_account |
| idx_uses_subequity | ART | 是 | fund_account, exchange_type, stock_account, fund_account, exchange_type, stock_account |
| uk_rpt_usessubequity | ART | 是 | init_date, fund_account, exchange_type, stock_account, init_date, fund_account, exchange_type, stock_account |
| idx_uses_subequity_fund_account | 默认 | 否 | fund_account, fund_account |
| idx_uses_subequity | ART | 是 | fund_account, exchange_type, stock_account, fund_account, exchange_type, stock_account |
| uk_rpt_usessubequity | ART | 是 | init_date, fund_account, exchange_type, stock_account, init_date, fund_account, exchange_type, stock_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_subequity | fund_account, stock_account, exchange_type, fund_account, stock_account, exchange_type |
| idx_uses_subequity | fund_account, stock_account, exchange_type, fund_account, stock_account, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:42:11 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-07-29 11:27:08 | 3.0.6.1002 | tongck54118 | 物理表uses_subequity，添加了表字段(branch_no);
物理表uses_subequity，添加了表... |
| 2024-10-18 11:28:24 | 3.0.5.1001 | 全春辉 | 表uses_subequity，增加索引(idx_uses_subequity_fund_account:[fund_a... |
| 2024-04-28 17:04:51 | 3.0.2.3 | 阮善宏 | 物理表uses_subequity，添加了表字段(partition_no);
物理表uses_subequity，添... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-09 13:42:11 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-07-29 11:27:08 | 3.0.6.1002 | tongck54118 | 物理表uses_subequity，添加了表字段(branch_no);
物理表uses_subequity，添加了表... |
| 2024-10-18 11:28:24 | 3.0.5.1001 | 全春辉 | 表uses_subequity，增加索引(idx_uses_subequity_fund_account:[fund_a... |
| 2024-04-28 17:04:51 | 3.0.2.3 | 阮善宏 | 物理表uses_subequity，添加了表字段(partition_no);
物理表uses_subequity，添... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

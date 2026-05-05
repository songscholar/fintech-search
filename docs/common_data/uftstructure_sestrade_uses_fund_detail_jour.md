# uses_fund_detail_jour - 证券交易资金详细信息流水表

**表对象ID**: 5510
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_microtime | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | fund_enable_level | 否 |  |  |
| 8 | money_type | 否 |  |  |
| 9 | fund_update_direction | 否 |  |  |
| 10 | occur_balance | 否 |  |  |
| 11 | post_balance | 否 |  |  |
| 12 | real_action | 否 |  |  |
| 13 | business_flag | 否 |  |  |
| 14 | cancel_serial_no | 否 |  |  |
| 15 | remark | 否 |  |  |
| 16 | sett_batch_no | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | position_str | 否 |  | fund_account(18)+init_date(10)+serial_no(10) |
| 19 | finance_type | 否 |  |  |
| 20 | entrust_date | 否 |  |  |
| 21 | init_date | 否 |  |  |
| 22 | serial_no | 否 |  |  |
| 23 | curr_date | 否 |  |  |
| 24 | curr_microtime | 否 |  |  |
| 25 | client_id | 否 |  |  |
| 26 | fund_account | 否 |  |  |
| 27 | fund_enable_level | 否 |  |  |
| 28 | money_type | 否 |  |  |
| 29 | fund_update_direction | 否 |  |  |
| 30 | occur_balance | 否 |  |  |
| 31 | post_balance | 否 |  |  |
| 32 | real_action | 否 |  |  |
| 33 | business_flag | 否 |  |  |
| 34 | cancel_serial_no | 否 |  |  |
| 35 | remark | 否 |  |  |
| 36 | sett_batch_no | 否 |  |  |
| 37 | branch_no | 否 |  |  |
| 38 | position_str | 否 |  | fund_account(18)+init_date(10)+serial_no(10) |
| 39 | finance_type | 否 |  |  |
| 40 | entrust_date | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_fund_detail_jour | 默认 | 否 | fund_account, fund_account |
| idx_fund_detail_jour | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_fund_detail_jour_pos | ART | 是 | position_str, position_str |
| idx_rpt_fund_detail_jour | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_fund_detail_jour | 默认 | 否 | fund_account, fund_account |
| idx_fund_detail_jour | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_fund_detail_jour_pos | ART | 是 | position_str, position_str |
| idx_rpt_fund_detail_jour | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_fund_detail_jour | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_fund_detail_jour | fund_account, init_date, serial_no, fund_account, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:37:04 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-18 17:05:09 | V3.0.2.74 | 洪略 | 支持分区存储 |
| 2025-12-11 14:00:39 | V3.0.8.28 | yusz | 所有表uses_fund_detail_jour，添加了表字段(entrust_date);
 |
| 2025-12-08 13:25:11 | 3.0.6.13 | 洪略 | 历史表索引加rpt前缀 |
| 2025-11-07 11:34:49 | V3.0.2.103 | 洪略 | 增加历史表 |
| 2025-07-24 10:24:01 | 3.0.6.13 | 张华佳 | 物理表uses_fund_detail_jour，添加了表字段(branch_no);
 |
| 2025-05-23 11:12:58 | 3.0.2.69 | 范文浩 | 物理表uses_fund_detail_jour，添加了表字段(remark);
 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2024-05-15 22:23:45 | 3.0.2.10 | 乐闽庭 | 增加内存表索引字段(索引idx_fund_detail_jour:增加了索引字段：fund_account); |
| 2024-05-15 22:23:11 | 3.0.2.9 | 乐闽庭 | 物理表uses_fund_detail_jour，增加索引字段(索引idx_fund_detail_jour:增加了索引... |
| 2024-04-28 20:41:32 | 3.0.2.3 | 阮善宏 | 内存表uses_fund_detail_jour，删除了表索引(idx_fund_detail_jour);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-09 13:37:04 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-18 17:05:09 | V3.0.2.74 | 洪略 | 支持分区存储 |
| 2025-12-11 14:00:39 | V3.0.8.28 | yusz | 所有表uses_fund_detail_jour，添加了表字段(entrust_date);
 |

> 共 24 条修改记录，仅显示最近15条

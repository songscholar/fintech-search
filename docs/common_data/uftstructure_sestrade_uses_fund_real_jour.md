# uses_fund_real_jour - 证券交易资金变动表

**表对象ID**: 5508
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 58 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | finance_type | 否 |  |  |
| 8 | money_type | 否 |  |  |
| 9 | occur_balance | 否 |  |  |
| 10 | post_balance | 否 |  |  |
| 11 | real_action | 否 |  |  |
| 12 | business_flag | 否 |  |  |
| 13 | asset_prop | 否 |  |  |
| 14 | real_serialno | 否 |  |  |
| 15 | cancel_serial_no | 否 |  |  |
| 16 | fund_real_jour_kind | 否 |  |  |
| 17 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 18 | branch_no | 否 |  |  |
| 19 | sett_batch_no | 否 |  |  |
| 20 | client_name | 否 | H |  |
| 21 | corp_client_group | 否 | H |  |
| 22 | client_group | 否 | H |  |
| 23 | room_code | 否 | H |  |
| 24 | limit_flag | 否 | H |  |
| 25 | client_prop | 否 | H |  |
| 26 | asset_level | 否 | H |  |
| 27 | risk_level | 否 | H |  |
| 28 | corp_risk_level | 否 | H |  |
| 29 | remark | 否 |  |  |
| 30 | init_date | 否 |  |  |
| 31 | serial_no | 否 |  |  |
| 32 | curr_date | 否 |  |  |
| 33 | curr_time | 否 |  |  |
| 34 | client_id | 否 |  |  |
| 35 | fund_account | 否 |  |  |
| 36 | finance_type | 否 |  |  |
| 37 | money_type | 否 |  |  |
| 38 | occur_balance | 否 |  |  |
| 39 | post_balance | 否 |  |  |
| 40 | real_action | 否 |  |  |
| 41 | business_flag | 否 |  |  |
| 42 | asset_prop | 否 |  |  |
| 43 | real_serialno | 否 |  |  |
| 44 | cancel_serial_no | 否 |  |  |
| 45 | fund_real_jour_kind | 否 |  |  |
| 46 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 47 | branch_no | 否 |  |  |
| 48 | sett_batch_no | 否 |  |  |
| 49 | client_name | 否 | H |  |
| 50 | corp_client_group | 否 | H |  |
| 51 | client_group | 否 | H |  |
| 52 | room_code | 否 | H |  |
| 53 | limit_flag | 否 | H |  |
| 54 | client_prop | 否 | H |  |
| 55 | asset_level | 否 | H |  |
| 56 | risk_level | 否 | H |  |
| 57 | corp_risk_level | 否 | H |  |
| 58 | remark | 否 |  |  |

## 索引（共 16 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_secu_fund_real_jour | 默认 | 否 | fund_real_jour_kind, fund_real_jour_kind |
| idx_uft_secu_fund_real_jour | 默认 | 否 | init_date, serial_no, init_date, serial_no |
| idx_uses_fund_real_jour | 默认 | 否 |  |
| idx_uft_secu_fund_real_jour | ART | 是 | fund_account, money_type, init_date, serial_no, fund_real_jour_kind, fund_account, money_type, init_date, serial_no, fund_real_jour_kind |
| idx_uft_secu_fund_real_jour_unique | ART | 是 | fund_account, init_date, serial_no, fund_real_jour_kind, fund_account, init_date, serial_no, fund_real_jour_kind |
| idx_uses_fund_real_jour_pos | ART | 是 | position_str, position_str |
| uk_rpt_usesfundrealjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_usesfundrealjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_uft_secu_fund_real_jour | 默认 | 否 | fund_real_jour_kind, fund_real_jour_kind |
| idx_uft_secu_fund_real_jour | 默认 | 否 | init_date, serial_no, init_date, serial_no |
| idx_uses_fund_real_jour | 默认 | 否 |  |
| idx_uft_secu_fund_real_jour | ART | 是 | fund_account, money_type, init_date, serial_no, fund_real_jour_kind, fund_account, money_type, init_date, serial_no, fund_real_jour_kind |
| idx_uft_secu_fund_real_jour_unique | ART | 是 | fund_account, init_date, serial_no, fund_real_jour_kind, fund_account, init_date, serial_no, fund_real_jour_kind |
| idx_uses_fund_real_jour_pos | ART | 是 | position_str, position_str |
| uk_rpt_usesfundrealjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_usesfundrealjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_secu_fund_real_jour | fund_account, init_date, serial_no, fund_real_jour_kind, fund_account, init_date, serial_no, fund_real_jour_kind |
| idx_uft_secu_fund_real_jour | fund_account, init_date, serial_no, fund_real_jour_kind, fund_account, init_date, serial_no, fund_real_jour_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:34:43 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-18 16:19:44 | 3.0.2.74 | 洪略 | 补充分区信息 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-07-27 19:44:39 | 3.0.2.73 | 全春辉 | 数据导出相关表增加定位串查询索引 |
| 2025-07-23 13:43:59 | 3.0.6.13 | 张华佳 | 物理表uses_fund_real_jour，添加了表字段(branch_no);
 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-04-14 21:36:30 | 3.0.2.65 | 乐闽庭 | 物理表uses_fund_real_jour，增加索引字段(索引idx_uft_secu_fund_real_jour:... |
| 2025-03-21 13:46:56 | 3.0.2.63 | 张训华 | 支持二次上场，增加全局唯一索引idx_uft_secu_fund_real_jour_unique |
| 2024-08-14 14:10:07 | 3.0.2.39 | 张剑 | remark设置为变长字段 |
| 2024-04-28 20:36:19 | 3.0.2.3 | 阮善宏 | 物理表uses_fund_real_jour，增加索引(idx_uft_secu_fund_real_jour:[ini... |
| 2024-04-28 20:35:00 | 3.0.2.3 | 阮善宏 | 物理表uses_fund_real_jour，删除了表索引(idx_uses_fund_real_jour);
 |
| 2024-04-28 11:20:13 | 3.0.2.3 | 阮善宏 | 物理表uses_fund_real_jour，添加了表字段(position_str);
 |
| 2024-01-17 14:57:04 | 3.0.1.406 | 范文浩 | 物理表uses_fund_real_jour，添加了表字段(fund_real_jour_kind);
物理表uses... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 14:24 | 0.0.0.7 | 程猛 | 删除表字段order_no |

> 共 30 条修改记录，仅显示最近15条

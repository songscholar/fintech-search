# uses_stock_real_jour - 证券股份交易信息流水表

**表对象ID**: 5513
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 64 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_microtime | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | stock_account | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | real_action | 否 |  |  |
| 11 | business_flag | 否 |  |  |
| 12 | occur_amount | 否 |  |  |
| 13 | post_amount | 否 |  |  |
| 14 | trustee_seat_no | 否 |  |  |
| 15 | cancel_serial_no | 否 |  |  |
| 16 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 17 | sett_batch_no | 否 |  |  |
| 18 | client_name | 否 | H |  |
| 19 | corp_client_group | 否 | H |  |
| 20 | branch_no | 否 | H |  |
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
| 32 | remark | 否 |  |  |
| 33 | init_date | 否 |  |  |
| 34 | serial_no | 否 |  |  |
| 35 | curr_date | 否 |  |  |
| 36 | curr_microtime | 否 |  |  |
| 37 | client_id | 否 |  |  |
| 38 | fund_account | 否 |  |  |
| 39 | exchange_type | 否 |  |  |
| 40 | stock_account | 否 |  |  |
| 41 | stock_code | 否 |  |  |
| 42 | real_action | 否 |  |  |
| 43 | business_flag | 否 |  |  |
| 44 | occur_amount | 否 |  |  |
| 45 | post_amount | 否 |  |  |
| 46 | trustee_seat_no | 否 |  |  |
| 47 | cancel_serial_no | 否 |  |  |
| 48 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 49 | sett_batch_no | 否 |  |  |
| 50 | client_name | 否 | H |  |
| 51 | corp_client_group | 否 | H |  |
| 52 | branch_no | 否 | H |  |
| 53 | client_group | 否 | H |  |
| 54 | room_code | 否 | H |  |
| 55 | asset_prop | 否 | H |  |
| 56 | limit_flag | 否 | H |  |
| 57 | client_prop | 否 | H |  |
| 58 | asset_level | 否 | H |  |
| 59 | risk_level | 否 | H |  |
| 60 | corp_risk_level | 否 | H |  |
| 61 | stock_name | 否 | H |  |
| 62 | stock_type | 否 | H |  |
| 63 | sub_stock_type | 否 | H |  |
| 64 | remark | 否 |  |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_stock_real_jour_no | ART | 是 | stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, init_date, serial_no, stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, init_date, serial_no |
| idx_uses_stock_real_jour_cancel | ART | 是 | fund_account, cancel_serial_no, fund_account, cancel_serial_no |
| idx_uses_stock_real_jour_fundacct | ART | 是 | fund_account, fund_account |
| idx_uses_stock_real_jour | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_uses_stock_real_jour_pos | ART | 是 | position_str, position_str |
| uk_rpt_usesstockrealjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_usesstockrealjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_uses_stock_real_jour_no | ART | 是 | stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, init_date, serial_no, stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, init_date, serial_no |
| idx_uses_stock_real_jour_cancel | ART | 是 | fund_account, cancel_serial_no, fund_account, cancel_serial_no |
| idx_uses_stock_real_jour_fundacct | ART | 是 | fund_account, fund_account |
| idx_uses_stock_real_jour | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_uses_stock_real_jour_pos | ART | 是 | position_str, position_str |
| uk_rpt_usesstockrealjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_usesstockrealjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_stock_real_jour | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_uses_stock_real_jour | fund_account, init_date, serial_no, fund_account, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:41:01 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-18 16:21:13 | 3.0.2.74 | 洪略 | 补充分区信息 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-07-27 19:47:11 | 3.0.2.73 | 全春辉 | 数据导出相关表增加定位串查询索引 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-03-21 13:46:56 | 3.0.2.63 | 张训华 | 支持二次上场，增加全局唯一索引idx_uses_stock_real_jour |
| 2024-12-27 14:28:13 | 3.0.2.43 | 李江霖 | 增加position_str的备注 |
| 2024-08-22 15:37:44 | 3.0.2.42 | 范文浩 | 物理表uses_stock_real_jour，添加了索引idx_uses_stock_real_jour_fundac... |
| 2024-08-22 15:37:44 | 3.0.2.42 | 范文浩 | 物理表uses_stock_real_jour，添加了表字段(remark);
 |
| 2024-05-07 20:52:53 | 3.0.2.6 | 阮善宏 | 内存表删除frozen_amount |
| 2024-04-28 20:39:25 | 3.0.2.3 | 阮善宏 | 内存表uses_stock_real_jour，增加索引(idx_uses_stock_real_jour_no:[in... |
| 2024-04-28 13:44:03 | 3.0.2.3 | 阮善宏 | 物理表uses_stock_real_jour，添加了表字段(position_str);
 |
| 2024-04-28 13:43:16 | 3.0.2.3 | 阮善宏 | 物理表uses_stock_real_jour，删除了表字段(frozen_amount);
物理表uses_stoc... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-09 13:41:01 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |

> 共 28 条修改记录，仅显示最近15条

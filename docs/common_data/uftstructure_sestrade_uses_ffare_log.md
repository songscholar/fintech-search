# uses_ffare_log - 证券前台费用日志表

**表对象ID**: 5512
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 68 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | business_flag | 否 |  |  |
| 3 | cancel_serial_no | 否 |  |  |
| 4 | curr_date | 否 |  |  |
| 5 | curr_microtime | 否 |  |  |
| 6 | entrust_no | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | fare | 否 |  |  |
| 9 | fare_date | 否 |  |  |
| 10 | fare_type | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | init_date | 否 |  |  |
| 13 | money_type | 否 |  |  |
| 14 | op_branch_no | 否 |  |  |
| 15 | op_entrust_way | 否 |  |  |
| 16 | op_station | 否 |  |  |
| 17 | operator_no | 否 |  |  |
| 18 | prev_status | 否 |  |  |
| 19 | serial_no | 否 |  |  |
| 20 | status | 否 |  |  |
| 21 | stock_account | 否 |  |  |
| 22 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 23 | data_src | 否 |  |  |
| 24 | client_id | 否 | H |  |
| 25 | client_name | 否 | H |  |
| 26 | corp_client_group | 否 | H |  |
| 27 | client_group | 否 | H |  |
| 28 | room_code | 否 | H |  |
| 29 | asset_prop | 否 | H |  |
| 30 | limit_flag | 否 | H |  |
| 31 | client_prop | 否 | H |  |
| 32 | asset_level | 否 | H |  |
| 33 | risk_level | 否 | H |  |
| 34 | corp_risk_level | 否 | H |  |
| 35 | branch_no | 否 |  |  |
| 36 | business_flag | 否 |  |  |
| 37 | cancel_serial_no | 否 |  |  |
| 38 | curr_date | 否 |  |  |
| 39 | curr_microtime | 否 |  |  |
| 40 | entrust_no | 否 |  |  |
| 41 | exchange_type | 否 |  |  |
| 42 | fare | 否 |  |  |
| 43 | fare_date | 否 |  |  |
| 44 | fare_type | 否 |  |  |
| 45 | fund_account | 否 |  |  |
| 46 | init_date | 否 |  |  |
| 47 | money_type | 否 |  |  |
| 48 | op_branch_no | 否 |  |  |
| 49 | op_entrust_way | 否 |  |  |
| 50 | op_station | 否 |  |  |
| 51 | operator_no | 否 |  |  |
| 52 | prev_status | 否 |  |  |
| 53 | serial_no | 否 |  |  |
| 54 | status | 否 |  |  |
| 55 | stock_account | 否 |  |  |
| 56 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 57 | data_src | 否 |  |  |
| 58 | client_id | 否 | H |  |
| 59 | client_name | 否 | H |  |
| 60 | corp_client_group | 否 | H |  |
| 61 | client_group | 否 | H |  |
| 62 | room_code | 否 | H |  |
| 63 | asset_prop | 否 | H |  |
| 64 | limit_flag | 否 | H |  |
| 65 | client_prop | 否 | H |  |
| 66 | asset_level | 否 | H |  |
| 67 | risk_level | 否 | H |  |
| 68 | corp_risk_level | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_ffare_log_pos | 默认 | 否 |  |
| idx_uses_ffare_log | 默认 | 否 | data_src, data_src |
| idx_uses_ffare_log | ART | 是 | fund_account, init_date, serial_no, data_src, fund_account, init_date, serial_no, data_src |
| idx_uses_ffare_log_rpt | ART | 是 | entrust_no, branch_no, fund_account, entrust_no, branch_no, fund_account |
| idx_uses_ffare_log_pos | ART | 是 | position_str, position_str |
| uk_rpt_usesffarelog | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_usesffarelog_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_uses_ffare_log_pos | 默认 | 否 |  |
| idx_uses_ffare_log | 默认 | 否 | data_src, data_src |
| idx_uses_ffare_log | ART | 是 | fund_account, init_date, serial_no, data_src, fund_account, init_date, serial_no, data_src |
| idx_uses_ffare_log_rpt | ART | 是 | entrust_no, branch_no, fund_account, entrust_no, branch_no, fund_account |
| idx_uses_ffare_log_pos | ART | 是 | position_str, position_str |
| uk_rpt_usesffarelog | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_usesffarelog_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_ffare_log | fund_account, init_date, serial_no, data_src, fund_account, init_date, serial_no, data_src |
| idx_uses_ffare_log | fund_account, init_date, serial_no, data_src, fund_account, init_date, serial_no, data_src |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:40:26 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-12-01 16:41:25 | 3.0.2.104 | taocong45644 | 当前表uses_ffare_log，修改了索引idx_uses_ffare_log_pos,索引字段修改为：(posit... |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-03-21 13:46:56 | 3.0.2.63 | 张训华 | 支持二次上场，idx_uses_ffare_log修改为全局唯一索引 |
| 2024-12-27 14:28:13 | 3.0.2.31 | 李江霖 | 增加position_str的备注 |
| 2024-07-25 14:03:44 | 3.0.2.30 | 乐闽庭 | 内存表索引idx_uses_ffare_log增加索引字段data_src |
| 2024-07-17 14:00:33 | 3.0.2.30 | 乐闽庭 | 物理表uses_ffare_log，增加索引字段(索引idx_uses_ffare_log:增加了索引字段：data_s... |
| 2024-07-17 13:59:20 | 3.0.2.30 | 乐闽庭 | 物理表uses_ffare_log，添加了表字段(data_src);
 |
| 2024-04-28 13:28:22 | 3.0.2.3 | 阮善宏 | 物理表uses_ffare_log，添加了表字段(position_str);
 |
| 2024-04-28 13:27:48 | 3.0.2.3 | 阮善宏 | 物理表uses_ffare_log，删除了表字段(bank_no);
物理表uses_ffare_log，删除了表字段... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-09 13:40:26 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-12-01 16:41:25 | 3.0.2.104 | taocong45644 | 当前表uses_ffare_log，修改了索引idx_uses_ffare_log_pos,索引字段修改为：(posit... |

> 共 24 条修改记录，仅显示最近15条

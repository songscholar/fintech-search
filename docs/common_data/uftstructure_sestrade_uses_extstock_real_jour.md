# uses_extstock_real_jour - 证券股份交易信息扩展流水表

**表对象ID**: 5514
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 62 个）

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
| 10 | trustee_seat_no | 否 |  |  |
| 11 | real_action | 否 |  |  |
| 12 | business_flag | 否 |  |  |
| 13 | occur_amount | 否 |  |  |
| 14 | post_amount | 否 |  |  |
| 15 | cancel_serial_no | 否 |  |  |
| 16 | remark | 否 |  |  |
| 17 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
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
| 32 | init_date | 否 |  |  |
| 33 | serial_no | 否 |  |  |
| 34 | curr_date | 否 |  |  |
| 35 | curr_microtime | 否 |  |  |
| 36 | client_id | 否 |  |  |
| 37 | fund_account | 否 |  |  |
| 38 | exchange_type | 否 |  |  |
| 39 | stock_account | 否 |  |  |
| 40 | stock_code | 否 |  |  |
| 41 | trustee_seat_no | 否 |  |  |
| 42 | real_action | 否 |  |  |
| 43 | business_flag | 否 |  |  |
| 44 | occur_amount | 否 |  |  |
| 45 | post_amount | 否 |  |  |
| 46 | cancel_serial_no | 否 |  |  |
| 47 | remark | 否 |  |  |
| 48 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 49 | client_name | 否 | H |  |
| 50 | corp_client_group | 否 | H |  |
| 51 | branch_no | 否 | H |  |
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

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_extstock_real_jour | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| uk_rpt_usesextstockrealjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_usesextstockrealjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_uses_extstock_real_jour | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| uk_rpt_usesextstockrealjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_usesextstockrealjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_extstock_real_jour | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_uses_extstock_real_jour | fund_account, init_date, serial_no, fund_account, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:41:33 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-04-17 11:13:42 | 3.0.2.65 | 於达 | 内存表uses_extstock_real_jour，添加了表字段(position_str);
 |
| 2024-12-11 15:23:28 | 3.0.2.52 | 谢宗艺 | 内存表uses_extstock_real_jour，添加了表字段(remark); |
| 2024-05-21 21:14:16 | 3.0.2.10 | 乐闽庭 | 内存表增加索引 idx_uses_extstock_real_jour(fund_account + init_date... |
| 2024-05-10 10:43:57 | 3.0.2.7 | 程猛 | 物理表uses_extstock_real_jour，添加了表字段(cancel_serial_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-09 13:41:33 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-04-17 11:13:42 | 3.0.2.65 | 於达 | 内存表uses_extstock_real_jour，添加了表字段(position_str);
 |
| 2024-12-11 15:23:28 | 3.0.2.52 | 谢宗艺 | 内存表uses_extstock_real_jour，添加了表字段(remark); |
| 2024-05-21 21:14:16 | 3.0.2.10 | 乐闽庭 | 内存表增加索引 idx_uses_extstock_real_jour(fund_account + init_date... |
| 2024-05-10 10:43:57 | 3.0.2.7 | 程猛 | 物理表uses_extstock_real_jour，添加了表字段(cancel_serial_no);
 |

> 共 16 条修改记录，仅显示最近15条

# uses_extstock_real - 证券股份交易信息扩展表

**表对象ID**: 5511
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | money_type | 否 |  |  |
| 8 | stock_type | 否 |  |  |
| 9 | available_amount | 否 |  |  |
| 10 | frozen_amount | 否 |  |  |
| 11 | unfrozen_amount | 否 |  |  |
| 12 | tradable_amount | 否 |  |  |
| 13 | trustee_seat_no | 否 |  |  |
| 14 | position_str | 否 |  | branch_no(5)+fund_account(18)+exchange_type(4)+stock_account |
| 15 | client_name | 否 | H |  |
| 16 | corp_client_group | 否 | H |  |
| 17 | branch_no | 否 | H |  |
| 18 | client_group | 否 | H |  |
| 19 | room_code | 否 | H |  |
| 20 | asset_prop | 否 | H |  |
| 21 | limit_flag | 否 | H |  |
| 22 | client_prop | 否 | H |  |
| 23 | asset_level | 否 | H |  |
| 24 | risk_level | 否 | H |  |
| 25 | corp_risk_level | 否 | H |  |
| 26 | stock_name | 否 | H |  |
| 27 | sub_stock_type | 否 | H |  |
| 28 | init_date | 否 |  |  |
| 29 | stock_account | 否 |  |  |
| 30 | stock_code | 否 |  |  |
| 31 | exchange_type | 否 |  |  |
| 32 | fund_account | 否 |  |  |
| 33 | client_id | 否 |  |  |
| 34 | money_type | 否 |  |  |
| 35 | stock_type | 否 |  |  |
| 36 | available_amount | 否 |  |  |
| 37 | frozen_amount | 否 |  |  |
| 38 | unfrozen_amount | 否 |  |  |
| 39 | tradable_amount | 否 |  |  |
| 40 | trustee_seat_no | 否 |  |  |
| 41 | position_str | 否 |  | branch_no(5)+fund_account(18)+exchange_type(4)+stock_account |
| 42 | client_name | 否 | H |  |
| 43 | corp_client_group | 否 | H |  |
| 44 | branch_no | 否 | H |  |
| 45 | client_group | 否 | H |  |
| 46 | room_code | 否 | H |  |
| 47 | asset_prop | 否 | H |  |
| 48 | limit_flag | 否 | H |  |
| 49 | client_prop | 否 | H |  |
| 50 | asset_level | 否 | H |  |
| 51 | risk_level | 否 | H |  |
| 52 | corp_risk_level | 否 | H |  |
| 53 | stock_name | 否 | H |  |
| 54 | sub_stock_type | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_extstock_real | ART | 是 | stock_account, stock_code, exchange_type, stock_account, stock_code, exchange_type |
| idx_uses_extstock_real_unique | ART | 是 | exchange_type, stock_account, fund_account, stock_code, trustee_seat_no, exchange_type, stock_account, fund_account, stock_code, trustee_seat_no |
| idx_uses_extstock_real_exch | ART | 是 | exchange_type, exchange_type |
| uk_rpt_usesextstockreal | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_usesextstockreal_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_uses_extstock_real | ART | 是 | stock_account, stock_code, exchange_type, stock_account, stock_code, exchange_type |
| idx_uses_extstock_real_unique | ART | 是 | exchange_type, stock_account, fund_account, stock_code, trustee_seat_no, exchange_type, stock_account, fund_account, stock_code, trustee_seat_no |
| idx_uses_extstock_real_exch | ART | 是 | exchange_type, exchange_type |
| uk_rpt_usesextstockreal | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_usesextstockreal_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_extstock_real | fund_account, stock_code, exchange_type, stock_account, trustee_seat_no, fund_account, stock_code, exchange_type, stock_account, trustee_seat_no |
| idx_uses_extstock_real | fund_account, stock_code, exchange_type, stock_account, trustee_seat_no, fund_account, stock_code, exchange_type, stock_account, trustee_seat_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:39:34 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-08-14 10:02:29 | 3.0.2.76 | 高志强 | 增加DB模式,避免写表失败 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-04-17 11:16:51 | 3.0.2.65 | 於达 | 内存表uses_extstock_real，添加了表字段(position_str);
 |
| 2024-04-28 17:02:51 | 3.0.2.3 | 阮善宏 | 物理表uses_extstock_real，删除了表字段(branch_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-09 13:39:34 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-08-14 10:02:29 | 3.0.2.76 | 高志强 | 增加DB模式,避免写表失败 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-04-17 11:16:51 | 3.0.2.65 | 於达 | 内存表uses_extstock_real，添加了表字段(position_str);
 |
| 2024-04-28 17:02:51 | 3.0.2.3 | 阮善宏 | 物理表uses_extstock_real，删除了表字段(branch_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

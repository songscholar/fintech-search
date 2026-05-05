# uqms_szreduction - 深圳减持信息表

**表对象ID**: 1607
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 68 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | trustee_seat_no | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | stock_total_amount | 否 |  |  |
| 7 | frozen_amount | 否 |  |  |
| 8 | stock_amount1 | 否 |  |  |
| 9 | stock_amount2 | 否 |  |  |
| 10 | stock_amount3 | 否 |  |  |
| 11 | stock_amount4 | 否 |  |  |
| 12 | stock_amount5 | 否 |  |  |
| 13 | stock_amount6 | 否 |  |  |
| 14 | stock_amount1_ex | 否 |  |  |
| 15 | stock_amount2_ex | 否 |  |  |
| 16 | stock_amount3_ex | 否 |  |  |
| 17 | stock_amount4_ex | 否 |  |  |
| 18 | begin_enable_quota | 否 |  |  |
| 19 | block_enable_quota | 否 |  |  |
| 20 | block_enable_quota1 | 否 |  |  |
| 21 | pre_used_quota | 否 |  |  |
| 22 | preblock_used_quota | 否 |  |  |
| 23 | prereduce_used_quota | 否 |  |  |
| 24 | used_quota | 否 |  |  |
| 25 | block_used_quota | 否 |  |  |
| 26 | reduce_used_quota | 否 |  |  |
| 27 | remark | 否 |  |  |
| 28 | company_no | 否 |  |  |
| 29 | stock_amount3_t | 否 |  |  |
| 30 | position_str | 否 |  | init_date(8)+company_no(4)+seat_no(6)+exchange_type(4)+stock |
| 31 | modify_date | 否 |  |  |
| 32 | stock_name | 否 | H |  |
| 33 | sub_stock_type | 否 | H |  |
| 34 | stock_type | 否 | H |  |
| 35 | init_date | 否 |  |  |
| 36 | exchange_type | 否 |  |  |
| 37 | stock_account | 否 |  |  |
| 38 | trustee_seat_no | 否 |  |  |
| 39 | stock_code | 否 |  |  |
| 40 | stock_total_amount | 否 |  |  |
| 41 | frozen_amount | 否 |  |  |
| 42 | stock_amount1 | 否 |  |  |
| 43 | stock_amount2 | 否 |  |  |
| 44 | stock_amount3 | 否 |  |  |
| 45 | stock_amount4 | 否 |  |  |
| 46 | stock_amount5 | 否 |  |  |
| 47 | stock_amount6 | 否 |  |  |
| 48 | stock_amount1_ex | 否 |  |  |
| 49 | stock_amount2_ex | 否 |  |  |
| 50 | stock_amount3_ex | 否 |  |  |
| 51 | stock_amount4_ex | 否 |  |  |
| 52 | begin_enable_quota | 否 |  |  |
| 53 | block_enable_quota | 否 |  |  |
| 54 | block_enable_quota1 | 否 |  |  |
| 55 | pre_used_quota | 否 |  |  |
| 56 | preblock_used_quota | 否 |  |  |
| 57 | prereduce_used_quota | 否 |  |  |
| 58 | used_quota | 否 |  |  |
| 59 | block_used_quota | 否 |  |  |
| 60 | reduce_used_quota | 否 |  |  |
| 61 | remark | 否 |  |  |
| 62 | company_no | 否 |  |  |
| 63 | stock_amount3_t | 否 |  |  |
| 64 | position_str | 否 |  | init_date(8)+company_no(4)+seat_no(6)+exchange_type(4)+stock |
| 65 | modify_date | 否 |  |  |
| 66 | stock_name | 否 | H |  |
| 67 | sub_stock_type | 否 | H |  |
| 68 | stock_type | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_qms_szreduction | ART | 是 | stock_account, stock_code, trustee_seat_no, exchange_type, company_no, stock_account, stock_code, trustee_seat_no, exchange_type, company_no |
| uk_rpt_uqmsszreduction | ART | 是 | init_date, position_str, init_date, position_str |
| uk_qms_szreduction | ART | 是 | stock_account, stock_code, trustee_seat_no, exchange_type, company_no, stock_account, stock_code, trustee_seat_no, exchange_type, company_no |
| uk_rpt_uqmsszreduction | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_qms_szreduction | stock_account, stock_code, trustee_seat_no, exchange_type, company_no, stock_account, stock_code, trustee_seat_no, exchange_type, company_no |
| idx_qms_szreduction | stock_account, stock_code, trustee_seat_no, exchange_type, company_no, stock_account, stock_code, trustee_seat_no, exchange_type, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:40:16 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-11-21 19:56:55 | V3.0.6.14 | 周兆军 | 维护历史表 |
| 2025-04-11 15:18:27 | 3.0.2.6 | 李江霖 | 修改物理表索引名 |
| 2024-12-27 14:28:13 | 3.0.2.5 | 李江霖 | 增加position_str的备注 |
| 2024-03-27 20:26:14 | 3.0.2.4 | 徐志坚 | 增加modify_date字段用于控制手工修改后不再被行情更新 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-05 16:40:16 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-11-21 19:56:55 | V3.0.6.14 | 周兆军 | 维护历史表 |
| 2025-04-11 15:18:27 | 3.0.2.6 | 李江霖 | 修改物理表索引名 |
| 2024-12-27 14:28:13 | 3.0.2.5 | 李江霖 | 增加position_str的备注 |
| 2024-03-27 20:26:14 | 3.0.2.4 | 徐志坚 | 增加modify_date字段用于控制手工修改后不再被行情更新 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

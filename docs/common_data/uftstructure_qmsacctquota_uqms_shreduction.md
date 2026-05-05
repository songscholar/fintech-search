# uqms_shreduction - 上海减持信息表

**表对象ID**: 1606
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 60 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | seat_no | 否 |  |  |
| 6 | cognizancestock_amount1 | 否 |  |  |
| 7 | cognizancestock_amount2 | 否 |  |  |
| 8 | reducectrl_amount | 否 |  |  |
| 9 | blockreducectrl_amount | 否 |  |  |
| 10 | surplusstock_amount | 否 |  |  |
| 11 | blockrecectrl_amount | 否 |  |  |
| 12 | frozen_amount | 否 |  |  |
| 13 | begin_enable_quota | 否 |  |  |
| 14 | block_enable_quota | 否 |  |  |
| 15 | pre_used_quota | 否 |  |  |
| 16 | prereduce_used_quota | 否 |  |  |
| 17 | used_quota | 否 |  |  |
| 18 | reduce_used_quota | 否 |  |  |
| 19 | remark | 否 |  |  |
| 20 | company_no | 否 |  |  |
| 21 | block_enable_quota1 | 否 |  |  |
| 22 | preblock_used_quota | 否 |  |  |
| 23 | block_used_quota | 否 |  |  |
| 24 | stock_circulate_amount | 否 |  |  |
| 25 | position_str | 否 |  | init_date(8)+company_no(4)+seat_no(6)+exchange_type(4)+stock |
| 26 | modify_date | 否 |  |  |
| 27 | sett_batch_no | 否 |  |  |
| 28 | stock_name | 否 | H |  |
| 29 | sub_stock_type | 否 | H |  |
| 30 | stock_type | 否 | H |  |
| 31 | init_date | 否 |  |  |
| 32 | exchange_type | 否 |  |  |
| 33 | stock_account | 否 |  |  |
| 34 | stock_code | 否 |  |  |
| 35 | seat_no | 否 |  |  |
| 36 | cognizancestock_amount1 | 否 |  |  |
| 37 | cognizancestock_amount2 | 否 |  |  |
| 38 | reducectrl_amount | 否 |  |  |
| 39 | blockreducectrl_amount | 否 |  |  |
| 40 | surplusstock_amount | 否 |  |  |
| 41 | blockrecectrl_amount | 否 |  |  |
| 42 | frozen_amount | 否 |  |  |
| 43 | begin_enable_quota | 否 |  |  |
| 44 | block_enable_quota | 否 |  |  |
| 45 | pre_used_quota | 否 |  |  |
| 46 | prereduce_used_quota | 否 |  |  |
| 47 | used_quota | 否 |  |  |
| 48 | reduce_used_quota | 否 |  |  |
| 49 | remark | 否 |  |  |
| 50 | company_no | 否 |  |  |
| 51 | block_enable_quota1 | 否 |  |  |
| 52 | preblock_used_quota | 否 |  |  |
| 53 | block_used_quota | 否 |  |  |
| 54 | stock_circulate_amount | 否 |  |  |
| 55 | position_str | 否 |  | init_date(8)+company_no(4)+seat_no(6)+exchange_type(4)+stock |
| 56 | modify_date | 否 |  |  |
| 57 | sett_batch_no | 否 |  |  |
| 58 | stock_name | 否 | H |  |
| 59 | sub_stock_type | 否 | H |  |
| 60 | stock_type | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_qms_shreduction | ART | 是 | stock_account, stock_code, exchange_type, company_no, seat_no, stock_account, stock_code, exchange_type, company_no, seat_no |
| uk_rpt_uqmsshreduction | ART | 是 | init_date, position_str, init_date, position_str |
| uk_qms_shreduction | ART | 是 | stock_account, stock_code, exchange_type, company_no, seat_no, stock_account, stock_code, exchange_type, company_no, seat_no |
| uk_rpt_uqmsshreduction | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_qms_shreduction | stock_account, stock_code, exchange_type, company_no, seat_no, stock_account, stock_code, exchange_type, company_no, seat_no |
| idx_qms_shreduction | stock_account, stock_code, exchange_type, company_no, seat_no, stock_account, stock_code, exchange_type, company_no, seat_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:39:39 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-11-21 19:56:55 | V3.0.6.14 | 周兆军 | 维护历史表 |
| 2025-11-17 13:49:22 | 3.0.2.7 | yangxz | 所有表uqms_shreduction，添加了表字段(sett_batch_no);
 |
| 2025-04-11 15:18:27 | 3.0.2.6 | 李江霖 | 修改物理表索引名 |
| 2024-12-27 14:28:13 | 3.0.2.5 | 李江霖 | 增加position_str的备注 |
| 2024-03-27 20:23:25 | 3.0.2.4 | 徐志坚 | 1、增加modify_date字段用于控制手工修改后不再被行情更新
2、在内存和物理索引中均增加seat_no字段，并... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-05 16:39:39 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-11-21 19:56:55 | V3.0.6.14 | 周兆军 | 维护历史表 |
| 2025-11-17 13:49:22 | 3.0.2.7 | yangxz | 所有表uqms_shreduction，添加了表字段(sett_batch_no);
 |
| 2025-04-11 15:18:27 | 3.0.2.6 | 李江霖 | 修改物理表索引名 |
| 2024-12-27 14:28:13 | 3.0.2.5 | 李江霖 | 增加position_str的备注 |
| 2024-03-27 20:23:25 | 3.0.2.4 | 徐志坚 | 1、增加modify_date字段用于控制手工修改后不再被行情更新
2、在内存和物理索引中均增加seat_no字段，并... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

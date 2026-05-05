# uqms_stbstock_detail - 全国股转证券余额信息表

**表对象ID**: 1605
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | seat_no | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | stock_property | 否 |  |  |
| 6 | current_amount | 否 |  |  |
| 7 | frozen_amount | 否 |  |  |
| 8 | ocpused_amount | 否 |  |  |
| 9 | sett_batch_no | 否 |  |  |
| 10 | tohis_date | 否 | H |  |
| 11 | exchange_type | 否 |  |  |
| 12 | seat_no | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | stock_account | 否 |  |  |
| 15 | stock_property | 否 |  |  |
| 16 | current_amount | 否 |  |  |
| 17 | frozen_amount | 否 |  |  |
| 18 | ocpused_amount | 否 |  |  |
| 19 | sett_batch_no | 否 |  |  |
| 20 | tohis_date | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_uqms_stbstock_detail | ART | 是 | exchange_type, seat_no, stock_code, stock_account, stock_property, exchange_type, seat_no, stock_code, stock_account, stock_property |
| rpt_uqms_stbstock_detail | ART | 是 | tohis_date, stock_account, stock_code, exchange_type, seat_no, stock_property, tohis_date, stock_account, stock_code, exchange_type, seat_no, stock_property |
| uk_uqms_stbstock_detail | ART | 是 | exchange_type, seat_no, stock_code, stock_account, stock_property, exchange_type, seat_no, stock_code, stock_account, stock_property |
| rpt_uqms_stbstock_detail | ART | 是 | tohis_date, stock_account, stock_code, exchange_type, seat_no, stock_property, tohis_date, stock_account, stock_code, exchange_type, seat_no, stock_property |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_stbstock_detail | exchange_type, seat_no, stock_code, stock_account, stock_property, exchange_type, seat_no, stock_code, stock_account, stock_property |
| idx_uqms_stbstock_detail | exchange_type, seat_no, stock_code, stock_account, stock_property, exchange_type, seat_no, stock_code, stock_account, stock_property |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:39:13 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-11-19 19:41:49 | 3.0.2.3 | 洪略 | 补齐资源 |
| 2025-11-17 13:47:35 | 3.0.2.2 | yangxz | 所有表uqms_stbstock_detail，添加了表字段(sett_batch_no);
 |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引名 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-05 16:39:13 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-11-19 19:41:49 | 3.0.2.3 | 洪略 | 补齐资源 |
| 2025-11-17 13:47:35 | 3.0.2.2 | yangxz | 所有表uqms_stbstock_detail，添加了表字段(sett_batch_no);
 |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引名 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

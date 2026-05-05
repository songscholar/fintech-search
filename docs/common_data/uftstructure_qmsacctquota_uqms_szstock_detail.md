# uqms_szstock_detail - 深圳证券余额信息表

**表对象ID**: 1604
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | trustee_seat_no | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | current_amount | 否 |  |  |
| 6 | stock_property | 否 |  |  |
| 7 | ocpused_amount | 否 |  |  |
| 8 | frozen_amount | 否 |  |  |
| 9 | sett_batch_no | 否 |  |  |
| 10 | tohis_date | 否 | H |  |
| 11 | exchange_type | 否 |  |  |
| 12 | trustee_seat_no | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | stock_account | 否 |  |  |
| 15 | current_amount | 否 |  |  |
| 16 | stock_property | 否 |  |  |
| 17 | ocpused_amount | 否 |  |  |
| 18 | frozen_amount | 否 |  |  |
| 19 | sett_batch_no | 否 |  |  |
| 20 | tohis_date | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_uqms_szstock_detail | ART | 是 | exchange_type, trustee_seat_no, stock_code, stock_account, stock_property, exchange_type, trustee_seat_no, stock_code, stock_account, stock_property |
| idx_szstock_detail_act | ART | 是 | stock_account, exchange_type, stock_code, trustee_seat_no, stock_account, exchange_type, stock_code, trustee_seat_no |
| uk_rpt_uqmsszstockdetail | ART | 是 | tohis_date, stock_account, stock_code, exchange_type, trustee_seat_no, stock_property, tohis_date, stock_account, stock_code, exchange_type, trustee_seat_no, stock_property |
| uk_uqms_szstock_detail | ART | 是 | exchange_type, trustee_seat_no, stock_code, stock_account, stock_property, exchange_type, trustee_seat_no, stock_code, stock_account, stock_property |
| idx_szstock_detail_act | ART | 是 | stock_account, exchange_type, stock_code, trustee_seat_no, stock_account, exchange_type, stock_code, trustee_seat_no |
| uk_rpt_uqmsszstockdetail | ART | 是 | tohis_date, stock_account, stock_code, exchange_type, trustee_seat_no, stock_property, tohis_date, stock_account, stock_code, exchange_type, trustee_seat_no, stock_property |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_szstock_detail | exchange_type, trustee_seat_no, stock_code, stock_account, stock_property, exchange_type, trustee_seat_no, stock_code, stock_account, stock_property |
| idx_uqms_szstock_detail | exchange_type, trustee_seat_no, stock_code, stock_account, stock_property, exchange_type, trustee_seat_no, stock_code, stock_account, stock_property |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:38:44 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-11-19 19:35:31 | 3.0.2.2 | 洪略 |  |
| 2025-11-17 13:46:40 | 3.0.2.2 | yangxz | 所有表uqms_szstock_detail，添加了表字段(sett_batch_no);
 |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引名 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-05 16:38:44 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-11-19 19:35:31 | 3.0.2.2 | 洪略 |  |
| 2025-11-17 13:46:40 | 3.0.2.2 | yangxz | 所有表uqms_szstock_detail，添加了表字段(sett_batch_no);
 |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引名 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

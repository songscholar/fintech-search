# uqms_shstock_detail - 上海证券余额信息表

**表对象ID**: 1603
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | pbu_clear_no | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | trustee_seat_no | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | shdc_stock_type | 否 |  |  |
| 7 | shdc_circulate_type | 否 |  |  |
| 8 | shdc_authority_type | 否 |  |  |
| 9 | shdc_market_year | 否 |  |  |
| 10 | total_amount | 否 |  |  |
| 11 | end_frozen_amount | 否 |  |  |
| 12 | shdc_by | 否 |  |  |
| 13 | shdc_end_date | 否 |  |  |
| 14 | ocpused_amount | 否 |  |  |
| 15 | sett_batch_no | 否 |  |  |
| 16 | tohis_date | 否 | H |  |
| 17 | exchange_type | 否 |  |  |
| 18 | pbu_clear_no | 否 |  |  |
| 19 | stock_account | 否 |  |  |
| 20 | trustee_seat_no | 否 |  |  |
| 21 | stock_code | 否 |  |  |
| 22 | shdc_stock_type | 否 |  |  |
| 23 | shdc_circulate_type | 否 |  |  |
| 24 | shdc_authority_type | 否 |  |  |
| 25 | shdc_market_year | 否 |  |  |
| 26 | total_amount | 否 |  |  |
| 27 | end_frozen_amount | 否 |  |  |
| 28 | shdc_by | 否 |  |  |
| 29 | shdc_end_date | 否 |  |  |
| 30 | ocpused_amount | 否 |  |  |
| 31 | sett_batch_no | 否 |  |  |
| 32 | tohis_date | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_uqms_shstock_detail | ART | 是 | exchange_type, stock_account, stock_code, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year, exchange_type, stock_account, stock_code, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year |
| idx_uqms_shstock_detail_part | ART | 是 | stock_account, exchange_type, stock_code, stock_account, exchange_type, stock_code |
| uk_rpt_uqmsshstockdetail | ART | 是 | tohis_date, exchange_type, stock_account, stock_code, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year, tohis_date, exchange_type, stock_account, stock_code, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year |
| uk_uqms_shstock_detail | ART | 是 | exchange_type, stock_account, stock_code, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year, exchange_type, stock_account, stock_code, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year |
| idx_uqms_shstock_detail_part | ART | 是 | stock_account, exchange_type, stock_code, stock_account, exchange_type, stock_code |
| uk_rpt_uqmsshstockdetail | ART | 是 | tohis_date, exchange_type, stock_account, stock_code, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year, tohis_date, exchange_type, stock_account, stock_code, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_shstock_detail | exchange_type, stock_account, stock_code, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year, exchange_type, stock_account, stock_code, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year |
| idx_uqms_shstock_detail | exchange_type, stock_account, stock_code, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year, exchange_type, stock_account, stock_code, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:38:20 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-11-19 19:18:07 | 3.0.2.2 | 洪略 | 补齐资源 |
| 2025-11-17 13:45:26 | 3.0.2.2 | yangxz | 所有表uqms_shstock_detail，添加了表字段(sett_batch_no);
 |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引名 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-05 16:38:20 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-11-19 19:18:07 | 3.0.2.2 | 洪略 | 补齐资源 |
| 2025-11-17 13:45:26 | 3.0.2.2 | yangxz | 所有表uqms_shstock_detail，添加了表字段(sett_batch_no);
 |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引名 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

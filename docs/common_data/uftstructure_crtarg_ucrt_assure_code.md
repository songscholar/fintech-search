# ucrt_assure_code - 担保证券信息表

**表对象ID**: 7020
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 72 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | assure_std_ratio | 否 |  |  |
| 5 | assure_ratio | 否 |  |  |
| 6 | circulate_amount | 否 |  |  |
| 7 | capital_amount | 否 |  |  |
| 8 | static_pe_ratio | 否 |  |  |
| 9 | fair_price | 否 |  |  |
| 10 | fair_price_flag | 否 |  |  |
| 11 | fair_ratio | 否 |  |  |
| 12 | end_date | 否 |  |  |
| 13 | assure_status | 否 |  |  |
| 14 | slo_sellbuy_status | 否 |  |  |
| 15 | allow_blocktrade_flag | 否 |  |  |
| 16 | ensurescale_value | 否 |  |  |
| 17 | init_ensurescale_value | 否 |  |  |
| 18 | stock_type | 否 |  |  |
| 19 | short_ensurescale_value | 否 |  |  |
| 20 | short_init_ensurescale_value | 否 |  |  |
| 21 | avg_business_balance_20 | 否 |  |  |
| 22 | transaction_no | 否 |  |  |
| 23 | collateral_ratio | 否 |  |  |
| 24 | collateral_pe_ratio | 否 |  |  |
| 25 | old_assure_ratio | 否 |  |  |
| 26 | upper_assure_hold_amount | 否 |  |  |
| 27 | modify_date | 否 |  |  |
| 28 | dyna_fair_price_flag | 否 |  |  |
| 29 | old_assure_std_ratio | 否 |  |  |
| 30 | transin_date | 否 |  |  |
| 31 | remark | 否 |  |  |
| 32 | modify_flag | 否 |  |  |
| 33 | update_date | 否 |  |  |
| 34 | update_time | 否 |  |  |
| 35 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 36 | tohis_date | 否 | H |  |
| 37 | init_date | 否 |  |  |
| 38 | exchange_type | 否 |  |  |
| 39 | stock_code | 否 |  |  |
| 40 | assure_std_ratio | 否 |  |  |
| 41 | assure_ratio | 否 |  |  |
| 42 | circulate_amount | 否 |  |  |
| 43 | capital_amount | 否 |  |  |
| 44 | static_pe_ratio | 否 |  |  |
| 45 | fair_price | 否 |  |  |
| 46 | fair_price_flag | 否 |  |  |
| 47 | fair_ratio | 否 |  |  |
| 48 | end_date | 否 |  |  |
| 49 | assure_status | 否 |  |  |
| 50 | slo_sellbuy_status | 否 |  |  |
| 51 | allow_blocktrade_flag | 否 |  |  |
| 52 | ensurescale_value | 否 |  |  |
| 53 | init_ensurescale_value | 否 |  |  |
| 54 | stock_type | 否 |  |  |
| 55 | short_ensurescale_value | 否 |  |  |
| 56 | short_init_ensurescale_value | 否 |  |  |
| 57 | avg_business_balance_20 | 否 |  |  |
| 58 | transaction_no | 否 |  |  |
| 59 | collateral_ratio | 否 |  |  |
| 60 | collateral_pe_ratio | 否 |  |  |
| 61 | old_assure_ratio | 否 |  |  |
| 62 | upper_assure_hold_amount | 否 |  |  |
| 63 | modify_date | 否 |  |  |
| 64 | dyna_fair_price_flag | 否 |  |  |
| 65 | old_assure_std_ratio | 否 |  |  |
| 66 | transin_date | 否 |  |  |
| 67 | remark | 否 |  |  |
| 68 | modify_flag | 否 |  |  |
| 69 | update_date | 否 |  |  |
| 70 | update_time | 否 |  |  |
| 71 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 72 | tohis_date | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_assure_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| uk_rpt_ucrtassurecode | ART | 是 | tohis_date, position_str, tohis_date, position_str |
| idx_ucrt_assure_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| uk_rpt_ucrtassurecode | ART | 是 | tohis_date, position_str, tohis_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_assure_code | stock_code, exchange_type, stock_code, exchange_type |
| idx_ucrt_assure_code | stock_code, exchange_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-02-17 19:52:09 | 3.0.6.54 | 李想 | 物理表ucrt_assure_code，添加了表字段(dyna_fair_price_flag);
物理表ucrt_a... |
| 2025-01-08 15:23:54 | 3.0.6.29 | 沈勋 | 物理表ucrt_assure_code，添加了表字段(modify_date);
 |
| 2024-03-20 11:21:30 | 3.0.2.6 | 楼欣欣 | 物理表ucrt_assure_code，添加了表字段(old_assure_ratio);
 |
| 2023-09-27 18:18:23 | 3.0.1.5 | 吴丽丽 | 物理表ucrt_assure_code，添加了表字段(collateral_ratio);
物理表ucrt_assur... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:20 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-02-17 19:52:09 | 3.0.6.54 | 李想 | 物理表ucrt_assure_code，添加了表字段(dyna_fair_price_flag);
物理表ucrt_a... |
| 2025-01-08 15:23:54 | 3.0.6.29 | 沈勋 | 物理表ucrt_assure_code，添加了表字段(modify_date);
 |
| 2024-03-20 11:21:30 | 3.0.2.6 | 楼欣欣 | 物理表ucrt_assure_code，添加了表字段(old_assure_ratio);
 |
| 2023-09-27 18:18:23 | 3.0.1.5 | 吴丽丽 | 物理表ucrt_assure_code，添加了表字段(collateral_ratio);
物理表ucrt_assur... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:20 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |

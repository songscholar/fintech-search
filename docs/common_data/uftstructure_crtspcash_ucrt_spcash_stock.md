# ucrt_spcash_stock - 客户专项头寸股份表

**表对象ID**: 8003
**所属模块**: crtspcash
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | cashgroup_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | slo_total_amount | 否 |  |  |
| 6 | slo_used_amount | 否 |  |  |
| 7 | ref_due_amount | 否 |  |  |
| 8 | enable_amount | 否 |  |  |
| 9 | frozen_amount | 否 |  |  |
| 10 | surstock_amount | 否 |  |  |
| 11 | real_buy_amount | 否 |  |  |
| 12 | sloreturn_business_amount | 否 |  |  |
| 13 | tohis_date | 否 | H |  |
| 14 | stock_name | 否 | H |  |
| 15 | sub_stock_type | 否 | H |  |
| 16 | cashgroup_no | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | stock_type | 否 |  |  |
| 20 | slo_total_amount | 否 |  |  |
| 21 | slo_used_amount | 否 |  |  |
| 22 | ref_due_amount | 否 |  |  |
| 23 | enable_amount | 否 |  |  |
| 24 | frozen_amount | 否 |  |  |
| 25 | surstock_amount | 否 |  |  |
| 26 | real_buy_amount | 否 |  |  |
| 27 | sloreturn_business_amount | 否 |  |  |
| 28 | tohis_date | 否 | H |  |
| 29 | stock_name | 否 | H |  |
| 30 | sub_stock_type | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_spcash_stock_unique | ART | 是 | cashgroup_no, exchange_type, stock_code, cashgroup_no, exchange_type, stock_code |
| uk_rpt_ucrtspcashstock | ART | 是 | tohis_date, cashgroup_no, stock_code, exchange_type, tohis_date, cashgroup_no, stock_code, exchange_type |
| idx_ucrt_spcash_stock_unique | ART | 是 | cashgroup_no, exchange_type, stock_code, cashgroup_no, exchange_type, stock_code |
| uk_rpt_ucrtspcashstock | ART | 是 | tohis_date, cashgroup_no, stock_code, exchange_type, tohis_date, cashgroup_no, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_spcash_stock_unique | cashgroup_no, exchange_type, stock_code, cashgroup_no, exchange_type, stock_code |
| idx_ucrt_spcash_stock_unique | cashgroup_no, exchange_type, stock_code, cashgroup_no, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-10-15 09:58:47 | 3.0.6.5 | 牟家乐 | 物理表ucrt_spcash_stock，添加了表字段(sloreturn_business_amount);
 |
| 2023-08-21 17:46:44 | 0.3.3.140 | 程猛 | ucrt_spcash_stockjour重命名为ucrt_spcash_stock_jour |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2024-10-15 09:58:47 | 3.0.6.5 | 牟家乐 | 物理表ucrt_spcash_stock，添加了表字段(sloreturn_business_amount);
 |
| 2023-08-21 17:46:44 | 0.3.3.140 | 程猛 | ucrt_spcash_stockjour重命名为ucrt_spcash_stock_jour |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

# inco_unfin_info_ext - 固收未结算扩展信息表

**表对象ID**: 2346
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | income_busi_type | 否 |  |  |
| 3 | business_date | 否 |  |  |
| 4 | cbp_business_id | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | impawn_amount | 否 |  |  |
| 8 | stock_account | 否 |  |  |
| 9 | current_assure_value | 否 |  |  |
| 10 | remark | 否 |  |  |
| 11 | stock_name | 否 | H |  |
| 12 | stock_type | 否 | H |  |
| 13 | sub_stock_type | 否 | H |  |
| 14 | init_date | 否 |  |  |
| 15 | income_busi_type | 否 |  |  |
| 16 | business_date | 否 |  |  |
| 17 | cbp_business_id | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | stock_code | 否 |  |  |
| 20 | impawn_amount | 否 |  |  |
| 21 | stock_account | 否 |  |  |
| 22 | current_assure_value | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | stock_name | 否 | H |  |
| 25 | stock_type | 否 | H |  |
| 26 | sub_stock_type | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_incounfininfoext | 默认 | 否 |  |
| idx_incounfininfoext | ART | 是 | init_date, business_date, income_busi_type, cbp_business_id, exchange_type, stock_code, init_date, business_date, income_busi_type, cbp_business_id, exchange_type, stock_code |
| uk_rpt_incounfininfoext | ART | 是 | init_date, business_date, income_busi_type, cbp_business_id, exchange_type, stock_code, init_date, business_date, income_busi_type, cbp_business_id, exchange_type, stock_code |
| idx_incounfininfoext | 默认 | 否 |  |
| idx_incounfininfoext | ART | 是 | init_date, business_date, income_busi_type, cbp_business_id, exchange_type, stock_code, init_date, business_date, income_busi_type, cbp_business_id, exchange_type, stock_code |
| uk_rpt_incounfininfoext | ART | 是 | init_date, business_date, income_busi_type, cbp_business_id, exchange_type, stock_code, init_date, business_date, income_busi_type, cbp_business_id, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_incounfininfoext | init_date, business_date, income_busi_type, cbp_business_id, exchange_type, stock_code, init_date, business_date, income_busi_type, cbp_business_id, exchange_type, stock_code |
| idx_incounfininfoext | init_date, business_date, income_busi_type, cbp_business_id, exchange_type, stock_code, init_date, business_date, income_busi_type, cbp_business_id, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:35:06 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-11-17 15:07:04 | 8.26.2.93 |  | 所有表inco_unfin_info_ext，修改了表字段类型（cbp_business_id）；
 |
| 2024-09-23 15:40:23 | V3.0.2.1007 | 张明月 | 新增 |
| 2026-03-04 15:35:06 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-11-17 15:07:04 | 8.26.2.93 |  | 所有表inco_unfin_info_ext，修改了表字段类型（cbp_business_id）；
 |
| 2024-09-23 15:40:23 | V3.0.2.1007 | 张明月 | 新增 |

# assure_code_cp - 担保证券信息备份表

**表对象ID**: 7103
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 64 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | assure_ratio | 否 |  |  |
| 5 | assure_std_ratio | 否 |  |  |
| 6 | circulate_amount | 否 |  |  |
| 7 | capital_amount | 否 |  |  |
| 8 | upper_assure_hold_amount | 否 |  |  |
| 9 | fair_price | 否 |  |  |
| 10 | fair_price_flag | 否 |  |  |
| 11 | fair_ratio | 否 |  |  |
| 12 | end_date | 否 |  |  |
| 13 | assure_status | 否 |  |  |
| 14 | modify_date | 否 |  |  |
| 15 | remark | 否 |  |  |
| 16 | slo_sellbuy_status | 否 |  |  |
| 17 | old_assure_ratio | 否 |  |  |
| 18 | old_assure_std_ratio | 否 |  |  |
| 19 | static_pe_ratio | 否 |  |  |
| 20 | ensurescale_value | 否 |  |  |
| 21 | init_ensurescale_value | 否 |  |  |
| 22 | allow_blocktrade_flag | 否 |  |  |
| 23 | short_ensurescale_value | 否 |  |  |
| 24 | short_init_ensurescale_value | 否 |  |  |
| 25 | dyna_fair_price_flag | 否 |  |  |
| 26 | avg_business_balance_20 | 否 |  |  |
| 27 | transin_date | 否 |  |  |
| 28 | collateral_ratio | 否 |  |  |
| 29 | collateral_pe_ratio | 否 |  |  |
| 30 | modify_flag | 否 |  |  |
| 31 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 32 | stock_type | 是 |  |  |
| 33 | init_date | 否 |  |  |
| 34 | exchange_type | 否 |  |  |
| 35 | stock_code | 否 |  |  |
| 36 | assure_ratio | 否 |  |  |
| 37 | assure_std_ratio | 否 |  |  |
| 38 | circulate_amount | 否 |  |  |
| 39 | capital_amount | 否 |  |  |
| 40 | upper_assure_hold_amount | 否 |  |  |
| 41 | fair_price | 否 |  |  |
| 42 | fair_price_flag | 否 |  |  |
| 43 | fair_ratio | 否 |  |  |
| 44 | end_date | 否 |  |  |
| 45 | assure_status | 否 |  |  |
| 46 | modify_date | 否 |  |  |
| 47 | remark | 否 |  |  |
| 48 | slo_sellbuy_status | 否 |  |  |
| 49 | old_assure_ratio | 否 |  |  |
| 50 | old_assure_std_ratio | 否 |  |  |
| 51 | static_pe_ratio | 否 |  |  |
| 52 | ensurescale_value | 否 |  |  |
| 53 | init_ensurescale_value | 否 |  |  |
| 54 | allow_blocktrade_flag | 否 |  |  |
| 55 | short_ensurescale_value | 否 |  |  |
| 56 | short_init_ensurescale_value | 否 |  |  |
| 57 | dyna_fair_price_flag | 否 |  |  |
| 58 | avg_business_balance_20 | 否 |  |  |
| 59 | transin_date | 否 |  |  |
| 60 | collateral_ratio | 否 |  |  |
| 61 | collateral_pe_ratio | 否 |  |  |
| 62 | modify_flag | 否 |  |  |
| 63 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 64 | stock_type | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_assure_code_cp | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_assure_code_cp | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_assure_code_cp | stock_code, exchange_type, stock_code, exchange_type |
| idx_assure_code_cp | stock_code, exchange_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-06 21:14:06 | 3.0.6.1065 | tongck4118 | 所有表assure_code_cp，添加了表字段(stock_type);
 |
| 2025-02-19 11:05:08 | 3.0.6.89 | 李想 | 新增表 |
| 2025-09-06 21:14:06 | 3.0.6.1065 | tongck4118 | 所有表assure_code_cp，添加了表字段(stock_type);
 |
| 2025-02-19 11:05:08 | 3.0.6.89 | 李想 | 新增表 |

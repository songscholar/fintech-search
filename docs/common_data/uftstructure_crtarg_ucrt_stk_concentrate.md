# ucrt_stk_concentrate - 证券集中度控制表

**表对象ID**: 7026
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | assurescale_value | 否 |  |  |
| 6 | stock_conc_ratio | 否 |  |  |
| 7 | end_date | 否 |  |  |
| 8 | conc_ratio_type | 否 |  |  |
| 9 | market_forward_date_type | 否 |  |  |
| 10 | stockgroup_no | 否 |  |  |
| 11 | organ_flag | 否 |  |  |
| 12 | registration_flag | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | collateral_flag | 否 |  |  |
| 15 | ratio_package_kind | 否 |  |  |
| 16 | followdate_flag | 否 |  |  |
| 17 | remark | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | position_str | 否 |  | conc_ratio_type(1)+company_no(4)+ratio_package_kind(10)+orga |
| 21 | company_no | 否 |  |  |
| 22 | exchange_type | 否 |  |  |
| 23 | stock_code | 否 |  |  |
| 24 | stock_type | 否 |  |  |
| 25 | assurescale_value | 否 |  |  |
| 26 | stock_conc_ratio | 否 |  |  |
| 27 | end_date | 否 |  |  |
| 28 | conc_ratio_type | 否 |  |  |
| 29 | market_forward_date_type | 否 |  |  |
| 30 | stockgroup_no | 否 |  |  |
| 31 | organ_flag | 否 |  |  |
| 32 | registration_flag | 否 |  |  |
| 33 | transaction_no | 否 |  |  |
| 34 | collateral_flag | 否 |  |  |
| 35 | ratio_package_kind | 否 |  |  |
| 36 | followdate_flag | 否 |  |  |
| 37 | remark | 否 |  |  |
| 38 | update_date | 否 |  |  |
| 39 | update_time | 否 |  |  |
| 40 | position_str | 否 |  | conc_ratio_type(1)+company_no(4)+ratio_package_kind(10)+orga |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_stk_concentrate | 默认 | 否 |  |
| idx_ucrt_stk_concentrate | 默认 | 否 | conc_ratio_type, company_no, ratio_package_kind, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value, collateral_flag, followdate_flag, conc_ratio_type, company_no, ratio_package_kind, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value, collateral_flag, followdate_flag |
| idx_ucrt_stk_concentrate | 默认 | 否 | ratio_package_kind, ratio_package_kind |
| idx_ucrt_stk_concentrate | 默认 | 否 | collateral_flag, collateral_flag |
| idx_ucrt_stk_concentrate | ART | 是 | conc_ratio_type, company_no, ratio_package_kind, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value, collateral_flag, followdate_flag, conc_ratio_type, company_no, ratio_package_kind, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value, collateral_flag, followdate_flag |
| idx_ucrt_stk_concentrate_flag | ART | 是 | conc_ratio_type, company_no, ratio_package_kind, organ_flag, market_forward_date_type, assurescale_value, stock_conc_ratio, conc_ratio_type, company_no, ratio_package_kind, organ_flag, market_forward_date_type, assurescale_value, stock_conc_ratio |
| idx_ucrt_stk_concentrate | 默认 | 否 |  |
| idx_ucrt_stk_concentrate | 默认 | 否 | conc_ratio_type, company_no, ratio_package_kind, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value, collateral_flag, followdate_flag, conc_ratio_type, company_no, ratio_package_kind, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value, collateral_flag, followdate_flag |
| idx_ucrt_stk_concentrate | 默认 | 否 | ratio_package_kind, ratio_package_kind |
| idx_ucrt_stk_concentrate | 默认 | 否 | collateral_flag, collateral_flag |
| idx_ucrt_stk_concentrate | ART | 是 | conc_ratio_type, company_no, ratio_package_kind, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value, collateral_flag, followdate_flag, conc_ratio_type, company_no, ratio_package_kind, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value, collateral_flag, followdate_flag |
| idx_ucrt_stk_concentrate_flag | ART | 是 | conc_ratio_type, company_no, ratio_package_kind, organ_flag, market_forward_date_type, assurescale_value, stock_conc_ratio, conc_ratio_type, company_no, ratio_package_kind, organ_flag, market_forward_date_type, assurescale_value, stock_conc_ratio |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_stk_concentrate | conc_ratio_type, company_no, ratio_package_kind, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value, collateral_flag, followdate_flag, conc_ratio_type, company_no, ratio_package_kind, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value, collateral_flag, followdate_flag |
| idx_ucrt_stk_concentrate | conc_ratio_type, company_no, ratio_package_kind, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value, collateral_flag, followdate_flag, conc_ratio_type, company_no, ratio_package_kind, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value, collateral_flag, followdate_flag |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-19 17:20:22 | 3.0.6.118 | 常行 | 当前表ucrt_stk_concentrate，修改了索引idx_ucrt_stk_concentrate,索引字段修改... |
| 2025-08-19 16:25:39 | 3.0.6.118 | 常行 | 当前表ucrt_stk_concentrate，修改了索引idx_ucrt_stk_concentrate,索引字段修改... |
| 2025-02-18 10:15:05 | 3.0.6.69 | 李想 | 物理表ucrt_stk_concentrate，添加了表字段(followdate_flag);
物理表ucrt_st... |
| 2024-12-24 10:59:52 | 3.0.6.23 | 沈勋 | 物理表ucrt_stk_concentrate，增加索引字段(索引idx_ucrt_stk_concentrate:增加... |
| 2024-12-24 10:59:33 | 3.0.6.23 | 沈勋 | 物理表ucrt_stk_concentrate，添加了表字段(ratio_package_kind);
 |
| 2024-07-10 09:15:19 | 3.0.3.3 | 徐志坚 | 为了提升性能，将两个索引都改为分级索引 |
| 2023-09-27 10:37:29 | 3.0.1.3 | 吴丽丽 | 物理表ucrt_stk_concentrate，增加索引字段(索引idx_ucrt_stk_concentrate:增加... |
| 2023-09-27 10:35:15 | 3.0.1.3 | 吴丽丽 | 物理表ucrt_stk_concentrate，添加了表字段(collateral_flag);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:09 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2025-08-19 17:20:22 | 3.0.6.118 | 常行 | 当前表ucrt_stk_concentrate，修改了索引idx_ucrt_stk_concentrate,索引字段修改... |
| 2025-08-19 16:25:39 | 3.0.6.118 | 常行 | 当前表ucrt_stk_concentrate，修改了索引idx_ucrt_stk_concentrate,索引字段修改... |
| 2025-02-18 10:15:05 | 3.0.6.69 | 李想 | 物理表ucrt_stk_concentrate，添加了表字段(followdate_flag);
物理表ucrt_st... |
| 2024-12-24 10:59:52 | 3.0.6.23 | 沈勋 | 物理表ucrt_stk_concentrate，增加索引字段(索引idx_ucrt_stk_concentrate:增加... |
| 2024-12-24 10:59:33 | 3.0.6.23 | 沈勋 | 物理表ucrt_stk_concentrate，添加了表字段(ratio_package_kind);
 |

> 共 20 条修改记录，仅显示最近15条

# ucrt_stk_group_concentrate - 证券分组集中度控制表

**表对象ID**: 7029
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stockgroup_no | 否 |  |  |
| 2 | stock_type | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | assurescale_value | 否 |  |  |
| 5 | groupconcentratio | 否 |  |  |
| 6 | conc_ratio_type | 否 |  |  |
| 7 | end_date | 否 |  |  |
| 8 | market_forward_date_type | 否 |  |  |
| 9 | organ_flag | 否 |  |  |
| 10 | registration_flag | 否 |  |  |
| 11 | stockgroup_name | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | groupratio_package_kind | 否 |  |  |
| 14 | followdate_flag | 否 |  |  |
| 15 | remark | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | position_str | 否 |  | stockgroup_no(10)+conc_ratio_type(1)+stock_type(4)+market_fo |
| 19 | stockgroup_no | 否 |  |  |
| 20 | stock_type | 否 |  |  |
| 21 | fund_account | 否 |  |  |
| 22 | assurescale_value | 否 |  |  |
| 23 | groupconcentratio | 否 |  |  |
| 24 | conc_ratio_type | 否 |  |  |
| 25 | end_date | 否 |  |  |
| 26 | market_forward_date_type | 否 |  |  |
| 27 | organ_flag | 否 |  |  |
| 28 | registration_flag | 否 |  |  |
| 29 | stockgroup_name | 否 |  |  |
| 30 | transaction_no | 否 |  |  |
| 31 | groupratio_package_kind | 否 |  |  |
| 32 | followdate_flag | 否 |  |  |
| 33 | remark | 否 |  |  |
| 34 | update_date | 否 |  |  |
| 35 | update_time | 否 |  |  |
| 36 | position_str | 否 |  | stockgroup_no(10)+conc_ratio_type(1)+stock_type(4)+market_fo |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_stk_group_concentrate | 默认 | 否 | groupratio_package_kind, groupratio_package_kind |
| idx_crdtgroupconc_stockgroupno | ART | 是 | stockgroup_no, stockgroup_no |
| idx_ucrt_stk_group_concentrate | ART | 是 | conc_ratio_type, groupratio_package_kind, stockgroup_no, stock_type, market_forward_date_type, registration_flag, fund_account, organ_flag, assurescale_value, groupconcentratio, conc_ratio_type, groupratio_package_kind, stockgroup_no, stock_type, market_forward_date_type, registration_flag, fund_account, organ_flag, assurescale_value, groupconcentratio |
| idx_ucrt_stk_group_concentrate_account | ART | 是 | fund_account, conc_ratio_type, groupratio_package_kind, stockgroup_no, stock_type, market_forward_date_type, registration_flag, organ_flag, assurescale_value, groupconcentratio, fund_account, conc_ratio_type, groupratio_package_kind, stockgroup_no, stock_type, market_forward_date_type, registration_flag, organ_flag, assurescale_value, groupconcentratio |
| idx_ucrt_stk_group_concentrate_type | ART | 是 | conc_ratio_type, stockgroup_no, stock_type, market_forward_date_type, registration_flag, fund_account, groupratio_package_kind, organ_flag, assurescale_value, groupconcentratio, conc_ratio_type, stockgroup_no, stock_type, market_forward_date_type, registration_flag, fund_account, groupratio_package_kind, organ_flag, assurescale_value, groupconcentratio |
| idx_ucrt_stk_group_concentrate | 默认 | 否 | groupratio_package_kind, groupratio_package_kind |
| idx_crdtgroupconc_stockgroupno | ART | 是 | stockgroup_no, stockgroup_no |
| idx_ucrt_stk_group_concentrate | ART | 是 | conc_ratio_type, groupratio_package_kind, stockgroup_no, stock_type, market_forward_date_type, registration_flag, fund_account, organ_flag, assurescale_value, groupconcentratio, conc_ratio_type, groupratio_package_kind, stockgroup_no, stock_type, market_forward_date_type, registration_flag, fund_account, organ_flag, assurescale_value, groupconcentratio |
| idx_ucrt_stk_group_concentrate_account | ART | 是 | fund_account, conc_ratio_type, groupratio_package_kind, stockgroup_no, stock_type, market_forward_date_type, registration_flag, organ_flag, assurescale_value, groupconcentratio, fund_account, conc_ratio_type, groupratio_package_kind, stockgroup_no, stock_type, market_forward_date_type, registration_flag, organ_flag, assurescale_value, groupconcentratio |
| idx_ucrt_stk_group_concentrate_type | ART | 是 | conc_ratio_type, stockgroup_no, stock_type, market_forward_date_type, registration_flag, fund_account, groupratio_package_kind, organ_flag, assurescale_value, groupconcentratio, conc_ratio_type, stockgroup_no, stock_type, market_forward_date_type, registration_flag, fund_account, groupratio_package_kind, organ_flag, assurescale_value, groupconcentratio |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_stk_group_concentrate | stockgroup_no, conc_ratio_type, stock_type, market_forward_date_type, registration_flag, fund_account, groupratio_package_kind, organ_flag, assurescale_value, groupconcentratio, stockgroup_no, conc_ratio_type, stock_type, market_forward_date_type, registration_flag, fund_account, groupratio_package_kind, organ_flag, assurescale_value, groupconcentratio |
| idx_ucrt_stk_group_concentrate | stockgroup_no, conc_ratio_type, stock_type, market_forward_date_type, registration_flag, fund_account, groupratio_package_kind, organ_flag, assurescale_value, groupconcentratio, stockgroup_no, conc_ratio_type, stock_type, market_forward_date_type, registration_flag, fund_account, groupratio_package_kind, organ_flag, assurescale_value, groupconcentratio |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-20 11:09:51 | 3.0.6.1076 | 沈勋 | 调整索引中的stockgroup_no字段排序，由升序改为降序 |
| 2025-02-18 10:41:54 | 3.0.6.73 | 李想 | 物理表ucrt_stk_group_concentrate，添加了表字段(followdate_flag);
物理表u... |
| 2025-02-18 14:49:05 | 3.0.6.39 | 沈勋 | 修改内存索引idx_ucrt_stk_group_concentrate_type，调整字段升降序 |
| 2025-02-18 14:49:05 | 3.0.6.39 | 沈勋 | 修改内存索引idx_ucrt_stk_group_concentrate_type，调整字段升降序 |
| 2025-01-22 10:46:13 | 3.0.6.32 | 沈勋 | 新增内存索引idx_ucrt_stk_group_concentrate_type |
| 2024-12-24 11:06:18 | 3.0.6.23 | 沈勋 | 物理表ucrt_stk_group_concentrate，增加索引字段(索引idx_ucrt_stk_group_co... |
| 2024-12-24 11:06:06 | 3.0.6.23 | 沈勋 | 物理表ucrt_stk_group_concentrate，添加了表字段(groupratio_package_kind... |
| 2024-07-10 09:30:45 | 3.0.3.3 | 徐志坚 | 将idx_ucrt_stk_group_concentrate改为分级索引，并增加分级索引idx_ucrt_stk_gr... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-07-05 09:43 | 0.3.3.123 | 程猛 | ucrt_stk_group、ucrt_stk_group_concentrate取消N:N的关联关系 |
| 2023-06-30 09:06 | 0.3.3.119 | 吴威 | 删除删除索引 |
| 2023-06-29 20:36 | 0.3.3.116 | 吴威 | 新增删除索引 |
| 2023-06-13 15:22 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no |
| 2026-03-20 11:09:51 | 3.0.6.1076 | 沈勋 | 调整索引中的stockgroup_no字段排序，由升序改为降序 |
| 2025-02-18 10:41:54 | 3.0.6.73 | 李想 | 物理表ucrt_stk_group_concentrate，添加了表字段(followdate_flag);
物理表u... |

> 共 26 条修改记录，仅显示最近15条

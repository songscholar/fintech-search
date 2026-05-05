# ucrt_stk_group_concwhite - 证券分组集中度白名单表

**表对象ID**: 7003
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | stockgroup_no | 否 |  |  |
| 3 | stockgroup_name | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | conc_ratio_type | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | groupratio_package_kind | 否 |  |  |
| 10 | remark | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | position_str | 否 |  | stockgroup_no(10)+stock_code(8)+exchange_type(4)+fund_accoun |
| 14 | fund_account | 否 |  |  |
| 15 | stockgroup_no | 否 |  |  |
| 16 | stockgroup_name | 否 |  |  |
| 17 | stock_type | 否 |  |  |
| 18 | conc_ratio_type | 否 |  |  |
| 19 | stock_code | 否 |  |  |
| 20 | exchange_type | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | groupratio_package_kind | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | position_str | 否 |  | stockgroup_no(10)+stock_code(8)+exchange_type(4)+fund_accoun |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_stk_group_concwhite | 默认 | 否 | groupratio_package_kind, groupratio_package_kind |
| idx_ucrt_stk_group_concwhite | ART | 是 | stockgroup_no, stock_code, exchange_type, fund_account, groupratio_package_kind, stock_type, conc_ratio_type, stockgroup_no, stock_code, exchange_type, fund_account, groupratio_package_kind, stock_type, conc_ratio_type |
| idx_ucrt_stk_group_concwhite | 默认 | 否 | groupratio_package_kind, groupratio_package_kind |
| idx_ucrt_stk_group_concwhite | ART | 是 | stockgroup_no, stock_code, exchange_type, fund_account, groupratio_package_kind, stock_type, conc_ratio_type, stockgroup_no, stock_code, exchange_type, fund_account, groupratio_package_kind, stock_type, conc_ratio_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_stk_group_concwhite | stockgroup_no, stock_code, exchange_type, fund_account, groupratio_package_kind, stock_type, conc_ratio_type, stockgroup_no, stock_code, exchange_type, fund_account, groupratio_package_kind, stock_type, conc_ratio_type |
| idx_ucrt_stk_group_concwhite | stockgroup_no, stock_code, exchange_type, fund_account, groupratio_package_kind, stock_type, conc_ratio_type, stockgroup_no, stock_code, exchange_type, fund_account, groupratio_package_kind, stock_type, conc_ratio_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 11:06:01 | 3.0.6.75 | 李想 | 物理表ucrt_stk_group_concwhite，添加了表字段(remark);
物理表ucrt_stk_gro... |
| 2024-12-24 10:53:11 | 3.0.6.23 | 沈勋 | 物理表ucrt_stk_group_concwhite，增加索引字段(索引idx_ucrt_stk_group_conc... |
| 2024-12-24 10:52:37 | 3.0.6.23 | 沈勋 | 物理表ucrt_stk_group_concwhite，添加了表字段(groupratio_package_kind);... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:23 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no |
| 2025-02-18 11:06:01 | 3.0.6.75 | 李想 | 物理表ucrt_stk_group_concwhite，添加了表字段(remark);
物理表ucrt_stk_gro... |
| 2024-12-24 10:53:11 | 3.0.6.23 | 沈勋 | 物理表ucrt_stk_group_concwhite，增加索引字段(索引idx_ucrt_stk_group_conc... |
| 2024-12-24 10:52:37 | 3.0.6.23 | 沈勋 | 物理表ucrt_stk_group_concwhite，添加了表字段(groupratio_package_kind);... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:23 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no |

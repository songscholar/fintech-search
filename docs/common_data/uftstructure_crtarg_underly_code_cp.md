# underly_code_cp - 标的证券信息备份表

**表对象ID**: 7104
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 48 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | fin_ratio | 否 |  |  |
| 5 | fin_std_ratio | 否 |  |  |
| 6 | fin_status | 否 |  |  |
| 7 | fin_end_date | 否 |  |  |
| 8 | slo_ratio | 否 |  |  |
| 9 | slo_std_ratio | 否 |  |  |
| 10 | slo_end_date | 否 |  |  |
| 11 | slo_status | 否 |  |  |
| 12 | slo_lack_flag | 否 |  |  |
| 13 | slo_pricelim_flag | 否 |  |  |
| 14 | modify_date | 否 |  |  |
| 15 | remark | 否 |  |  |
| 16 | fin_max_balance | 否 |  |  |
| 17 | slo_compact_end_date | 否 |  |  |
| 18 | last_day_slo_balance | 否 |  |  |
| 19 | last_day_fin_balance | 否 |  |  |
| 20 | last_day_slo_amount | 否 |  |  |
| 21 | transin_date | 否 |  |  |
| 22 | modify_flag | 否 |  |  |
| 23 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 24 | stock_type | 是 |  |  |
| 25 | init_date | 否 |  |  |
| 26 | exchange_type | 否 |  |  |
| 27 | stock_code | 否 |  |  |
| 28 | fin_ratio | 否 |  |  |
| 29 | fin_std_ratio | 否 |  |  |
| 30 | fin_status | 否 |  |  |
| 31 | fin_end_date | 否 |  |  |
| 32 | slo_ratio | 否 |  |  |
| 33 | slo_std_ratio | 否 |  |  |
| 34 | slo_end_date | 否 |  |  |
| 35 | slo_status | 否 |  |  |
| 36 | slo_lack_flag | 否 |  |  |
| 37 | slo_pricelim_flag | 否 |  |  |
| 38 | modify_date | 否 |  |  |
| 39 | remark | 否 |  |  |
| 40 | fin_max_balance | 否 |  |  |
| 41 | slo_compact_end_date | 否 |  |  |
| 42 | last_day_slo_balance | 否 |  |  |
| 43 | last_day_fin_balance | 否 |  |  |
| 44 | last_day_slo_amount | 否 |  |  |
| 45 | transin_date | 否 |  |  |
| 46 | modify_flag | 否 |  |  |
| 47 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 48 | stock_type | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_underly_code_cp | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_underly_code_cp | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_underly_code_cp | stock_code, exchange_type, stock_code, exchange_type |
| idx_underly_code_cp | stock_code, exchange_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-06 21:15:18 | 3.0.6.1065 | tongck54118 | 所有表underly_code_cp，添加了表字段(stock_type);
 |
| 2025-02-19 11:08:47 | 3.0.6.90 | 李想 | 新增表 |
| 2025-09-06 21:15:18 | 3.0.6.1065 | tongck54118 | 所有表underly_code_cp，添加了表字段(stock_type);
 |
| 2025-02-19 11:08:47 | 3.0.6.90 | 李想 | 新增表 |

# ucrt_underly_code - 标的证券信息表

**表对象ID**: 7022
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 56 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | fin_std_ratio | 否 |  |  |
| 5 | fin_ratio | 否 |  |  |
| 6 | fin_status | 否 |  |  |
| 7 | fin_end_date | 否 |  |  |
| 8 | slo_std_ratio | 否 |  |  |
| 9 | slo_ratio | 否 |  |  |
| 10 | slo_end_date | 否 |  |  |
| 11 | slo_status | 否 |  |  |
| 12 | slo_lack_flag | 否 |  |  |
| 13 | slo_pricelim_flag | 否 |  |  |
| 14 | stock_type | 否 |  |  |
| 15 | slo_compact_end_date | 否 |  |  |
| 16 | last_day_slo_balance | 否 |  |  |
| 17 | last_day_fin_balance | 否 |  |  |
| 18 | last_day_slo_amount | 否 |  |  |
| 19 | fin_max_balance | 否 |  |  |
| 20 | transaction_no | 否 |  |  |
| 21 | modify_date | 否 |  |  |
| 22 | modify_flag | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | transin_date | 否 |  |  |
| 27 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 28 | tohis_date | 否 | H |  |
| 29 | init_date | 否 |  |  |
| 30 | exchange_type | 否 |  |  |
| 31 | stock_code | 否 |  |  |
| 32 | fin_std_ratio | 否 |  |  |
| 33 | fin_ratio | 否 |  |  |
| 34 | fin_status | 否 |  |  |
| 35 | fin_end_date | 否 |  |  |
| 36 | slo_std_ratio | 否 |  |  |
| 37 | slo_ratio | 否 |  |  |
| 38 | slo_end_date | 否 |  |  |
| 39 | slo_status | 否 |  |  |
| 40 | slo_lack_flag | 否 |  |  |
| 41 | slo_pricelim_flag | 否 |  |  |
| 42 | stock_type | 否 |  |  |
| 43 | slo_compact_end_date | 否 |  |  |
| 44 | last_day_slo_balance | 否 |  |  |
| 45 | last_day_fin_balance | 否 |  |  |
| 46 | last_day_slo_amount | 否 |  |  |
| 47 | fin_max_balance | 否 |  |  |
| 48 | transaction_no | 否 |  |  |
| 49 | modify_date | 否 |  |  |
| 50 | modify_flag | 否 |  |  |
| 51 | remark | 否 |  |  |
| 52 | update_date | 否 |  |  |
| 53 | update_time | 否 |  |  |
| 54 | transin_date | 否 |  |  |
| 55 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 56 | tohis_date | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_underly_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| uk_rpt_ucrtunderlycode | ART | 是 | tohis_date, position_str, tohis_date, position_str |
| idx_ucrt_underly_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| uk_rpt_ucrtunderlycode | ART | 是 | tohis_date, position_str, tohis_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_underly_code | stock_code, exchange_type, stock_code, exchange_type |
| idx_ucrt_underly_code | stock_code, exchange_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-02-17 20:52:55 | 3.0.6.57 | 李想 | 物理表ucrt_underly_code，添加了表字段(transin_date);
物理表ucrt_underly_... |
| 2025-01-08 15:26:31 | 3.0.6.29 | 沈勋 | 物理表ucrt_underly_code，添加了表字段(modify_date);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:17 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-02-17 20:52:55 | 3.0.6.57 | 李想 | 物理表ucrt_underly_code，添加了表字段(transin_date);
物理表ucrt_underly_... |
| 2025-01-08 15:26:31 | 3.0.6.29 | 沈勋 | 物理表ucrt_underly_code，添加了表字段(modify_date);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:17 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |

# pre_underly_code - 预导入标的证券信息表

**表对象ID**: 7089
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | fin_ratio | 否 |  |  |
| 4 | fin_std_ratio | 否 |  |  |
| 5 | slo_ratio | 否 |  |  |
| 6 | slo_std_ratio | 否 |  |  |
| 7 | fin_status | 否 |  |  |
| 8 | slo_status | 否 |  |  |
| 9 | std_fin_status | 否 |  |  |
| 10 | std_slo_status | 否 |  |  |
| 11 | com_fin_status | 否 |  |  |
| 12 | com_slo_status | 否 |  |  |
| 13 | com_fin_ratio | 否 |  |  |
| 14 | com_slo_ratio | 否 |  |  |
| 15 | std_fin_ratio | 否 |  |  |
| 16 | std_slo_ratio | 否 |  |  |
| 17 | slo_pricelim_flag | 否 |  |  |
| 18 | slo_lack_flag | 否 |  |  |
| 19 | crdtfile_kind_str | 否 |  |  |
| 20 | fin_max_balance | 否 |  |  |
| 21 | slo_compact_end_date | 否 |  |  |
| 22 | last_day_slo_balance | 否 |  |  |
| 23 | last_day_fin_balance | 否 |  |  |
| 24 | last_day_slo_amount | 否 |  |  |
| 25 | update_date | 否 |  |  |
| 26 | update_time | 否 |  |  |
| 27 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 28 | exchange_type | 否 |  |  |
| 29 | stock_code | 否 |  |  |
| 30 | fin_ratio | 否 |  |  |
| 31 | fin_std_ratio | 否 |  |  |
| 32 | slo_ratio | 否 |  |  |
| 33 | slo_std_ratio | 否 |  |  |
| 34 | fin_status | 否 |  |  |
| 35 | slo_status | 否 |  |  |
| 36 | std_fin_status | 否 |  |  |
| 37 | std_slo_status | 否 |  |  |
| 38 | com_fin_status | 否 |  |  |
| 39 | com_slo_status | 否 |  |  |
| 40 | com_fin_ratio | 否 |  |  |
| 41 | com_slo_ratio | 否 |  |  |
| 42 | std_fin_ratio | 否 |  |  |
| 43 | std_slo_ratio | 否 |  |  |
| 44 | slo_pricelim_flag | 否 |  |  |
| 45 | slo_lack_flag | 否 |  |  |
| 46 | crdtfile_kind_str | 否 |  |  |
| 47 | fin_max_balance | 否 |  |  |
| 48 | slo_compact_end_date | 否 |  |  |
| 49 | last_day_slo_balance | 否 |  |  |
| 50 | last_day_fin_balance | 否 |  |  |
| 51 | last_day_slo_amount | 否 |  |  |
| 52 | update_date | 否 |  |  |
| 53 | update_time | 否 |  |  |
| 54 | position_str | 否 |  | stock_code(8)+exchange_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_pre_underly_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_pre_underly_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_pre_underly_code | stock_code, exchange_type, stock_code, exchange_type |
| idx_pre_underly_code | stock_code, exchange_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-17 21:01:41 | 3.0.6.58 | 李想 | 新增表 |
| 2025-02-17 21:01:41 | 3.0.6.58 | 李想 | 新增表 |

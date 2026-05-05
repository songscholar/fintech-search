# ucrt_compact_audit - 合约展期条件控制表

**表对象ID**: 7011
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 66 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | crdtaudit_way | 是 |  |  |
| 2 | crdtaudit_type | 是 |  |  |
| 3 | min_crdtaudit_value | 是 |  |  |
| 4 | max_crdtaudit_value | 是 |  |  |
| 5 | crdtaudit_status | 是 |  |  |
| 6 | en_compact_type | 是 |  |  |
| 7 | en_organ_flag | 是 |  |  |
| 8 | max_term | 是 |  |  |
| 9 | en_crdt_level | 是 |  |  |
| 10 | en_elig_risk_level | 是 |  |  |
| 11 | en_corp_risk_level | 是 |  |  |
| 12 | max_times | 是 |  |  |
| 13 | stock_conc_ratio | 是 |  |  |
| 14 | risk_conc_ratio | 是 |  |  |
| 15 | papercont_str | 是 |  |  |
| 16 | stopstock_asset_ratio | 是 |  |  |
| 17 | stock_type | 是 |  |  |
| 18 | stockgroup_no | 是 |  |  |
| 19 | en_aml_risk_level | 是 |  |  |
| 20 | include_outasset_flag | 是 |  |  |
| 21 | postpone_param_level | 是 |  |  |
| 22 | assurescale_type | 是 |  |  |
| 23 | en_underly_status | 是 |  |  |
| 24 | en_stock_type | 是 |  |  |
| 25 | transaction_no | 是 |  |  |
| 26 | position_str | 是 |  | init_date(8)+serial_no(10) |
| 27 | max_debit_balance | 是 |  |  |
| 28 | min_debit_balance | 是 |  |  |
| 29 | followdate_flag | 是 |  |  |
| 30 | market_forward5_date_flag | 是 |  |  |
| 31 | remark | 是 |  |  |
| 32 | update_date | 是 |  |  |
| 33 | update_time | 是 |  |  |
| 34 | crdtaudit_way | 是 |  |  |
| 35 | crdtaudit_type | 是 |  |  |
| 36 | min_crdtaudit_value | 是 |  |  |
| 37 | max_crdtaudit_value | 是 |  |  |
| 38 | crdtaudit_status | 是 |  |  |
| 39 | en_compact_type | 是 |  |  |
| 40 | en_organ_flag | 是 |  |  |
| 41 | max_term | 是 |  |  |
| 42 | en_crdt_level | 是 |  |  |
| 43 | en_elig_risk_level | 是 |  |  |
| 44 | en_corp_risk_level | 是 |  |  |
| 45 | max_times | 是 |  |  |
| 46 | stock_conc_ratio | 是 |  |  |
| 47 | risk_conc_ratio | 是 |  |  |
| 48 | papercont_str | 是 |  |  |
| 49 | stopstock_asset_ratio | 是 |  |  |
| 50 | stock_type | 是 |  |  |
| 51 | stockgroup_no | 是 |  |  |
| 52 | en_aml_risk_level | 是 |  |  |
| 53 | include_outasset_flag | 是 |  |  |
| 54 | postpone_param_level | 是 |  |  |
| 55 | assurescale_type | 是 |  |  |
| 56 | en_underly_status | 是 |  |  |
| 57 | en_stock_type | 是 |  |  |
| 58 | transaction_no | 是 |  |  |
| 59 | position_str | 是 |  | init_date(8)+serial_no(10) |
| 60 | max_debit_balance | 是 |  |  |
| 61 | min_debit_balance | 是 |  |  |
| 62 | followdate_flag | 是 |  |  |
| 63 | market_forward5_date_flag | 是 |  |  |
| 64 | remark | 是 |  |  |
| 65 | update_date | 是 |  |  |
| 66 | update_time | 是 |  |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_compact_audit | 默认 | 否 | crdtaudit_type, crdtaudit_way, min_crdtaudit_value, max_crdtaudit_value, en_elig_risk_level, stock_type, stockgroup_no, followdate_flag, postpone_param_level, en_stock_type, en_compact_type, market_forward5_date_flag, en_organ_flag, crdtaudit_type, crdtaudit_way, min_crdtaudit_value, max_crdtaudit_value, en_elig_risk_level, stock_type, stockgroup_no, followdate_flag, postpone_param_level, en_stock_type, en_compact_type, market_forward5_date_flag, en_organ_flag |
| idx_ucrt_compact_audit_pos | 默认 | 否 | position_str, position_str |
| idx_ucrt_compact_audit_pos | 默认 | 否 |  |
| idx_ucrt_compact_audit_pos | 默认 | 否 | position_str, position_str |
| idx_ucrt_compact_audit | 默认 | 否 |  |
| idx_ucrt_compact_audit | ART | 是 | crdtaudit_way, crdtaudit_type, min_crdtaudit_value, max_crdtaudit_value, en_elig_risk_level, stock_type, stockgroup_no, postpone_param_level, en_stock_type, en_compact_type, en_organ_flag, crdtaudit_way, crdtaudit_type, min_crdtaudit_value, max_crdtaudit_value, en_elig_risk_level, stock_type, stockgroup_no, postpone_param_level, en_stock_type, en_compact_type, en_organ_flag |
| idx_ucrt_compact_audit | 默认 | 否 | crdtaudit_type, crdtaudit_way, min_crdtaudit_value, max_crdtaudit_value, en_elig_risk_level, stock_type, stockgroup_no, followdate_flag, postpone_param_level, en_stock_type, en_compact_type, market_forward5_date_flag, en_organ_flag, crdtaudit_type, crdtaudit_way, min_crdtaudit_value, max_crdtaudit_value, en_elig_risk_level, stock_type, stockgroup_no, followdate_flag, postpone_param_level, en_stock_type, en_compact_type, market_forward5_date_flag, en_organ_flag |
| idx_ucrt_compact_audit_pos | 默认 | 否 | position_str, position_str |
| idx_ucrt_compact_audit_pos | 默认 | 否 |  |
| idx_ucrt_compact_audit_pos | 默认 | 否 | position_str, position_str |
| idx_ucrt_compact_audit | 默认 | 否 |  |
| idx_ucrt_compact_audit | ART | 是 | crdtaudit_way, crdtaudit_type, min_crdtaudit_value, max_crdtaudit_value, en_elig_risk_level, stock_type, stockgroup_no, postpone_param_level, en_stock_type, en_compact_type, en_organ_flag, crdtaudit_way, crdtaudit_type, min_crdtaudit_value, max_crdtaudit_value, en_elig_risk_level, stock_type, stockgroup_no, postpone_param_level, en_stock_type, en_compact_type, en_organ_flag |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_compact_audit | crdtaudit_way, crdtaudit_type, min_crdtaudit_value, max_crdtaudit_value, en_elig_risk_level, stock_type, stockgroup_no, postpone_param_level, en_stock_type, en_compact_type, en_organ_flag, crdtaudit_way, crdtaudit_type, min_crdtaudit_value, max_crdtaudit_value, en_elig_risk_level, stock_type, stockgroup_no, postpone_param_level, en_stock_type, en_compact_type, en_organ_flag |
| idx_ucrt_compact_audit_pos | position_str, position_str |
| idx_ucrt_compact_audit | crdtaudit_way, crdtaudit_type, min_crdtaudit_value, max_crdtaudit_value, en_elig_risk_level, stock_type, stockgroup_no, postpone_param_level, en_stock_type, en_compact_type, en_organ_flag, crdtaudit_way, crdtaudit_type, min_crdtaudit_value, max_crdtaudit_value, en_elig_risk_level, stock_type, stockgroup_no, postpone_param_level, en_stock_type, en_compact_type, en_organ_flag |
| idx_ucrt_compact_audit_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-02-10 15:33:57 | 3.0.6.1074 | 袁文龙 | 调整索引(idx_ucrt_compact_audit)调整字段crdtaudit_type顺序，删除字段followd... |
| 2025-07-17 09:25:29 | 3.0.6.115 | 常行 | 物理表ucrt_compact_audit，增加索引(idx_ucrt_compact_audit:[crdtaudit... |
| 2025-07-17 17:05:19 | 3.0.6.116 | 常行 | 物理表ucrt_compact_audit，删除了表索引(idx_ucrt_compact_audit_pos);
 |
| 2025-02-18 12:14:26 | 3.0.6.79 | 李想 | 物理表ucrt_compact_audit，添加了表字段(followdate_flag);
物理表ucrt_comp... |
| 2024-12-31 10:55:24 | 3.0.6.22 | huangzh | 调整内存索引idx_ucrt_compact_audit |
| 2024-11-19 09:26:19 | 3.0.6.17 | 沈勋 | 调整内存索引idx_ucrt_compact_audit |
| 2024-11-11 15:48:20 | 3.0.6.15 | 汪杰 | 物理表ucrt_compact_audit，添加了表字段(max_debit_balance);
物理表ucrt_co... |
| 2024-08-06 10:24:12 | 3.0.3.6 | 汪杰 | 物理表ucrt_compact_audit，增加索引(idx_ucrt_compact_audit_pos:[posit... |
| 2024-08-06 10:15:51 | 3.0.3.6 | 汪杰 | 物理表ucrt_compact_audit，删除了表索引(idx_ucrt_compact_audit);
 |
| 2024-08-06 10:14:47 | 3.0.3.6 | 汪杰 | 物理表ucrt_compact_audit，添加了表字段(position_str);
 |
| 2023-10-16 14:37:30 | V3.0.1.9 | 吴丽丽 | 调整ucrt_compact_audit(idx_ucrt_compact_audit)的排序，crdtaudit_wa... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:24 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no |
| 2026-02-10 15:33:57 | 3.0.6.1074 | 袁文龙 | 调整索引(idx_ucrt_compact_audit)调整字段crdtaudit_type顺序，删除字段followd... |
| 2025-07-17 09:25:29 | 3.0.6.115 | 常行 | 物理表ucrt_compact_audit，增加索引(idx_ucrt_compact_audit:[crdtaudit... |

> 共 26 条修改记录，仅显示最近15条

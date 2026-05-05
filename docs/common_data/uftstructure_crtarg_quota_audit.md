# quota_audit - 额度调整申请参数表

**表对象ID**: 7086
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | quotaaudit_way | 否 |  |  |
| 2 | quotaaudit_type | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | stockgroup_no | 否 |  |  |
| 5 | min_quotaaudit_value | 否 |  |  |
| 6 | max_quotaaudit_value | 否 |  |  |
| 7 | papercont_str | 否 |  |  |
| 8 | en_corp_risk_level | 否 |  |  |
| 9 | include_outasset_flag | 否 |  |  |
| 10 | stock_conc_ratio | 否 |  |  |
| 11 | en_organ_flag | 否 |  |  |
| 12 | quotaaudit_status | 否 |  |  |
| 13 | remark | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 18 | quotaaudit_way | 否 |  |  |
| 19 | quotaaudit_type | 否 |  |  |
| 20 | stock_type | 否 |  |  |
| 21 | stockgroup_no | 否 |  |  |
| 22 | min_quotaaudit_value | 否 |  |  |
| 23 | max_quotaaudit_value | 否 |  |  |
| 24 | papercont_str | 否 |  |  |
| 25 | en_corp_risk_level | 否 |  |  |
| 26 | include_outasset_flag | 否 |  |  |
| 27 | stock_conc_ratio | 否 |  |  |
| 28 | en_organ_flag | 否 |  |  |
| 29 | quotaaudit_status | 否 |  |  |
| 30 | remark | 否 |  |  |
| 31 | update_date | 否 |  |  |
| 32 | update_time | 否 |  |  |
| 33 | transaction_no | 否 |  |  |
| 34 | position_str | 否 |  | init_date(8)+serial_no(10) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_quota_audit | ART | 是 | quotaaudit_way, quotaaudit_type, min_quotaaudit_value, max_quotaaudit_value, stock_type, stockgroup_no, en_organ_flag, quotaaudit_way, quotaaudit_type, min_quotaaudit_value, max_quotaaudit_value, stock_type, stockgroup_no, en_organ_flag |
| idx_quota_audit | ART | 是 | quotaaudit_way, quotaaudit_type, min_quotaaudit_value, max_quotaaudit_value, stock_type, stockgroup_no, en_organ_flag, quotaaudit_way, quotaaudit_type, min_quotaaudit_value, max_quotaaudit_value, stock_type, stockgroup_no, en_organ_flag |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_quota_audit | quotaaudit_way, quotaaudit_type, min_quotaaudit_value, max_quotaaudit_value, stock_type, stockgroup_no, en_organ_flag, quotaaudit_way, quotaaudit_type, min_quotaaudit_value, max_quotaaudit_value, stock_type, stockgroup_no, en_organ_flag |
| idx_quota_audit | quotaaudit_way, quotaaudit_type, min_quotaaudit_value, max_quotaaudit_value, stock_type, stockgroup_no, en_organ_flag, quotaaudit_way, quotaaudit_type, min_quotaaudit_value, max_quotaaudit_value, stock_type, stockgroup_no, en_organ_flag |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-17 19:36:51 | 3.0.6.51 | 李想 | 新增表 |
| 2025-02-17 19:36:51 | 3.0.6.51 | 李想 | 新增表 |

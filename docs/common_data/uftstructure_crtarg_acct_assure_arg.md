# acct_assure_arg - 个人维保比例调整规则参数表

**表对象ID**: 7083
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | rule_no | 否 |  |  |
| 2 | rule_type | 否 |  |  |
| 3 | rulecondition_type | 否 |  |  |
| 4 | stockgroup_no | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | en_stock_type | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | stock_conc_ratio | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 13 | rule_no | 否 |  |  |
| 14 | rule_type | 否 |  |  |
| 15 | rulecondition_type | 否 |  |  |
| 16 | stockgroup_no | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | en_stock_type | 否 |  |  |
| 19 | stock_code | 否 |  |  |
| 20 | stock_conc_ratio | 否 |  |  |
| 21 | update_date | 否 |  |  |
| 22 | update_time | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | position_str | 否 |  | init_date(8)+serial_no(10) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_acct_assure_arg | ART | 是 | position_str, position_str |
| idx_acct_assure_arg | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_acct_assure_arg | position_str, position_str |
| idx_acct_assure_arg | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-17 17:04:01 | 3.0.6.48 | 李想 | 新增表 |
| 2025-02-17 17:04:01 | 3.0.6.48 | 李想 | 新增表 |

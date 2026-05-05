# uarg_usersyncinfobizarg - 用户同步异常信息定位表

**表对象ID**: 140
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | table_category | 否 |  |  |
| 2 | transaction_no | 否 |  |  |
| 3 | param_name | 否 |  |  |
| 4 | param_type | 否 |  |  |
| 5 | param_width | 否 |  |  |
| 6 | param_scale | 否 |  |  |
| 7 | param_value | 否 |  |  |
| 8 | date_clear | 否 |  |  |
| 9 | position_str | 否 |  |  |
| 10 | table_category | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | param_name | 否 |  |  |
| 13 | param_type | 否 |  |  |
| 14 | param_width | 否 |  |  |
| 15 | param_scale | 否 |  |  |
| 16 | param_value | 否 |  |  |
| 17 | date_clear | 否 |  |  |
| 18 | position_str | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_usersyncinfobizarg | 默认 | 否 | table_category, transaction_no, param_name, position_str, table_category, transaction_no, param_name, position_str |
| uk_rpt_uargusersyncinfobizarg | ART | 是 | date_clear, table_category, transaction_no, date_clear, table_category, transaction_no |
| idx_uarg_usersyncinfobizarg | 默认 | 否 | table_category, transaction_no, param_name, position_str, table_category, transaction_no, param_name, position_str |
| uk_rpt_uargusersyncinfobizarg | ART | 是 | date_clear, table_category, transaction_no, date_clear, table_category, transaction_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_usersyncinfobizarg | table_category, transaction_no, param_name, position_str, table_category, transaction_no, param_name, position_str |
| idx_uarg_usersyncinfobizarg | table_category, transaction_no, param_name, position_str, table_category, transaction_no, param_name, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 19:56:55 | V3.0.6.1019 | 周兆军 | 维护历史表 |
| 2025-02-22 14:42:48 | 3.0.6.119 | 李想 | 新增表 |
| 2025-11-21 19:56:55 | V3.0.6.1019 | 周兆军 | 维护历史表 |
| 2025-02-22 14:42:48 | 3.0.6.119 | 李想 | 新增表 |

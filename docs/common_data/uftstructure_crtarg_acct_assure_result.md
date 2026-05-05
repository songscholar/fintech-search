# acct_assure_result - 个人维保比例调整结果参数表

**表对象ID**: 7085
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | rule_no | 否 |  |  |
| 2 | assurescale_type | 否 |  |  |
| 3 | assurescale_value | 否 |  |  |
| 4 | update_date | 否 |  |  |
| 5 | update_time | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | position_str | 否 |  | rule_no(10)+assurescale_type(1) |
| 8 | rule_no | 否 |  |  |
| 9 | assurescale_type | 否 |  |  |
| 10 | assurescale_value | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | position_str | 否 |  | rule_no(10)+assurescale_type(1) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_acct_assure_result | ART | 是 | rule_no, assurescale_type, rule_no, assurescale_type |
| idx_acct_assure_result | ART | 是 | rule_no, assurescale_type, rule_no, assurescale_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_acct_assure_result | rule_no, assurescale_type, rule_no, assurescale_type |
| idx_acct_assure_result | rule_no, assurescale_type, rule_no, assurescale_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-17 19:25:47 | 3.0.6.50 | 李想 | 新增表 |
| 2025-02-17 19:25:47 | 3.0.6.50 | 李想 | 新增表 |

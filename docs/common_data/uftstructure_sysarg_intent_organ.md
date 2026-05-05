# intent_organ - 意向平台机构信息表

**表对象ID**: 136
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | organ_code | 否 |  |  |
| 2 | organ_name | 否 |  |  |
| 3 | en_entrust_type | 否 |  |  |
| 4 | en_company_no | 否 |  |  |
| 5 | update_date | 否 |  |  |
| 6 | update_time | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | organ_code | 否 |  |  |
| 9 | organ_name | 否 |  |  |
| 10 | en_entrust_type | 否 |  |  |
| 11 | en_company_no | 否 |  |  |
| 12 | update_date | 否 |  |  |
| 13 | update_time | 否 |  |  |
| 14 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_intent_organ_pos | 默认 | 否 |  |
| idx_intent_organ_pos | ART | 是 | organ_code, organ_code |
| idx_intent_organ_pos | 默认 | 否 |  |
| idx_intent_organ_pos | ART | 是 | organ_code, organ_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_intent_organ_pos | organ_code, organ_code |
| idx_intent_organ_pos | organ_code, organ_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:45:47 | 3.0.2.103 | taocong45644 | 当前表intent_organ，修改了索引idx_intent_organ_pos,索引字段修改为：(organ_cod... |
| 2025-02-19 14:24:22 | 3.0.6.91 | 李想 | 新增表 |
| 2025-12-01 14:45:47 | 3.0.2.103 | taocong45644 | 当前表intent_organ，修改了索引idx_intent_organ_pos,索引字段修改为：(organ_cod... |
| 2025-02-19 14:24:22 | 3.0.6.91 | 李想 | 新增表 |

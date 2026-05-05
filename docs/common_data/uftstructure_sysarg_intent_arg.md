# intent_arg - 意向平台参数表

**表对象ID**: 135
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_status | 否 |  |  |
| 3 | update_date | 否 |  |  |
| 4 | update_time | 否 |  |  |
| 5 | init_date | 否 |  |  |
| 6 | exchange_status | 否 |  |  |
| 7 | update_date | 否 |  |  |
| 8 | update_time | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_intent_arg | 默认 | 否 |  |
| idx_intent_arg | ART | 是 | init_date, init_date |
| idx_intent_arg | 默认 | 否 |  |
| idx_intent_arg | ART | 是 | init_date, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_intent_arg | init_date, init_date |
| idx_intent_arg | init_date, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:45:08 | 3.0.2.103 | taocong45644 | 当前表intent_arg，修改了索引idx_intent_arg,索引字段修改为：(init_date),索引唯一性修... |
| 2025-02-19 14:22:59 | 3.0.6.90 | 李想 | 新增表 |
| 2025-12-01 14:45:08 | 3.0.2.103 | taocong45644 | 当前表intent_arg，修改了索引idx_intent_arg,索引字段修改为：(init_date),索引唯一性修... |
| 2025-02-19 14:22:59 | 3.0.6.90 | 李想 | 新增表 |

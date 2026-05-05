# act_intent_account - 意向平台投资者信息

**表对象ID**: 2474
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | intent_acct_level | 否 |  |  |
| 4 | entrust_type | 否 |  |  |
| 5 | modify_date | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | intent_acct_level | 否 |  |  |
| 9 | entrust_type | 否 |  |  |
| 10 | modify_date | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_act_intent_account | 默认 | 否 |  |
| idx_act_intent_account | ART | 是 | stock_account, entrust_type, stock_account, entrust_type |
| idx_act_intent_account | 默认 | 否 |  |
| idx_act_intent_account | ART | 是 | stock_account, entrust_type, stock_account, entrust_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_act_intent_account | stock_account, entrust_type, stock_account, entrust_type |
| idx_act_intent_account | stock_account, entrust_type, stock_account, entrust_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:33:38 | 3.0.2.103 | taocong45644 | 当前表act_intent_account，修改了索引idx_act_intent_account,索引字段修改为：(s... |
| 2025-04-25 17:04:30 | 3.0.6.134 | 常行 | 新增表 |
| 2025-12-01 14:33:38 | 3.0.2.103 | taocong45644 | 当前表act_intent_account，修改了索引idx_act_intent_account,索引字段修改为：(s... |
| 2025-04-25 17:04:30 | 3.0.6.134 | 常行 | 新增表 |

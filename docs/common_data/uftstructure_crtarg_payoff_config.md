# payoff_config - 平仓名单生成参数表

**表对象ID**: 7098
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | rule_no | 否 |  |  |
| 2 | crdt_operator | 否 |  |  |
| 3 | close_rate | 否 |  |  |
| 4 | crdt_operator1 | 否 |  |  |
| 5 | close_rate1 | 否 |  |  |
| 6 | crdt_operator2 | 否 |  |  |
| 7 | close_rate2 | 否 |  |  |
| 8 | crdt_operator3 | 否 |  |  |
| 9 | close_rate3 | 否 |  |  |
| 10 | update_date | 否 |  |  |
| 11 | update_time | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | rule_no | 否 |  |  |
| 14 | crdt_operator | 否 |  |  |
| 15 | close_rate | 否 |  |  |
| 16 | crdt_operator1 | 否 |  |  |
| 17 | close_rate1 | 否 |  |  |
| 18 | crdt_operator2 | 否 |  |  |
| 19 | close_rate2 | 否 |  |  |
| 20 | crdt_operator3 | 否 |  |  |
| 21 | close_rate3 | 否 |  |  |
| 22 | update_date | 否 |  |  |
| 23 | update_time | 否 |  |  |
| 24 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_payoff_config | ART | 是 | rule_no, rule_no |
| idx_payoff_config | ART | 是 | rule_no, rule_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_payoff_config | rule_no, rule_no |
| idx_payoff_config | rule_no, rule_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 13:44:12 | 3.0.6.80 | 李想 | 新增表 |
| 2025-02-18 13:44:12 | 3.0.6.80 | 李想 | 新增表 |

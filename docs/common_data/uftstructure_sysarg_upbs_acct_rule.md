# upbs_acct_rule - 账户分片规则表

**表对象ID**: 14
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | umt_begin_account | 否 |  |  |
| 2 | umt_end_account | 否 |  |  |
| 3 | acct_rule_type | 否 |  |  |
| 4 | partition_no | 否 |  |  |
| 5 | sysnode_id | 否 |  |  |
| 6 | account_len | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | transaction_str | 否 |  |  |
| 9 | position_str | 否 |  | UF2.0:umt_begin_account(32)+acct_rule_type(1)+sysnode_id(10) |
| 10 | umt_begin_account | 否 |  |  |
| 11 | umt_end_account | 否 |  |  |
| 12 | acct_rule_type | 否 |  |  |
| 13 | partition_no | 否 |  |  |
| 14 | sysnode_id | 否 |  |  |
| 15 | account_len | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | transaction_str | 否 |  |  |
| 18 | position_str | 否 |  | UF2.0:umt_begin_account(32)+acct_rule_type(1)+sysnode_id(10) |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_acct_rule_uk | 默认 | 否 | position_str, position_str |
| idx_upbs_acct_rule | 默认 | 否 | umt_begin_account, acct_rule_type, sysnode_id, umt_begin_account, acct_rule_type, sysnode_id |
| idx_upbs_acct_rule_uk | ART | 是 | position_str, position_str |
| idx_upbs_acct_rule | 默认 | 否 |  |
| idx_upbs_acct_rule | ART | 是 | umt_begin_account, acct_rule_type, sysnode_id, umt_begin_account, acct_rule_type, sysnode_id |
| idx_upbs_acct_rule_uk | ART | 是 | position_str, position_str |
| idx_upbs_acct_rule_uk | 默认 | 否 | position_str, position_str |
| idx_upbs_acct_rule | 默认 | 否 | umt_begin_account, acct_rule_type, sysnode_id, umt_begin_account, acct_rule_type, sysnode_id |
| idx_upbs_acct_rule_uk | ART | 是 | position_str, position_str |
| idx_upbs_acct_rule | 默认 | 否 |  |
| idx_upbs_acct_rule | ART | 是 | umt_begin_account, acct_rule_type, sysnode_id, umt_begin_account, acct_rule_type, sysnode_id |
| idx_upbs_acct_rule_uk | ART | 是 | position_str, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_acct_rule | umt_begin_account, acct_rule_type, sysnode_id, umt_begin_account, acct_rule_type, sysnode_id |
| idx_upbs_acct_rule_uk | position_str, position_str |
| idx_upbs_acct_rule | umt_begin_account, acct_rule_type, sysnode_id, umt_begin_account, acct_rule_type, sysnode_id |
| idx_upbs_acct_rule_uk | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-02 14:29:44 | 3.0.2.93 | 高志强 | 当前表upbs_acct_rule，增加索引(idx_upbs_acct_rule_uk:[position_str])... |
| 2025-09-02 14:29:18 | 3.0.2.93 | 高志强 | 当前表upbs_acct_rule，修改了索引idx_upbs_acct_rule,索引字段修改为：(umt_begin... |
| 2025-09-02 14:26:00 | 3.0.2.93 | 高志强 | 当前表upbs_acct_rule，增加索引（ idx_upbs_acct_rule_uk:[position_str]... |
| 2025-09-02 14:25:27 | 3.0.2.93 | 高志强 | 当前表upbs_acct_rule，修改了索引idx_upbs_acct_rule,索引字段修改为：(umt_begin... |
| 2025-09-02 14:15:49 | 3.0.2.93 | 高志强 | 所有表upbs_acct_rule，添加了表字段(position_str);
 |
| 2025-06-13 14:51:16 | 3.0.6.1002 | 汪迎 | 物理表upbs_acct_rule，添加了表字段(transaction_str);
 |
| 2025-02-12 16:27:58 | 3.0.2.54 | 范文浩 | 物理表upbs_acct_rule，添加了表字段(account_len);
 |
| 2025-01-13 10:46:34 | 3.0.2.51 | 董乾坤 | 物理表upbs_acct_rule，添加了表字段(transaction_no);
 |
| 2024-09-09 11:02:28 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-09-02 14:29:44 | 3.0.2.93 | 高志强 | 当前表upbs_acct_rule，增加索引(idx_upbs_acct_rule_uk:[position_str])... |
| 2025-09-02 14:29:18 | 3.0.2.93 | 高志强 | 当前表upbs_acct_rule，修改了索引idx_upbs_acct_rule,索引字段修改为：(umt_begin... |
| 2025-09-02 14:26:00 | 3.0.2.93 | 高志强 | 当前表upbs_acct_rule，增加索引（ idx_upbs_acct_rule_uk:[position_str]... |
| 2025-09-02 14:25:27 | 3.0.2.93 | 高志强 | 当前表upbs_acct_rule，修改了索引idx_upbs_acct_rule,索引字段修改为：(umt_begin... |
| 2025-09-02 14:15:49 | 3.0.2.93 | 高志强 | 所有表upbs_acct_rule，添加了表字段(position_str);
 |

> 共 20 条修改记录，仅显示最近15条

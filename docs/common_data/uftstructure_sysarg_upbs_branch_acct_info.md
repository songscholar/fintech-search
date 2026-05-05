# upbs_branch_acct_info - 机构对应账户信息

**表对象ID**: 2469
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | branch_account_type | 否 |  |  |
| 3 | branch_account | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | branch_account_type | 否 |  |  |
| 7 | branch_account | 否 |  |  |
| 8 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_branchacctinfo | 默认 | 否 |  |
| idx_branchacctinfo | ART | 是 | branch_no, branch_account_type, branch_no, branch_account_type |
| idx_branchacctinfo | 默认 | 否 |  |
| idx_branchacctinfo | ART | 是 | branch_no, branch_account_type, branch_no, branch_account_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_branchacctinfo | branch_no, branch_account_type, branch_no, branch_account_type |
| idx_branchacctinfo | branch_no, branch_account_type, branch_no, branch_account_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 15:33:56 | 3.0.2.103 | taocong45644 | 当前表upbs_branch_acct_info，修改了索引idx_branchacctinfo,索引字段修改为：(br... |
| 2025-04-11 17:37:22 | 3.0.2.2004 | 蒋浩 |  |
| 2025-12-01 15:33:56 | 3.0.2.103 | taocong45644 | 当前表upbs_branch_acct_info，修改了索引idx_branchacctinfo,索引字段修改为：(br... |
| 2025-04-11 17:37:22 | 3.0.2.2004 | 蒋浩 |  |

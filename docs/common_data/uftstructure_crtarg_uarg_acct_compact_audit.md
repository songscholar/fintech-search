# uarg_acct_compact_audit - 合约展期账户控制表2

**表对象ID**: 7117
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | res_entrust_way | 否 |  |  |
| 4 | max_term | 否 |  |  |
| 5 | control_flag | 否 |  |  |
| 6 | en_postpone_restrict_type | 否 |  |  |
| 7 | en_crdtaudit_type | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | postpone_restrict_reason | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | op_branch_no | 否 |  |  |
| 12 | operator_no | 否 |  |  |
| 13 | remark | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | fund_account | 否 |  |  |
| 18 | res_entrust_way | 否 |  |  |
| 19 | max_term | 否 |  |  |
| 20 | control_flag | 否 |  |  |
| 21 | en_postpone_restrict_type | 否 |  |  |
| 22 | en_crdtaudit_type | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | postpone_restrict_reason | 否 |  |  |
| 25 | branch_no | 否 |  |  |
| 26 | op_branch_no | 否 |  |  |
| 27 | operator_no | 否 |  |  |
| 28 | remark | 否 |  |  |
| 29 | update_date | 否 |  |  |
| 30 | update_time | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_acct_compact_audit_term | ART | 是 | fund_account, res_entrust_way, max_term, postpone_restrict_reason, fund_account, res_entrust_way, max_term, postpone_restrict_reason |
| idx_uarg_acct_compact_audit_account | ART | 是 | fund_account, res_entrust_way, postpone_restrict_reason, fund_account, res_entrust_way, postpone_restrict_reason |
| idx_uarg_acct_compact_audit_term | ART | 是 | fund_account, res_entrust_way, max_term, postpone_restrict_reason, fund_account, res_entrust_way, max_term, postpone_restrict_reason |
| idx_uarg_acct_compact_audit_account | ART | 是 | fund_account, res_entrust_way, postpone_restrict_reason, fund_account, res_entrust_way, postpone_restrict_reason |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_acct_compact_audit | fund_account, res_entrust_way, postpone_restrict_reason, fund_account, res_entrust_way, postpone_restrict_reason |
| idx_uarg_acct_compact_audit | fund_account, res_entrust_way, postpone_restrict_reason, fund_account, res_entrust_way, postpone_restrict_reason |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-03-13 15:11:57 | 3.0.6.105 | 李想 | 新增表 |
| 2025-03-13 15:11:57 | 3.0.6.105 | 李想 | 新增表 |

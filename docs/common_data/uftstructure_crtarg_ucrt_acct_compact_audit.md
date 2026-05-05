# ucrt_acct_compact_audit - 合约展期账户控制表

**表对象ID**: 7013
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 18 个）

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
| 10 | client_id | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | res_entrust_way | 否 |  |  |
| 13 | max_term | 否 |  |  |
| 14 | control_flag | 否 |  |  |
| 15 | en_postpone_restrict_type | 否 |  |  |
| 16 | en_crdtaudit_type | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | postpone_restrict_reason | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_ucrt_acct_compact_audit | 默认 | 否 | fund_account, res_entrust_way, postpone_restrict_reason, fund_account, res_entrust_way, postpone_restrict_reason |
| uk_ucrt_acct_compact_audit | 默认 | 否 |  |
| idx_ucrt_acct_compact_audit_term | ART | 是 | fund_account, res_entrust_way, max_term, postpone_restrict_reason, fund_account, res_entrust_way, max_term, postpone_restrict_reason |
| idx_ucrt_acct_compact_audit_account | ART | 是 | fund_account, res_entrust_way, postpone_restrict_reason, fund_account, res_entrust_way, postpone_restrict_reason |
| uk_ucrt_acct_compact_audit | 默认 | 否 | fund_account, res_entrust_way, postpone_restrict_reason, fund_account, res_entrust_way, postpone_restrict_reason |
| uk_ucrt_acct_compact_audit | 默认 | 否 |  |
| idx_ucrt_acct_compact_audit_term | ART | 是 | fund_account, res_entrust_way, max_term, postpone_restrict_reason, fund_account, res_entrust_way, max_term, postpone_restrict_reason |
| idx_ucrt_acct_compact_audit_account | ART | 是 | fund_account, res_entrust_way, postpone_restrict_reason, fund_account, res_entrust_way, postpone_restrict_reason |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_acct_compact_audit | fund_account, res_entrust_way, postpone_restrict_reason, fund_account, res_entrust_way, postpone_restrict_reason |
| idx_ucrt_acct_compact_audit | fund_account, res_entrust_way, postpone_restrict_reason, fund_account, res_entrust_way, postpone_restrict_reason |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引uk_ucrt_acct_compact_audit为idx_ucrt_acct_compact_audi... |
| 2024-10-21 10:29:39 | 3.0.6.9 | 汪杰 | 物理表ucrt_acct_compact_audit，增加索引(uk_ucrt_acct_compact_audit:[... |
| 2024-10-21 10:27:43 | 3.0.6.9 | 汪杰 | 物理表ucrt_acct_compact_audit，删除了表索引(uk_ucrt_acct_compact_audit... |
| 2024-10-21 10:25:38 | 3.0.6.9 | 汪杰 |  |
| 2024-10-21 10:24:52 | 3.0.6.9 | 汪杰 | 物理表ucrt_acct_compact_audit，添加了表字段(postpone_restrict_reason);... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:22 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引uk_ucrt_acct_compact_audit为idx_ucrt_acct_compact_audi... |
| 2024-10-21 10:29:39 | 3.0.6.9 | 汪杰 | 物理表ucrt_acct_compact_audit，增加索引(uk_ucrt_acct_compact_audit:[... |
| 2024-10-21 10:27:43 | 3.0.6.9 | 汪杰 | 物理表ucrt_acct_compact_audit，删除了表索引(uk_ucrt_acct_compact_audit... |
| 2024-10-21 10:25:38 | 3.0.6.9 | 汪杰 |  |
| 2024-10-21 10:24:52 | 3.0.6.9 | 汪杰 | 物理表ucrt_acct_compact_audit，添加了表字段(postpone_restrict_reason);... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:22 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no |

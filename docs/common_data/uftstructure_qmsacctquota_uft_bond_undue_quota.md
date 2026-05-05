# uft_bond_undue_quota - UFT客户未到期余额汇总表

**表对象ID**: 1653
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | acode_account | 否 |  |  |
| 2 | day_due_balance | 否 |  |  |
| 3 | day_used_quota | 否 |  |  |
| 4 | uncome_balance | 否 |  |  |
| 5 | total_quota | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | branch_no | 否 |  |  |
| 9 | order_no | 否 |  |  |
| 10 | acode_account | 否 |  |  |
| 11 | day_due_balance | 否 |  |  |
| 12 | day_used_quota | 否 |  |  |
| 13 | uncome_balance | 否 |  |  |
| 14 | total_quota | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_account | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | order_no | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uftassetbondjour | 默认 | 否 |  |
| idx_uftassetbondjour_acct | 默认 | 否 |  |
| idx_uftassetbondjour | ART | 是 | acode_account, acode_account |
| idx_uftassetbondjour_acct | ART | 是 | exchange_type, stock_account, acode_account, branch_no, exchange_type, stock_account, acode_account, branch_no |
| idx_uftassetbondjour | 默认 | 否 |  |
| idx_uftassetbondjour_acct | 默认 | 否 |  |
| idx_uftassetbondjour | ART | 是 | acode_account, acode_account |
| idx_uftassetbondjour_acct | ART | 是 | exchange_type, stock_account, acode_account, branch_no, exchange_type, stock_account, acode_account, branch_no |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_uftassetbondjour | acode_account, acode_account |
| idx_uftassetbondjour_acct | exchange_type, stock_account, acode_account, branch_no, exchange_type, stock_account, acode_account, branch_no |
| idx_uftassetbondjour | acode_account, acode_account |
| idx_uftassetbondjour_acct | exchange_type, stock_account, acode_account, branch_no, exchange_type, stock_account, acode_account, branch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:50:11 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:47:19 | 3.0.2.103 | taocong45644 | 当前表uft_bond_undue_quota，修改了索引idx_uftassetbondjour,索引字段修改为：(a... |
| 2025-03-22 18:23:04 | 3.0.2.2002 | 高志强 | 调整对象号避免和feature_ses分支冲突 |
| 2025-03-20 17:43:48 | 3.0.2.2001 | 杨新照 |  |
| 2026-03-05 16:50:11 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:47:19 | 3.0.2.103 | taocong45644 | 当前表uft_bond_undue_quota，修改了索引idx_uftassetbondjour,索引字段修改为：(a... |
| 2025-03-22 18:23:04 | 3.0.2.2002 | 高志强 | 调整对象号避免和feature_ses分支冲突 |
| 2025-03-20 17:43:48 | 3.0.2.2001 | 杨新照 |  |

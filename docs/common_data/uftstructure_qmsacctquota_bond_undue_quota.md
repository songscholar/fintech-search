# bond_undue_quota - 客户未到期余额汇总表

**表对象ID**: 1615
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
| 9 | adlm_undue_bal | 否 |  |  |
| 10 | acode_account | 否 |  |  |
| 11 | day_due_balance | 否 |  |  |
| 12 | day_used_quota | 否 |  |  |
| 13 | uncome_balance | 否 |  |  |
| 14 | total_quota | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_account | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | adlm_undue_bal | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_assetbondjour | ART | 是 | acode_account, acode_account |
| idx_assetbondjour_acct | ART | 是 | exchange_type, stock_account, acode_account, branch_no, exchange_type, stock_account, acode_account, branch_no |
| idx_assetbondjour | ART | 是 | acode_account, acode_account |
| idx_assetbondjour_acct | ART | 是 | exchange_type, stock_account, acode_account, branch_no, exchange_type, stock_account, acode_account, branch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_assetbondjour_acct | exchange_type, stock_account, acode_account, branch_no, exchange_type, stock_account, acode_account, branch_no |
| idx_assetbondjour_acct | exchange_type, stock_account, acode_account, branch_no, exchange_type, stock_account, acode_account, branch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:44:36 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2024-06-29 16:11:06 | 3.0.2.6 | 张云焘 | 由sestrade迁移至uqms |
| 2026-03-05 16:44:36 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2024-06-29 16:11:06 | 3.0.2.6 | 张云焘 | 由sestrade迁移至uqms |

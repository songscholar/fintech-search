# uses_sub_fund_account - 资金子账户表

**表对象ID**: 5575
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | sub_fund_account | 否 |  |  |
| 5 | sub_acct_type | 否 |  |  |
| 6 | sub_acct_classify | 否 |  |  |
| 7 | sub_acct_num | 否 |  |  |
| 8 | sub_acct_alias | 否 |  |  |
| 9 | position_str | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | branch_no | 否 |  |  |
| 12 | client_id | 否 |  |  |
| 13 | fund_account | 否 |  |  |
| 14 | sub_fund_account | 否 |  |  |
| 15 | sub_acct_type | 否 |  |  |
| 16 | sub_acct_classify | 否 |  |  |
| 17 | sub_acct_num | 否 |  |  |
| 18 | sub_acct_alias | 否 |  |  |
| 19 | position_str | 否 |  |  |
| 20 | transaction_no | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_subfundaccount | ART | 是 | sub_fund_account, sub_fund_account |
| idx_subfundaccount_id | ART | 是 | client_id, client_id |
| idx_subfundaccount_acct | ART | 是 | fund_account, fund_account |
| idx_subfundaccount_pos | ART | 是 | position_str, position_str |
| idx_subfundaccount | ART | 是 | sub_fund_account, sub_fund_account |
| idx_subfundaccount_id | ART | 是 | client_id, client_id |
| idx_subfundaccount_acct | ART | 是 | fund_account, fund_account |
| idx_subfundaccount_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_subfundaccount | sub_fund_account, sub_fund_account |
| idx_subfundaccount | sub_fund_account, sub_fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:25:30 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-26 19:51:09 | 3.0.2.48 | 张明月 | 物理表uses_sub_fund_account，添加了表字段(transaction_no);
 |
| 2024-09-23 17:06:31 | 3.0.2.48 | 张明月 | 新增 |
| 2026-03-09 14:25:30 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-26 19:51:09 | 3.0.2.48 | 张明月 | 物理表uses_sub_fund_account，添加了表字段(transaction_no);
 |
| 2024-09-23 17:06:31 | 3.0.2.48 | 张明月 | 新增 |

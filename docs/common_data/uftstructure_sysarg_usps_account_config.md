# usps_account_config - 账户号补位规则表

**表对象ID**: 325
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | acctconfig_type | 否 |  |  |
| 3 | account_start | 否 |  |  |
| 4 | account_stop | 否 |  |  |
| 5 | append_number | 否 |  |  |
| 6 | length_need | 否 |  |  |
| 7 | config_type | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | acctconfig_type | 否 |  |  |
| 11 | account_start | 否 |  |  |
| 12 | account_stop | 否 |  |  |
| 13 | append_number | 否 |  |  |
| 14 | length_need | 否 |  |  |
| 15 | config_type | 否 |  |  |
| 16 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_accountconfig | ART | 是 | branch_no, acctconfig_type, account_start, account_stop, branch_no, acctconfig_type, account_start, account_stop |
| idx_accountconfig | ART | 是 | branch_no, acctconfig_type, account_start, account_stop, branch_no, acctconfig_type, account_start, account_stop |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_accountconfig | branch_no, acctconfig_type, account_start, account_stop, branch_no, acctconfig_type, account_start, account_stop |
| idx_accountconfig | branch_no, acctconfig_type, account_start, account_stop, branch_no, acctconfig_type, account_start, account_stop |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-09-26 19:52:20 | 3.0.3.14 | 张明月 | 物理表usps_account_config，添加了表字段(transaction_no);
 |
| 2024-09-23 15:37:41 | 3.0.3.12 | 张明月 | 新增 |
| 2024-09-26 19:52:20 | 3.0.3.14 | 张明月 | 物理表usps_account_config，添加了表字段(transaction_no);
 |
| 2024-09-23 15:37:41 | 3.0.3.12 | 张明月 | 新增 |

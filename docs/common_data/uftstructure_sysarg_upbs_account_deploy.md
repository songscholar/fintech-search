# upbs_account_deploy - 账户部署表

**表对象ID**: 362
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | sysnode_id | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | sysnode_id | 否 |  |  |
| 8 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_accountdeploy | ART | 是 | fund_account, fund_account |
| idx_accountdeploy | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_accountdeploy | fund_account, fund_account |
| idx_accountdeploy | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-01-13 11:03:29 | 3.0.2.51 | 董乾坤 | 新增 |
| 2025-01-13 11:03:29 | 3.0.2.51 | 董乾坤 | 新增 |

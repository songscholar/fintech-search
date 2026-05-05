# usps_acct_assinfo - 账户辅助信息表

**表对象ID**: 60
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 4 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | sysnode_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | sysnode_id | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_acct_assinfo | ART | 是 | fund_account, fund_account |
| idx_usps_acct_assinfo | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_acct_assinfo | fund_account, fund_account |
| idx_usps_acct_assinfo | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-09-09 11:03:45 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2024-09-09 11:03:45 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

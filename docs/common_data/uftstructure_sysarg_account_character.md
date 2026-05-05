# account_character - 账户特征信息表

**表对象ID**: 144
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | account_character_str | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | asset_prop | 否 |  |  |
| 5 | update_date | 否 |  |  |
| 6 | update_time | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | account_character_str | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | asset_prop | 否 |  |  |
| 12 | update_date | 否 |  |  |
| 13 | update_time | 否 |  |  |
| 14 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_accountcharacter | 默认 | 否 |  |
| idx_accountcharacter | ART | 是 | fund_account, fund_account |
| idx_accountcharacter | 默认 | 否 |  |
| idx_accountcharacter | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_accountcharacter | fund_account, fund_account |
| idx_accountcharacter | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:32:58 | 3.0.2.103 | taocong45644 | 当前表account_character，修改了索引idx_accountcharacter,索引字段修改为：(fund... |
| 2025-04-23 16:59:45 | 3.0.6.133 | 常行 | 新增表 |
| 2025-12-01 14:32:58 | 3.0.2.103 | taocong45644 | 当前表account_character，修改了索引idx_accountcharacter,索引字段修改为：(fund... |
| 2025-04-23 16:59:45 | 3.0.6.133 | 常行 | 新增表 |

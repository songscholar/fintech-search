# income_accttraderrel - 固收客户交易员关系表

**表对象ID**: 2335
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | trader_id | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | branch_no | 否 |  |  |
| 9 | client_id | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | trader_id | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | update_date | 否 |  |  |
| 14 | update_time | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_incomeaccttraderrel | 默认 | 否 |  |
| idx_incomeaccttraderrel | ART | 是 | fund_account, fund_account |
| idx_incomeaccttraderrel | 默认 | 否 |  |
| idx_incomeaccttraderrel | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_incomeaccttraderrel | fund_account, fund_account |
| idx_incomeaccttraderrel | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:29:37 | V3.0.2.78 | taocong45644 | 当前表income_accttraderrel，修改了索引idx_incomeaccttraderrel,索引字段修改为... |
| 2025-02-19 16:45:04 | V3.0.5.1010 | 李想 | 物理表income_accttraderrel，添加了表字段(update_date);
物理表income_acct... |
| 2024-08-06 19:25:47 | V3.0.2.1004 | 骆鹏程 | 新增 |
| 2026-03-04 15:29:37 | V3.0.2.78 | taocong45644 | 当前表income_accttraderrel，修改了索引idx_incomeaccttraderrel,索引字段修改为... |
| 2025-02-19 16:45:04 | V3.0.5.1010 | 李想 | 物理表income_accttraderrel，添加了表字段(update_date);
物理表income_acct... |
| 2024-08-06 19:25:47 | V3.0.2.1004 | 骆鹏程 | 新增 |

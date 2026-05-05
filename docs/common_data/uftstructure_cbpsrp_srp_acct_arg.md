# srp_acct_arg - 股票质押客户综合设置表

**表对象ID**: 2608
**所属模块**: cbpsrp
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | money_type | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | interest_period_type | 否 |  |  |
| 6 | en_entrust_way | 否 |  |  |
| 7 | srprepay_order | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | position_str | 否 |  | fund_account(18)+money_type(3) |
| 12 | branch_no | 否 |  |  |
| 13 | money_type | 否 |  |  |
| 14 | fund_account | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | interest_period_type | 否 |  |  |
| 17 | en_entrust_way | 否 |  |  |
| 18 | srprepay_order | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | position_str | 否 |  | fund_account(18)+money_type(3) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpacctarg | ART | 是 | fund_account, money_type, fund_account, money_type |
| idx_srpacctarg | ART | 是 | fund_account, money_type, fund_account, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpacctarg | fund_account, money_type, fund_account, money_type |
| idx_srpacctarg | fund_account, money_type, fund_account, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:46:56 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-05-19 17:35:14 | 3.0.3.12 | 常行 | 物理表srp_acct_arg，添加了表字段(update_date);
物理表srp_acct_arg，添加了表字段... |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:21:39 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:46:56 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-05-19 17:35:14 | 3.0.3.12 | 常行 | 物理表srp_acct_arg，添加了表字段(update_date);
物理表srp_acct_arg，添加了表字段... |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:21:39 | 3.0.3.1 | wuxd | 新增 |

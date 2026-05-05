# arp_fixed_rate - 约定购回固定利率表

**表对象ID**: 2529
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | money_type | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | fixed_ratio | 否 |  |  |
| 6 | valid_date | 否 |  |  |
| 7 | rate_mode | 否 |  |  |
| 8 | cbpacct_type | 否 |  |  |
| 9 | transaction_no | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | money_type | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | client_id | 否 |  |  |
| 14 | fixed_ratio | 否 |  |  |
| 15 | valid_date | 否 |  |  |
| 16 | rate_mode | 否 |  |  |
| 17 | cbpacct_type | 否 |  |  |
| 18 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arpfixedrate | ART | 是 | fund_account, money_type, cbpacct_type, fund_account, money_type, cbpacct_type |
| idx_arpfixedrate | ART | 是 | fund_account, money_type, cbpacct_type, fund_account, money_type, cbpacct_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_arpfixedrate | fund_account, money_type, cbpacct_type, fund_account, money_type, cbpacct_type |
| idx_arpfixedrate | fund_account, money_type, cbpacct_type, fund_account, money_type, cbpacct_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:19:33 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2026-03-04 16:19:33 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |

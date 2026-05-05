# arp_stk_used_rate - 约定购回用券利率表

**表对象ID**: 2535
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stkused_year_rate | 否 |  |  |
| 5 | valid_date | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | stkused_year_rate | 否 |  |  |
| 11 | valid_date | 否 |  |  |
| 12 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arpstkusedrate | ART | 是 | fund_account, exchange_type, stock_code, valid_date, fund_account, exchange_type, stock_code, valid_date |
| idx_arpstkusedrate | ART | 是 | fund_account, exchange_type, stock_code, valid_date, fund_account, exchange_type, stock_code, valid_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_arpstkusedrate | fund_account, exchange_type, stock_code, valid_date, fund_account, exchange_type, stock_code, valid_date |
| idx_arpstkusedrate | fund_account, exchange_type, stock_code, valid_date, fund_account, exchange_type, stock_code, valid_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:22:24 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2026-03-04 16:22:24 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |

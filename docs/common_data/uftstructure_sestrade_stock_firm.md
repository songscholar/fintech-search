# stock_firm - 沪B境外账户结算会员

**表对象ID**: 5529
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | firm_id | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | firm_id | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stock_firm | ART | 是 | fund_account, exchange_type, stock_account, firm_id, fund_account, exchange_type, stock_account, firm_id |
| idx_stock_firm | ART | 是 | fund_account, exchange_type, stock_account, firm_id, fund_account, exchange_type, stock_account, firm_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stock_firm | fund_account, exchange_type, stock_account, firm_id, fund_account, exchange_type, stock_account, firm_id |
| idx_stock_firm | fund_account, exchange_type, stock_account, firm_id, fund_account, exchange_type, stock_account, firm_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:48:47 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-09 11:14:08 | 3.0.2.43 | 杨森峰 | 表属性调整为不回库 |
| 2026-03-09 13:48:47 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-09 11:14:08 | 3.0.2.43 | 杨森峰 | 表属性调整为不回库 |

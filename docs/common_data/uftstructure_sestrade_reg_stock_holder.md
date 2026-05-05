# reg_stock_holder - 证券指定交易信息表

**表对象ID**: 5539
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | regflag | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | stock_account | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | regflag | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_reg_stock_holder | ART | 是 | fund_account, stock_account, exchange_type, fund_account, stock_account, exchange_type |
| idx_reg_stock_holder | ART | 是 | fund_account, stock_account, exchange_type, fund_account, stock_account, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_reg_stock_holder | fund_account, stock_account, exchange_type, fund_account, stock_account, exchange_type |
| idx_reg_stock_holder | fund_account, stock_account, exchange_type, fund_account, stock_account, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:53:08 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-06-19 20:51:53 | 3.0.2.21 | 董乾坤 | 物理表reg_stock_holder，添加了表字段(fund_account);
物理表reg_stock_hold... |
| 2026-03-09 13:53:08 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-06-19 20:51:53 | 3.0.2.21 | 董乾坤 | 物理表reg_stock_holder，添加了表字段(fund_account);
物理表reg_stock_hold... |

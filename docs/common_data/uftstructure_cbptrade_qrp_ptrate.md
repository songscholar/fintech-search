# qrp_ptrate - 报价回购提前终止收益率表

**表对象ID**: 2323
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | preterm_year_rate | 否 |  |  |
| 5 | company_no | 否 |  |  |
| 6 | hold_days | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | init_date | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | preterm_year_rate | 否 |  |  |
| 12 | company_no | 否 |  |  |
| 13 | hold_days | 否 |  |  |
| 14 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_qrpptrate | 默认 | 否 |  |
| idx_qrpptrate | ART | 是 | init_date, exchange_type, stock_code, company_no, hold_days, init_date, exchange_type, stock_code, company_no, hold_days |
| idx_qrpptrate | 默认 | 否 |  |
| idx_qrpptrate | ART | 是 | init_date, exchange_type, stock_code, company_no, hold_days, init_date, exchange_type, stock_code, company_no, hold_days |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_qrpptrate | init_date, exchange_type, stock_code, company_no, hold_days, init_date, exchange_type, stock_code, company_no, hold_days |
| idx_qrpptrate | init_date, exchange_type, stock_code, company_no, hold_days, init_date, exchange_type, stock_code, company_no, hold_days |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:23:12 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2024-08-06 10:25:47 | V3.0.2.1003 | 骆鹏程 | 新增 |
| 2026-03-04 15:23:12 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2024-08-06 10:25:47 | V3.0.2.1003 | 骆鹏程 | 新增 |

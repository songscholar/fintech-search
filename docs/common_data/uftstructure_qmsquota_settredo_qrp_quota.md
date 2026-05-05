# settredo_qrp_quota - 清算重做入账报价回购额度控制表

**表对象ID**: 2669
**所属模块**: qmsquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | qrp_impawn_balance | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | company_no | 否 |  |  |
| 5 | sett_batch_no | 否 |  |  |
| 6 | qrp_impawn_balance | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | company_no | 否 |  |  |
| 10 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_qrp_quota | ART | 是 | sett_batch_no, stock_code, exchange_type, company_no, sett_batch_no, stock_code, exchange_type, company_no |
| idx_settredo_qrp_quota | ART | 是 | sett_batch_no, stock_code, exchange_type, company_no, sett_batch_no, stock_code, exchange_type, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_qrp_quota | sett_batch_no, stock_code, exchange_type, company_no, sett_batch_no, stock_code, exchange_type, company_no |
| idx_settredo_qrp_quota | sett_batch_no, stock_code, exchange_type, company_no, sett_batch_no, stock_code, exchange_type, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 17:04:39 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-08-04 15:55:07 | 8.26.2.91 | 马天宇 | 新建表结构 |
| 2026-03-05 17:04:39 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-08-04 15:55:07 | 8.26.2.91 | 马天宇 | 新建表结构 |

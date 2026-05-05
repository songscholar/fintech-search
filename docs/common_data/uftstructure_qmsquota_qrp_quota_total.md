# qrp_quota_total - 报价回购额度汇总表

**表对象ID**: 1598
**所属模块**: qmsquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | uncome_term_balance_total | 否 |  |  |
| 5 | uncome_buyterm_balance_total | 否 |  |  |
| 6 | postpone_entrust_balance_total | 否 |  |  |
| 7 | postpone_cancel_balance_total | 否 |  |  |
| 8 | company_no | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | uncome_term_balance_total | 否 |  |  |
| 12 | uncome_buyterm_balance_total | 否 |  |  |
| 13 | postpone_entrust_balance_total | 否 |  |  |
| 14 | postpone_cancel_balance_total | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_qrp_quota_total | ART | 是 | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |
| idx_qrp_quota_total | ART | 是 | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_qrp_quota_total | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |
| idx_qrp_quota_total | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 17:03:17 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2024-09-09 16:26:11 | 3.0.2.3 | 张云焘 | 新增 |
| 2026-03-05 17:03:17 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2024-09-09 16:26:11 | 3.0.2.3 | 张云焘 | 新增 |

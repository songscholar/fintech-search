# qrp_quota - 报价回购额度控制表

**表对象ID**: 1597
**所属模块**: qmsquota
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | qrp_approv_quota | 否 |  |  |
| 5 | qrp_actual_quota | 否 |  |  |
| 6 | qrp_impawn_balance | 否 |  |  |
| 7 | qrp_buy_quota | 否 |  |  |
| 8 | qrp_term_quota | 否 |  |  |
| 9 | qrp_huge_ratio | 否 |  |  |
| 10 | qrp_buy_balance | 否 |  |  |
| 11 | qrp_term_balance | 否 |  |  |
| 12 | qrp_undue_balance | 否 |  |  |
| 13 | qrp_due_balance | 否 |  |  |
| 14 | company_no | 否 |  |  |
| 15 | modify_date | 否 |  |  |
| 16 | cash_balance | 否 |  |  |
| 17 | qrp_day_orderup_quota | 否 |  |  |
| 18 | qrp_sum_uncomebalance_limit | 否 |  |  |
| 19 | exclusive_quota_flag | 否 |  |  |
| 20 | exclusive_quota_endtime | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | init_date | 否 |  |  |
| 23 | exchange_type | 否 |  |  |
| 24 | stock_code | 否 |  |  |
| 25 | qrp_approv_quota | 否 |  |  |
| 26 | qrp_actual_quota | 否 |  |  |
| 27 | qrp_impawn_balance | 否 |  |  |
| 28 | qrp_buy_quota | 否 |  |  |
| 29 | qrp_term_quota | 否 |  |  |
| 30 | qrp_huge_ratio | 否 |  |  |
| 31 | qrp_buy_balance | 否 |  |  |
| 32 | qrp_term_balance | 否 |  |  |
| 33 | qrp_undue_balance | 否 |  |  |
| 34 | qrp_due_balance | 否 |  |  |
| 35 | company_no | 否 |  |  |
| 36 | modify_date | 否 |  |  |
| 37 | cash_balance | 否 |  |  |
| 38 | qrp_day_orderup_quota | 否 |  |  |
| 39 | qrp_sum_uncomebalance_limit | 否 |  |  |
| 40 | exclusive_quota_flag | 否 |  |  |
| 41 | exclusive_quota_endtime | 否 |  |  |
| 42 | transaction_no | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_qrp_quota | ART | 是 | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |
| idx_qrp_quota_company | ART | 是 | company_no, company_no |
| uk_rpt_qrpquota | ART | 是 | init_date, stock_code, exchange_type, company_no, init_date, stock_code, exchange_type, company_no |
| idx_qrp_quota | ART | 是 | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |
| idx_qrp_quota_company | ART | 是 | company_no, company_no |
| uk_rpt_qrpquota | ART | 是 | init_date, stock_code, exchange_type, company_no, init_date, stock_code, exchange_type, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_qrp_quota | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |
| idx_qrp_quota | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 17:02:54 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-22 09:43:53 | 3.0.2.4 | 洪略 | 维护历史信息 |
| 2025-07-18 10:17:01 | 3.0.5.1002 | 袁文龙 | 勾选不回库 |
| 2024-09-28 15:53:36 | 3.0.2.4 | 骆鹏程 | 新增事务号 |
| 2024-09-05 13:21:48 | 3.0.2.2 | 曾剑辉 | 物理表qrp_quota，删除了表字段(transaction_no);
 |
| 2024-08-15 15:32:30 | 3.0.2.1 | weill | 新增表结构 |
| 2026-03-05 17:02:54 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-22 09:43:53 | 3.0.2.4 | 洪略 | 维护历史信息 |
| 2025-07-18 10:17:01 | 3.0.5.1002 | 袁文龙 | 勾选不回库 |
| 2024-09-28 15:53:36 | 3.0.2.4 | 骆鹏程 | 新增事务号 |
| 2024-09-05 13:21:48 | 3.0.2.2 | 曾剑辉 | 物理表qrp_quota，删除了表字段(transaction_no);
 |
| 2024-08-15 15:32:30 | 3.0.2.1 | weill | 新增表结构 |

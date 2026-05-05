# finexe_quota - 融资行权额度表

**表对象ID**: 1502
**所属模块**: qmsquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | net_capital | 否 |  |  |
| 3 | finexe_actual_scale | 否 |  |  |
| 4 | finexe_uncome_scale | 否 |  |  |
| 5 | finexe_entrust_scale | 否 |  |  |
| 6 | stock_conc_ratio | 否 |  |  |
| 7 | client_conc_ratio | 否 |  |  |
| 8 | interest_cycle | 否 |  |  |
| 9 | finexe_max_days | 否 |  |  |
| 10 | min_interest_days | 否 |  |  |
| 11 | company_no | 否 |  |  |
| 12 | net_capital | 否 |  |  |
| 13 | finexe_actual_scale | 否 |  |  |
| 14 | finexe_uncome_scale | 否 |  |  |
| 15 | finexe_entrust_scale | 否 |  |  |
| 16 | stock_conc_ratio | 否 |  |  |
| 17 | client_conc_ratio | 否 |  |  |
| 18 | interest_cycle | 否 |  |  |
| 19 | finexe_max_days | 否 |  |  |
| 20 | min_interest_days | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_finexe_quota | 默认 | 否 |  |
| idx_finexe_quota | ART | 是 | company_no, company_no |
| idx_finexe_quota | 默认 | 否 |  |
| idx_finexe_quota | ART | 是 | company_no, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_finexe_quota | company_no, company_no |
| idx_finexe_quota | company_no, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:59:17 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:56:13 | 3.0.2.5 | taocong45644 | 当前表finexe_quota，修改了索引idx_finexe_quota,索引字段修改为：(company_no),索... |
| 2025-03-11 16:09:11 | V3.0.2.2001 | 蒋浩宇 | 新增表结构 |
| 2026-03-05 16:59:17 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:56:13 | 3.0.2.5 | taocong45644 | 当前表finexe_quota，修改了索引idx_finexe_quota,索引字段修改为：(company_no),索... |
| 2025-03-11 16:09:11 | V3.0.2.2001 | 蒋浩宇 | 新增表结构 |

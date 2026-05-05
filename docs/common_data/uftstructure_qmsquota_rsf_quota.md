# rsf_quota - 限制性股票融资额度表

**表对象ID**: 1507
**所属模块**: qmsquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | net_capital | 否 |  |  |
| 3 | rsf_approved_quota | 否 |  |  |
| 4 | rsf_actual_quota | 否 |  |  |
| 5 | rsf_uncome_scale | 否 |  |  |
| 6 | rsf_entrust_scale | 否 |  |  |
| 7 | stock_conc_ratio | 否 |  |  |
| 8 | client_conc_ratio | 否 |  |  |
| 9 | min_interest_days | 否 |  |  |
| 10 | interest_cycle | 否 |  |  |
| 11 | company_no | 否 |  |  |
| 12 | net_capital | 否 |  |  |
| 13 | rsf_approved_quota | 否 |  |  |
| 14 | rsf_actual_quota | 否 |  |  |
| 15 | rsf_uncome_scale | 否 |  |  |
| 16 | rsf_entrust_scale | 否 |  |  |
| 17 | stock_conc_ratio | 否 |  |  |
| 18 | client_conc_ratio | 否 |  |  |
| 19 | min_interest_days | 否 |  |  |
| 20 | interest_cycle | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_rsfquota | 默认 | 否 |  |
| idx_rsfquota | ART | 是 | company_no, company_no |
| idx_rsfquota | 默认 | 否 |  |
| idx_rsfquota | ART | 是 | company_no, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_rsfquota | company_no, company_no |
| idx_rsfquota | company_no, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 17:01:18 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:05:33 | 3.0.2.5 | taocong45644 | 当前表rsf_quota，修改了索引idx_rsfquota,索引字段修改为：(company_no),索引唯一性修改为... |
| 2025-05-22 17:05:07 | 3.0.2.2003 | 宋作强 | 新增 |
| 2026-03-05 17:01:18 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:05:33 | 3.0.2.5 | taocong45644 | 当前表rsf_quota，修改了索引idx_rsfquota,索引字段修改为：(company_no),索引唯一性修改为... |
| 2025-05-22 17:05:07 | 3.0.2.2003 | 宋作强 | 新增 |

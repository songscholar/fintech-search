# finexe_stk_quota - 融资行权证券额度表

**表对象ID**: 1501
**所属模块**: qmsquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | sopt_code | 否 |  |  |
| 4 | total_quota | 否 |  |  |
| 5 | enable_quota_ratio | 否 |  |  |
| 6 | company_no | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | sopt_code | 否 |  |  |
| 9 | total_quota | 否 |  |  |
| 10 | enable_quota_ratio | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_finexe_stk_quota | 默认 | 否 |  |
| idx_finexe_stk_quota | ART | 是 | company_no, exchange_type, sopt_code, company_no, exchange_type, sopt_code |
| idx_finexe_stk_quota | 默认 | 否 |  |
| idx_finexe_stk_quota | ART | 是 | company_no, exchange_type, sopt_code, company_no, exchange_type, sopt_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_finexe_stk_quota | company_no, exchange_type, sopt_code, company_no, exchange_type, sopt_code |
| idx_finexe_stk_quota | company_no, exchange_type, sopt_code, company_no, exchange_type, sopt_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:58:53 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:56:45 | 3.0.2.5 | taocong45644 | 当前表finexe_stk_quota，修改了索引idx_finexe_stk_quota,索引字段修改为：(compa... |
| 2025-03-11 16:09:11 | V3.0.2.2001 | 蒋浩宇 | 新增表结构 |
| 2026-03-05 16:58:53 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:56:45 | 3.0.2.5 | taocong45644 | 当前表finexe_stk_quota，修改了索引idx_finexe_stk_quota,索引字段修改为：(compa... |
| 2025-03-11 16:09:11 | V3.0.2.2001 | 蒋浩宇 | 新增表结构 |

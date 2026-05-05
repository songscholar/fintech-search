# srp_quota - 股票质押额度表

**表对象ID**: 1500
**所属模块**: qmsquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | srp_kind | 否 |  |  |
| 4 | net_capital | 否 |  |  |
| 5 | srp_approved_quota | 否 |  |  |
| 6 | srp_actual_quota | 否 |  |  |
| 7 | stock_conc_ratio | 否 |  |  |
| 8 | client_conc_ratio | 否 |  |  |
| 9 | srp_one_down_limit | 否 |  |  |
| 10 | srp_one_up_limit | 否 |  |  |
| 11 | srp_uncome_scale | 否 |  |  |
| 12 | srp_entrust_scale | 否 |  |  |
| 13 | srp_max_days | 否 |  |  |
| 14 | min_interest_days | 否 |  |  |
| 15 | interest_cycle | 否 |  |  |
| 16 | assetmg_actual_quota | 否 |  |  |
| 17 | assetmg_entrust_scale | 否 |  |  |
| 18 | assetmg_uncome_scale | 否 |  |  |
| 19 | join_down_limit | 否 |  |  |
| 20 | self_client_conc_ratio | 否 |  |  |
| 21 | credit_quota | 否 |  |  |
| 22 | company_no | 否 |  |  |
| 23 | exchange_type | 否 |  |  |
| 24 | srp_kind | 否 |  |  |
| 25 | net_capital | 否 |  |  |
| 26 | srp_approved_quota | 否 |  |  |
| 27 | srp_actual_quota | 否 |  |  |
| 28 | stock_conc_ratio | 否 |  |  |
| 29 | client_conc_ratio | 否 |  |  |
| 30 | srp_one_down_limit | 否 |  |  |
| 31 | srp_one_up_limit | 否 |  |  |
| 32 | srp_uncome_scale | 否 |  |  |
| 33 | srp_entrust_scale | 否 |  |  |
| 34 | srp_max_days | 否 |  |  |
| 35 | min_interest_days | 否 |  |  |
| 36 | interest_cycle | 否 |  |  |
| 37 | assetmg_actual_quota | 否 |  |  |
| 38 | assetmg_entrust_scale | 否 |  |  |
| 39 | assetmg_uncome_scale | 否 |  |  |
| 40 | join_down_limit | 否 |  |  |
| 41 | self_client_conc_ratio | 否 |  |  |
| 42 | credit_quota | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srp_quota | 默认 | 否 |  |
| idx_srp_quota | ART | 是 | exchange_type, srp_kind, company_no, exchange_type, srp_kind, company_no |
| idx_srp_quota | 默认 | 否 |  |
| idx_srp_quota | ART | 是 | exchange_type, srp_kind, company_no, exchange_type, srp_kind, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srp_quota | exchange_type, srp_kind, company_no, exchange_type, srp_kind, company_no |
| idx_srp_quota | exchange_type, srp_kind, company_no, exchange_type, srp_kind, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:58:27 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:09:44 | 3.0.2.5 | taocong45644 | 当前表srp_quota，修改了索引idx_srp_quota,索引字段修改为：(exchange_type,srp_k... |
| 2025-03-11 16:09:11 | V3.0.2.2001 | 蒋浩宇 | 新增表结构 |
| 2026-03-05 16:58:27 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:09:44 | 3.0.2.5 | taocong45644 | 当前表srp_quota，修改了索引idx_srp_quota,索引字段修改为：(exchange_type,srp_k... |
| 2025-03-11 16:09:11 | V3.0.2.2001 | 蒋浩宇 | 新增表结构 |

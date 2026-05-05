# arp_quota - 约定购回额度表

**表对象ID**: 1504
**所属模块**: qmsquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | company_no | 否 |  |  |
| 3 | net_capital | 否 |  |  |
| 4 | arp_approv_quota | 否 |  |  |
| 5 | arp_actual_quota | 否 |  |  |
| 6 | stock_conc_ratio | 否 |  |  |
| 7 | client_conc_ratio | 否 |  |  |
| 8 | arp_one_down_limit | 否 |  |  |
| 9 | arp_one_up_limit | 否 |  |  |
| 10 | margin_focus_ratio | 否 |  |  |
| 11 | margin_alert_ratio | 否 |  |  |
| 12 | margin_treat_ratio | 否 |  |  |
| 13 | arp_uncome_scale | 否 |  |  |
| 14 | arp_entrust_scale | 否 |  |  |
| 15 | fixed_ratio | 否 |  |  |
| 16 | arp_max_days | 否 |  |  |
| 17 | supply_balance | 否 |  |  |
| 18 | min_interest_days | 否 |  |  |
| 19 | interest_cycle | 否 |  |  |
| 20 | exchange_type | 否 |  |  |
| 21 | company_no | 否 |  |  |
| 22 | net_capital | 否 |  |  |
| 23 | arp_approv_quota | 否 |  |  |
| 24 | arp_actual_quota | 否 |  |  |
| 25 | stock_conc_ratio | 否 |  |  |
| 26 | client_conc_ratio | 否 |  |  |
| 27 | arp_one_down_limit | 否 |  |  |
| 28 | arp_one_up_limit | 否 |  |  |
| 29 | margin_focus_ratio | 否 |  |  |
| 30 | margin_alert_ratio | 否 |  |  |
| 31 | margin_treat_ratio | 否 |  |  |
| 32 | arp_uncome_scale | 否 |  |  |
| 33 | arp_entrust_scale | 否 |  |  |
| 34 | fixed_ratio | 否 |  |  |
| 35 | arp_max_days | 否 |  |  |
| 36 | supply_balance | 否 |  |  |
| 37 | min_interest_days | 否 |  |  |
| 38 | interest_cycle | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arp_quota | 默认 | 否 |  |
| idx_arp_quota | ART | 是 | exchange_type, company_no, exchange_type, company_no |
| idx_arp_quota | 默认 | 否 |  |
| idx_arp_quota | ART | 是 | exchange_type, company_no, exchange_type, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_arp_quota | exchange_type, company_no, exchange_type, company_no |
| idx_arp_quota | exchange_type, company_no, exchange_type, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 17:00:06 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:54:09 | 3.0.2.5 | taocong45644 | 当前表arp_quota，修改了索引idx_arp_quota,索引字段修改为：(exchange_type,compa... |
| 2025-03-04 19:22:05 | 3.0.2.2001 | tongck54118 | 物理表arp_quota，增加索引(idx_arp_quota:[exchange_type,company_no]); |
| 2025-03-04 19:18:22 | 3.0.2.2001 | tongck54118 | 物理表arp_quota，添加了表字段(exchange_type);
物理表arp_quota，添加了表字段(com... |
| 2026-03-05 17:00:06 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:54:09 | 3.0.2.5 | taocong45644 | 当前表arp_quota，修改了索引idx_arp_quota,索引字段修改为：(exchange_type,compa... |
| 2025-03-04 19:22:05 | 3.0.2.2001 | tongck54118 | 物理表arp_quota，增加索引(idx_arp_quota:[exchange_type,company_no]); |
| 2025-03-04 19:18:22 | 3.0.2.2001 | tongck54118 | 物理表arp_quota，添加了表字段(exchange_type);
物理表arp_quota，添加了表字段(com... |

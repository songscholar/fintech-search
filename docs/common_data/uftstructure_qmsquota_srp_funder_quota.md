# srp_funder_quota - 股票质押融出方产品额度表

**表对象ID**: 1503
**所属模块**: qmsquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | funder_no | 否 |  |  |
| 2 | srp_kind | 否 |  |  |
| 3 | total_quota | 否 |  |  |
| 4 | used_quota | 否 |  |  |
| 5 | today_actual_quota | 否 |  |  |
| 6 | today_entrust_scale | 否 |  |  |
| 7 | adv_entrust_quota | 否 |  |  |
| 8 | adv_entrust_scale | 否 |  |  |
| 9 | funder_no | 否 |  |  |
| 10 | srp_kind | 否 |  |  |
| 11 | total_quota | 否 |  |  |
| 12 | used_quota | 否 |  |  |
| 13 | today_actual_quota | 否 |  |  |
| 14 | today_entrust_scale | 否 |  |  |
| 15 | adv_entrust_quota | 否 |  |  |
| 16 | adv_entrust_scale | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srp_funder_quota | 默认 | 否 |  |
| idx_srp_funder_quota | ART | 是 | funder_no, srp_kind, funder_no, srp_kind |
| idx_srp_funder_quota | 默认 | 否 |  |
| idx_srp_funder_quota | ART | 是 | funder_no, srp_kind, funder_no, srp_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srp_funder_quota | funder_no, srp_kind, funder_no, srp_kind |
| idx_srp_funder_quota | funder_no, srp_kind, funder_no, srp_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:59:42 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:08:01 | 3.0.2.5 | taocong45644 | 当前表srp_funder_quota，修改了索引idx_srp_funder_quota,索引字段修改为：(funde... |
| 2025-03-11 16:09:11 | V3.0.2.2001 | 蒋浩宇 | 新增表结构 |
| 2026-03-05 16:59:42 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:08:01 | 3.0.2.5 | taocong45644 | 当前表srp_funder_quota，修改了索引idx_srp_funder_quota,索引字段修改为：(funde... |
| 2025-03-11 16:09:11 | V3.0.2.2001 | 蒋浩宇 | 新增表结构 |

# arp_funder - 约定购回融出方信息表

**表对象ID**: 2668
**所属模块**: qmsquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | funder_no | 否 |  |  |
| 3 | funder_name | 否 |  |  |
| 4 | pledgee_type | 否 |  |  |
| 5 | pledgee_name | 否 |  |  |
| 6 | funder_type | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | seat_no | 否 |  |  |
| 9 | treat_account | 否 |  |  |
| 10 | treat_seat_no | 否 |  |  |
| 11 | sz_client_account | 否 |  |  |
| 12 | sz_client_seat_no | 否 |  |  |
| 13 | sz_organ_account | 否 |  |  |
| 14 | sz_organ_seat_no | 否 |  |  |
| 15 | sz_treat_account | 否 |  |  |
| 16 | sz_treat_seat_no | 否 |  |  |
| 17 | last_agree_version | 否 |  |  |
| 18 | min_agree_version | 否 |  |  |
| 19 | total_quota | 否 |  |  |
| 20 | used_quota | 否 |  |  |
| 21 | status | 否 |  |  |
| 22 | company_no | 否 |  |  |
| 23 | funder_no | 否 |  |  |
| 24 | funder_name | 否 |  |  |
| 25 | pledgee_type | 否 |  |  |
| 26 | pledgee_name | 否 |  |  |
| 27 | funder_type | 否 |  |  |
| 28 | stock_account | 否 |  |  |
| 29 | seat_no | 否 |  |  |
| 30 | treat_account | 否 |  |  |
| 31 | treat_seat_no | 否 |  |  |
| 32 | sz_client_account | 否 |  |  |
| 33 | sz_client_seat_no | 否 |  |  |
| 34 | sz_organ_account | 否 |  |  |
| 35 | sz_organ_seat_no | 否 |  |  |
| 36 | sz_treat_account | 否 |  |  |
| 37 | sz_treat_seat_no | 否 |  |  |
| 38 | last_agree_version | 否 |  |  |
| 39 | min_agree_version | 否 |  |  |
| 40 | total_quota | 否 |  |  |
| 41 | used_quota | 否 |  |  |
| 42 | status | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arpfunder | 默认 | 否 |  |
| idx_arpfunder | ART | 是 | funder_no, funder_no |
| idx_arpfunder | 默认 | 否 |  |
| idx_arpfunder | ART | 是 | funder_no, funder_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_arpfunder | funder_no, funder_no |
| idx_arpfunder | funder_no, funder_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 17:04:15 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:52:42 | 3.0.2.5 | taocong45644 | 当前表arp_funder，修改了索引idx_arpfunder,索引字段修改为：(funder_no),索引唯一性修改... |
| 2026-03-05 17:04:15 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:52:42 | 3.0.2.5 | taocong45644 | 当前表arp_funder，修改了索引idx_arpfunder,索引字段修改为：(funder_no),索引唯一性修改... |

# confer_no_log - 约定号记录表

**表对象ID**: 1506
**所属模块**: qmsquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | entrust_prop | 否 |  |  |
| 4 | entrust_bs | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | cbpconfer_id | 否 |  |  |
| 7 | trader_id | 否 |  |  |
| 8 | agency_no | 否 |  |  |
| 9 | oppo_trader_id | 否 |  |  |
| 10 | oppo_agency | 否 |  |  |
| 11 | deal_status | 否 |  |  |
| 12 | init_date | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | entrust_prop | 否 |  |  |
| 15 | entrust_bs | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | cbpconfer_id | 否 |  |  |
| 18 | trader_id | 否 |  |  |
| 19 | agency_no | 否 |  |  |
| 20 | oppo_trader_id | 否 |  |  |
| 21 | oppo_agency | 否 |  |  |
| 22 | deal_status | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_confer_no_log | 默认 | 否 |  |
| idx_confer_no_log | ART | 是 | cbpconfer_id, init_date, cbpconfer_id, init_date |
| idx_confer_no_log | 默认 | 否 |  |
| idx_confer_no_log | ART | 是 | cbpconfer_id, init_date, cbpconfer_id, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_confer_no_log | cbpconfer_id, init_date, cbpconfer_id, init_date |
| idx_confer_no_log | cbpconfer_id, init_date, cbpconfer_id, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 17:00:54 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:55:14 | 3.0.2.5 | taocong45644 | 当前表confer_no_log，修改了索引idx_confer_no_log,索引字段修改为：(cbpconfer_i... |
| 2026-03-05 17:00:54 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:55:14 | 3.0.2.5 | taocong45644 | 当前表confer_no_log，修改了索引idx_confer_no_log,索引字段修改为：(cbpconfer_i... |

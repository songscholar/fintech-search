# uses_sell_frozen_stock - 证券可售冻结股份表

**表对象ID**: 5985
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 44 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_type | 否 |  |  |
| 6 | available_amount | 否 |  |  |
| 7 | seat_no | 否 |  |  |
| 8 | stock_property | 否 |  |  |
| 9 | hkdc_circulate_type | 否 |  |  |
| 10 | date_clear | 否 |  |  |
| 11 | position_str | 否 |  |  |
| 12 | init_date | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_type | 否 |  |  |
| 17 | available_amount | 否 |  |  |
| 18 | seat_no | 否 |  |  |
| 19 | stock_property | 否 |  |  |
| 20 | hkdc_circulate_type | 否 |  |  |
| 21 | date_clear | 否 |  |  |
| 22 | position_str | 否 |  |  |
| 23 | init_date | 否 |  |  |
| 24 | stock_account | 否 |  |  |
| 25 | stock_code | 否 |  |  |
| 26 | exchange_type | 否 |  |  |
| 27 | stock_type | 否 |  |  |
| 28 | available_amount | 否 |  |  |
| 29 | seat_no | 否 |  |  |
| 30 | stock_property | 否 |  |  |
| 31 | hkdc_circulate_type | 否 |  |  |
| 32 | date_clear | 否 |  |  |
| 33 | position_str | 否 |  |  |
| 34 | init_date | 否 |  |  |
| 35 | stock_account | 否 |  |  |
| 36 | stock_code | 否 |  |  |
| 37 | exchange_type | 否 |  |  |
| 38 | stock_type | 否 |  |  |
| 39 | available_amount | 否 |  |  |
| 40 | seat_no | 否 |  |  |
| 41 | stock_property | 否 |  |  |
| 42 | hkdc_circulate_type | 否 |  |  |
| 43 | date_clear | 否 |  |  |
| 44 | position_str | 否 |  |  |

## 索引（共 22 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_sell_frozen_stock | 默认 | 否 |  |
| idx_uses_sell_frozen_stock_pos | 默认 | 否 |  |
| idx_user_sell_frozen_stock_pos | 默认 | 否 |  |
| idx_uses_sell_frozen_stock_pos | 默认 | 否 | position_str, position_str |
| idx_uses_sell_frozen_stock | 默认 | 是 | stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type, stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type |
| idx_uses_sell_frozen_stock_pos | 默认 | 是 | position_str, position_str |
| idx_user_sell_frozen_stock_pos | 默认 | 是 | init_date, position_str, init_date, position_str |
| idx_uses_sell_frozen_stock_pos | 默认 | 否 | position_str, position_str |
| idx_uses_sell_frozen_stock | ART | 是 | stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type, stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type |
| idx_uses_sell_frozen_stock_pos | ART | 是 | position_str, position_str |
| idx_rpt_user_sell_frozen_stock_pos | ART | 是 | init_date, position_str, init_date, position_str |
| idx_uses_sell_frozen_stock | 默认 | 否 |  |
| idx_uses_sell_frozen_stock_pos | 默认 | 否 |  |
| idx_user_sell_frozen_stock_pos | 默认 | 否 |  |
| idx_uses_sell_frozen_stock_pos | 默认 | 否 | position_str, position_str |
| idx_uses_sell_frozen_stock | 默认 | 是 | stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type, stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type |
| idx_uses_sell_frozen_stock_pos | 默认 | 是 | position_str, position_str |
| idx_user_sell_frozen_stock_pos | 默认 | 是 | init_date, position_str, init_date, position_str |
| idx_uses_sell_frozen_stock_pos | 默认 | 否 | position_str, position_str |
| idx_uses_sell_frozen_stock | ART | 是 | stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type, stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type |
| idx_uses_sell_frozen_stock_pos | ART | 是 | position_str, position_str |
| idx_rpt_user_sell_frozen_stock_pos | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_sell_frozen_stock_pos | position_str, position_str |
| idx_uses_sell_frozen_stock_pos | position_str, position_str |
| idx_uses_sell_frozen_stock_pos | position_str, position_str |
| idx_uses_sell_frozen_stock_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:53:04 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:28:55 | V3.0.8.23 | 洪略 | 历史表索引加rpt前缀 |
| 2025-12-01 16:48:39 | 3.0.2.104 | taocong45644 | 当前表uses_sell_frozen_stock，修改了索引idx_uses_sell_frozen_stock,索引... |
| 2025-11-05 18:50:05 | V3.0.1.2 | 洪略 | 添加历史表 |
| 2025-11-05 18:50:05 | V3.0.1.2 | 洪略 | 补齐历史表 |
| 2024-01-05 09:00:31 | 3.0.1.3 |  | 物理表ucrt_sellfrozenstock，增加索引(idx_sellfrozenstock_pos:[positi... |
| 2024-01-05 09:00:31 | 3.0.1.3 |  | 物理表ucrt_sellfrozenstock，增加索引(idx_sellfrozenstock_pos:[positi... |
| 2026-03-09 14:53:04 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:28:55 | V3.0.8.23 | 洪略 | 历史表索引加rpt前缀 |
| 2025-12-01 16:48:39 | 3.0.2.104 | taocong45644 | 当前表uses_sell_frozen_stock，修改了索引idx_uses_sell_frozen_stock,索引... |
| 2025-11-05 18:50:05 | V3.0.1.2 | 洪略 | 添加历史表 |
| 2025-11-05 18:50:05 | V3.0.1.2 | 洪略 | 补齐历史表 |
| 2024-01-05 09:00:31 | 3.0.1.3 |  | 物理表ucrt_sellfrozenstock，增加索引(idx_sellfrozenstock_pos:[positi... |
| 2024-01-05 09:00:31 | 3.0.1.3 |  | 物理表ucrt_sellfrozenstock，增加索引(idx_sellfrozenstock_pos:[positi... |

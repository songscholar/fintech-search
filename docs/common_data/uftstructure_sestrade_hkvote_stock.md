# hkvote_stock - 港股投票份额表

**表对象ID**: 5567
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | current_amount | 否 |  |  |
| 7 | date_clear | 否 |  |  |
| 8 | position_str | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | init_date | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | fund_account | 否 |  |  |
| 14 | stock_account | 否 |  |  |
| 15 | current_amount | 否 |  |  |
| 16 | date_clear | 否 |  |  |
| 17 | position_str | 否 |  |  |
| 18 | remark | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_hkvote_stock_pos | ART | 是 | position_str, position_str |
| idx_hkvote_stock | ART | 是 | exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code, fund_account |
| idx_hkvote_stock_pos | ART | 是 | position_str, position_str |
| idx_hkvote_stock_pos | ART | 是 | position_str, position_str |
| idx_hkvote_stock | ART | 是 | exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code, fund_account |
| idx_hkvote_stock_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_hkvote_stock_pos | position_str, position_str |
| idx_hkvote_stock_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 15:26:20 | V3.0.2.106 | taocong45644 | 当前表hkvote_stock，增加索引（ idx_hkvote_stock_pos:[position_str]）;... |
| 2024-07-26 14:39:10 | 3.0.2.30 | 余世泽 | 新增 |
| 2026-03-09 15:26:20 | V3.0.2.106 | taocong45644 | 当前表hkvote_stock，增加索引（ idx_hkvote_stock_pos:[position_str]）;... |
| 2024-07-26 14:39:10 | 3.0.2.30 | 余世泽 | 新增 |

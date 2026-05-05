# bond_imp_cash_assure - 债券回购现金担保品余额表

**表对象ID**: 2482
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | reserve_account | 否 |  |  |
| 6 | seat_no | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | stock_account | 否 |  |  |
| 9 | cashassure_amount | 否 |  |  |
| 10 | used_fetch_amount | 否 |  |  |
| 11 | position_str | 否 |  | init_date(8)+reserve_account_in(20)+'0'(18)+exchange_type(4) |
| 12 | set_seat_no | 否 |  |  |
| 13 | init_date | 否 |  |  |
| 14 | branch_no | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | fund_account | 否 |  |  |
| 17 | reserve_account | 否 |  |  |
| 18 | seat_no | 否 |  |  |
| 19 | exchange_type | 否 |  |  |
| 20 | stock_account | 否 |  |  |
| 21 | cashassure_amount | 否 |  |  |
| 22 | used_fetch_amount | 否 |  |  |
| 23 | position_str | 否 |  | init_date(8)+reserve_account_in(20)+'0'(18)+exchange_type(4) |
| 24 | set_seat_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_bondimpcashassure_pos | ART | 是 | position_str, position_str |
| idx_bondimpcashassure_acct | ART | 是 | fund_account, stock_account, exchange_type, fund_account, stock_account, exchange_type |
| idx_bondimpcashassure_pos | ART | 是 | position_str, position_str |
| idx_bondimpcashassure_acct | ART | 是 | fund_account, stock_account, exchange_type, fund_account, stock_account, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_bondimpcashassure_pos | position_str, position_str |
| idx_bondimpcashassure_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:47:14 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2024-11-28 10:22:47 | 3.0.2.48 | 王云乾 | 新增 |
| 2026-03-04 15:47:14 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2024-11-28 10:22:47 | 3.0.2.48 | 王云乾 | 新增 |

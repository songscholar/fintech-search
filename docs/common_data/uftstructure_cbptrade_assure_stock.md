# assure_stock - 担保持仓表

**表对象ID**: 2365
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | stock_open_date | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | stock_type | 否 |  |  |
| 9 | assure_type | 否 |  |  |
| 10 | impawn_amount | 否 |  |  |
| 11 | pre_impawn_amount | 否 |  |  |
| 12 | position_str | 否 |  | branch_no(5) +fund_account(18) +exchange_type(4) +stock_acco |
| 13 | remark | 否 |  |  |
| 14 | out_impawn_amount | 否 |  |  |
| 15 | fund_account | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | stock_account | 否 |  |  |
| 18 | stock_open_date | 否 |  |  |
| 19 | branch_no | 否 |  |  |
| 20 | stock_code | 否 |  |  |
| 21 | exchange_type | 否 |  |  |
| 22 | stock_type | 否 |  |  |
| 23 | assure_type | 否 |  |  |
| 24 | impawn_amount | 否 |  |  |
| 25 | pre_impawn_amount | 否 |  |  |
| 26 | position_str | 否 |  | branch_no(5) +fund_account(18) +exchange_type(4) +stock_acco |
| 27 | remark | 否 |  |  |
| 28 | out_impawn_amount | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_assurestock_acct | ART | 是 | fund_account, fund_account |
| idx_assurestock_pos | ART | 是 | position_str, position_str |
| idx_assurestock_acct | ART | 是 | fund_account, fund_account |
| idx_assurestock_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_assurestock_pos | position_str, position_str |
| idx_assurestock_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:42:43 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-03-21 13:41:46 | 3.0.2.54 | 张训华 | 支持二次上场，将idx_assurestock_pos修改为全局唯一索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-09-25 21:37:18 | V3.0.2.1008 | 张明月 | 新增 |
| 2026-03-04 15:42:43 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-03-21 13:41:46 | 3.0.2.54 | 张训华 | 支持二次上场，将idx_assurestock_pos修改为全局唯一索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-09-25 21:37:18 | V3.0.2.1008 | 张明月 | 新增 |

# qrp_undue_pawn - 未到期报价回购质押明细表

**表对象ID**: 2341
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | self_stock_account | 否 |  |  |
| 7 | report_account | 否 |  |  |
| 8 | stock_account | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | entrust_amount | 否 |  |  |
| 11 | entrust_balance | 否 |  |  |
| 12 | impawn_code | 否 |  |  |
| 13 | impawn_amount | 否 |  |  |
| 14 | entrust_date | 否 |  |  |
| 15 | entrust_no | 否 |  |  |
| 16 | business_no | 否 |  |  |
| 17 | business_id | 否 |  |  |
| 18 | impawn_status | 否 |  |  |
| 19 | position_str | 否 |  |  |
| 20 | init_date | 否 |  |  |
| 21 | serial_no | 否 |  |  |
| 22 | client_id | 否 |  |  |
| 23 | fund_account | 否 |  |  |
| 24 | exchange_type | 否 |  |  |
| 25 | self_stock_account | 否 |  |  |
| 26 | report_account | 否 |  |  |
| 27 | stock_account | 否 |  |  |
| 28 | stock_code | 否 |  |  |
| 29 | entrust_amount | 否 |  |  |
| 30 | entrust_balance | 否 |  |  |
| 31 | impawn_code | 否 |  |  |
| 32 | impawn_amount | 否 |  |  |
| 33 | entrust_date | 否 |  |  |
| 34 | entrust_no | 否 |  |  |
| 35 | business_no | 否 |  |  |
| 36 | business_id | 否 |  |  |
| 37 | impawn_status | 否 |  |  |
| 38 | position_str | 否 |  |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_qrp_undue_pawn_pos | 默认 | 否 |  |
| idx_qrp_undue_pawn_pos | ART | 是 | position_str, position_str |
| idx_qrp_undue_pawn_stk | ART | 是 | stock_account, stock_account |
| idx_qrp_undue_pawn_id | ART | 是 | client_id, client_id |
| idx_qrp_undue_pawn_acct | ART | 是 | fund_account, fund_account |
| idx_qrp_undue_pawn_pos | 默认 | 否 |  |
| idx_qrp_undue_pawn_pos | ART | 是 | position_str, position_str |
| idx_qrp_undue_pawn_stk | ART | 是 | stock_account, stock_account |
| idx_qrp_undue_pawn_id | ART | 是 | client_id, client_id |
| idx_qrp_undue_pawn_acct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_qrp_undue_pawn_pos | position_str, position_str |
| idx_qrp_undue_pawn_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:32:46 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2024-09-05 10:01:59 | V3.0.2.14 | 曾剑辉 | 新增表结构 |
| 2026-03-04 15:32:46 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2024-09-05 10:01:59 | V3.0.2.14 | 曾剑辉 | 新增表结构 |

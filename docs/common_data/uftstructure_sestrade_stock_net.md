# stock_net - 股份轧差表

**表对象ID**: 5524
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_account | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | stock_type | 否 |  |  |
| 8 | stocknet_kind | 否 |  |  |
| 9 | begin_gap_amount | 否 |  |  |
| 10 | buy_real_amount1 | 否 |  |  |
| 11 | buy_real_amount2 | 否 |  |  |
| 12 | prev_amount | 否 |  |  |
| 13 | trustee_seat_no | 否 |  |  |
| 14 | stock_account | 否 |  |  |
| 15 | stock_code | 否 |  |  |
| 16 | branch_no | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | fund_account | 否 |  |  |
| 19 | client_id | 否 |  |  |
| 20 | stock_type | 否 |  |  |
| 21 | stocknet_kind | 否 |  |  |
| 22 | begin_gap_amount | 否 |  |  |
| 23 | buy_real_amount1 | 否 |  |  |
| 24 | buy_real_amount2 | 否 |  |  |
| 25 | prev_amount | 否 |  |  |
| 26 | trustee_seat_no | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stock_net | 默认 | 否 | trustee_seat_no, trustee_seat_no |
| idx_stock_net | ART | 是 | stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no, stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no |
| idx_stock_net_acct | ART | 是 | fund_account, fund_account |
| idx_stock_net | 默认 | 否 | trustee_seat_no, trustee_seat_no |
| idx_stock_net | ART | 是 | stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no, stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no |
| idx_stock_net_acct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stock_net | stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no, stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no |
| idx_stock_net | stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no, stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:46:07 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-08-18 15:24:28 | 3.0.6.1003 | 李江霖 | 物理表stock_net，增加索引字段(索引idx_stock_net:增加了索引字段：trustee_seat_no)... |
| 2026-03-09 13:46:07 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-08-18 15:24:28 | 3.0.6.1003 | 李江霖 | 物理表stock_net，增加索引字段(索引idx_stock_net:增加了索引字段：trustee_seat_no)... |

# uft_ses_stock_net - UFT股份轧差表

**表对象ID**: 5973
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 28 个）

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
| 14 | order_no | 否 |  |  |
| 15 | stock_account | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | fund_account | 否 |  |  |
| 20 | client_id | 否 |  |  |
| 21 | stock_type | 否 |  |  |
| 22 | stocknet_kind | 否 |  |  |
| 23 | begin_gap_amount | 否 |  |  |
| 24 | buy_real_amount1 | 否 |  |  |
| 25 | buy_real_amount2 | 否 |  |  |
| 26 | prev_amount | 否 |  |  |
| 27 | trustee_seat_no | 否 |  |  |
| 28 | order_no | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_ses_stock_net | 默认 | 否 |  |
| idx_uft_ses_stock_net_act | 默认 | 否 |  |
| idx_uft_ses_stock_net | ART | 是 | stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no, stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no |
| idx_uft_ses_stock_net_act | ART | 是 | fund_account, fund_account |
| idx_uft_ses_stock_net | 默认 | 否 |  |
| idx_uft_ses_stock_net_act | 默认 | 否 |  |
| idx_uft_ses_stock_net | ART | 是 | stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no, stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no |
| idx_uft_ses_stock_net_act | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_ses_stock_net | stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no, stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no |
| idx_uft_ses_stock_net | stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no, stock_account, stock_code, fund_account, exchange_type, stocknet_kind, trustee_seat_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:49:24 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:33:46 | 3.0.2.104 | taocong45644 | 当前表uft_ses_stock_net，修改了索引idx_uft_ses_stock_net,索引字段修改为：(sto... |
| 2025-03-11 11:03:25 | 3.0.2.2001 | 杨新照 | 新增表结构 |
| 2026-03-09 14:49:24 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:33:46 | 3.0.2.104 | taocong45644 | 当前表uft_ses_stock_net，修改了索引idx_uft_ses_stock_net,索引字段修改为：(sto... |
| 2025-03-11 11:03:25 | 3.0.2.2001 | 杨新照 | 新增表结构 |

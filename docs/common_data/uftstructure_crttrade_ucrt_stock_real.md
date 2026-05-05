# ucrt_stock_real - 融资融券股份交易信息表

**表对象ID**: 7538
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 78 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | begin_gap_amount | 否 |  |  |
| 2 | buy_real_amount1 | 否 |  |  |
| 3 | buy_real_amount2 | 否 |  |  |
| 4 | correct_amount | 否 |  |  |
| 5 | cost_price | 否 |  |  |
| 6 | current_amount | 否 |  |  |
| 7 | enable_amount | 否 |  |  |
| 8 | entrust_sell_amount | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | frozen_amount | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | money_type | 否 |  |  |
| 13 | real_buy_amount | 否 |  |  |
| 14 | real_buy_balance | 否 |  |  |
| 15 | real_buy_used_amount | 否 |  |  |
| 16 | real_sell_amount | 否 |  |  |
| 17 | real_sell_balance | 否 |  |  |
| 18 | sell_frozen_amount1 | 否 |  |  |
| 19 | sell_frozen_amount2 | 否 |  |  |
| 20 | sell_real_amount1 | 否 |  |  |
| 21 | sell_real_amount2 | 否 |  |  |
| 22 | stock_account | 否 |  |  |
| 23 | stock_code | 否 |  |  |
| 24 | stock_flag | 否 |  |  |
| 25 | stock_type | 否 |  |  |
| 26 | sum_buy_amount | 否 |  |  |
| 27 | sum_buy_balance | 否 |  |  |
| 28 | sum_sell_amount | 否 |  |  |
| 29 | sum_sell_balance | 否 |  |  |
| 30 | trustee_seat_no | 否 |  |  |
| 31 | uncome_buy_amount | 否 |  |  |
| 32 | uncome_sell_amount | 否 |  |  |
| 33 | unfrozen_amount | 否 |  |  |
| 34 | crdtnontrade_frozen_amount | 否 |  |  |
| 35 | create_date | 否 |  |  |
| 36 | create_time | 否 |  |  |
| 37 | position_str | 否 |  |  |
| 38 | branch_no | 否 |  |  |
| 39 | sub_stock_type | 否 |  |  |
| 40 | begin_gap_amount | 否 |  |  |
| 41 | buy_real_amount1 | 否 |  |  |
| 42 | buy_real_amount2 | 否 |  |  |
| 43 | correct_amount | 否 |  |  |
| 44 | cost_price | 否 |  |  |
| 45 | current_amount | 否 |  |  |
| 46 | enable_amount | 否 |  |  |
| 47 | entrust_sell_amount | 否 |  |  |
| 48 | exchange_type | 否 |  |  |
| 49 | frozen_amount | 否 |  |  |
| 50 | fund_account | 否 |  |  |
| 51 | money_type | 否 |  |  |
| 52 | real_buy_amount | 否 |  |  |
| 53 | real_buy_balance | 否 |  |  |
| 54 | real_buy_used_amount | 否 |  |  |
| 55 | real_sell_amount | 否 |  |  |
| 56 | real_sell_balance | 否 |  |  |
| 57 | sell_frozen_amount1 | 否 |  |  |
| 58 | sell_frozen_amount2 | 否 |  |  |
| 59 | sell_real_amount1 | 否 |  |  |
| 60 | sell_real_amount2 | 否 |  |  |
| 61 | stock_account | 否 |  |  |
| 62 | stock_code | 否 |  |  |
| 63 | stock_flag | 否 |  |  |
| 64 | stock_type | 否 |  |  |
| 65 | sum_buy_amount | 否 |  |  |
| 66 | sum_buy_balance | 否 |  |  |
| 67 | sum_sell_amount | 否 |  |  |
| 68 | sum_sell_balance | 否 |  |  |
| 69 | trustee_seat_no | 否 |  |  |
| 70 | uncome_buy_amount | 否 |  |  |
| 71 | uncome_sell_amount | 否 |  |  |
| 72 | unfrozen_amount | 否 |  |  |
| 73 | crdtnontrade_frozen_amount | 否 |  |  |
| 74 | create_date | 否 |  |  |
| 75 | create_time | 否 |  |  |
| 76 | position_str | 否 |  |  |
| 77 | branch_no | 否 |  |  |
| 78 | sub_stock_type | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_stock_real | ART | 是 | fund_account, exchange_type, stock_account, stock_code, trustee_seat_no, fund_account, exchange_type, stock_account, stock_code, trustee_seat_no |
| idx_ucrt_stock_real | ART | 是 | fund_account, exchange_type, stock_account, stock_code, trustee_seat_no, fund_account, exchange_type, stock_account, stock_code, trustee_seat_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_stock_real_unique | stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, stock_account, stock_code, exchange_type, fund_account, trustee_seat_no |
| idx_ucrt_stock_real_unique | stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, stock_account, stock_code, exchange_type, fund_account, trustee_seat_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 13:25:57 | 3.0.8.15 | xucq | 所有表ucrt_stock_real，添加了表字段(sub_stock_type);
 |
| 2025-08-23 11:15:11 | 3.0.6.1066 | 徐世晗 | 物理表ucrt_stock_real，添加了表字段(branch_no);
 |
| 2025-03-12 20:06:56 | 3.0.6.42 | 徐世晗 | 物理表ucrt_stock_real，添加了表字段(position_str);
 |
| 2024-10-23 14:28:38 | 3.0.6.8 | huangzh | 物理表ucrt_stock_real，添加了表字段(create_date);
物理表ucrt_stock_real，... |
| 2024-05-16 15:05:42 | 3.0.2.9 | 叶慧军 | 开发工具告警的关联索引相关问题修改 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-04 13:25:57 | 3.0.8.15 | xucq | 所有表ucrt_stock_real，添加了表字段(sub_stock_type);
 |
| 2025-08-23 11:15:11 | 3.0.6.1066 | 徐世晗 | 物理表ucrt_stock_real，添加了表字段(branch_no);
 |
| 2025-03-12 20:06:56 | 3.0.6.42 | 徐世晗 | 物理表ucrt_stock_real，添加了表字段(position_str);
 |
| 2024-10-23 14:28:38 | 3.0.6.8 | huangzh | 物理表ucrt_stock_real，添加了表字段(create_date);
物理表ucrt_stock_real，... |
| 2024-05-16 15:05:42 | 3.0.2.9 | 叶慧军 | 开发工具告警的关联索引相关问题修改 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

# uses_stock_real - 证券股份交易信息表

**表对象ID**: 5506
**所属模块**: sestrade
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
| 15 | real_sell_amount | 否 |  |  |
| 16 | real_sell_balance | 否 |  |  |
| 17 | sell_frozen_amount1 | 否 |  |  |
| 18 | sell_frozen_amount2 | 否 |  |  |
| 19 | sell_real_amount1 | 否 |  |  |
| 20 | sell_real_amount2 | 否 |  |  |
| 21 | stock_account | 否 |  |  |
| 22 | stock_code | 否 |  |  |
| 23 | stock_flag | 否 |  |  |
| 24 | stock_type | 否 |  |  |
| 25 | sum_buy_amount | 否 |  |  |
| 26 | sum_buy_balance | 否 |  |  |
| 27 | sum_sell_amount | 否 |  |  |
| 28 | sum_sell_balance | 否 |  |  |
| 29 | trustee_seat_no | 否 |  |  |
| 30 | uncome_buy_amount | 否 |  |  |
| 31 | uncome_sell_amount | 否 |  |  |
| 32 | unfrozen_amount | 否 |  |  |
| 33 | partition_no | 否 |  |  |
| 34 | sub_stock_type | 否 |  |  |
| 35 | position_str | 否 |  | branch_no(5) +fund_account(18)+exchange_type(4) +stock_accou |
| 36 | create_date | 否 |  |  |
| 37 | create_time | 否 |  |  |
| 38 | json_data | 否 |  |  |
| 39 | tag_code | 是 |  |  |
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
| 54 | real_sell_amount | 否 |  |  |
| 55 | real_sell_balance | 否 |  |  |
| 56 | sell_frozen_amount1 | 否 |  |  |
| 57 | sell_frozen_amount2 | 否 |  |  |
| 58 | sell_real_amount1 | 否 |  |  |
| 59 | sell_real_amount2 | 否 |  |  |
| 60 | stock_account | 否 |  |  |
| 61 | stock_code | 否 |  |  |
| 62 | stock_flag | 否 |  |  |
| 63 | stock_type | 否 |  |  |
| 64 | sum_buy_amount | 否 |  |  |
| 65 | sum_buy_balance | 否 |  |  |
| 66 | sum_sell_amount | 否 |  |  |
| 67 | sum_sell_balance | 否 |  |  |
| 68 | trustee_seat_no | 否 |  |  |
| 69 | uncome_buy_amount | 否 |  |  |
| 70 | uncome_sell_amount | 否 |  |  |
| 71 | unfrozen_amount | 否 |  |  |
| 72 | partition_no | 否 |  |  |
| 73 | sub_stock_type | 否 |  |  |
| 74 | position_str | 否 |  | branch_no(5) +fund_account(18)+exchange_type(4) +stock_accou |
| 75 | create_date | 否 |  |  |
| 76 | create_time | 否 |  |  |
| 77 | json_data | 否 |  |  |
| 78 | tag_code | 是 |  |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_stock_real_pos | 默认 | 否 |  |
| idx_uses_stockreal_unique | ART | 是 | stock_account, exchange_type, fund_account, stock_code, trustee_seat_no, stock_account, exchange_type, fund_account, stock_code, trustee_seat_no |
| idx_uses_stockreal_fund_acct | ART | 是 | fund_account, stock_account, fund_account, stock_account |
| idx_uses_stockreal_all | ART | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_uses_stock_real_pos | ART | 是 | fund_account, position_str, fund_account, position_str |
| idx_uses_stock_real_pos | 默认 | 否 |  |
| idx_uses_stockreal_unique | ART | 是 | stock_account, exchange_type, fund_account, stock_code, trustee_seat_no, stock_account, exchange_type, fund_account, stock_code, trustee_seat_no |
| idx_uses_stockreal_fund_acct | ART | 是 | fund_account, stock_account, fund_account, stock_account |
| idx_uses_stockreal_all | ART | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_uses_stock_real_pos | ART | 是 | fund_account, position_str, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_stockreal_unique | stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, stock_account, stock_code, exchange_type, fund_account, trustee_seat_no |
| idx_uses_stockreal_unique | stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, stock_account, stock_code, exchange_type, fund_account, trustee_seat_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-26 17:34:03 | V3.0.8.12 | 马天宇 | 当前表uses_stock_real，修改了索引idx_uses_stock_real_pos,索引字段修改为：(fun... |
| 2025-09-25 13:49:58 | 3.0.2.74 | yusz | 所有表uses_stock_real，添加了表字段(tag_code);
 |
| 2025-07-27 19:39:11 | 3.0.2.73 | 全春辉 | 数据导出相关表增加定位串查询索引 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2024-12-17 11:24:49 | 3.0.2.52 | 张云焘 | 物理表uses_stock_real，添加了表字段(json_data);
 |
| 2024-11-01 20:09:56 | 3.0.5.1056 | 祝丁恺 | 分级索引idx_uses_stockreal_all中将stock_code变为二级索引，exchange_type变为... |
| 2024-10-25 18:17:14 | 3.0.5.1054 | 陈键中 | 物理表uses_stock_real，修改idx_uses_stockreal_all为分级索引 |
| 2024-10-22 14:41:42 | 3.0.5.1052 | 雷玄 | 
物理表uses_stock_real，将idx_uses_stockreal_fund_acct修改为分级索引 |
| 2024-09-24 11:06:40 | 3.0.2.48 | 杨森峰 | 物理表uses_stock_real，添加了表字段(create_time);
 |
| 2024-09-10 18:51:34 | 3.0.2.43 | 陈键中 | 物理表uses_stock_real，添加了表字段(create_date);
 |
| 2024-04-29 18:54:23 | 3.0.2.3 | 阮善宏 | 物理表uses_stock_real，删除了表字段(real_buy_used_amount);
 |
| 2024-04-24 10:28:55 | 3.0.2.3 | 阮善宏 | 物理表uses_stock_real，添加了表字段(sub_stock_type);
物理表uses_stock_re... |
| 2024-01-29 14:41:18 | 3.0.0.10 | 叶慧军 | 删除关联索引idx_uses_stock_real中的重复字段exchange_type |
| 2023-11-23 14:45:45 | 3.0.0.9 | 杨森峰 | 物理表uses_stock_real，修改索引 |
| 2023-11-14 11:40:03 | 3.0.0.6 | weill | 物理表uses_stock_real，添加了表字段(partition_no);
 |

> 共 32 条修改记录，仅显示最近15条

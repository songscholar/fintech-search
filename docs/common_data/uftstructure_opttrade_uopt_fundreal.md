# uopt_fundreal - 期权交易资金表

**表对象ID**: 9602
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 44 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | begin_balance | 否 |  |  |
| 5 | current_balance | 否 |  |  |
| 6 | opt_total_margin | 否 |  |  |
| 7 | optadvance_balance | 否 |  |  |
| 8 | frozen_balance | 否 |  |  |
| 9 | unfrozen_balance | 否 |  |  |
| 10 | entrust_buy_balance | 否 |  |  |
| 11 | real_buy_balance | 否 |  |  |
| 12 | real_sell_balance | 否 |  |  |
| 13 | foregift_balance | 否 |  |  |
| 14 | static_margin | 否 |  |  |
| 15 | max_static_margin | 否 |  |  |
| 16 | mortgage_balance | 否 |  |  |
| 17 | order_no | 否 |  |  |
| 18 | partition_no | 否 |  |  |
| 19 | cash_balance | 否 |  |  |
| 20 | check_balance | 否 |  |  |
| 21 | correct_balance | 否 |  |  |
| 22 | position_str | 否 |  |  |
| 23 | client_id | 否 |  |  |
| 24 | fund_account | 否 |  |  |
| 25 | money_type | 否 |  |  |
| 26 | begin_balance | 否 |  |  |
| 27 | current_balance | 否 |  |  |
| 28 | opt_total_margin | 否 |  |  |
| 29 | optadvance_balance | 否 |  |  |
| 30 | frozen_balance | 否 |  |  |
| 31 | unfrozen_balance | 否 |  |  |
| 32 | entrust_buy_balance | 否 |  |  |
| 33 | real_buy_balance | 否 |  |  |
| 34 | real_sell_balance | 否 |  |  |
| 35 | foregift_balance | 否 |  |  |
| 36 | static_margin | 否 |  |  |
| 37 | max_static_margin | 否 |  |  |
| 38 | mortgage_balance | 否 |  |  |
| 39 | order_no | 否 |  |  |
| 40 | partition_no | 否 |  |  |
| 41 | cash_balance | 否 |  |  |
| 42 | check_balance | 否 |  |  |
| 43 | correct_balance | 否 |  |  |
| 44 | position_str | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_fundreal | 默认 | 是 | fund_account, money_type, fund_account, money_type |
| idx_uopt_fundreal_money | 默认 | 否 | money_type, money_type |
| idx_uopt_fundreal_pos | 默认 | 是 | position_str, position_str |
| idx_uopt_fundreal | 默认 | 是 | fund_account, money_type, fund_account, money_type |
| idx_uopt_fundreal_money | 默认 | 否 | money_type, money_type |
| idx_uopt_fundreal_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_fundreal | fund_account, money_type, fund_account, money_type |
| idx_uopt_fundreal | fund_account, money_type, fund_account, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-09 13:49:06 | V3.0.2.14 | wuxd | 去除差量redo |
| 2025-09-04 16:26:55 | V3.0.2.6 | 韦子晗 | 所有表uopt_fundreal，添加了表字段(position_str);
 |
| 2025-06-17 15:04:31 | V3.0.3.16 | 汪迎 | 物理表uopt_fundreal，添加了表字段(cash_balance);
物理表uopt_fundreal，添加了... |
| 2024-05-09 09:31:37 | V3.0.3.5 | 韦子晗 | 新增partition_no字段 |
| 2025-10-09 13:49:06 | V3.0.2.14 | wuxd | 去除差量redo |
| 2025-09-04 16:26:55 | V3.0.2.6 | 韦子晗 | 所有表uopt_fundreal，添加了表字段(position_str);
 |
| 2025-06-17 15:04:31 | V3.0.3.16 | 汪迎 | 物理表uopt_fundreal，添加了表字段(cash_balance);
物理表uopt_fundreal，添加了... |
| 2024-05-09 09:31:37 | V3.0.3.5 | 韦子晗 | 新增partition_no字段 |

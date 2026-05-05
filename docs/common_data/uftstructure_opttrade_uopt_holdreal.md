# uopt_holdreal - 期权合约持仓实时交易表

**表对象ID**: 9613
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 64 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | seat_no | 否 |  |  |
| 6 | option_code | 否 |  |  |
| 7 | option_type | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | stock_type | 否 |  |  |
| 10 | opthold_type | 否 |  |  |
| 11 | current_amount | 否 |  |  |
| 12 | uncome_open_amount | 否 |  |  |
| 13 | uncome_drop_amount | 否 |  |  |
| 14 | frozen_amount | 否 |  |  |
| 15 | unfrozen_amount | 否 |  |  |
| 16 | optcomb_used_amount | 否 |  |  |
| 17 | enable_amount | 否 |  |  |
| 18 | real_open_amount | 否 |  |  |
| 19 | real_drop_amount | 否 |  |  |
| 20 | real_buy_balance | 否 |  |  |
| 21 | real_sell_balance | 否 |  |  |
| 22 | entrust_drop_amount | 否 |  |  |
| 23 | sum_open_amount | 否 |  |  |
| 24 | sum_drop_amount | 否 |  |  |
| 25 | sum_buy_balance | 否 |  |  |
| 26 | sum_sell_balance | 否 |  |  |
| 27 | used_pur_quota | 否 |  |  |
| 28 | uncome_pur_quota | 否 |  |  |
| 29 | order_no | 否 |  |  |
| 30 | average_open_price | 否 |  |  |
| 31 | partition_no | 否 |  |  |
| 32 | position_str | 否 |  | branch_no(5)+exchange_type(2)+stock_account(10)+opthold_type |
| 33 | client_id | 否 |  |  |
| 34 | exchange_type | 否 |  |  |
| 35 | fund_account | 否 |  |  |
| 36 | stock_account | 否 |  |  |
| 37 | seat_no | 否 |  |  |
| 38 | option_code | 否 |  |  |
| 39 | option_type | 否 |  |  |
| 40 | stock_code | 否 |  |  |
| 41 | stock_type | 否 |  |  |
| 42 | opthold_type | 否 |  |  |
| 43 | current_amount | 否 |  |  |
| 44 | uncome_open_amount | 否 |  |  |
| 45 | uncome_drop_amount | 否 |  |  |
| 46 | frozen_amount | 否 |  |  |
| 47 | unfrozen_amount | 否 |  |  |
| 48 | optcomb_used_amount | 否 |  |  |
| 49 | enable_amount | 否 |  |  |
| 50 | real_open_amount | 否 |  |  |
| 51 | real_drop_amount | 否 |  |  |
| 52 | real_buy_balance | 否 |  |  |
| 53 | real_sell_balance | 否 |  |  |
| 54 | entrust_drop_amount | 否 |  |  |
| 55 | sum_open_amount | 否 |  |  |
| 56 | sum_drop_amount | 否 |  |  |
| 57 | sum_buy_balance | 否 |  |  |
| 58 | sum_sell_balance | 否 |  |  |
| 59 | used_pur_quota | 否 |  |  |
| 60 | uncome_pur_quota | 否 |  |  |
| 61 | order_no | 否 |  |  |
| 62 | average_open_price | 否 |  |  |
| 63 | partition_no | 否 |  |  |
| 64 | position_str | 否 |  | branch_no(5)+exchange_type(2)+stock_account(10)+opthold_type |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_holdreal_pos | 默认 | 否 | position_str, position_str |
| idx_uopt_holdreal | 默认 | 否 | opthold_type, option_code, opthold_type, option_code |
| idx_uopt_holdreal_global | 默认 | 是 | exchange_type, fund_account, stock_account, option_code, opthold_type, exchange_type, fund_account, stock_account, option_code, opthold_type |
| idx_uopt_holdreal_pos | 默认 | 是 | position_str, position_str |
| idx_uopt_holdreal_pos | 默认 | 否 | position_str, position_str |
| idx_uopt_holdreal | 默认 | 否 | opthold_type, option_code, opthold_type, option_code |
| idx_uopt_holdreal_global | 默认 | 是 | exchange_type, fund_account, stock_account, option_code, opthold_type, exchange_type, fund_account, stock_account, option_code, opthold_type |
| idx_uopt_holdreal_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_holdreal | exchange_type, option_code, opthold_type, fund_account, stock_account, exchange_type, option_code, opthold_type, fund_account, stock_account |
| idx_uopt_holdreal | exchange_type, option_code, opthold_type, fund_account, stock_account, exchange_type, option_code, opthold_type, fund_account, stock_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-09 13:49:06 | V3.0.2.14 | wuxd | 去除差量redo |
| 2025-07-25 16:56:10 | V3.0.2.1 | 汪迎 | 物理表uopt_holdreal，添加了表字段(position_str);
,物理表uopt_holdreal，增加... |
| 2024-05-09 09:32:42 | V3.0.3.6 | 韦子晗 | 新增partition_no字段 |
| 2025-10-09 13:49:06 | V3.0.2.14 | wuxd | 去除差量redo |
| 2025-07-25 16:56:10 | V3.0.2.1 | 汪迎 | 物理表uopt_holdreal，添加了表字段(position_str);
,物理表uopt_holdreal，增加... |
| 2024-05-09 09:32:42 | V3.0.3.6 | 韦子晗 | 新增partition_no字段 |

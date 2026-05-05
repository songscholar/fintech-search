# uopt_combholdreal - 期权组合策略持仓实时交易表

**表对象ID**: 9616
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | optcomb_id | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | optcomb_code | 否 |  |  |
| 7 | component_count | 否 |  |  |
| 8 | first_option_code | 否 |  |  |
| 9 | first_opthold_type | 否 |  |  |
| 10 | second_option_code | 否 |  |  |
| 11 | second_opthold_type | 否 |  |  |
| 12 | current_amount | 否 |  |  |
| 13 | enable_amount | 否 |  |  |
| 14 | real_comb_amount | 否 |  |  |
| 15 | real_split_amount | 否 |  |  |
| 16 | entrust_split_amount | 否 |  |  |
| 17 | order_no | 否 |  |  |
| 18 | position_str | 否 |  |  |
| 19 | optcomb_id | 否 |  |  |
| 20 | client_id | 否 |  |  |
| 21 | fund_account | 否 |  |  |
| 22 | stock_account | 否 |  |  |
| 23 | exchange_type | 否 |  |  |
| 24 | optcomb_code | 否 |  |  |
| 25 | component_count | 否 |  |  |
| 26 | first_option_code | 否 |  |  |
| 27 | first_opthold_type | 否 |  |  |
| 28 | second_option_code | 否 |  |  |
| 29 | second_opthold_type | 否 |  |  |
| 30 | current_amount | 否 |  |  |
| 31 | enable_amount | 否 |  |  |
| 32 | real_comb_amount | 否 |  |  |
| 33 | real_split_amount | 否 |  |  |
| 34 | entrust_split_amount | 否 |  |  |
| 35 | order_no | 否 |  |  |
| 36 | position_str | 否 |  |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_combholdreal_pos | 默认 | 否 | position_str, position_str |
| idx_uopt_combholdreal | 默认 | 否 | optcomb_id, optcomb_id |
| idx_uopt_combholdreal_acct | 默认 | 是 | fund_account, fund_account |
| idx_uopt_combholdreal_global | 默认 | 是 | optcomb_id, fund_account, stock_account, exchange_type, optcomb_id, fund_account, stock_account, exchange_type |
| idx_uopt_combholdreal_pos | 默认 | 是 | position_str, position_str |
| idx_uopt_combholdreal_pos | 默认 | 否 | position_str, position_str |
| idx_uopt_combholdreal | 默认 | 否 | optcomb_id, optcomb_id |
| idx_uopt_combholdreal_acct | 默认 | 是 | fund_account, fund_account |
| idx_uopt_combholdreal_global | 默认 | 是 | optcomb_id, fund_account, stock_account, exchange_type, optcomb_id, fund_account, stock_account, exchange_type |
| idx_uopt_combholdreal_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_combholdreal | fund_account, exchange_type, optcomb_id, stock_account, fund_account, exchange_type, optcomb_id, stock_account |
| idx_uopt_combholdreal | fund_account, exchange_type, optcomb_id, stock_account, fund_account, exchange_type, optcomb_id, stock_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-09 13:49:06 | V3.0.2.14 | wuxd | 去除差量redo |
| 2025-07-25 16:58:06 | V3.0.2.1 | 汪迎 | 物理表uopt_combholdreal，添加了表字段(position_str);
,物理表uopt_combhol... |
| 2025-10-09 13:49:06 | V3.0.2.14 | wuxd | 去除差量redo |
| 2025-07-25 16:58:06 | V3.0.2.1 | 汪迎 | 物理表uopt_combholdreal，添加了表字段(position_str);
,物理表uopt_combhol... |

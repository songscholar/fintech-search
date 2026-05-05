# surstock_tosett - 余券信息表2

**表对象ID**: 3076
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | cashgroup_no | 是 |  |  |
| 2 | fund_account | 是 |  |  |
| 3 | client_id | 是 |  |  |
| 4 | branch_no | 是 |  |  |
| 5 | exchange_type | 是 |  |  |
| 6 | stock_account | 是 |  |  |
| 7 | stock_code | 是 |  |  |
| 8 | stock_type | 是 |  |  |
| 9 | money_type | 是 |  |  |
| 10 | begin_amount | 是 |  |  |
| 11 | current_amount | 是 |  |  |
| 12 | surplus_amount | 是 |  |  |
| 13 | correct_amount | 是 |  |  |
| 14 | position_str_long | 是 |  |  |
| 15 | update_date | 是 |  |  |
| 16 | update_time | 是 |  |  |
| 17 | transaction_no | 是 |  |  |
| 18 | position_str | 是 |  |  |
| 19 | asset_prop | 是 |  |  |
| 20 | cashgroup_no | 是 |  |  |
| 21 | fund_account | 是 |  |  |
| 22 | client_id | 是 |  |  |
| 23 | branch_no | 是 |  |  |
| 24 | exchange_type | 是 |  |  |
| 25 | stock_account | 是 |  |  |
| 26 | stock_code | 是 |  |  |
| 27 | stock_type | 是 |  |  |
| 28 | money_type | 是 |  |  |
| 29 | begin_amount | 是 |  |  |
| 30 | current_amount | 是 |  |  |
| 31 | surplus_amount | 是 |  |  |
| 32 | correct_amount | 是 |  |  |
| 33 | position_str_long | 是 |  |  |
| 34 | update_date | 是 |  |  |
| 35 | update_time | 是 |  |  |
| 36 | transaction_no | 是 |  |  |
| 37 | position_str | 是 |  |  |
| 38 | asset_prop | 是 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_surstock | 默认 | 是 | position_str_long, position_str_long |
| idx_surstock_id | 默认 | 是 | client_id, client_id |
| idx_surstock_acct | 默认 | 是 | fund_account, fund_account |
| idx_surstock_stk | 默认 | 是 | stock_account, stock_code, branch_no, exchange_type, cashgroup_no, stock_account, stock_code, branch_no, exchange_type, cashgroup_no |
| idx_surstock | 默认 | 是 | position_str_long, position_str_long |
| idx_surstock_id | 默认 | 是 | client_id, client_id |
| idx_surstock_acct | 默认 | 是 | fund_account, fund_account |
| idx_surstock_stk | 默认 | 是 | stock_account, stock_code, branch_no, exchange_type, cashgroup_no, stock_account, stock_code, branch_no, exchange_type, cashgroup_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_surstock | position_str_long, position_str_long |
| idx_surstock | position_str_long, position_str_long |

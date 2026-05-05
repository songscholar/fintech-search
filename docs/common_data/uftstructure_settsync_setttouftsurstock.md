# setttouftsurstock - 清算余券信息表

**表对象ID**: 3066
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 30 个）

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
| 14 | position_str_long | 是 |  | branch_no(5)+exchange_type(4)+stock_account(10)+stock_code(6 |
| 15 | uft_data_change_status | 是 |  |  |
| 16 | cashgroup_no | 是 |  |  |
| 17 | fund_account | 是 |  |  |
| 18 | client_id | 是 |  |  |
| 19 | branch_no | 是 |  |  |
| 20 | exchange_type | 是 |  |  |
| 21 | stock_account | 是 |  |  |
| 22 | stock_code | 是 |  |  |
| 23 | stock_type | 是 |  |  |
| 24 | money_type | 是 |  |  |
| 25 | begin_amount | 是 |  |  |
| 26 | current_amount | 是 |  |  |
| 27 | surplus_amount | 是 |  |  |
| 28 | correct_amount | 是 |  |  |
| 29 | position_str_long | 是 |  | branch_no(5)+exchange_type(4)+stock_account(10)+stock_code(6 |
| 30 | uft_data_change_status | 是 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settsurstock | 默认 | 是 | position_str_long, position_str_long |
| idx_settsurstock_exch | 默认 | 是 | stock_code, stock_account, exchange_type, stock_code, stock_account, exchange_type |
| idx_settsurstock_acct | 默认 | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_settsurstock | 默认 | 是 | position_str_long, position_str_long |
| idx_settsurstock_exch | 默认 | 是 | stock_code, stock_account, exchange_type, stock_code, stock_account, exchange_type |
| idx_settsurstock_acct | 默认 | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |

## 数据库索引（共 6 个）

| 索引名 | 字段 |
|--------|------|
| idx_surstock | position_str_long, position_str_long |
| idx_surstock_id | client_id, client_id |
| idx_surstock_acct | fund_account, fund_account |
| idx_surstock | position_str_long, position_str_long |
| idx_surstock_id | client_id, client_id |
| idx_surstock_acct | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-12-11 15:19 | 8.26.2.47 | 董子文 | 修改idx_settsurstock_acct索引，添加部分索引 |
| 2018-06-05 10:28 | 8.26.1.24 | 廖景辉 | 修改idx_settsurstock_exch分级索引顺序 |
| 2018-04-14 13:13 | 8.26.1.11 | 曾哲 | 修改idx_settsurstock_exch索引字段顺序 |
| 2023-12-11 15:19 | 8.26.2.47 | 董子文 | 修改idx_settsurstock_acct索引，添加部分索引 |
| 2018-06-05 10:28 | 8.26.1.24 | 廖景辉 | 修改idx_settsurstock_exch分级索引顺序 |
| 2018-04-14 13:13 | 8.26.1.11 | 曾哲 | 修改idx_settsurstock_exch索引字段顺序 |

# setttouftbrpcontractext - 清算债券质押协议回购合约扩展表

**表对象ID**: 3050
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | branch_no | 是 |  |  |
| 3 | fund_account | 是 |  |  |
| 4 | stock_account | 是 |  |  |
| 5 | exchange_type | 是 |  |  |
| 6 | join_position_str | 是 |  |  |
| 7 | orig_report_id | 是 |  |  |
| 8 | stock_code | 是 |  |  |
| 9 | impawn_amount | 是 |  |  |
| 10 | exch_in_amount | 是 |  |  |
| 11 | exch_out_amount | 是 |  |  |
| 12 | uft_data_change_status | 是 |  |  |
| 13 | stock_property | 是 |  |  |
| 14 | use_date | 是 |  |  |
| 15 | init_date | 是 |  |  |
| 16 | branch_no | 是 |  |  |
| 17 | fund_account | 是 |  |  |
| 18 | stock_account | 是 |  |  |
| 19 | exchange_type | 是 |  |  |
| 20 | join_position_str | 是 |  |  |
| 21 | orig_report_id | 是 |  |  |
| 22 | stock_code | 是 |  |  |
| 23 | impawn_amount | 是 |  |  |
| 24 | exch_in_amount | 是 |  |  |
| 25 | exch_out_amount | 是 |  |  |
| 26 | uft_data_change_status | 是 |  |  |
| 27 | stock_property | 是 |  |  |
| 28 | use_date | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settbrpcontractext_id | 默认 | 是 | exchange_type, join_position_str, stock_code, stock_property, exchange_type, join_position_str, stock_code, stock_property |
| idx_settbrpcontractext_acct | 默认 | 是 | fund_account, fund_account |
| idx_settbrpcontractext_id | 默认 | 是 | exchange_type, join_position_str, stock_code, stock_property, exchange_type, join_position_str, stock_code, stock_property |
| idx_settbrpcontractext_acct | 默认 | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settbrpcontractext_id | exchange_type, join_position_str, exchange_type, join_position_str |
| idx_settbrpcontractext_id | exchange_type, join_position_str, exchange_type, join_position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2021-04-06 23:26 | 8.26.1.117 | 郑天翔 | 增加use_date,修改索引 |
| 2021-01-11 10:16 | 8.26.1.108 | 李浩奇 | 新增stock_property |
| 2020-10-29 14:42 | 8.26.1.103 | 罗佳楠 | 新增 |
| 2021-04-06 23:26 | 8.26.1.117 | 郑天翔 | 增加use_date,修改索引 |
| 2021-01-11 10:16 | 8.26.1.108 | 李浩奇 | 新增stock_property |
| 2020-10-29 14:42 | 8.26.1.103 | 罗佳楠 | 新增 |

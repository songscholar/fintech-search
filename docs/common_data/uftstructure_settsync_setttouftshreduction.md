# setttouftshreduction - 上海减持信息控制表

**表对象ID**: 3002
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | company_no | 是 |  |  |
| 3 | exchange_type | 是 |  |  |
| 4 | stock_account | 是 |  |  |
| 5 | stock_code | 是 |  |  |
| 6 | seat_no | 是 |  |  |
| 7 | cognizancestock_amount1 | 是 |  |  |
| 8 | cognizancestock_amount2 | 是 |  |  |
| 9 | reducectrl_amount | 是 |  |  |
| 10 | blockreducectrl_amount | 是 |  |  |
| 11 | surplusstock_amount | 是 |  |  |
| 12 | blockrecectrl_amount | 是 |  |  |
| 13 | frozen_amount | 是 |  |  |
| 14 | begin_enable_quota | 是 |  |  |
| 15 | block_enable_quota | 是 |  |  |
| 16 | pre_used_quota | 是 |  |  |
| 17 | prereduce_used_quota | 是 |  |  |
| 18 | used_quota | 是 |  |  |
| 19 | reduce_used_quota | 是 |  |  |
| 20 | block_enable_quota1 | 是 |  |  |
| 21 | preblock_used_quota | 是 |  |  |
| 22 | block_used_quota | 是 |  |  |
| 23 | stock_circulate_amount | 是 |  |  |
| 24 | set_seat_no | 是 |  |  |
| 25 | modify_date | 是 |  |  |
| 26 | remark | 是 |  |  |
| 27 | position_str | 是 |  |  |
| 28 | init_date | 是 |  |  |
| 29 | company_no | 是 |  |  |
| 30 | exchange_type | 是 |  |  |
| 31 | stock_account | 是 |  |  |
| 32 | stock_code | 是 |  |  |
| 33 | seat_no | 是 |  |  |
| 34 | cognizancestock_amount1 | 是 |  |  |
| 35 | cognizancestock_amount2 | 是 |  |  |
| 36 | reducectrl_amount | 是 |  |  |
| 37 | blockreducectrl_amount | 是 |  |  |
| 38 | surplusstock_amount | 是 |  |  |
| 39 | blockrecectrl_amount | 是 |  |  |
| 40 | frozen_amount | 是 |  |  |
| 41 | begin_enable_quota | 是 |  |  |
| 42 | block_enable_quota | 是 |  |  |
| 43 | pre_used_quota | 是 |  |  |
| 44 | prereduce_used_quota | 是 |  |  |
| 45 | used_quota | 是 |  |  |
| 46 | reduce_used_quota | 是 |  |  |
| 47 | block_enable_quota1 | 是 |  |  |
| 48 | preblock_used_quota | 是 |  |  |
| 49 | block_used_quota | 是 |  |  |
| 50 | stock_circulate_amount | 是 |  |  |
| 51 | set_seat_no | 是 |  |  |
| 52 | modify_date | 是 |  |  |
| 53 | remark | 是 |  |  |
| 54 | position_str | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_shreduction_pos | 默认 | 是 | position_str, position_str |
| idx_shreduction_acct | 默认 | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_shreduction_pos | 默认 | 是 | position_str, position_str |
| idx_shreduction_acct | 默认 | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_shreduction_pos | position_str, position_str |
| idx_shreduction_acct | stock_account, stock_code, stock_account, stock_code |
| idx_shreduction_pos | position_str, position_str |
| idx_shreduction_acct | stock_account, stock_code, stock_account, stock_code |

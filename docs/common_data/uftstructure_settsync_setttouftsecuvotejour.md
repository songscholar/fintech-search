# setttouftsecuvotejour - 清算投票流水表

**表对象ID**: 3015
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 48 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | sett_batch_no | 是 |  |  |
| 3 | sett_id | 是 |  |  |
| 4 | entrust_date | 是 |  |  |
| 5 | client_id | 是 |  |  |
| 6 | branch_no | 是 |  |  |
| 7 | fund_account | 是 |  |  |
| 8 | business_id | 是 |  |  |
| 9 | exchange_type | 是 |  |  |
| 10 | stock_code | 是 |  |  |
| 11 | stock_name | 是 |  |  |
| 12 | stock_account | 是 |  |  |
| 13 | entrust_no | 是 |  |  |
| 14 | order_id | 是 |  |  |
| 15 | business_amount | 是 |  |  |
| 16 | business_price | 是 |  |  |
| 17 | placard_id | 是 |  |  |
| 18 | motion_id | 是 |  |  |
| 19 | approve_amount | 是 |  |  |
| 20 | oppose_amount | 是 |  |  |
| 21 | waive_amount | 是 |  |  |
| 22 | error_no | 是 |  |  |
| 23 | remark | 是 |  |  |
| 24 | position_str | 是 |  |  |
| 25 | init_date | 是 |  |  |
| 26 | sett_batch_no | 是 |  |  |
| 27 | sett_id | 是 |  |  |
| 28 | entrust_date | 是 |  |  |
| 29 | client_id | 是 |  |  |
| 30 | branch_no | 是 |  |  |
| 31 | fund_account | 是 |  |  |
| 32 | business_id | 是 |  |  |
| 33 | exchange_type | 是 |  |  |
| 34 | stock_code | 是 |  |  |
| 35 | stock_name | 是 |  |  |
| 36 | stock_account | 是 |  |  |
| 37 | entrust_no | 是 |  |  |
| 38 | order_id | 是 |  |  |
| 39 | business_amount | 是 |  |  |
| 40 | business_price | 是 |  |  |
| 41 | placard_id | 是 |  |  |
| 42 | motion_id | 是 |  |  |
| 43 | approve_amount | 是 |  |  |
| 44 | oppose_amount | 是 |  |  |
| 45 | waive_amount | 是 |  |  |
| 46 | error_no | 是 |  |  |
| 47 | remark | 是 |  |  |
| 48 | position_str | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_secuvotejour | 默认 | 是 | stock_account, exchange_type, stock_code, branch_no, order_id, entrust_date, stock_account, exchange_type, stock_code, branch_no, order_id, entrust_date |
| idx_secuvotejour_pos | 默认 | 是 | position_str, position_str |
| idx_secuvotejour | 默认 | 是 | stock_account, exchange_type, stock_code, branch_no, order_id, entrust_date, stock_account, exchange_type, stock_code, branch_no, order_id, entrust_date |
| idx_secuvotejour_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_secuvotejour | stock_account, exchange_type, branch_no, stock_code, order_id, entrust_date, stock_account, exchange_type, branch_no, stock_code, order_id, entrust_date |
| idx_secuvotejour | stock_account, exchange_type, branch_no, stock_code, order_id, entrust_date, stock_account, exchange_type, branch_no, stock_code, order_id, entrust_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2019-02-13 17:12 | 8.26.1.55 | 彭立 | 增加字段sett_batch_no |
| 2019-02-13 17:12 | 8.26.1.55 | 彭立 | 增加字段sett_batch_no |

# vote_jour - 投票流水表

**表对象ID**: 5751
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 46 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | entrust_date | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | branch_no | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | business_no | 否 |  |  |
| 7 | business_id | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | stock_name | 否 |  | 证券名称，投票名称 |
| 11 | stock_account | 否 |  |  |
| 12 | entrust_no | 否 |  |  |
| 13 | business_amount | 否 |  |  |
| 14 | business_price | 否 |  |  |
| 15 | error_no | 否 |  |  |
| 16 | remark | 否 |  | 备注，错误原因等 |
| 17 | position_str | 否 |  | 定位串　init_date || right('0000' || exchange_type) || right('00 |
| 18 | placard_id | 否 |  |  |
| 19 | motion_id | 否 |  |  |
| 20 | approve_amount | 否 |  |  |
| 21 | oppose_amount | 否 |  |  |
| 22 | waive_amount | 否 |  |  |
| 23 | order_id | 否 |  |  |
| 24 | init_date | 否 |  |  |
| 25 | entrust_date | 否 |  |  |
| 26 | client_id | 否 |  |  |
| 27 | branch_no | 否 |  |  |
| 28 | fund_account | 否 |  |  |
| 29 | business_no | 否 |  |  |
| 30 | business_id | 否 |  |  |
| 31 | exchange_type | 否 |  |  |
| 32 | stock_code | 否 |  |  |
| 33 | stock_name | 否 |  | 证券名称，投票名称 |
| 34 | stock_account | 否 |  |  |
| 35 | entrust_no | 否 |  |  |
| 36 | business_amount | 否 |  |  |
| 37 | business_price | 否 |  |  |
| 38 | error_no | 否 |  |  |
| 39 | remark | 否 |  | 备注，错误原因等 |
| 40 | position_str | 否 |  | 定位串　init_date || right('0000' || exchange_type) || right('00 |
| 41 | placard_id | 否 |  |  |
| 42 | motion_id | 否 |  |  |
| 43 | approve_amount | 否 |  |  |
| 44 | oppose_amount | 否 |  |  |
| 45 | waive_amount | 否 |  |  |
| 46 | order_id | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_vote_jour | ART | 是 | entrust_date, exchange_type, stock_account, stock_code, branch_no, order_id, entrust_date, exchange_type, stock_account, stock_code, branch_no, order_id |
| idx_vote_jour_pos | ART | 是 | position_str, position_str |
| idx_vote_jour | ART | 是 | entrust_date, exchange_type, stock_account, stock_code, branch_no, order_id, entrust_date, exchange_type, stock_account, stock_code, branch_no, order_id |
| idx_vote_jour_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_vote_jour | entrust_date, exchange_type, stock_account, stock_code, branch_no, order_id, entrust_date, exchange_type, stock_account, stock_code, branch_no, order_id |
| idx_vote_jour | entrust_date, exchange_type, stock_account, stock_code, branch_no, order_id, entrust_date, exchange_type, stock_account, stock_code, branch_no, order_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-25 17:34:12 | 3.0.8.6 | luofan |  |
| 2025-09-25 17:34:12 | 3.0.8.6 | luofan |  |

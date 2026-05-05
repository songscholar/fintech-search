# uft_pend_fare - UFT待扣收表

**表对象ID**: 7569
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | pendfare_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | stock_account | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | stock_type | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | compact_id | 否 |  |  |
| 11 | pendfare_type | 否 |  |  |
| 12 | money_type | 否 |  |  |
| 13 | cashgroup_no | 否 |  |  |
| 14 | total_pend_fare | 否 |  |  |
| 15 | pend_fare | 否 |  |  |
| 16 | date_clear | 否 |  |  |
| 17 | remark | 否 |  |  |
| 18 | order_no | 否 |  |  |
| 19 | position_str | 否 |  |  |
| 20 | pend_trans_flag | 否 |  |  |
| 21 | init_date | 否 |  |  |
| 22 | pendfare_id | 否 |  |  |
| 23 | branch_no | 否 |  |  |
| 24 | fund_account | 否 |  |  |
| 25 | client_id | 否 |  |  |
| 26 | stock_account | 否 |  |  |
| 27 | exchange_type | 否 |  |  |
| 28 | stock_type | 否 |  |  |
| 29 | stock_code | 否 |  |  |
| 30 | compact_id | 否 |  |  |
| 31 | pendfare_type | 否 |  |  |
| 32 | money_type | 否 |  |  |
| 33 | cashgroup_no | 否 |  |  |
| 34 | total_pend_fare | 否 |  |  |
| 35 | pend_fare | 否 |  |  |
| 36 | date_clear | 否 |  |  |
| 37 | remark | 否 |  |  |
| 38 | order_no | 否 |  |  |
| 39 | position_str | 否 |  |  |
| 40 | pend_trans_flag | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uftpendfare_pos | ART | 是 | position_str, position_str |
| idx_uftpendfare_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uftpendfare_pos | position_str, position_str |
| idx_uftpendfare_pos | position_str, position_str |

# crdtsloequity_tosett - 融券股份权益信息表2

**表对象ID**: 3083
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 76 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | serial_no | 是 |  |  |
| 3 | curr_date | 是 |  |  |
| 4 | curr_time | 是 |  |  |
| 5 | operator_no | 是 |  |  |
| 6 | op_branch_no | 是 |  |  |
| 7 | op_entrust_way | 是 |  |  |
| 8 | op_station | 是 |  |  |
| 9 | branch_no | 是 |  |  |
| 10 | fund_account | 是 |  |  |
| 11 | client_id | 是 |  |  |
| 12 | stock_account | 是 |  |  |
| 13 | exchange_type | 是 |  |  |
| 14 | stock_code | 是 |  |  |
| 15 | stock_type | 是 |  |  |
| 16 | money_type | 是 |  |  |
| 17 | equity_type | 是 |  |  |
| 18 | current_amount | 是 |  |  |
| 19 | recoup_amount | 是 |  |  |
| 20 | recoup_amount_decimal | 是 |  |  |
| 21 | recoup_balance | 是 |  |  |
| 22 | recoup_type | 是 |  |  |
| 23 | register_date | 是 |  |  |
| 24 | compact_id | 是 |  |  |
| 25 | divid_date | 是 |  |  |
| 26 | cashgroup_no | 是 |  |  |
| 27 | equity_discount_ratio | 是 |  |  |
| 28 | equity_discount_flag | 是 |  |  |
| 29 | deal_status | 是 |  |  |
| 30 | date_clear | 是 |  |  |
| 31 | remark | 是 |  |  |
| 32 | position_str | 是 |  |  |
| 33 | compact_source | 是 |  |  |
| 34 | pre_recoup_balance | 是 |  |  |
| 35 | update_date | 是 |  |  |
| 36 | update_time | 是 |  |  |
| 37 | transaction_no | 是 |  |  |
| 38 | asset_prop | 是 |  |  |
| 39 | init_date | 是 |  |  |
| 40 | serial_no | 是 |  |  |
| 41 | curr_date | 是 |  |  |
| 42 | curr_time | 是 |  |  |
| 43 | operator_no | 是 |  |  |
| 44 | op_branch_no | 是 |  |  |
| 45 | op_entrust_way | 是 |  |  |
| 46 | op_station | 是 |  |  |
| 47 | branch_no | 是 |  |  |
| 48 | fund_account | 是 |  |  |
| 49 | client_id | 是 |  |  |
| 50 | stock_account | 是 |  |  |
| 51 | exchange_type | 是 |  |  |
| 52 | stock_code | 是 |  |  |
| 53 | stock_type | 是 |  |  |
| 54 | money_type | 是 |  |  |
| 55 | equity_type | 是 |  |  |
| 56 | current_amount | 是 |  |  |
| 57 | recoup_amount | 是 |  |  |
| 58 | recoup_amount_decimal | 是 |  |  |
| 59 | recoup_balance | 是 |  |  |
| 60 | recoup_type | 是 |  |  |
| 61 | register_date | 是 |  |  |
| 62 | compact_id | 是 |  |  |
| 63 | divid_date | 是 |  |  |
| 64 | cashgroup_no | 是 |  |  |
| 65 | equity_discount_ratio | 是 |  |  |
| 66 | equity_discount_flag | 是 |  |  |
| 67 | deal_status | 是 |  |  |
| 68 | date_clear | 是 |  |  |
| 69 | remark | 是 |  |  |
| 70 | position_str | 是 |  |  |
| 71 | compact_source | 是 |  |  |
| 72 | pre_recoup_balance | 是 |  |  |
| 73 | update_date | 是 |  |  |
| 74 | update_time | 是 |  |  |
| 75 | transaction_no | 是 |  |  |
| 76 | asset_prop | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_idx_crdtsloequity_pos | 默认 | 是 | position_str, position_str |
| idx_idx_crdtsloequity_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_idx_crdtsloequity_pos | position_str, position_str |
| idx_idx_crdtsloequity_pos | position_str, position_str |

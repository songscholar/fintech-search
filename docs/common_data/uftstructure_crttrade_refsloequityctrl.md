# refsloequityctrl - 资券管理融券权益信息控制表

**表对象ID**: 7987
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 66 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | operator_no | 否 |  |  |
| 6 | op_branch_no | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | op_station | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | stock_type | 否 |  |  |
| 16 | money_type | 否 |  |  |
| 17 | equity_type | 否 |  |  |
| 18 | current_amount | 否 |  |  |
| 19 | recoup_amount | 否 |  |  |
| 20 | recoup_amount_decimal | 否 |  |  |
| 21 | recoup_balance | 否 |  |  |
| 22 | recoup_type | 否 |  |  |
| 23 | register_date | 否 |  |  |
| 24 | cashcompact_id | 否 |  |  |
| 25 | divid_date | 否 |  |  |
| 26 | cashgroup_no | 否 |  |  |
| 27 | equity_discount_ratio | 否 |  |  |
| 28 | equity_discount_flag | 否 |  |  |
| 29 | deal_status | 否 |  |  |
| 30 | date_clear | 否 |  |  |
| 31 | remark | 否 |  |  |
| 32 | position_str | 否 |  |  |
| 33 | pre_recoup_balance | 否 |  |  |
| 34 | init_date | 否 |  |  |
| 35 | serial_no | 否 |  |  |
| 36 | curr_date | 否 |  |  |
| 37 | curr_time | 否 |  |  |
| 38 | operator_no | 否 |  |  |
| 39 | op_branch_no | 否 |  |  |
| 40 | op_entrust_way | 否 |  |  |
| 41 | op_station | 否 |  |  |
| 42 | branch_no | 否 |  |  |
| 43 | fund_account | 否 |  |  |
| 44 | client_id | 否 |  |  |
| 45 | stock_account | 否 |  |  |
| 46 | exchange_type | 否 |  |  |
| 47 | stock_code | 否 |  |  |
| 48 | stock_type | 否 |  |  |
| 49 | money_type | 否 |  |  |
| 50 | equity_type | 否 |  |  |
| 51 | current_amount | 否 |  |  |
| 52 | recoup_amount | 否 |  |  |
| 53 | recoup_amount_decimal | 否 |  |  |
| 54 | recoup_balance | 否 |  |  |
| 55 | recoup_type | 否 |  |  |
| 56 | register_date | 否 |  |  |
| 57 | cashcompact_id | 否 |  |  |
| 58 | divid_date | 否 |  |  |
| 59 | cashgroup_no | 否 |  |  |
| 60 | equity_discount_ratio | 否 |  |  |
| 61 | equity_discount_flag | 否 |  |  |
| 62 | deal_status | 否 |  |  |
| 63 | date_clear | 否 |  |  |
| 64 | remark | 否 |  |  |
| 65 | position_str | 否 |  |  |
| 66 | pre_recoup_balance | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refsloequityctrl_pos | ART | 是 | position_str, position_str |
| idx_refsloequityctrl_acct | ART | 是 | fund_account, fund_account |
| idx_refsloequityctrl_pos | ART | 是 | position_str, position_str |
| idx_refsloequityctrl_acct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_refsloequityctrl_pos | position_str, position_str |
| idx_refsloequityctrl_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-30 15:45:37 | 3.0.6.61 | 黄佳平 | 新增表refsloequityctrl |
| 2025-07-30 15:45:37 | 3.0.6.61 | 黄佳平 | 新增表refsloequityctrl |

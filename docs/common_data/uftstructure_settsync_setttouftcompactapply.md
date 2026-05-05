# setttouftcompactapply - 清算合约展期申请表

**表对象ID**: 3072
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 52 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | curr_date | 是 |  |  |
| 3 | curr_time | 是 |  |  |
| 4 | serial_no | 是 |  |  |
| 5 | branch_no | 是 |  |  |
| 6 | compact_id | 是 |  |  |
| 7 | client_id | 是 |  |  |
| 8 | fund_account | 是 |  |  |
| 9 | stock_account | 是 |  |  |
| 10 | exchange_type | 是 |  |  |
| 11 | stock_code | 是 |  |  |
| 12 | cash_asset | 是 |  |  |
| 13 | market_value_begin | 是 |  |  |
| 14 | total_debit | 是 |  |  |
| 15 | per_assurescale_value | 是 |  |  |
| 16 | risk_remind_info | 是 |  |  |
| 17 | assist_info | 是 |  |  |
| 18 | compact_apply_status | 是 |  |  |
| 19 | date_clear | 是 |  |  |
| 20 | remark | 是 |  |  |
| 21 | position_str | 是 |  |  |
| 22 | autoaudit_fail_reason | 是 |  |  |
| 23 | op_station | 是 |  |  |
| 24 | real_compact_balance | 是 |  |  |
| 25 | real_compact_fare | 是 |  |  |
| 26 | uft_data_change_status | 是 |  |  |
| 27 | init_date | 是 |  |  |
| 28 | curr_date | 是 |  |  |
| 29 | curr_time | 是 |  |  |
| 30 | serial_no | 是 |  |  |
| 31 | branch_no | 是 |  |  |
| 32 | compact_id | 是 |  |  |
| 33 | client_id | 是 |  |  |
| 34 | fund_account | 是 |  |  |
| 35 | stock_account | 是 |  |  |
| 36 | exchange_type | 是 |  |  |
| 37 | stock_code | 是 |  |  |
| 38 | cash_asset | 是 |  |  |
| 39 | market_value_begin | 是 |  |  |
| 40 | total_debit | 是 |  |  |
| 41 | per_assurescale_value | 是 |  |  |
| 42 | risk_remind_info | 是 |  |  |
| 43 | assist_info | 是 |  |  |
| 44 | compact_apply_status | 是 |  |  |
| 45 | date_clear | 是 |  |  |
| 46 | remark | 是 |  |  |
| 47 | position_str | 是 |  |  |
| 48 | autoaudit_fail_reason | 是 |  |  |
| 49 | op_station | 是 |  |  |
| 50 | real_compact_balance | 是 |  |  |
| 51 | real_compact_fare | 是 |  |  |
| 52 | uft_data_change_status | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_settcompactapply | 默认 | 是 | position_str, position_str |
| idx_settcompactapply_fund | 默认 | 是 | fund_account, compact_id, fund_account, compact_id |
| uk_settcompactapply | 默认 | 是 | position_str, position_str |
| idx_settcompactapply_fund | 默认 | 是 | fund_account, compact_id, fund_account, compact_id |

## 数据库索引（共 8 个）

| 索引名 | 字段 |
|--------|------|
| idx_compactapply_pos | position_str, position_str |
| idx_compactapply_acct | fund_account, fund_account |
| idx_compactapply_stock | stock_code, exchange_type, stock_code, exchange_type |
| idx_compactapply | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_compactapply_pos | position_str, position_str |
| idx_compactapply_acct | fund_account, fund_account |
| idx_compactapply_stock | stock_code, exchange_type, stock_code, exchange_type |
| idx_compactapply | serial_no, branch_no, init_date, serial_no, branch_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2021-07-12 10:59 | 8.26.2.2 | 罗佳楠 | 修改索引 |
| 2019-05-07 15:03 | 8.26.1.51 | 林忠芝 | 新增 |
| 2021-07-12 10:59 | 8.26.2.2 | 罗佳楠 | 修改索引 |
| 2019-05-07 15:03 | 8.26.1.51 | 林忠芝 | 新增 |

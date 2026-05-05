# setttouftsrpassure - 清算股票质押担保物表

**表对象ID**: 3045
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 是 |  |  |
| 2 | client_id | 是 |  |  |
| 3 | branch_no | 是 |  |  |
| 4 | stock_account | 是 |  |  |
| 5 | impawn_asset_type | 是 |  |  |
| 6 | contract_id | 是 |  |  |
| 7 | stock_code | 是 |  |  |
| 8 | exchange_type | 是 |  |  |
| 9 | seat_no | 是 |  |  |
| 10 | stock_property | 是 |  |  |
| 11 | stock_describe | 是 |  |  |
| 12 | impawn_id | 是 |  |  |
| 13 | report_id | 是 |  |  |
| 14 | current_amount | 是 |  |  |
| 15 | enable_amount | 是 |  |  |
| 16 | current_balance | 是 |  |  |
| 17 | enable_balance | 是 |  |  |
| 18 | enable_sell | 是 |  |  |
| 19 | settle_flag | 是 |  |  |
| 20 | position_str | 是 |  |  |
| 21 | fund_account | 是 |  |  |
| 22 | client_id | 是 |  |  |
| 23 | branch_no | 是 |  |  |
| 24 | stock_account | 是 |  |  |
| 25 | impawn_asset_type | 是 |  |  |
| 26 | contract_id | 是 |  |  |
| 27 | stock_code | 是 |  |  |
| 28 | exchange_type | 是 |  |  |
| 29 | seat_no | 是 |  |  |
| 30 | stock_property | 是 |  |  |
| 31 | stock_describe | 是 |  |  |
| 32 | impawn_id | 是 |  |  |
| 33 | report_id | 是 |  |  |
| 34 | current_amount | 是 |  |  |
| 35 | enable_amount | 是 |  |  |
| 36 | current_balance | 是 |  |  |
| 37 | enable_balance | 是 |  |  |
| 38 | enable_sell | 是 |  |  |
| 39 | settle_flag | 是 |  |  |
| 40 | position_str | 是 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_settsrpassure | 默认 | 是 | position_str, position_str |
| idx_settsrpassure_id | 默认 | 是 | contract_id, contract_id |
| idx_settsrpassure_report | 默认 | 是 | report_id, report_id |
| idx_settsrpassure_acct | 默认 | 是 | stock_account, exchange_type, stock_account, exchange_type |
| uk_settsrpassure | 默认 | 是 | position_str, position_str |
| idx_settsrpassure_id | 默认 | 是 | contract_id, contract_id |
| idx_settsrpassure_report | 默认 | 是 | report_id, report_id |
| idx_settsrpassure_acct | 默认 | 是 | stock_account, exchange_type, stock_account, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| uk_settsrpassure | position_str, position_str |
| uk_settsrpassure | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2021-12-06 15:47 | 8.26.2.15 | 徐开 | settsrpassure增加索引 |
| 2020-03-16 09:36 | 8.26.1.76 | 曾哲 | 新增索引idx_settsrpassure_report |
| 2021-12-06 15:47 | 8.26.2.15 | 徐开 | settsrpassure增加索引 |
| 2020-03-16 09:36 | 8.26.1.76 | 曾哲 | 新增索引idx_settsrpassure_report |

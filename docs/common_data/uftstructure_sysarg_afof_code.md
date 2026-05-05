# afof_code - 基金盘后业务代码表

**表对象ID**: 129
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 84 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | modify_date | 否 |  |  |
| 5 | stock_name | 否 |  |  |
| 6 | fund_status | 否 |  |  |
| 7 | nav_date | 否 |  |  |
| 8 | nav | 否 |  |  |
| 9 | nav_total | 否 |  |  |
| 10 | main_stockcode | 否 |  |  |
| 11 | merge_allow_flag | 否 |  |  |
| 12 | split_allow_flag | 否 |  |  |
| 13 | mergesplit_status | 否 |  |  |
| 14 | mergesplit_amount | 否 |  |  |
| 15 | min_mergeamount | 否 |  |  |
| 16 | min_splitamount | 否 |  |  |
| 17 | oftrans_status | 否 |  |  |
| 18 | en_change_code | 否 |  |  |
| 19 | manage_id | 否 |  |  |
| 20 | ta_no | 否 |  |  |
| 21 | redeem_delaydate | 否 |  |  |
| 22 | draw_delaydate | 否 |  |  |
| 23 | unassure_flag | 否 |  |  |
| 24 | redeem_method | 否 |  |  |
| 25 | app_unit | 否 |  |  |
| 26 | redemption_unit | 否 |  |  |
| 27 | max_redemptionvol | 否 |  |  |
| 28 | min_redemptionvol | 否 |  |  |
| 29 | min_accountbalance | 否 |  |  |
| 30 | min_app_balance | 否 |  |  |
| 31 | transfer_price | 否 |  |  |
| 32 | remark | 否 |  |  |
| 33 | sub_unit | 否 |  |  |
| 34 | en_business_status | 否 |  |  |
| 35 | mergesplit_unit | 否 |  |  |
| 36 | lof_type | 否 |  |  |
| 37 | min_subsamountbyindi | 否 |  |  |
| 38 | max_perdapp_balance | 否 |  |  |
| 39 | update_date | 否 |  |  |
| 40 | update_time | 否 |  |  |
| 41 | transaction_no | 否 |  |  |
| 42 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 43 | exchange_type | 否 |  |  |
| 44 | stock_code | 否 |  |  |
| 45 | money_type | 否 |  |  |
| 46 | modify_date | 否 |  |  |
| 47 | stock_name | 否 |  |  |
| 48 | fund_status | 否 |  |  |
| 49 | nav_date | 否 |  |  |
| 50 | nav | 否 |  |  |
| 51 | nav_total | 否 |  |  |
| 52 | main_stockcode | 否 |  |  |
| 53 | merge_allow_flag | 否 |  |  |
| 54 | split_allow_flag | 否 |  |  |
| 55 | mergesplit_status | 否 |  |  |
| 56 | mergesplit_amount | 否 |  |  |
| 57 | min_mergeamount | 否 |  |  |
| 58 | min_splitamount | 否 |  |  |
| 59 | oftrans_status | 否 |  |  |
| 60 | en_change_code | 否 |  |  |
| 61 | manage_id | 否 |  |  |
| 62 | ta_no | 否 |  |  |
| 63 | redeem_delaydate | 否 |  |  |
| 64 | draw_delaydate | 否 |  |  |
| 65 | unassure_flag | 否 |  |  |
| 66 | redeem_method | 否 |  |  |
| 67 | app_unit | 否 |  |  |
| 68 | redemption_unit | 否 |  |  |
| 69 | max_redemptionvol | 否 |  |  |
| 70 | min_redemptionvol | 否 |  |  |
| 71 | min_accountbalance | 否 |  |  |
| 72 | min_app_balance | 否 |  |  |
| 73 | transfer_price | 否 |  |  |
| 74 | remark | 否 |  |  |
| 75 | sub_unit | 否 |  |  |
| 76 | en_business_status | 否 |  |  |
| 77 | mergesplit_unit | 否 |  |  |
| 78 | lof_type | 否 |  |  |
| 79 | min_subsamountbyindi | 否 |  |  |
| 80 | max_perdapp_balance | 否 |  |  |
| 81 | update_date | 否 |  |  |
| 82 | update_time | 否 |  |  |
| 83 | transaction_no | 否 |  |  |
| 84 | position_str | 否 |  | stock_code(8)+exchange_type(4) |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_afof_code | 默认 | 否 |  |
| idx_afof_code_main | 默认 | 否 |  |
| idx_afof_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_afof_code_main | ART | 是 | main_stockcode, exchange_type, main_stockcode, exchange_type |
| idx_afof_code | 默认 | 否 |  |
| idx_afof_code_main | 默认 | 否 |  |
| idx_afof_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_afof_code_main | ART | 是 | main_stockcode, exchange_type, main_stockcode, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_afof_code | stock_code, exchange_type, stock_code, exchange_type |
| idx_afof_code | stock_code, exchange_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:35:25 | 3.0.2.103 | taocong45644 | 当前表afof_code，修改了索引idx_afof_code,索引字段修改为：(stock_code,exchange... |
| 2025-02-18 17:31:46 | 3.0.6.73 | 李想 | 新增表 |
| 2025-12-01 14:35:25 | 3.0.2.103 | taocong45644 | 当前表afof_code，修改了索引idx_afof_code,索引字段修改为：(stock_code,exchange... |
| 2025-02-18 17:31:46 | 3.0.6.73 | 李想 | 新增表 |

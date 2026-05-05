# ucrt_surplus_stock_jour - 余券信息流水表

**表对象ID**: 7548
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 72 个）

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
| 9 | real_action | 否 |  |  |
| 10 | client_id | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | stock_type | 否 |  |  |
| 16 | money_type | 否 |  |  |
| 17 | business_flag | 否 |  |  |
| 18 | occur_amount | 否 |  |  |
| 19 | post_amount | 否 |  |  |
| 20 | surstock_end_balance | 否 |  |  |
| 21 | cancel_serial_no | 否 |  |  |
| 22 | cashgroup_no | 否 |  |  |
| 23 | branch_no | 否 |  |  |
| 24 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 25 | client_group | 否 | H |  |
| 26 | room_code | 否 | H |  |
| 27 | asset_prop | 否 | H |  |
| 28 | corp_client_group | 否 | H |  |
| 29 | risk_level | 否 | H |  |
| 30 | limit_flag | 否 | H |  |
| 31 | client_name | 否 | H |  |
| 32 | asset_level | 否 | H |  |
| 33 | corp_risk_level | 否 | H |  |
| 34 | client_prop | 否 | H |  |
| 35 | stock_name | 否 | H |  |
| 36 | sub_stock_type | 否 | H |  |
| 37 | init_date | 否 |  |  |
| 38 | serial_no | 否 |  |  |
| 39 | curr_date | 否 |  |  |
| 40 | curr_time | 否 |  |  |
| 41 | operator_no | 否 |  |  |
| 42 | op_branch_no | 否 |  |  |
| 43 | op_entrust_way | 否 |  |  |
| 44 | op_station | 否 |  |  |
| 45 | real_action | 否 |  |  |
| 46 | client_id | 否 |  |  |
| 47 | fund_account | 否 |  |  |
| 48 | exchange_type | 否 |  |  |
| 49 | stock_account | 否 |  |  |
| 50 | stock_code | 否 |  |  |
| 51 | stock_type | 否 |  |  |
| 52 | money_type | 否 |  |  |
| 53 | business_flag | 否 |  |  |
| 54 | occur_amount | 否 |  |  |
| 55 | post_amount | 否 |  |  |
| 56 | surstock_end_balance | 否 |  |  |
| 57 | cancel_serial_no | 否 |  |  |
| 58 | cashgroup_no | 否 |  |  |
| 59 | branch_no | 否 |  |  |
| 60 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 61 | client_group | 否 | H |  |
| 62 | room_code | 否 | H |  |
| 63 | asset_prop | 否 | H |  |
| 64 | corp_client_group | 否 | H |  |
| 65 | risk_level | 否 | H |  |
| 66 | limit_flag | 否 | H |  |
| 67 | client_name | 否 | H |  |
| 68 | asset_level | 否 | H |  |
| 69 | corp_risk_level | 否 | H |  |
| 70 | client_prop | 否 | H |  |
| 71 | stock_name | 否 | H |  |
| 72 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_urct_surplusstockjour | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_ucrt_surplusstockjour_cash | ART | 是 | fund_account, cashgroup_no, exchange_type, stock_code, fund_account, cashgroup_no, exchange_type, stock_code |
| uk_rpt_ucrtsurplusstockjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtsurplusstockjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_urct_surplusstockjour | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_ucrt_surplusstockjour_cash | ART | 是 | fund_account, cashgroup_no, exchange_type, stock_code, fund_account, cashgroup_no, exchange_type, stock_code |
| uk_rpt_ucrtsurplusstockjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtsurplusstockjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_surplus_stock_jour | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_ucrt_surplus_stock_jour | fund_account, init_date, serial_no, fund_account, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-21 14:41:21 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_surplus_stock_jour，添加了表字段(branch_no);
物理表ucrt_surpl... |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-29 10:35 | 0.0.0.14 | 杨森峰 | 修改索引类型 |
| 2023-06-01 14:58 | 0.0.0.2 | 杨森峰 | 支持两融撤成功能 |
| 2025-08-21 14:41:21 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_surplus_stock_jour，添加了表字段(branch_no);
物理表ucrt_surpl... |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-29 10:35 | 0.0.0.14 | 杨森峰 | 修改索引类型 |
| 2023-06-01 14:58 | 0.0.0.2 | 杨森峰 | 支持两融撤成功能 |

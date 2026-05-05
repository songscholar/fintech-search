# ucrt_out_asset_jour - 场外资产信息流水表

**表对象ID**: 7514
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 70 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | operator_no | 否 |  |  |
| 6 | op_branch_no | 否 |  |  |
| 7 | op_station | 否 |  |  |
| 8 | client_id | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | out_asset_type | 否 |  |  |
| 11 | business_flag | 否 |  |  |
| 12 | occur_balance | 否 |  |  |
| 13 | post_balance | 否 |  |  |
| 14 | remark | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | current_amount | 否 |  |  |
| 18 | assure_ratio | 否 |  |  |
| 19 | post_amount | 否 |  |  |
| 20 | occur_amount | 否 |  |  |
| 21 | branch_no | 否 |  |  |
| 22 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 23 | stock_name | 否 | H |  |
| 24 | sub_stock_type | 否 | H |  |
| 25 | stock_type | 否 | H |  |
| 26 | client_group | 否 | H |  |
| 27 | room_code | 否 | H |  |
| 28 | asset_prop | 否 | H |  |
| 29 | limit_flag | 否 | H |  |
| 30 | risk_level | 否 | H |  |
| 31 | corp_client_group | 否 | H |  |
| 32 | corp_risk_level | 否 | H |  |
| 33 | asset_level | 否 | H |  |
| 34 | client_name | 否 | H |  |
| 35 | client_prop | 否 | H |  |
| 36 | init_date | 否 |  |  |
| 37 | serial_no | 否 |  |  |
| 38 | curr_date | 否 |  |  |
| 39 | curr_time | 否 |  |  |
| 40 | operator_no | 否 |  |  |
| 41 | op_branch_no | 否 |  |  |
| 42 | op_station | 否 |  |  |
| 43 | client_id | 否 |  |  |
| 44 | fund_account | 否 |  |  |
| 45 | out_asset_type | 否 |  |  |
| 46 | business_flag | 否 |  |  |
| 47 | occur_balance | 否 |  |  |
| 48 | post_balance | 否 |  |  |
| 49 | remark | 否 |  |  |
| 50 | exchange_type | 否 |  |  |
| 51 | stock_code | 否 |  |  |
| 52 | current_amount | 否 |  |  |
| 53 | assure_ratio | 否 |  |  |
| 54 | post_amount | 否 |  |  |
| 55 | occur_amount | 否 |  |  |
| 56 | branch_no | 否 |  |  |
| 57 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 58 | stock_name | 否 | H |  |
| 59 | sub_stock_type | 否 | H |  |
| 60 | stock_type | 否 | H |  |
| 61 | client_group | 否 | H |  |
| 62 | room_code | 否 | H |  |
| 63 | asset_prop | 否 | H |  |
| 64 | limit_flag | 否 | H |  |
| 65 | risk_level | 否 | H |  |
| 66 | corp_client_group | 否 | H |  |
| 67 | corp_risk_level | 否 | H |  |
| 68 | asset_level | 否 | H |  |
| 69 | client_name | 否 | H |  |
| 70 | client_prop | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_out_asset_jour | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| uk_rpt_ucrtoutassetjour | ART | 是 | init_date, position_str, init_date, position_str |
| idx_ucrt_out_asset_jour | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| uk_rpt_ucrtoutassetjour | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_out_asset_jour | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_ucrt_out_asset_jour | fund_account, init_date, serial_no, fund_account, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-10 09:45:52 | 3.0.8.10 | 许琮擎 | 增加唯一索引，支持数据二次上场 |
| 2025-08-21 18:38:01 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_out_asset_jour，添加了表字段(branch_no);
物理表ucrt_out_asset... |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-07 16:28 | 0.0.0.7 | 程猛 | 新增字段occur_balance |
| 2025-10-10 09:45:52 | 3.0.8.10 | 许琮擎 | 增加唯一索引，支持数据二次上场 |
| 2025-08-21 18:38:01 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_out_asset_jour，添加了表字段(branch_no);
物理表ucrt_out_asset... |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-07 16:28 | 0.0.0.7 | 程猛 | 新增字段occur_balance |

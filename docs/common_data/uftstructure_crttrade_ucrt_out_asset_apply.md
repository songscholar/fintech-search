# ucrt_out_asset_apply - 信用场外资产登记申请表

**表对象ID**: 7527
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 72 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_microtime | 否 |  |  |
| 4 | serial_no | 否 |  |  |
| 5 | operator_no | 否 |  |  |
| 6 | op_branch_no | 否 |  |  |
| 7 | op_station | 否 |  |  |
| 8 | client_id | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | per_assurescale_value | 否 |  |  |
| 11 | asset_cmd_type | 否 |  |  |
| 12 | out_asset_type | 否 |  |  |
| 13 | out_apply_status | 否 |  |  |
| 14 | out_assure_value | 否 |  |  |
| 15 | valid_date | 否 |  |  |
| 16 | date_clear | 否 |  |  |
| 17 | remark | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | stock_code | 否 |  |  |
| 20 | current_amount | 否 |  |  |
| 21 | assure_ratio | 否 |  |  |
| 22 | branch_no | 否 |  |  |
| 23 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 24 | stock_name | 否 | H |  |
| 25 | sub_stock_type | 否 | H |  |
| 26 | stock_type | 否 | H |  |
| 27 | client_group | 否 | H |  |
| 28 | room_code | 否 | H |  |
| 29 | asset_prop | 否 | H |  |
| 30 | limit_flag | 否 | H |  |
| 31 | risk_level | 否 | H |  |
| 32 | corp_client_group | 否 | H |  |
| 33 | corp_risk_level | 否 | H |  |
| 34 | asset_level | 否 | H |  |
| 35 | client_name | 否 | H |  |
| 36 | client_prop | 否 | H |  |
| 37 | init_date | 否 |  |  |
| 38 | curr_date | 否 |  |  |
| 39 | curr_microtime | 否 |  |  |
| 40 | serial_no | 否 |  |  |
| 41 | operator_no | 否 |  |  |
| 42 | op_branch_no | 否 |  |  |
| 43 | op_station | 否 |  |  |
| 44 | client_id | 否 |  |  |
| 45 | fund_account | 否 |  |  |
| 46 | per_assurescale_value | 否 |  |  |
| 47 | asset_cmd_type | 否 |  |  |
| 48 | out_asset_type | 否 |  |  |
| 49 | out_apply_status | 否 |  |  |
| 50 | out_assure_value | 否 |  |  |
| 51 | valid_date | 否 |  |  |
| 52 | date_clear | 否 |  |  |
| 53 | remark | 否 |  |  |
| 54 | exchange_type | 否 |  |  |
| 55 | stock_code | 否 |  |  |
| 56 | current_amount | 否 |  |  |
| 57 | assure_ratio | 否 |  |  |
| 58 | branch_no | 否 |  |  |
| 59 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 60 | stock_name | 否 | H |  |
| 61 | sub_stock_type | 否 | H |  |
| 62 | stock_type | 否 | H |  |
| 63 | client_group | 否 | H |  |
| 64 | room_code | 否 | H |  |
| 65 | asset_prop | 否 | H |  |
| 66 | limit_flag | 否 | H |  |
| 67 | risk_level | 否 | H |  |
| 68 | corp_client_group | 否 | H |  |
| 69 | corp_risk_level | 否 | H |  |
| 70 | asset_level | 否 | H |  |
| 71 | client_name | 否 | H |  |
| 72 | client_prop | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_out_asset_apply_globe | ART | 是 | init_date, serial_no, fund_account, init_date, serial_no, fund_account |
| idx_ucrt_out_asset_apply | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| uk_rpt_ucrtoutassetapply | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtoutassetapply_cid | ART | 是 | init_date, client_id, fund_account, init_date, client_id, fund_account |
| idx_rpt_ucrtoutassetapply_tolast | ART | 是 | date_clear, date_clear |
| idx_ucrt_out_asset_apply_globe | ART | 是 | init_date, serial_no, fund_account, init_date, serial_no, fund_account |
| idx_ucrt_out_asset_apply | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| uk_rpt_ucrtoutassetapply | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtoutassetapply_cid | ART | 是 | init_date, client_id, fund_account, init_date, client_id, fund_account |
| idx_rpt_ucrtoutassetapply_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_out_asset_apply | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_ucrt_out_asset_apply | fund_account, init_date, serial_no, fund_account, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-21 18:38:34 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_out_asset_apply，添加了表字段(branch_no);
物理表ucrt_out_asse... |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2023-10-19 09:24:46 | V3.0.1.8 | 黄积冲 | ucrt_out_asset_apply增加全局索引idx_ucrt_out_asset_apply_globe |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-08-21 18:38:34 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_out_asset_apply，添加了表字段(branch_no);
物理表ucrt_out_asse... |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2023-10-19 09:24:46 | V3.0.1.8 | 黄积冲 | ucrt_out_asset_apply增加全局索引idx_ucrt_out_asset_apply_globe |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

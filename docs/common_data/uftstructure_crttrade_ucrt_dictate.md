# ucrt_dictate - 平仓指令信息表

**表对象ID**: 7509
**所属模块**: crttrade
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 84 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | dictate_type | 否 |  |  |
| 5 | dictate_status | 否 |  |  |
| 6 | crdtsrc_type | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | date_clear | 否 |  |  |
| 9 | op_branch_no | 否 |  |  |
| 10 | operator_no | 否 |  |  |
| 11 | op_entrust_way | 否 |  |  |
| 12 | op_station | 否 |  |  |
| 13 | client_id | 否 |  |  |
| 14 | branch_no | 否 |  |  |
| 15 | assure_asset | 否 |  |  |
| 16 | total_debit | 否 |  |  |
| 17 | assurescale_value | 否 |  |  |
| 18 | dictate_applicant | 否 |  |  |
| 19 | apply_date | 否 |  |  |
| 20 | apply_time | 否 |  |  |
| 21 | dictate_sender | 否 |  |  |
| 22 | send_date | 否 |  |  |
| 23 | send_time | 否 |  |  |
| 24 | dictate_closer | 否 |  |  |
| 25 | close_date | 否 |  |  |
| 26 | close_time | 否 |  |  |
| 27 | limit_days | 否 |  |  |
| 28 | remark | 否 |  |  |
| 29 | position_str | 否 |  |  |
| 30 | en_payoff_reason | 否 |  |  |
| 31 | update_date | 否 |  |  |
| 32 | update_time | 否 |  |  |
| 33 | client_group | 否 | H |  |
| 34 | room_code | 否 | H |  |
| 35 | asset_prop | 否 | H |  |
| 36 | limit_flag | 否 | H |  |
| 37 | risk_level | 否 | H |  |
| 38 | corp_client_group | 否 | H |  |
| 39 | corp_risk_level | 否 | H |  |
| 40 | asset_level | 否 | H |  |
| 41 | client_name | 否 | H |  |
| 42 | client_prop | 否 | H |  |
| 43 | init_date | 否 |  |  |
| 44 | serial_no | 否 |  |  |
| 45 | fund_account | 否 |  |  |
| 46 | dictate_type | 否 |  |  |
| 47 | dictate_status | 否 |  |  |
| 48 | crdtsrc_type | 否 |  |  |
| 49 | transaction_no | 否 |  |  |
| 50 | date_clear | 否 |  |  |
| 51 | op_branch_no | 否 |  |  |
| 52 | operator_no | 否 |  |  |
| 53 | op_entrust_way | 否 |  |  |
| 54 | op_station | 否 |  |  |
| 55 | client_id | 否 |  |  |
| 56 | branch_no | 否 |  |  |
| 57 | assure_asset | 否 |  |  |
| 58 | total_debit | 否 |  |  |
| 59 | assurescale_value | 否 |  |  |
| 60 | dictate_applicant | 否 |  |  |
| 61 | apply_date | 否 |  |  |
| 62 | apply_time | 否 |  |  |
| 63 | dictate_sender | 否 |  |  |
| 64 | send_date | 否 |  |  |
| 65 | send_time | 否 |  |  |
| 66 | dictate_closer | 否 |  |  |
| 67 | close_date | 否 |  |  |
| 68 | close_time | 否 |  |  |
| 69 | limit_days | 否 |  |  |
| 70 | remark | 否 |  |  |
| 71 | position_str | 否 |  |  |
| 72 | en_payoff_reason | 否 |  |  |
| 73 | update_date | 否 |  |  |
| 74 | update_time | 否 |  |  |
| 75 | client_group | 否 | H |  |
| 76 | room_code | 否 | H |  |
| 77 | asset_prop | 否 | H |  |
| 78 | limit_flag | 否 | H |  |
| 79 | risk_level | 否 | H |  |
| 80 | corp_client_group | 否 | H |  |
| 81 | corp_risk_level | 否 | H |  |
| 82 | asset_level | 否 | H |  |
| 83 | client_name | 否 | H |  |
| 84 | client_prop | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_dictate | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| uk_rpt_ucrtdictate | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtdictate_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_ucrtdictate_tolast | ART | 是 | date_clear, date_clear |
| idx_ucrt_dictate | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| uk_rpt_ucrtdictate | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtdictate_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_ucrtdictate_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_dictate | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_ucrt_dictate | fund_account, init_date, serial_no, fund_account, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-17 16:36:42 | 3.0.2.21 | 常行 | ucrt_dictate表空间改为HS_USMS_DATA，存储介质改为DB+MDB |
| 2025-10-17 15:36:37 | 3.0.2.21 | 常行 | 物理表ucrt_dictate，添加了表字段(update_date);
所有表ucrt_dictate，添加了表字段... |
| 2025-07-08 13:09:23 | 3.0.2.2008 | huangzh | 物理表ucrt_dictate，添加了表字段(op_branch_no);
物理表ucrt_dictate，添加了表字... |
| 2025-04-04 11:27:20 | 3.0.2.2001 | 卢杰 | 物理表ucrt_dictate，添加了表字段(date_clear);
 |
| 2023-08-22 13:33:32 | 0.3.3.141 | 徐志坚 | 因参数同步需要增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-10-17 16:36:42 | 3.0.2.21 | 常行 | ucrt_dictate表空间改为HS_USMS_DATA，存储介质改为DB+MDB |
| 2025-10-17 15:36:37 | 3.0.2.21 | 常行 | 物理表ucrt_dictate，添加了表字段(update_date);
所有表ucrt_dictate，添加了表字段... |
| 2025-07-08 13:09:23 | 3.0.2.2008 | huangzh | 物理表ucrt_dictate，添加了表字段(op_branch_no);
物理表ucrt_dictate，添加了表字... |
| 2025-04-04 11:27:20 | 3.0.2.2001 | 卢杰 | 物理表ucrt_dictate，添加了表字段(date_clear);
 |
| 2023-08-22 13:33:32 | 0.3.3.141 | 徐志坚 | 因参数同步需要增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

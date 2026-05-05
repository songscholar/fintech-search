# ucrt_fund_real_jour - 融资融券交易资金变动表

**表对象ID**: 7533
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 58 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | finance_type | 否 |  |  |
| 8 | money_type | 否 |  |  |
| 9 | occur_balance | 否 |  |  |
| 10 | post_balance | 否 |  |  |
| 11 | real_action | 否 |  |  |
| 12 | business_flag | 否 |  |  |
| 13 | asset_prop | 否 |  |  |
| 14 | real_serialno | 否 |  |  |
| 15 | cancel_serial_no | 否 |  |  |
| 16 | fund_real_jour_kind | 否 |  |  |
| 17 | sett_batch_no | 否 |  |  |
| 18 | branch_no | 否 |  |  |
| 19 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 20 | client_group | 否 | H |  |
| 21 | room_code | 否 | H |  |
| 22 | limit_flag | 否 | H |  |
| 23 | risk_level | 否 | H |  |
| 24 | corp_client_group | 否 | H |  |
| 25 | corp_risk_level | 否 | H |  |
| 26 | asset_level | 否 | H |  |
| 27 | client_name | 否 | H |  |
| 28 | client_prop | 否 | H |  |
| 29 | remark | 否 |  |  |
| 30 | init_date | 否 |  |  |
| 31 | serial_no | 否 |  |  |
| 32 | curr_date | 否 |  |  |
| 33 | curr_time | 否 |  |  |
| 34 | client_id | 否 |  |  |
| 35 | fund_account | 否 |  |  |
| 36 | finance_type | 否 |  |  |
| 37 | money_type | 否 |  |  |
| 38 | occur_balance | 否 |  |  |
| 39 | post_balance | 否 |  |  |
| 40 | real_action | 否 |  |  |
| 41 | business_flag | 否 |  |  |
| 42 | asset_prop | 否 |  |  |
| 43 | real_serialno | 否 |  |  |
| 44 | cancel_serial_no | 否 |  |  |
| 45 | fund_real_jour_kind | 否 |  |  |
| 46 | sett_batch_no | 否 |  |  |
| 47 | branch_no | 否 |  |  |
| 48 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 49 | client_group | 否 | H |  |
| 50 | room_code | 否 | H |  |
| 51 | limit_flag | 否 | H |  |
| 52 | risk_level | 否 | H |  |
| 53 | corp_client_group | 否 | H |  |
| 54 | corp_risk_level | 否 | H |  |
| 55 | asset_level | 否 | H |  |
| 56 | client_name | 否 | H |  |
| 57 | client_prop | 否 | H |  |
| 58 | remark | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_fund_real_jour | ART | 是 | fund_account, money_type, init_date, serial_no, fund_account, money_type, init_date, serial_no |
| uk_rpt_ucrtfundrealjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtfundrealjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_ucrt_fund_real_jour | ART | 是 | fund_account, money_type, init_date, serial_no, fund_account, money_type, init_date, serial_no |
| uk_rpt_ucrtfundrealjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtfundrealjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_fund_real_jour | fund_account, money_type, init_date, serial_no, fund_account, money_type, init_date, serial_no |
| idx_ucrt_fund_real_jour | fund_account, money_type, init_date, serial_no, fund_account, money_type, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-27 11:09:52 | 3.0.6.1065 | 周兆军 | 所有表ucrt_fund_detail_jour，添加了表字段(position_str);
 |
| 2025-08-21 14:42:55 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_fund_real_jour，添加了表字段(branch_no);
物理表ucrt_fund_real... |
| 2025-08-18 09:01:49 | 3.0.2.1 | 曾阳璞 | 所有表ucrt_fund_real_jour，添加了表字段(sett_batch_no);
 |
| 2023-11-01 15:35:55 | V3.0.1.15 | 范文浩 | 物理表ucrt_fund_real_jour，添加了表字段(fund_real_jour_kind);
物理表ucrt... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 14:26 | 0.0.0.7 | 程猛 | 删除表字段order_no |
| 2025-08-27 11:09:52 | 3.0.6.1065 | 周兆军 | 所有表ucrt_fund_detail_jour，添加了表字段(position_str);
 |
| 2025-08-21 14:42:55 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_fund_real_jour，添加了表字段(branch_no);
物理表ucrt_fund_real... |
| 2025-08-18 09:01:49 | 3.0.2.1 | 曾阳璞 | 所有表ucrt_fund_real_jour，添加了表字段(sett_batch_no);
 |
| 2023-11-01 15:35:55 | V3.0.1.15 | 范文浩 | 物理表ucrt_fund_real_jour，添加了表字段(fund_real_jour_kind);
物理表ucrt... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 14:26 | 0.0.0.7 | 程猛 | 删除表字段order_no |

# ucrt_fund_detail_jour - 融资融券交易资金详细信息流水表

**表对象ID**: 7535
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 56 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_microtime | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | fund_enable_level | 否 |  |  |
| 8 | money_type | 否 |  |  |
| 9 | fund_update_direction | 否 |  |  |
| 10 | occur_balance | 否 |  |  |
| 11 | post_balance | 否 |  |  |
| 12 | real_action | 否 |  |  |
| 13 | business_flag | 否 |  |  |
| 14 | cancel_serial_no | 否 |  |  |
| 15 | remark | 否 |  |  |
| 16 | sett_batch_no | 否 |  |  |
| 17 | position_str | 否 |  | init_date(8)+partition_no(2)+serial_no(10) |
| 18 | branch_no | 否 | H |  |
| 19 | client_group | 否 | H |  |
| 20 | room_code | 否 | H |  |
| 21 | asset_prop | 否 | H |  |
| 22 | limit_flag | 否 | H |  |
| 23 | risk_level | 否 | H |  |
| 24 | corp_client_group | 否 | H |  |
| 25 | corp_risk_level | 否 | H |  |
| 26 | asset_level | 否 | H |  |
| 27 | client_name | 否 | H |  |
| 28 | client_prop | 否 | H |  |
| 29 | init_date | 否 |  |  |
| 30 | serial_no | 否 |  |  |
| 31 | curr_date | 否 |  |  |
| 32 | curr_microtime | 否 |  |  |
| 33 | client_id | 否 |  |  |
| 34 | fund_account | 否 |  |  |
| 35 | fund_enable_level | 否 |  |  |
| 36 | money_type | 否 |  |  |
| 37 | fund_update_direction | 否 |  |  |
| 38 | occur_balance | 否 |  |  |
| 39 | post_balance | 否 |  |  |
| 40 | real_action | 否 |  |  |
| 41 | business_flag | 否 |  |  |
| 42 | cancel_serial_no | 否 |  |  |
| 43 | remark | 否 |  |  |
| 44 | sett_batch_no | 否 |  |  |
| 45 | position_str | 否 |  | init_date(8)+partition_no(2)+serial_no(10) |
| 46 | branch_no | 否 | H |  |
| 47 | client_group | 否 | H |  |
| 48 | room_code | 否 | H |  |
| 49 | asset_prop | 否 | H |  |
| 50 | limit_flag | 否 | H |  |
| 51 | risk_level | 否 | H |  |
| 52 | corp_client_group | 否 | H |  |
| 53 | corp_risk_level | 否 | H |  |
| 54 | asset_level | 否 | H |  |
| 55 | client_name | 否 | H |  |
| 56 | client_prop | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_fund_detail_jour | ART | 是 | init_date, serial_no, init_date, serial_no |
| uk_rpt_ucrtfunddetailjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtfunddetailjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_ucrt_fund_detail_jour | ART | 是 | init_date, serial_no, init_date, serial_no |
| uk_rpt_ucrtfunddetailjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtfunddetailjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_fund_detail_jour | init_date, serial_no, init_date, serial_no |
| idx_ucrt_fund_detail_jour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-27 11:09:52 | 3.0.6.1065 | 周兆军 | 所有表ucrt_fund_detail_jour，添加了表字段(position_str);
 |
| 2025-08-18 09:00:35 | 3.0.2.1 | 曾阳璞 | 所有表ucrt_fund_detail_jour，添加了表字段(sett_batch_no);
 |
| 2025-06-03 21:00:00 | 3.0.6.58 | 范文浩 | 物理表ucrt_fund_detail_jour，添加了表字段(remark);
 |
| 2024-07-23 15:51:13 | 3.0.3.5 | 刘景锋 | 修复关联索引是全局索引问题 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-08-27 11:09:52 | 3.0.6.1065 | 周兆军 | 所有表ucrt_fund_detail_jour，添加了表字段(position_str);
 |
| 2025-08-18 09:00:35 | 3.0.2.1 | 曾阳璞 | 所有表ucrt_fund_detail_jour，添加了表字段(sett_batch_no);
 |
| 2025-06-03 21:00:00 | 3.0.6.58 | 范文浩 | 物理表ucrt_fund_detail_jour，添加了表字段(remark);
 |
| 2024-07-23 15:51:13 | 3.0.3.5 | 刘景锋 | 修复关联索引是全局索引问题 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

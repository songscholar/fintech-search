# ucrt_compact_jour - 合约流水表

**表对象ID**: 7519
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 104 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_microtime | 否 |  |  |
| 5 | operator_no | 否 |  |  |
| 6 | op_branch_no | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | op_station | 否 |  |  |
| 9 | compact_id | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | stock_type | 否 |  |  |
| 16 | money_type | 否 |  |  |
| 17 | compact_type | 否 |  |  |
| 18 | business_flag | 否 |  |  |
| 19 | occur_balance | 否 |  |  |
| 20 | post_balance | 否 |  |  |
| 21 | occur_amount | 否 |  |  |
| 22 | post_amount | 否 |  |  |
| 23 | occur_fare | 否 |  |  |
| 24 | post_fare | 否 |  |  |
| 25 | occur_interest | 否 |  |  |
| 26 | occur_fine_interest | 否 |  |  |
| 27 | post_interest | 否 |  |  |
| 28 | occur_frozen_interest | 否 |  |  |
| 29 | post_frozen_interest | 否 |  |  |
| 30 | compact_source | 否 |  |  |
| 31 | entrust_no | 否 |  |  |
| 32 | remark | 否 |  |  |
| 33 | cancel_serial_no | 否 |  |  |
| 34 | post_repaycost_balance | 否 |  |  |
| 35 | occur_repaycost_balance | 否 |  |  |
| 36 | prefer_balance | 否 |  |  |
| 37 | trans_pend_fare | 否 |  |  |
| 38 | interest_settle_date | 否 |  |  |
| 39 | branch_no | 否 |  |  |
| 40 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 41 | client_group | 否 | H |  |
| 42 | room_code | 否 | H |  |
| 43 | asset_prop | 否 | H |  |
| 44 | limit_flag | 否 | H |  |
| 45 | risk_level | 否 | H |  |
| 46 | corp_client_group | 否 | H |  |
| 47 | corp_risk_level | 否 | H |  |
| 48 | asset_level | 否 | H |  |
| 49 | client_name | 否 | H |  |
| 50 | stock_name | 否 | H |  |
| 51 | client_prop | 否 | H |  |
| 52 | sub_stock_type | 否 | H |  |
| 53 | init_date | 否 |  |  |
| 54 | serial_no | 否 |  |  |
| 55 | curr_date | 否 |  |  |
| 56 | curr_microtime | 否 |  |  |
| 57 | operator_no | 否 |  |  |
| 58 | op_branch_no | 否 |  |  |
| 59 | op_entrust_way | 否 |  |  |
| 60 | op_station | 否 |  |  |
| 61 | compact_id | 否 |  |  |
| 62 | fund_account | 否 |  |  |
| 63 | client_id | 否 |  |  |
| 64 | stock_account | 否 |  |  |
| 65 | exchange_type | 否 |  |  |
| 66 | stock_code | 否 |  |  |
| 67 | stock_type | 否 |  |  |
| 68 | money_type | 否 |  |  |
| 69 | compact_type | 否 |  |  |
| 70 | business_flag | 否 |  |  |
| 71 | occur_balance | 否 |  |  |
| 72 | post_balance | 否 |  |  |
| 73 | occur_amount | 否 |  |  |
| 74 | post_amount | 否 |  |  |
| 75 | occur_fare | 否 |  |  |
| 76 | post_fare | 否 |  |  |
| 77 | occur_interest | 否 |  |  |
| 78 | occur_fine_interest | 否 |  |  |
| 79 | post_interest | 否 |  |  |
| 80 | occur_frozen_interest | 否 |  |  |
| 81 | post_frozen_interest | 否 |  |  |
| 82 | compact_source | 否 |  |  |
| 83 | entrust_no | 否 |  |  |
| 84 | remark | 否 |  |  |
| 85 | cancel_serial_no | 否 |  |  |
| 86 | post_repaycost_balance | 否 |  |  |
| 87 | occur_repaycost_balance | 否 |  |  |
| 88 | prefer_balance | 否 |  |  |
| 89 | trans_pend_fare | 否 |  |  |
| 90 | interest_settle_date | 否 |  |  |
| 91 | branch_no | 否 |  |  |
| 92 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 93 | client_group | 否 | H |  |
| 94 | room_code | 否 | H |  |
| 95 | asset_prop | 否 | H |  |
| 96 | limit_flag | 否 | H |  |
| 97 | risk_level | 否 | H |  |
| 98 | corp_client_group | 否 | H |  |
| 99 | corp_risk_level | 否 | H |  |
| 100 | asset_level | 否 | H |  |
| 101 | client_name | 否 | H |  |
| 102 | stock_name | 否 | H |  |
| 103 | client_prop | 否 | H |  |
| 104 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_compact_jour_no | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_ucrt_compact_jour_pos | ART | 是 | position_str, position_str |
| uk_rpt_ucrtcompactjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtcompactjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_ucrt_compact_jour_no | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_ucrt_compact_jour_pos | ART | 是 | position_str, position_str |
| uk_rpt_ucrtcompactjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtcompactjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_compact_jour | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_ucrt_compact_jour | fund_account, init_date, serial_no, fund_account, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-25 17:06:16 | 3.0.2.2001 | 沈勋 | 新增idx_ucrt_compact_jour_pos索引 |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2025-04-02 10:15:40 | 3.0.2.2001 | 卢杰 | 物理表ucrt_compact_jour，添加了表字段(interest_settle_date);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-09-25 17:06:16 | 3.0.2.2001 | 沈勋 | 新增idx_ucrt_compact_jour_pos索引 |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2025-04-02 10:15:40 | 3.0.2.2001 | 卢杰 | 物理表ucrt_compact_jour，添加了表字段(interest_settle_date);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

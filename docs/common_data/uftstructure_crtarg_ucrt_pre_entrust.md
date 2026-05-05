# ucrt_pre_entrust - 信用预委托表

**表对象ID**: 7043
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 86 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | op_branch_no | 否 |  |  |
| 4 | operator_no | 否 |  |  |
| 5 | op_station | 否 |  |  |
| 6 | curr_date | 否 |  |  |
| 7 | curr_microtime | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | stock_account | 否 |  |  |
| 10 | client_id | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | compact_type | 否 |  |  |
| 14 | entrust_type | 否 |  |  |
| 15 | entrust_prop | 否 |  |  |
| 16 | entrust_bs | 否 |  |  |
| 17 | entrust_amount | 否 |  |  |
| 18 | entrust_price | 否 |  |  |
| 19 | entrust_balance | 否 |  |  |
| 20 | entrust_no | 否 |  |  |
| 21 | preentrust_status | 否 |  |  |
| 22 | fail_cause | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | date_clear | 否 |  |  |
| 25 | assure_asset | 否 |  |  |
| 26 | total_debit | 否 |  |  |
| 27 | per_assurescale_value | 否 |  |  |
| 28 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 29 | branch_no | 否 | H |  |
| 30 | tohis_date | 否 | H |  |
| 31 | stock_name | 否 | H |  |
| 32 | sub_stock_type | 否 | H |  |
| 33 | stock_type | 否 | H |  |
| 34 | client_group | 否 | H |  |
| 35 | room_code | 否 | H |  |
| 36 | asset_prop | 否 | H |  |
| 37 | limit_flag | 否 | H |  |
| 38 | risk_level | 否 | H |  |
| 39 | corp_client_group | 否 | H |  |
| 40 | corp_risk_level | 否 | H |  |
| 41 | asset_level | 否 | H |  |
| 42 | client_name | 否 | H |  |
| 43 | client_prop | 否 | H |  |
| 44 | init_date | 否 |  |  |
| 45 | serial_no | 否 |  |  |
| 46 | op_branch_no | 否 |  |  |
| 47 | operator_no | 否 |  |  |
| 48 | op_station | 否 |  |  |
| 49 | curr_date | 否 |  |  |
| 50 | curr_microtime | 否 |  |  |
| 51 | fund_account | 否 |  |  |
| 52 | stock_account | 否 |  |  |
| 53 | client_id | 否 |  |  |
| 54 | stock_code | 否 |  |  |
| 55 | exchange_type | 否 |  |  |
| 56 | compact_type | 否 |  |  |
| 57 | entrust_type | 否 |  |  |
| 58 | entrust_prop | 否 |  |  |
| 59 | entrust_bs | 否 |  |  |
| 60 | entrust_amount | 否 |  |  |
| 61 | entrust_price | 否 |  |  |
| 62 | entrust_balance | 否 |  |  |
| 63 | entrust_no | 否 |  |  |
| 64 | preentrust_status | 否 |  |  |
| 65 | fail_cause | 否 |  |  |
| 66 | remark | 否 |  |  |
| 67 | date_clear | 否 |  |  |
| 68 | assure_asset | 否 |  |  |
| 69 | total_debit | 否 |  |  |
| 70 | per_assurescale_value | 否 |  |  |
| 71 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 72 | branch_no | 否 | H |  |
| 73 | tohis_date | 否 | H |  |
| 74 | stock_name | 否 | H |  |
| 75 | sub_stock_type | 否 | H |  |
| 76 | stock_type | 否 | H |  |
| 77 | client_group | 否 | H |  |
| 78 | room_code | 否 | H |  |
| 79 | asset_prop | 否 | H |  |
| 80 | limit_flag | 否 | H |  |
| 81 | risk_level | 否 | H |  |
| 82 | corp_client_group | 否 | H |  |
| 83 | corp_risk_level | 否 | H |  |
| 84 | asset_level | 否 | H |  |
| 85 | client_name | 否 | H |  |
| 86 | client_prop | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdt_pre_entrust | 默认 | 否 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_crdt_pre_entrust | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| uk_rpt_ucrtpreentrust | ART | 是 | tohis_date, branch_no, position_str, tohis_date, branch_no, position_str |
| idx_rpt_ucrtpreentrust_cid | ART | 是 | tohis_date, client_id, fund_account, position_str, tohis_date, client_id, fund_account, position_str |
| idx_crdt_pre_entrust | 默认 | 否 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_crdt_pre_entrust | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| uk_rpt_ucrtpreentrust | ART | 是 | tohis_date, branch_no, position_str, tohis_date, branch_no, position_str |
| idx_rpt_ucrtpreentrust_cid | ART | 是 | tohis_date, client_id, fund_account, position_str, tohis_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdt_pre_entrust | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_crdt_pre_entrust | fund_account, init_date, serial_no, fund_account, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-02-27 17:26:51 | 3.0.6.1075 | 袁文龙 | 当前表ucrt_pre_entrust，修改了索引idx_crdt_pre_entrust,索引字段修改为：(fund_... |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2024-07-29 16:56:20 | 3.0.3.5 | 刘景锋 | 修复关联索引是全局索引问题，修改索引idx_crdt_pre_entrust |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-02-27 17:26:51 | 3.0.6.1075 | 袁文龙 | 当前表ucrt_pre_entrust，修改了索引idx_crdt_pre_entrust,索引字段修改为：(fund_... |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2024-07-29 16:56:20 | 3.0.3.5 | 刘景锋 | 修复关联索引是全局索引问题，修改索引idx_crdt_pre_entrust |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

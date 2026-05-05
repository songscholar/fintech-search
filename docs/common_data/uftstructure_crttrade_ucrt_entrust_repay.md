# ucrt_entrust_repay - 指定偿还表

**表对象ID**: 7543
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | entrust_no | 否 |  |  |
| 6 | compact_id | 否 |  |  |
| 7 | assign_type | 否 |  |  |
| 8 | position_str | 否 |  | curr_date(8)+partition_no(2)+curr_time(6)+branch_no(5)+entru |
| 9 | branch_no | 否 | H |  |
| 10 | client_group | 否 | H |  |
| 11 | room_code | 否 | H |  |
| 12 | limit_flag | 否 | H |  |
| 13 | asset_prop | 否 | H |  |
| 14 | risk_level | 否 | H |  |
| 15 | corp_client_group | 否 | H |  |
| 16 | corp_risk_level | 否 | H |  |
| 17 | asset_level | 否 | H |  |
| 18 | client_name | 否 | H |  |
| 19 | client_prop | 否 | H |  |
| 20 | init_date | 否 |  |  |
| 21 | serial_no | 否 |  |  |
| 22 | client_id | 否 |  |  |
| 23 | fund_account | 否 |  |  |
| 24 | entrust_no | 否 |  |  |
| 25 | compact_id | 否 |  |  |
| 26 | assign_type | 否 |  |  |
| 27 | position_str | 否 |  | curr_date(8)+partition_no(2)+curr_time(6)+branch_no(5)+entru |
| 28 | branch_no | 否 | H |  |
| 29 | client_group | 否 | H |  |
| 30 | room_code | 否 | H |  |
| 31 | limit_flag | 否 | H |  |
| 32 | asset_prop | 否 | H |  |
| 33 | risk_level | 否 | H |  |
| 34 | corp_client_group | 否 | H |  |
| 35 | corp_risk_level | 否 | H |  |
| 36 | asset_level | 否 | H |  |
| 37 | client_name | 否 | H |  |
| 38 | client_prop | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_entrust_repay | ART | 是 | fund_account, entrust_no, init_date, fund_account, entrust_no, init_date |
| idx_ucrt_entrust_repay_compact_id | ART | 是 | fund_account, compact_id, fund_account, compact_id |
| idx_ucrt_entrust_repay_unique | ART | 是 | fund_account, entrust_no, init_date, serial_no, fund_account, entrust_no, init_date, serial_no |
| uk_rpt_ucrtentrustrepay | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtentrustrepay_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_ucrt_entrust_repay | ART | 是 | fund_account, entrust_no, init_date, fund_account, entrust_no, init_date |
| idx_ucrt_entrust_repay_compact_id | ART | 是 | fund_account, compact_id, fund_account, compact_id |
| idx_ucrt_entrust_repay_unique | ART | 是 | fund_account, entrust_no, init_date, serial_no, fund_account, entrust_no, init_date, serial_no |
| uk_rpt_ucrtentrustrepay | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtentrustrepay_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_entrust_repay | fund_account, entrust_no, init_date, serial_no, fund_account, entrust_no, init_date, serial_no |
| idx_ucrt_entrust_repay | fund_account, entrust_no, init_date, serial_no, fund_account, entrust_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 添加了表字段(position_str);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 添加了表字段(position_str);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

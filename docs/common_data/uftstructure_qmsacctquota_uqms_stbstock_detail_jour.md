# uqms_stbstock_detail_jour - 全国股转证券余额信息流水表

**表对象ID**: 1614
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 60 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_microtime | 否 |  |  |
| 4 | serial_no | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | seat_no | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | stock_account | 否 |  |  |
| 10 | stock_property | 否 |  |  |
| 11 | occur_amount | 否 |  |  |
| 12 | post_amount | 否 |  |  |
| 13 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 14 | remark | 否 |  |  |
| 15 | real_action | 否 |  |  |
| 16 | client_id | 否 | H |  |
| 17 | client_name | 否 | H |  |
| 18 | branch_no | 否 | H |  |
| 19 | corp_client_group | 否 | H |  |
| 20 | client_group | 否 | H |  |
| 21 | room_code | 否 | H |  |
| 22 | asset_prop | 否 | H |  |
| 23 | limit_flag | 否 | H |  |
| 24 | client_prop | 否 | H |  |
| 25 | asset_level | 否 | H |  |
| 26 | risk_level | 否 | H |  |
| 27 | corp_risk_level | 否 | H |  |
| 28 | stock_name | 否 | H |  |
| 29 | stock_type | 否 | H |  |
| 30 | sub_stock_type | 否 | H |  |
| 31 | init_date | 否 |  |  |
| 32 | curr_date | 否 |  |  |
| 33 | curr_microtime | 否 |  |  |
| 34 | serial_no | 否 |  |  |
| 35 | fund_account | 否 |  |  |
| 36 | exchange_type | 否 |  |  |
| 37 | seat_no | 否 |  |  |
| 38 | stock_code | 否 |  |  |
| 39 | stock_account | 否 |  |  |
| 40 | stock_property | 否 |  |  |
| 41 | occur_amount | 否 |  |  |
| 42 | post_amount | 否 |  |  |
| 43 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 44 | remark | 否 |  |  |
| 45 | real_action | 否 |  |  |
| 46 | client_id | 否 | H |  |
| 47 | client_name | 否 | H |  |
| 48 | branch_no | 否 | H |  |
| 49 | corp_client_group | 否 | H |  |
| 50 | client_group | 否 | H |  |
| 51 | room_code | 否 | H |  |
| 52 | asset_prop | 否 | H |  |
| 53 | limit_flag | 否 | H |  |
| 54 | client_prop | 否 | H |  |
| 55 | asset_level | 否 | H |  |
| 56 | risk_level | 否 | H |  |
| 57 | corp_risk_level | 否 | H |  |
| 58 | stock_name | 否 | H |  |
| 59 | stock_type | 否 | H |  |
| 60 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stbstockdetailjour_pos | ART | 是 | position_str, position_str |
| idx_stbstockdetailjour_acc | ART | 是 | fund_account, fund_account |
| uk_rpt_uqmsstbstockdetailjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_uqmsstbstockdetailjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_stbstockdetailjour_pos | ART | 是 | position_str, position_str |
| idx_stbstockdetailjour_acc | ART | 是 | fund_account, fund_account |
| uk_rpt_uqmsstbstockdetailjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_uqmsstbstockdetailjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stbstockdetailjour_pos | position_str, position_str |
| idx_stbstockdetailjour_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:44:07 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.8 | 李江霖 | 增加position_str的备注 |
| 2024-09-23 14:36:25 | 3.0.2.7 | 卢杰 | 新增 |
| 2026-03-05 16:44:07 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.8 | 李江霖 | 增加position_str的备注 |
| 2024-09-23 14:36:25 | 3.0.2.7 | 卢杰 | 新增 |

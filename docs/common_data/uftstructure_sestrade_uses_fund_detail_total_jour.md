# uses_fund_detail_total_jour - 证券交易资金详细信息汇总流水表

**表对象ID**: 5992
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 44 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | money_type | 否 |  |  |
| 5 | curr_date | 否 |  |  |
| 6 | curr_time | 否 |  |  |
| 7 | business_frozen_balance | 否 |  |  |
| 8 | business_unfrozen_balance | 否 |  |  |
| 9 | fund_enable_level | 否 |  |  |
| 10 | flow_count | 否 |  |  |
| 11 | net_balance | 否 |  |  |
| 12 | branch_no | 否 | H |  |
| 13 | asset_prop | 否 | H |  |
| 14 | limit_flag | 否 | H |  |
| 15 | risk_level | 否 | H |  |
| 16 | corp_client_group | 否 | H |  |
| 17 | corp_risk_level | 否 | H |  |
| 18 | asset_level | 否 | H |  |
| 19 | client_name | 否 | H |  |
| 20 | client_prop | 否 | H |  |
| 21 | client_group | 否 | H |  |
| 22 | room_code | 否 | H |  |
| 23 | init_date | 否 |  |  |
| 24 | serial_no | 否 |  |  |
| 25 | fund_account | 否 |  |  |
| 26 | money_type | 否 |  |  |
| 27 | curr_date | 否 |  |  |
| 28 | curr_time | 否 |  |  |
| 29 | business_frozen_balance | 否 |  |  |
| 30 | business_unfrozen_balance | 否 |  |  |
| 31 | fund_enable_level | 否 |  |  |
| 32 | flow_count | 否 |  |  |
| 33 | net_balance | 否 |  |  |
| 34 | branch_no | 否 | H |  |
| 35 | asset_prop | 否 | H |  |
| 36 | limit_flag | 否 | H |  |
| 37 | risk_level | 否 | H |  |
| 38 | corp_client_group | 否 | H |  |
| 39 | corp_risk_level | 否 | H |  |
| 40 | asset_level | 否 | H |  |
| 41 | client_name | 否 | H |  |
| 42 | client_prop | 否 | H |  |
| 43 | client_group | 否 | H |  |
| 44 | room_code | 否 | H |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| id_usesfunddetailtotaljour | 默认 | 否 |  |
| id_usesfunddetailtotaljour_acc | 默认 | 否 |  |
| id_usesfunddetailtotaljour | ART | 是 | init_date, serial_no, init_date, serial_no |
| id_usesfunddetailtotaljour_acc | ART | 是 | fund_account, money_type, fund_enable_level, flow_count, fund_account, money_type, fund_enable_level, flow_count |
| id_rpt_usesfunddetailtotaljour | ART | 是 | init_date, serial_no, init_date, serial_no |
| id_rpt_usesfunddetailtotaljour_acc | ART | 是 | init_date, fund_account, init_date, fund_account |
| id_usesfunddetailtotaljour | 默认 | 否 |  |
| id_usesfunddetailtotaljour_acc | 默认 | 否 |  |
| id_usesfunddetailtotaljour | ART | 是 | init_date, serial_no, init_date, serial_no |
| id_usesfunddetailtotaljour_acc | ART | 是 | fund_account, money_type, fund_enable_level, flow_count, fund_account, money_type, fund_enable_level, flow_count |
| id_rpt_usesfunddetailtotaljour | ART | 是 | init_date, serial_no, init_date, serial_no |
| id_rpt_usesfunddetailtotaljour_acc | ART | 是 | init_date, fund_account, init_date, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| id_usesfunddetailtotaljour | init_date, serial_no, init_date, serial_no |
| id_usesfunddetailtotaljour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:55:18 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-29 09:43:05 | 3.0.2.105 | 洪略 | 增加历史表 |
| 2025-12-01 16:46:46 | 3.0.2.104 | taocong45644 | 当前表uses_fund_detail_total_jour，修改了索引id_usesfunddetailtotaljo... |
| 2025-11-07 15:13:19 | V3.0.8.10 | yangxz | 所有表uses_fund_detail_total_jour，添加了表字段(net_balance);
 |
| 2026-03-09 14:55:18 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-29 09:43:05 | 3.0.2.105 | 洪略 | 增加历史表 |
| 2025-12-01 16:46:46 | 3.0.2.104 | taocong45644 | 当前表uses_fund_detail_total_jour，修改了索引id_usesfunddetailtotaljo... |
| 2025-11-07 15:13:19 | V3.0.8.10 | yangxz | 所有表uses_fund_detail_total_jour，添加了表字段(net_balance);
 |

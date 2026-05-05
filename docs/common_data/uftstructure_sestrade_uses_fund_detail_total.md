# uses_fund_detail_total - 证券交易资金详细信息汇总表

**表对象ID**: 5987
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | business_frozen_balance | 否 |  |  |
| 5 | business_unfrozen_balance | 否 |  |  |
| 6 | net_balance | 否 |  | 记录预冻结金额 |
| 7 | fund_enable_level | 否 |  |  |
| 8 | flow_count | 否 |  |  |
| 9 | branch_no | 否 | H |  |
| 10 | asset_prop | 否 | H |  |
| 11 | limit_flag | 否 | H |  |
| 12 | risk_level | 否 | H |  |
| 13 | corp_client_group | 否 | H |  |
| 14 | corp_risk_level | 否 | H |  |
| 15 | asset_level | 否 | H |  |
| 16 | client_name | 否 | H |  |
| 17 | client_prop | 否 | H |  |
| 18 | room_code | 否 | H |  |
| 19 | init_date | 否 |  |  |
| 20 | fund_account | 否 |  |  |
| 21 | money_type | 否 |  |  |
| 22 | business_frozen_balance | 否 |  |  |
| 23 | business_unfrozen_balance | 否 |  |  |
| 24 | net_balance | 否 |  | 记录预冻结金额 |
| 25 | fund_enable_level | 否 |  |  |
| 26 | flow_count | 否 |  |  |
| 27 | branch_no | 否 | H |  |
| 28 | asset_prop | 否 | H |  |
| 29 | limit_flag | 否 | H |  |
| 30 | risk_level | 否 | H |  |
| 31 | corp_client_group | 否 | H |  |
| 32 | corp_risk_level | 否 | H |  |
| 33 | asset_level | 否 | H |  |
| 34 | client_name | 否 | H |  |
| 35 | client_prop | 否 | H |  |
| 36 | room_code | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| id_usesfunddetailtotal | 默认 | 否 |  |
| id_usesfunddetailtotal | ART | 是 | fund_account, money_type, fund_enable_level, init_date, flow_count, fund_account, money_type, fund_enable_level, init_date, flow_count |
| id_rpt_usesfunddetailtotal | ART | 是 | init_date, fund_account, money_type, fund_enable_level, flow_count, init_date, fund_account, money_type, fund_enable_level, flow_count |
| id_usesfunddetailtotal | 默认 | 否 |  |
| id_usesfunddetailtotal | ART | 是 | fund_account, money_type, fund_enable_level, init_date, flow_count, fund_account, money_type, fund_enable_level, init_date, flow_count |
| id_rpt_usesfunddetailtotal | ART | 是 | init_date, fund_account, money_type, fund_enable_level, flow_count, init_date, fund_account, money_type, fund_enable_level, flow_count |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| id_usesfunddetailtotal | fund_account, money_type, fund_enable_level, init_date, flow_count, fund_account, money_type, fund_enable_level, init_date, flow_count |
| id_usesfunddetailtotal | fund_account, money_type, fund_enable_level, init_date, flow_count, fund_account, money_type, fund_enable_level, init_date, flow_count |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:53:48 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-29 09:40:21 | 3.0.2.105 | 洪略 | 增加历史表 |
| 2025-12-01 16:45:46 | 3.0.2.104 | taocong45644 | 当前表uses_fund_detail_total，修改了索引id_usesfunddetailtotal,索引字段修改... |
| 2025-11-07 15:06:39 | V3.0.8.9 |  | 所有表uses_fund_detail_total，添加了表字段(net_balance);
 |
| 2026-03-09 14:53:48 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-29 09:40:21 | 3.0.2.105 | 洪略 | 增加历史表 |
| 2025-12-01 16:45:46 | 3.0.2.104 | taocong45644 | 当前表uses_fund_detail_total，修改了索引id_usesfunddetailtotal,索引字段修改... |
| 2025-11-07 15:06:39 | V3.0.8.9 |  | 所有表uses_fund_detail_total，添加了表字段(net_balance);
 |

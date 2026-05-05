# srp_contract_rate - 股票质押合约利率日期信息表

**表对象ID**: 2603
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | contract_id | 否 |  |  |
| 5 | begin_date | 否 |  |  |
| 6 | end_date | 否 |  |  |
| 7 | expire_year_rate | 否 |  |  |
| 8 | date_clear | 否 |  |  |
| 9 | client_id | 否 | H |  |
| 10 | client_name | 否 | H |  |
| 11 | corp_client_group | 否 | H |  |
| 12 | client_group | 否 | H |  |
| 13 | room_code | 否 | H |  |
| 14 | asset_prop | 否 | H |  |
| 15 | limit_flag | 否 | H |  |
| 16 | client_prop | 否 | H |  |
| 17 | asset_level | 否 | H |  |
| 18 | risk_level | 否 | H |  |
| 19 | corp_risk_level | 否 | H |  |
| 20 | init_date | 否 |  |  |
| 21 | branch_no | 否 |  |  |
| 22 | fund_account | 否 |  |  |
| 23 | contract_id | 否 |  |  |
| 24 | begin_date | 否 |  |  |
| 25 | end_date | 否 |  |  |
| 26 | expire_year_rate | 否 |  |  |
| 27 | date_clear | 否 |  |  |
| 28 | client_id | 否 | H |  |
| 29 | client_name | 否 | H |  |
| 30 | corp_client_group | 否 | H |  |
| 31 | client_group | 否 | H |  |
| 32 | room_code | 否 | H |  |
| 33 | asset_prop | 否 | H |  |
| 34 | limit_flag | 否 | H |  |
| 35 | client_prop | 否 | H |  |
| 36 | asset_level | 否 | H |  |
| 37 | risk_level | 否 | H |  |
| 38 | corp_risk_level | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpcontractrate_id  | 默认 | 否 | contract_id, begin_date, end_date, contract_id, begin_date, end_date |
| idx_srpcontractrate | ART | 是 | contract_id, contract_id |
| idx_srpcontractrate_id | ART | 是 | contract_id, begin_date, end_date, contract_id, begin_date, end_date |
| uk_rpt_srpcontractrate | ART | 是 | init_date, contract_id, init_date, contract_id |
| idx_rpt_srpcontractrate_tolast | ART | 是 | date_clear, date_clear |
| idx_srpcontractrate_id  | 默认 | 否 | contract_id, begin_date, end_date, contract_id, begin_date, end_date |
| idx_srpcontractrate | ART | 是 | contract_id, contract_id |
| idx_srpcontractrate_id | ART | 是 | contract_id, begin_date, end_date, contract_id, begin_date, end_date |
| uk_rpt_srpcontractrate | ART | 是 | init_date, contract_id, init_date, contract_id |
| idx_rpt_srpcontractrate_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpcontractrate_id | contract_id, begin_date, end_date, contract_id, begin_date, end_date |
| idx_srpcontractrate_id | contract_id, begin_date, end_date, contract_id, begin_date, end_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:44:23 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-04-29 09:37:55 | 3.0.2.3 | honglue | idx_srpcontractrate_id多个空格删除空格 |
| 2024-11-29 15:14:53 | 3.0.2.1 | 范文浩 | 物理表srp_contract_rate，增加索引(idx_srpcontractrate_id :[contract_... |
| 2024-10-22 18:02:54 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:44:23 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-04-29 09:37:55 | 3.0.2.3 | honglue | idx_srpcontractrate_id多个空格删除空格 |
| 2024-11-29 15:14:53 | 3.0.2.1 | 范文浩 | 物理表srp_contract_rate，增加索引(idx_srpcontractrate_id :[contract_... |
| 2024-10-22 18:02:54 | 3.0.3.1 | wuxd | 新增 |

# srp_integral_info - 股票质押结息日期信息表

**表对象ID**: 2609
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 50 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | branch_no | 否 |  |  |
| 5 | contract_id | 否 |  |  |
| 6 | funder_no | 否 |  |  |
| 7 | interest_date | 否 |  |  |
| 8 | agreed_interest | 否 |  |  |
| 9 | repaid_interest | 否 |  |  |
| 10 | auto_type | 否 |  |  |
| 11 | date_clear | 否 |  |  |
| 12 | position_str | 否 |  | contract_id(32)+interest_date(10) |
| 13 | payinterest_deal_flag | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | client_name | 否 | H |  |
| 17 | corp_client_group | 否 | H |  |
| 18 | client_group | 否 | H |  |
| 19 | room_code | 否 | H |  |
| 20 | asset_prop | 否 | H |  |
| 21 | limit_flag | 否 | H |  |
| 22 | client_prop | 否 | H |  |
| 23 | asset_level | 否 | H |  |
| 24 | risk_level | 否 | H |  |
| 25 | corp_risk_level | 否 | H |  |
| 26 | init_date | 否 |  |  |
| 27 | fund_account | 否 |  |  |
| 28 | client_id | 否 |  |  |
| 29 | branch_no | 否 |  |  |
| 30 | contract_id | 否 |  |  |
| 31 | funder_no | 否 |  |  |
| 32 | interest_date | 否 |  |  |
| 33 | agreed_interest | 否 |  |  |
| 34 | repaid_interest | 否 |  |  |
| 35 | auto_type | 否 |  |  |
| 36 | date_clear | 否 |  |  |
| 37 | position_str | 否 |  | contract_id(32)+interest_date(10) |
| 38 | payinterest_deal_flag | 否 |  |  |
| 39 | update_date | 否 |  |  |
| 40 | update_time | 否 |  |  |
| 41 | client_name | 否 | H |  |
| 42 | corp_client_group | 否 | H |  |
| 43 | client_group | 否 | H |  |
| 44 | room_code | 否 | H |  |
| 45 | asset_prop | 否 | H |  |
| 46 | limit_flag | 否 | H |  |
| 47 | client_prop | 否 | H |  |
| 48 | asset_level | 否 | H |  |
| 49 | risk_level | 否 | H |  |
| 50 | corp_risk_level | 否 | H |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpintegralinfo | ART | 是 | contract_id, interest_date, contract_id, interest_date |
| idx_srpintegralinfo_pos | ART | 是 | position_str, position_str |
| idx_srpintegralinfo_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_srpintegralinfo | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpintegralinfo_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_srpintegralinfo_tolast | ART | 是 | date_clear, date_clear |
| idx_srpintegralinfo | ART | 是 | contract_id, interest_date, contract_id, interest_date |
| idx_srpintegralinfo_pos | ART | 是 | position_str, position_str |
| idx_srpintegralinfo_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_srpintegralinfo | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpintegralinfo_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_srpintegralinfo_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpintegralinfo | contract_id, interest_date, contract_id, interest_date |
| idx_srpintegralinfo | contract_id, interest_date, contract_id, interest_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:47:23 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-08-26 17:02:17 | 3.0.2.5 | 高志强 | 数据存储介质改为MDB |
| 2025-02-19 17:34:06 | 3.0.3.7 | 李想 | 物理表srp_integral_info，添加了表字段(update_date);
物理表srp_integral_i... |
| 2024-12-05 17:37:34 | 3.0.2.2 | 范文浩 | 物理表srp_integral_info，删除了表字段(transaction_no);
 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:21:49 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:47:23 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-08-26 17:02:17 | 3.0.2.5 | 高志强 | 数据存储介质改为MDB |
| 2025-02-19 17:34:06 | 3.0.3.7 | 李想 | 物理表srp_integral_info，添加了表字段(update_date);
物理表srp_integral_i... |
| 2024-12-05 17:37:34 | 3.0.2.2 | 范文浩 | 物理表srp_integral_info，删除了表字段(transaction_no);
 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:21:49 | 3.0.3.1 | wuxd | 新增 |

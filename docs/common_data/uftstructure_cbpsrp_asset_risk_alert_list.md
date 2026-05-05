# asset_risk_alert_list - 风险客户警戒名单表

**表对象ID**: 2638
**所属模块**: cbpsrp
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 64 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | id_kind | 否 |  |  |
| 2 | id_no | 否 |  |  |
| 3 | seat_no | 否 |  |  |
| 4 | company_name | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | client_id | 否 |  |  |
| 8 | client_name | 否 |  |  |
| 9 | stock_account_sh | 否 |  |  |
| 10 | stock_account_sz | 否 |  |  |
| 11 | crdtsrc_type | 否 |  |  |
| 12 | crdtfine_type | 否 |  |  |
| 13 | remark | 否 |  |  |
| 14 | report_date | 否 |  |  |
| 15 | date_clear | 否 |  |  |
| 16 | init_date | 否 |  |  |
| 17 | position_str | 否 |  | init_date(10)+id_no(40)+id_kind(1)+crdtfine_type(1)+report_d |
| 18 | crdtlist_flag | 否 |  |  |
| 19 | stock_account_stb | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | transaction_no | 否 |  |  |
| 23 | breaker_name | 否 |  |  |
| 24 | client_group | 否 | H |  |
| 25 | room_code | 否 | H |  |
| 26 | asset_prop | 否 | H |  |
| 27 | client_prop | 否 | H |  |
| 28 | limit_flag | 否 | H |  |
| 29 | risk_level | 否 | H |  |
| 30 | corp_client_group | 否 | H |  |
| 31 | corp_risk_level | 否 | H |  |
| 32 | asset_level | 否 | H |  |
| 33 | id_kind | 否 |  |  |
| 34 | id_no | 否 |  |  |
| 35 | seat_no | 否 |  |  |
| 36 | company_name | 否 |  |  |
| 37 | branch_no | 否 |  |  |
| 38 | fund_account | 否 |  |  |
| 39 | client_id | 否 |  |  |
| 40 | client_name | 否 |  |  |
| 41 | stock_account_sh | 否 |  |  |
| 42 | stock_account_sz | 否 |  |  |
| 43 | crdtsrc_type | 否 |  |  |
| 44 | crdtfine_type | 否 |  |  |
| 45 | remark | 否 |  |  |
| 46 | report_date | 否 |  |  |
| 47 | date_clear | 否 |  |  |
| 48 | init_date | 否 |  |  |
| 49 | position_str | 否 |  | init_date(10)+id_no(40)+id_kind(1)+crdtfine_type(1)+report_d |
| 50 | crdtlist_flag | 否 |  |  |
| 51 | stock_account_stb | 否 |  |  |
| 52 | update_date | 否 |  |  |
| 53 | update_time | 否 |  |  |
| 54 | transaction_no | 否 |  |  |
| 55 | breaker_name | 否 |  |  |
| 56 | client_group | 否 | H |  |
| 57 | room_code | 否 | H |  |
| 58 | asset_prop | 否 | H |  |
| 59 | client_prop | 否 | H |  |
| 60 | limit_flag | 否 | H |  |
| 61 | risk_level | 否 | H |  |
| 62 | corp_client_group | 否 | H |  |
| 63 | corp_risk_level | 否 | H |  |
| 64 | asset_level | 否 | H |  |

## 索引（共 18 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_assetriskalertlist | 默认 | 否 | id_no, id_kind, id_no, id_kind |
| idx_assetriskalertlist_fund | 默认 | 否 | fund_account, fund_account |
| idx_assetriskalertlist | ART | 是 | id_no, id_kind, id_no, id_kind |
| idx_assetriskalertlist_fund | ART | 是 | fund_account, fund_account |
| idx_assetriskalertlist_id | ART | 是 | client_id, client_id |
| idx_assetriskalertlist_pos | ART | 是 | position_str, position_str |
| idx_rpt_assetriskalertlist_tolast | ART | 是 | date_clear, date_clear |
| idx_rpt_assetriskalertlist_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| uk_rpt_assetriskalertlist | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_assetriskalertlist | 默认 | 否 | id_no, id_kind, id_no, id_kind |
| idx_assetriskalertlist_fund | 默认 | 否 | fund_account, fund_account |
| idx_assetriskalertlist | ART | 是 | id_no, id_kind, id_no, id_kind |
| idx_assetriskalertlist_fund | ART | 是 | fund_account, fund_account |
| idx_assetriskalertlist_id | ART | 是 | client_id, client_id |
| idx_assetriskalertlist_pos | ART | 是 | position_str, position_str |
| idx_rpt_assetriskalertlist_tolast | ART | 是 | date_clear, date_clear |
| idx_rpt_assetriskalertlist_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| uk_rpt_assetriskalertlist | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |

## 数据库索引（共 6 个）

| 索引名 | 字段 |
|--------|------|
| idx_assetriskalertlist_pos | position_str, position_str |
| idx_assetriskalertlist | id_no, id_kind, id_no, id_kind |
| idx_assetriskalertlist_fund | fund_account, fund_account |
| idx_assetriskalertlist_pos | position_str, position_str |
| idx_assetriskalertlist | id_no, id_kind, id_no, id_kind |
| idx_assetriskalertlist_fund | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-17 14:54:32 | 8.26.2.93 | 袁文龙 | 所有表asset_risk_alert_list，添加了表字段(breaker_name);
 |
| 2026-03-06 16:59:38 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-18 14:02:05 | 3.0.3.17 | 洪略 | 补齐分区 |
| 2025-11-21 19:56:55 | 3.0.3.17 | 周兆军 | 维护历史表 |
| 2025-07-16 18:03:27 | 3.0.3.15 | 常行 | 物理表asset_risk_alert_list，增加索引(idx_assetriskalertlist:[id_no,... |
| 2025-06-23 15:29:00 | 3.0.3.13 | 常行 | 新增表 |
| 2026-03-17 14:54:32 | 8.26.2.93 | 袁文龙 | 所有表asset_risk_alert_list，添加了表字段(breaker_name);
 |
| 2026-03-06 16:59:38 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-18 14:02:05 | 3.0.3.17 | 洪略 | 补齐分区 |
| 2025-11-21 19:56:55 | 3.0.3.17 | 周兆军 | 维护历史表 |
| 2025-07-16 18:03:27 | 3.0.3.15 | 常行 | 物理表asset_risk_alert_list，增加索引(idx_assetriskalertlist:[id_no,... |
| 2025-06-23 15:29:00 | 3.0.3.13 | 常行 | 新增表 |

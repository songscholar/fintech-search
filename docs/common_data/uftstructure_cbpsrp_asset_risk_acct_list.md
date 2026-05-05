# asset_risk_acct_list - 账户风险客户名单表

**表对象ID**: 2616
**所属模块**: cbpsrp
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 52 个）

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
| 11 | riskaccount_type | 否 |  |  |
| 12 | crdtsrc_type | 否 |  |  |
| 13 | create_date | 否 |  |  |
| 14 | crdtfine_type | 否 |  |  |
| 15 | remark | 否 |  |  |
| 16 | report_date | 否 |  |  |
| 17 | date_clear | 否 |  |  |
| 18 | init_date | 否 |  |  |
| 19 | position_str | 否 |  | init_date(10)+id_no(40)+id_kind(1)+crdtfine_type(1)+fund_acc |
| 20 | crdtlist_flag | 否 |  |  |
| 21 | risk_enddate | 否 |  |  |
| 22 | stock_account_stb | 否 |  |  |
| 23 | update_date | 否 |  |  |
| 24 | update_time | 否 |  |  |
| 25 | transaction_no | 否 |  |  |
| 26 | breaker_name | 否 |  |  |
| 27 | id_kind | 否 |  |  |
| 28 | id_no | 否 |  |  |
| 29 | seat_no | 否 |  |  |
| 30 | company_name | 否 |  |  |
| 31 | branch_no | 否 |  |  |
| 32 | fund_account | 否 |  |  |
| 33 | client_id | 否 |  |  |
| 34 | client_name | 否 |  |  |
| 35 | stock_account_sh | 否 |  |  |
| 36 | stock_account_sz | 否 |  |  |
| 37 | riskaccount_type | 否 |  |  |
| 38 | crdtsrc_type | 否 |  |  |
| 39 | create_date | 否 |  |  |
| 40 | crdtfine_type | 否 |  |  |
| 41 | remark | 否 |  |  |
| 42 | report_date | 否 |  |  |
| 43 | date_clear | 否 |  |  |
| 44 | init_date | 否 |  |  |
| 45 | position_str | 否 |  | init_date(10)+id_no(40)+id_kind(1)+crdtfine_type(1)+fund_acc |
| 46 | crdtlist_flag | 否 |  |  |
| 47 | risk_enddate | 否 |  |  |
| 48 | stock_account_stb | 否 |  |  |
| 49 | update_date | 否 |  |  |
| 50 | update_time | 否 |  |  |
| 51 | transaction_no | 否 |  |  |
| 52 | breaker_name | 否 |  |  |

## 索引（共 16 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_assetriskacctlist | 默认 | 否 | id_no, id_kind, id_no, id_kind |
| idx_assetriskacctlist_fund | 默认 | 否 | fund_account, fund_account |
| idx_assetriskacctlist | ART | 是 | id_no, id_kind, id_no, id_kind |
| idx_assetriskacctlist_fund | ART | 是 | fund_account, fund_account |
| idx_assetriskacctlist_id | ART | 是 | client_id, client_id |
| idx_assetriskacctlist_pos | ART | 是 | position_str, position_str |
| idx_rpt_assetriskacctlist | ART | 是 | init_date, id_kind, id_no, init_date, id_kind, id_no |
| idx_rpt_assetriskacctlist_pos | ART | 是 | init_date, position_str, init_date, position_str |
| idx_assetriskacctlist | 默认 | 否 | id_no, id_kind, id_no, id_kind |
| idx_assetriskacctlist_fund | 默认 | 否 | fund_account, fund_account |
| idx_assetriskacctlist | ART | 是 | id_no, id_kind, id_no, id_kind |
| idx_assetriskacctlist_fund | ART | 是 | fund_account, fund_account |
| idx_assetriskacctlist_id | ART | 是 | client_id, client_id |
| idx_assetriskacctlist_pos | ART | 是 | position_str, position_str |
| idx_rpt_assetriskacctlist | ART | 是 | init_date, id_kind, id_no, init_date, id_kind, id_no |
| idx_rpt_assetriskacctlist_pos | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 6 个）

| 索引名 | 字段 |
|--------|------|
| idx_assetriskacctlist_pos | position_str, position_str |
| idx_assetriskacctlist | id_no, id_kind, id_no, id_kind |
| idx_assetriskacctlist_fund | fund_account, fund_account |
| idx_assetriskacctlist_pos | position_str, position_str |
| idx_assetriskacctlist | id_no, id_kind, id_no, id_kind |
| idx_assetriskacctlist_fund | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-17 14:55:00 | 8.26.2.93 | 袁文龙 | 所有表asset_risk_acct_list，添加了表字段(breaker_name);
 |
| 2026-03-06 16:50:37 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-11-06 13:38:21 | 3.0.3.17 | 洪略 | 补充历史表 |
| 2025-07-16 18:07:41 | 3.0.3.16 | 常行 | 物理表asset_risk_acct_list，增加索引(idx_assetriskacctlist:[id_no,id... |
| 2025-06-23 15:31:06 | 3.0.3.14 | 常行 | 物理表asset_risk_acct_list，添加了表字段(update_date);
物理表asset_risk_... |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:26:12 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-17 14:55:00 | 8.26.2.93 | 袁文龙 | 所有表asset_risk_acct_list，添加了表字段(breaker_name);
 |
| 2026-03-06 16:50:37 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-11-06 13:38:21 | 3.0.3.17 | 洪略 | 补充历史表 |
| 2025-07-16 18:07:41 | 3.0.3.16 | 常行 | 物理表asset_risk_acct_list，增加索引(idx_assetriskacctlist:[id_no,id... |
| 2025-06-23 15:31:06 | 3.0.3.14 | 常行 | 物理表asset_risk_acct_list，添加了表字段(update_date);
物理表asset_risk_... |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |

> 共 16 条修改记录，仅显示最近15条

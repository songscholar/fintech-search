# usms_asset_risk_acct_list - 账户风险客户名单表(交易管理)(作废)

**表对象ID**: 2813
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB

## 字段列表（共 44 个）

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
| 19 | position_str | 否 |  |  |
| 20 | crdtlist_flag | 否 |  |  |
| 21 | risk_enddate | 否 |  |  |
| 22 | stock_account_stb | 否 |  |  |
| 23 | id_kind | 否 |  |  |
| 24 | id_no | 否 |  |  |
| 25 | seat_no | 否 |  |  |
| 26 | company_name | 否 |  |  |
| 27 | branch_no | 否 |  |  |
| 28 | fund_account | 否 |  |  |
| 29 | client_id | 否 |  |  |
| 30 | client_name | 否 |  |  |
| 31 | stock_account_sh | 否 |  |  |
| 32 | stock_account_sz | 否 |  |  |
| 33 | riskaccount_type | 否 |  |  |
| 34 | crdtsrc_type | 否 |  |  |
| 35 | create_date | 否 |  |  |
| 36 | crdtfine_type | 否 |  |  |
| 37 | remark | 否 |  |  |
| 38 | report_date | 否 |  |  |
| 39 | date_clear | 否 |  |  |
| 40 | init_date | 否 |  |  |
| 41 | position_str | 否 |  |  |
| 42 | crdtlist_flag | 否 |  |  |
| 43 | risk_enddate | 否 |  |  |
| 44 | stock_account_stb | 否 |  |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usms_assetriskacctlist | 默认 | 是 | id_no, id_kind, id_no, id_kind |
| idx_usms_assetriskacctlist_fund | 默认 | 是 | fund_account, fund_account |
| idx_usms_assetriskacctlist_id | 默认 | 是 | client_id, client_id |
| idx_usms_assetriskacctlist_pos | 默认 | 是 | position_str, position_str |
| idx_rpt_usms_assetriskacctlist | ART | 是 | id_no, id_kind, position_str, id_no, id_kind, position_str |
| idx_rpt_usms_assetriskacctlist_pos | ART | 是 | init_date, position_str, init_date, position_str |
| idx_usms_assetriskacctlist | 默认 | 是 | id_no, id_kind, id_no, id_kind |
| idx_usms_assetriskacctlist_fund | 默认 | 是 | fund_account, fund_account |
| idx_usms_assetriskacctlist_id | 默认 | 是 | client_id, client_id |
| idx_usms_assetriskacctlist_pos | 默认 | 是 | position_str, position_str |
| idx_rpt_usms_assetriskacctlist | ART | 是 | id_no, id_kind, position_str, id_no, id_kind, position_str |
| idx_rpt_usms_assetriskacctlist_pos | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usms_assetriskacctlist_pos | position_str, position_str |
| idx_usms_assetriskacctlist_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-08 12:20:08 | 3.0.2.4 | 洪略 | 历史表索引增加rtp前缀 |
| 2025-11-07 15:42:26 | 3.0.2.4 | 洪略 | 新增历史表 |
| 2025-12-08 12:20:08 | 3.0.2.4 | 洪略 | 历史表索引增加rtp前缀 |
| 2025-11-07 15:42:26 | 3.0.2.4 | 洪略 | 新增历史表 |

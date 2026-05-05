# settredo_uarg_risk_list - 清算重做客户信用记录表

**表对象ID**: 7595
**所属模块**: crttrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 52 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | seat_no | 否 |  |  |
| 6 | stock_account_sh | 否 |  |  |
| 7 | stock_account_sz | 否 |  |  |
| 8 | fine_balance | 否 |  |  |
| 9 | crdtfine_type | 否 |  |  |
| 10 | crdtfine_src_type | 否 |  |  |
| 11 | crdtfine_rpt_type | 否 |  |  |
| 12 | crdtfine_no | 否 |  |  |
| 13 | create_date | 否 |  |  |
| 14 | stock_account_stb | 否 |  |  |
| 15 | compact_id_str | 否 |  |  |
| 16 | id_kind | 否 |  |  |
| 17 | id_no | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | risk_begindate | 否 |  |  |
| 20 | transaction_no | 否 |  |  |
| 21 | update_date | 否 |  |  |
| 22 | update_time | 否 |  |  |
| 23 | position_str | 否 |  | create_date(10)+id_no(40)+id_kind(1)+crdtfine_type(1)+crdtfi |
| 24 | init_date | 否 |  |  |
| 25 | sett_dml_type | 否 |  |  |
| 26 | sett_batch_no | 否 |  |  |
| 27 | company_no | 否 |  |  |
| 28 | branch_no | 否 |  |  |
| 29 | client_id | 否 |  |  |
| 30 | fund_account | 否 |  |  |
| 31 | seat_no | 否 |  |  |
| 32 | stock_account_sh | 否 |  |  |
| 33 | stock_account_sz | 否 |  |  |
| 34 | fine_balance | 否 |  |  |
| 35 | crdtfine_type | 否 |  |  |
| 36 | crdtfine_src_type | 否 |  |  |
| 37 | crdtfine_rpt_type | 否 |  |  |
| 38 | crdtfine_no | 否 |  |  |
| 39 | create_date | 否 |  |  |
| 40 | stock_account_stb | 否 |  |  |
| 41 | compact_id_str | 否 |  |  |
| 42 | id_kind | 否 |  |  |
| 43 | id_no | 否 |  |  |
| 44 | remark | 否 |  |  |
| 45 | risk_begindate | 否 |  |  |
| 46 | transaction_no | 否 |  |  |
| 47 | update_date | 否 |  |  |
| 48 | update_time | 否 |  |  |
| 49 | position_str | 否 |  | create_date(10)+id_no(40)+id_kind(1)+crdtfine_type(1)+crdtfi |
| 50 | init_date | 否 |  |  |
| 51 | sett_dml_type | 否 |  |  |
| 52 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_uarg_risk_list | ART | 是 | sett_batch_no, init_date, position_str, sett_batch_no, init_date, position_str |
| idx_settredo_uarg_risk_list | ART | 是 | sett_batch_no, init_date, position_str, sett_batch_no, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_uarg_risk_list | sett_batch_no, init_date, position_str, sett_batch_no, init_date, position_str |
| idx_settredo_uarg_risk_list | sett_batch_no, init_date, position_str, sett_batch_no, init_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-18 16:57:47 | 3.0.2.22 | 常行 | 修改定位串拼法 |
| 2025-08-20 13:50:49 | 3.0.2.1 | 曾阳璞 | 新增表 |
| 2025-11-18 16:57:47 | 3.0.2.22 | 常行 | 修改定位串拼法 |
| 2025-08-20 13:50:49 | 3.0.2.1 | 曾阳璞 | 新增表 |

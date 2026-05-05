# uarg_riskacct_list - 风险客户名单表2

**表对象ID**: 7567
**所属模块**: crttrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 46 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | id_kind | 否 |  |  |
| 2 | id_no | 否 |  |  |
| 3 | seat_no | 否 |  |  |
| 4 | branch_no | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | stock_account_sh | 否 |  |  |
| 8 | stock_account_sz | 否 |  |  |
| 9 | riskaccount_type | 否 |  |  |
| 10 | crdtsrc_type | 否 |  |  |
| 11 | create_date | 否 |  |  |
| 12 | crdtfine_type | 否 |  |  |
| 13 | remark | 否 |  |  |
| 14 | date_clear | 否 |  |  |
| 15 | risk_enddate | 否 |  |  |
| 16 | stock_account_stb | 否 |  |  |
| 17 | update_date | 否 |  |  |
| 18 | update_time | 否 |  |  |
| 19 | position_str | 否 |  | fund_account(18)+crdtfine_type(1)+create_date(10)+id_kind(1) |
| 20 | transaction_no | 否 |  |  |
| 21 | client_name | 是 |  |  |
| 22 | company_name | 是 |  |  |
| 23 | breaker_name | 否 |  |  |
| 24 | id_kind | 否 |  |  |
| 25 | id_no | 否 |  |  |
| 26 | seat_no | 否 |  |  |
| 27 | branch_no | 否 |  |  |
| 28 | fund_account | 否 |  |  |
| 29 | client_id | 否 |  |  |
| 30 | stock_account_sh | 否 |  |  |
| 31 | stock_account_sz | 否 |  |  |
| 32 | riskaccount_type | 否 |  |  |
| 33 | crdtsrc_type | 否 |  |  |
| 34 | create_date | 否 |  |  |
| 35 | crdtfine_type | 否 |  |  |
| 36 | remark | 否 |  |  |
| 37 | date_clear | 否 |  |  |
| 38 | risk_enddate | 否 |  |  |
| 39 | stock_account_stb | 否 |  |  |
| 40 | update_date | 否 |  |  |
| 41 | update_time | 否 |  |  |
| 42 | position_str | 否 |  | fund_account(18)+crdtfine_type(1)+create_date(10)+id_kind(1) |
| 43 | transaction_no | 否 |  |  |
| 44 | client_name | 是 |  |  |
| 45 | company_name | 是 |  |  |
| 46 | breaker_name | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_riskacct_list | 默认 | 否 | fund_account, crdtfine_type, create_date, id_kind, id_no, fund_account, crdtfine_type, create_date, id_kind, id_no |
| idx_uarg_riskacct_list_type | ART | 是 | fund_account, riskaccount_type, fund_account, riskaccount_type |
| idx_uarg_riskacct_list | ART | 是 | fund_account, crdtfine_type, create_date, id_kind, id_no, fund_account, crdtfine_type, create_date, id_kind, id_no |
| idx_uarg_riskacct_list | 默认 | 否 | fund_account, crdtfine_type, create_date, id_kind, id_no, fund_account, crdtfine_type, create_date, id_kind, id_no |
| idx_uarg_riskacct_list_type | ART | 是 | fund_account, riskaccount_type, fund_account, riskaccount_type |
| idx_uarg_riskacct_list | ART | 是 | fund_account, crdtfine_type, create_date, id_kind, id_no, fund_account, crdtfine_type, create_date, id_kind, id_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_riskacct_list | fund_account, crdtfine_type, create_date, id_kind, id_no, fund_account, crdtfine_type, create_date, id_kind, id_no |
| idx_uarg_riskacct_list | fund_account, crdtfine_type, create_date, id_kind, id_no, fund_account, crdtfine_type, create_date, id_kind, id_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-17 14:53:40 | 3.0.8.20 | 袁文龙 | 所有表uarg_riskacct_list，添加了表字段(breaker_name);
 |
| 2025-10-27 13:56:03 | 3.0.8.10 | 沈勋 | 当前表uarg_riskacct_list，修改了索引idx_uarg_riskacct_list,索引字段修改为：(f... |
| 2025-10-27 13:55:35 | 3.0.8.10 | 沈勋 | 所有表uarg_riskacct_list，添加了表字段(client_name);
所有表uarg_riskacct... |
| 2025-06-23 15:56:16 | 3.0.6.52 | 常行 | 新增表 |
| 2026-03-17 14:53:40 | 3.0.8.20 | 袁文龙 | 所有表uarg_riskacct_list，添加了表字段(breaker_name);
 |
| 2025-10-27 13:56:03 | 3.0.8.10 | 沈勋 | 当前表uarg_riskacct_list，修改了索引idx_uarg_riskacct_list,索引字段修改为：(f... |
| 2025-10-27 13:55:35 | 3.0.8.10 | 沈勋 | 所有表uarg_riskacct_list，添加了表字段(client_name);
所有表uarg_riskacct... |
| 2025-06-23 15:56:16 | 3.0.6.52 | 常行 | 新增表 |

# uarg_risk_list - 客户信用记录表2

**表对象ID**: 7565
**所属模块**: crttrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 46 个）

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
| 24 | company_no | 否 |  |  |
| 25 | branch_no | 否 |  |  |
| 26 | client_id | 否 |  |  |
| 27 | fund_account | 否 |  |  |
| 28 | seat_no | 否 |  |  |
| 29 | stock_account_sh | 否 |  |  |
| 30 | stock_account_sz | 否 |  |  |
| 31 | fine_balance | 否 |  |  |
| 32 | crdtfine_type | 否 |  |  |
| 33 | crdtfine_src_type | 否 |  |  |
| 34 | crdtfine_rpt_type | 否 |  |  |
| 35 | crdtfine_no | 否 |  |  |
| 36 | create_date | 否 |  |  |
| 37 | stock_account_stb | 否 |  |  |
| 38 | compact_id_str | 否 |  |  |
| 39 | id_kind | 否 |  |  |
| 40 | id_no | 否 |  |  |
| 41 | remark | 否 |  |  |
| 42 | risk_begindate | 否 |  |  |
| 43 | transaction_no | 否 |  |  |
| 44 | update_date | 否 |  |  |
| 45 | update_time | 否 |  |  |
| 46 | position_str | 否 |  | create_date(10)+id_no(40)+id_kind(1)+crdtfine_type(1)+crdtfi |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_risk_list | 默认 | 否 |  |
| idx_uarg_risk_list | ART | 是 | create_date, id_no, id_kind, crdtfine_type, crdtfine_no, risk_begindate, crdtfine_rpt_type, fund_account, create_date, id_no, id_kind, crdtfine_type, crdtfine_no, risk_begindate, crdtfine_rpt_type, fund_account |
| idx_uarg_risk_list | 默认 | 否 |  |
| idx_uarg_risk_list | ART | 是 | create_date, id_no, id_kind, crdtfine_type, crdtfine_no, risk_begindate, crdtfine_rpt_type, fund_account, create_date, id_no, id_kind, crdtfine_type, crdtfine_no, risk_begindate, crdtfine_rpt_type, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_risk_list | fund_account, create_date, crdtfine_type, crdtfine_no, crdtfine_rpt_type, fund_account, create_date, crdtfine_type, crdtfine_no, crdtfine_rpt_type |
| idx_uarg_risk_list | fund_account, create_date, crdtfine_type, crdtfine_no, crdtfine_rpt_type, fund_account, create_date, crdtfine_type, crdtfine_no, crdtfine_rpt_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-18 09:27:20 | 3.0.2.22 | 常行 | 当前表uarg_risk_list，修改了索引idx_uarg_risk_list,索引字段修改为：(create_da... |
| 2025-06-19 15:18:21 | 3.0.6.51 | 常行 | 新增表 |
| 2025-11-18 09:27:20 | 3.0.2.22 | 常行 | 当前表uarg_risk_list，修改了索引idx_uarg_risk_list,索引字段修改为：(create_da... |
| 2025-06-19 15:18:21 | 3.0.6.51 | 常行 | 新增表 |

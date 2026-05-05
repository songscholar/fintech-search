# ucrt_surplus_stock - 余券信息表

**表对象ID**: 7541
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 52 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | stock_type | 否 |  |  |
| 7 | begin_amount | 否 |  |  |
| 8 | current_amount | 否 |  |  |
| 9 | surplus_amount | 否 |  |  |
| 10 | correct_amount | 否 |  |  |
| 11 | cashgroup_no | 否 |  |  |
| 12 | branch_no | 否 |  |  |
| 13 | position_str_long | 否 |  | branch_no(5)+exchange_type(4)+stock_account(10)+stock_code(6 |
| 14 | tohis_date | 否 | H |  |
| 15 | stock_name | 否 | H |  |
| 16 | sub_stock_type | 否 | H |  |
| 17 | client_group | 否 | H |  |
| 18 | room_code | 否 | H |  |
| 19 | asset_prop | 否 | H |  |
| 20 | limit_flag | 否 | H |  |
| 21 | risk_level | 否 | H |  |
| 22 | corp_client_group | 否 | H |  |
| 23 | corp_risk_level | 否 | H |  |
| 24 | asset_level | 否 | H |  |
| 25 | client_name | 否 | H |  |
| 26 | client_prop | 否 | H |  |
| 27 | client_id | 否 |  |  |
| 28 | fund_account | 否 |  |  |
| 29 | exchange_type | 否 |  |  |
| 30 | stock_account | 否 |  |  |
| 31 | stock_code | 否 |  |  |
| 32 | stock_type | 否 |  |  |
| 33 | begin_amount | 否 |  |  |
| 34 | current_amount | 否 |  |  |
| 35 | surplus_amount | 否 |  |  |
| 36 | correct_amount | 否 |  |  |
| 37 | cashgroup_no | 否 |  |  |
| 38 | branch_no | 否 |  |  |
| 39 | position_str_long | 否 |  | branch_no(5)+exchange_type(4)+stock_account(10)+stock_code(6 |
| 40 | tohis_date | 否 | H |  |
| 41 | stock_name | 否 | H |  |
| 42 | sub_stock_type | 否 | H |  |
| 43 | client_group | 否 | H |  |
| 44 | room_code | 否 | H |  |
| 45 | asset_prop | 否 | H |  |
| 46 | limit_flag | 否 | H |  |
| 47 | risk_level | 否 | H |  |
| 48 | corp_client_group | 否 | H |  |
| 49 | corp_risk_level | 否 | H |  |
| 50 | asset_level | 否 | H |  |
| 51 | client_name | 否 | H |  |
| 52 | client_prop | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_surplus_stock_code | ART | 是 | fund_account, stock_code, exchange_type, cashgroup_no, fund_account, stock_code, exchange_type, cashgroup_no |
| uk_rpt_ucrtsurplusstock | ART | 是 | tohis_date, branch_no, position_str_long, tohis_date, branch_no, position_str_long |
| idx_rpt_ucrtsurplusstock_cid | ART | 是 | tohis_date, client_id, fund_account, position_str_long, tohis_date, client_id, fund_account, position_str_long |
| idx_ucrt_surplus_stock_code | ART | 是 | fund_account, stock_code, exchange_type, cashgroup_no, fund_account, stock_code, exchange_type, cashgroup_no |
| uk_rpt_ucrtsurplusstock | ART | 是 | tohis_date, branch_no, position_str_long, tohis_date, branch_no, position_str_long |
| idx_rpt_ucrtsurplusstock_cid | ART | 是 | tohis_date, client_id, fund_account, position_str_long, tohis_date, client_id, fund_account, position_str_long |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_surplus_stock | fund_account, stock_code, exchange_type, cashgroup_no, fund_account, stock_code, exchange_type, cashgroup_no |
| idx_ucrt_surplus_stock | fund_account, stock_code, exchange_type, cashgroup_no, fund_account, stock_code, exchange_type, cashgroup_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-21 14:38:46 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_surplus_stock，添加了表字段(branch_no);
物理表ucrt_surplus_st... |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-08-21 14:38:46 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_surplus_stock，添加了表字段(branch_no);
物理表ucrt_surplus_st... |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

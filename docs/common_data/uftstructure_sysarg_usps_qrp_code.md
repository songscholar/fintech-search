# usps_qrp_code - 报价回购代码表

**表对象ID**: 2322
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 58 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | expire_year_rate | 否 |  |  |
| 5 | preterm_year_rate | 否 |  |  |
| 6 | postpone_flag | 否 |  |  |
| 7 | en_branch_no | 否 |  |  |
| 8 | appterm_day | 否 |  |  |
| 9 | company_no | 否 |  |  |
| 10 | postpone_num | 否 |  |  |
| 11 | modify_date | 否 |  |  |
| 12 | qrpissue_mode | 否 |  |  |
| 13 | end_date | 否 |  |  |
| 14 | issue_date | 否 |  |  |
| 15 | pre_back_flag | 否 |  |  |
| 16 | en_qrpagent_num | 否 |  |  |
| 17 | scavenging_balance_limit | 否 |  |  |
| 18 | qrpcode_status | 否 |  |  |
| 19 | en_entrust_way | 否 |  |  |
| 20 | en_organ_flag | 否 |  |  |
| 21 | settle_start_date | 否 |  |  |
| 22 | settle_due_date | 否 |  |  |
| 23 | en_qrp_code | 否 |  |  |
| 24 | code_scavenging_ratio | 否 |  |  |
| 25 | transaction_no | 否 |  |  |
| 26 | update_date | 否 |  |  |
| 27 | update_time | 否 |  |  |
| 28 | position_str | 否 |  | stock_code(8)+exchange_type(4)+company_no(4) |
| 29 | stock_name | 否 | H |  |
| 30 | init_date | 否 |  |  |
| 31 | exchange_type | 否 |  |  |
| 32 | stock_code | 否 |  |  |
| 33 | expire_year_rate | 否 |  |  |
| 34 | preterm_year_rate | 否 |  |  |
| 35 | postpone_flag | 否 |  |  |
| 36 | en_branch_no | 否 |  |  |
| 37 | appterm_day | 否 |  |  |
| 38 | company_no | 否 |  |  |
| 39 | postpone_num | 否 |  |  |
| 40 | modify_date | 否 |  |  |
| 41 | qrpissue_mode | 否 |  |  |
| 42 | end_date | 否 |  |  |
| 43 | issue_date | 否 |  |  |
| 44 | pre_back_flag | 否 |  |  |
| 45 | en_qrpagent_num | 否 |  |  |
| 46 | scavenging_balance_limit | 否 |  |  |
| 47 | qrpcode_status | 否 |  |  |
| 48 | en_entrust_way | 否 |  |  |
| 49 | en_organ_flag | 否 |  |  |
| 50 | settle_start_date | 否 |  |  |
| 51 | settle_due_date | 否 |  |  |
| 52 | en_qrp_code | 否 |  |  |
| 53 | code_scavenging_ratio | 否 |  |  |
| 54 | transaction_no | 否 |  |  |
| 55 | update_date | 否 |  |  |
| 56 | update_time | 否 |  |  |
| 57 | position_str | 否 |  | stock_code(8)+exchange_type(4)+company_no(4) |
| 58 | stock_name | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_qrpcode | ART | 是 | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |
| uk_rpt_uspsqrpcode | ART | 是 | init_date, position_str, init_date, position_str |
| idx_qrpcode | ART | 是 | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |
| uk_rpt_uspsqrpcode | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_qrpcode | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |
| idx_qrpcode | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-05-01 10:32:29 | 3.0.2.2005 | 高志强 | 表结构移动到pbs |
| 2025-02-19 22:09:20 | V3.0.5.1019 | 李想 | 物理表usps_qrp_code，添加了表字段(update_date);
物理表usps_qrp_code，添加了表... |
| 2024-08-06 10:25:47 | V3.0.2.1003 | 骆鹏程 | 新增 |
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-05-01 10:32:29 | 3.0.2.2005 | 高志强 | 表结构移动到pbs |
| 2025-02-19 22:09:20 | V3.0.5.1019 | 李想 | 物理表usps_qrp_code，添加了表字段(update_date);
物理表usps_qrp_code，添加了表... |
| 2024-08-06 10:25:47 | V3.0.2.1003 | 骆鹏程 | 新增 |

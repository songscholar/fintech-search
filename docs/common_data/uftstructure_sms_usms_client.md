# usms_client - 客户信息

**表对象ID**: 2804
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 92 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | client_status | 否 |  |  |
| 3 | transaction_no | 否 |  |  |
| 4 | id_kind | 否 |  |  |
| 5 | id_no | 否 |  |  |
| 6 | id_begindate | 否 |  |  |
| 7 | id_enddate | 否 |  |  |
| 8 | branch_no | 否 |  |  |
| 9 | full_name | 否 |  |  |
| 10 | corp_client_group | 否 |  |  |
| 11 | corp_risk_level | 否 |  |  |
| 12 | organ_flag | 否 |  |  |
| 13 | open_date | 否 |  |  |
| 14 | cust_id | 否 |  |  |
| 15 | prodasset_flag | 否 |  |  |
| 16 | account_data | 否 |  |  |
| 17 | risk_info | 否 |  |  |
| 18 | statement_flag | 否 |  |  |
| 19 | receive_name | 否 |  |  |
| 20 | bill_template_type | 否 |  |  |
| 21 | en_contact_type | 否 |  |  |
| 22 | developer | 否 |  |  |
| 23 | cost_place | 否 |  |  |
| 24 | open_type | 否 |  |  |
| 25 | develop_source | 否 |  |  |
| 26 | contact_freq | 否 |  |  |
| 27 | confirm_date | 否 |  |  |
| 28 | cancel_date | 否 |  |  |
| 29 | trade_password | 否 |  |  |
| 30 | sign_flag | 否 |  |  |
| 31 | sign_date | 否 |  |  |
| 32 | open_business | 否 |  |  |
| 33 | contact_name | 否 |  |  |
| 34 | contact_id_kind | 否 |  |  |
| 35 | contact_id_no | 否 |  |  |
| 36 | contact_id_begindate | 否 |  |  |
| 37 | contact_id_enddate | 否 |  |  |
| 38 | contact_tel | 否 |  |  |
| 39 | contact_mobile | 否 |  |  |
| 40 | cardread_flag | 否 |  |  |
| 41 | mail_way | 否 |  |  |
| 42 | develop_net | 否 |  |  |
| 43 | crdtval_kind | 否 |  |  |
| 44 | remark | 否 |  |  |
| 45 | aml_risk_level | 是 |  |  |
| 46 | client_name | 否 |  |  |
| 47 | client_id | 否 |  |  |
| 48 | client_status | 否 |  |  |
| 49 | transaction_no | 否 |  |  |
| 50 | id_kind | 否 |  |  |
| 51 | id_no | 否 |  |  |
| 52 | id_begindate | 否 |  |  |
| 53 | id_enddate | 否 |  |  |
| 54 | branch_no | 否 |  |  |
| 55 | full_name | 否 |  |  |
| 56 | corp_client_group | 否 |  |  |
| 57 | corp_risk_level | 否 |  |  |
| 58 | organ_flag | 否 |  |  |
| 59 | open_date | 否 |  |  |
| 60 | cust_id | 否 |  |  |
| 61 | prodasset_flag | 否 |  |  |
| 62 | account_data | 否 |  |  |
| 63 | risk_info | 否 |  |  |
| 64 | statement_flag | 否 |  |  |
| 65 | receive_name | 否 |  |  |
| 66 | bill_template_type | 否 |  |  |
| 67 | en_contact_type | 否 |  |  |
| 68 | developer | 否 |  |  |
| 69 | cost_place | 否 |  |  |
| 70 | open_type | 否 |  |  |
| 71 | develop_source | 否 |  |  |
| 72 | contact_freq | 否 |  |  |
| 73 | confirm_date | 否 |  |  |
| 74 | cancel_date | 否 |  |  |
| 75 | trade_password | 否 |  |  |
| 76 | sign_flag | 否 |  |  |
| 77 | sign_date | 否 |  |  |
| 78 | open_business | 否 |  |  |
| 79 | contact_name | 否 |  |  |
| 80 | contact_id_kind | 否 |  |  |
| 81 | contact_id_no | 否 |  |  |
| 82 | contact_id_begindate | 否 |  |  |
| 83 | contact_id_enddate | 否 |  |  |
| 84 | contact_tel | 否 |  |  |
| 85 | contact_mobile | 否 |  |  |
| 86 | cardread_flag | 否 |  |  |
| 87 | mail_way | 否 |  |  |
| 88 | develop_net | 否 |  |  |
| 89 | crdtval_kind | 否 |  |  |
| 90 | remark | 否 |  |  |
| 91 | aml_risk_level | 是 |  |  |
| 92 | client_name | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usms_client | 默认 | 是 | client_id, client_id |
| idx_usms_client_idno | 默认 | 是 | id_no, full_name, id_kind, id_no, full_name, id_kind |
| idx_usms_client | 默认 | 是 | client_id, client_id |
| idx_usms_client_idno | 默认 | 是 | id_no, full_name, id_kind, id_no, full_name, id_kind |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_usms_client | client_id, client_id |
| idx_usms_client_idno | id_no, full_name, id_kind, id_no, full_name, id_kind |
| idx_usms_client | client_id, client_id |
| idx_usms_client_idno | id_no, full_name, id_kind, id_no, full_name, id_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-18 13:53:09 | 8.26.2.95 | huangzh | 所有表usms_client，添加了表字段(aml_risk_level);
 |
| 2025-11-25 11:04:14 | 8.26.2.94 | 刘大为 | 所有表usms_client，添加了表字段(cust_id);
所有表usms_client，添加了表字段(proda... |
| 2025-12-18 13:53:09 | 8.26.2.95 | huangzh | 所有表usms_client，添加了表字段(aml_risk_level);
 |
| 2025-11-25 11:04:14 | 8.26.2.94 | 刘大为 | 所有表usms_client，添加了表字段(cust_id);
所有表usms_client，添加了表字段(proda... |

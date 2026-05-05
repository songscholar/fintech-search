# uopt_client - 客户账户信息表

**表对象ID**: 9015
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 86 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | cust_id | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | client_name | 否 |  |  |
| 5 | full_name | 否 |  |  |
| 6 | organ_flag | 否 |  |  |
| 7 | id_kind | 否 |  |  |
| 8 | id_no | 否 |  |  |
| 9 | id_begindate | 否 |  |  |
| 10 | id_enddate | 否 |  |  |
| 11 | prodasset_flag | 否 |  |  |
| 12 | account_data | 否 |  |  |
| 13 | risk_info | 否 |  |  |
| 14 | statement_flag | 否 |  |  |
| 15 | receive_name | 否 |  |  |
| 16 | bill_template_type | 否 |  |  |
| 17 | crdtval_kind | 否 |  |  |
| 18 | en_contact_type | 否 |  |  |
| 19 | contact_freq | 否 |  |  |
| 20 | developer | 否 |  |  |
| 21 | cost_place | 否 |  |  |
| 22 | develop_source | 否 |  |  |
| 23 | open_type | 否 |  |  |
| 24 | open_date | 否 |  |  |
| 25 | confirm_date | 否 |  |  |
| 26 | cancel_date | 否 |  |  |
| 27 | trade_password | 否 |  |  |
| 28 | sign_flag | 否 |  |  |
| 29 | sign_date | 否 |  |  |
| 30 | client_status | 否 |  |  |
| 31 | open_business | 否 |  |  |
| 32 | contact_name | 否 |  |  |
| 33 | contact_id_kind | 否 |  |  |
| 34 | contact_id_no | 否 |  |  |
| 35 | contact_id_begindate | 否 |  |  |
| 36 | contact_id_enddate | 否 |  |  |
| 37 | contact_tel | 否 |  |  |
| 38 | contact_mobile | 否 |  |  |
| 39 | cardread_flag | 否 |  |  |
| 40 | mail_way | 否 |  |  |
| 41 | develop_net | 否 |  |  |
| 42 | partition_no | 否 |  |  |
| 43 | remark | 否 |  |  |
| 44 | branch_no | 否 |  |  |
| 45 | cust_id | 否 |  |  |
| 46 | client_id | 否 |  |  |
| 47 | client_name | 否 |  |  |
| 48 | full_name | 否 |  |  |
| 49 | organ_flag | 否 |  |  |
| 50 | id_kind | 否 |  |  |
| 51 | id_no | 否 |  |  |
| 52 | id_begindate | 否 |  |  |
| 53 | id_enddate | 否 |  |  |
| 54 | prodasset_flag | 否 |  |  |
| 55 | account_data | 否 |  |  |
| 56 | risk_info | 否 |  |  |
| 57 | statement_flag | 否 |  |  |
| 58 | receive_name | 否 |  |  |
| 59 | bill_template_type | 否 |  |  |
| 60 | crdtval_kind | 否 |  |  |
| 61 | en_contact_type | 否 |  |  |
| 62 | contact_freq | 否 |  |  |
| 63 | developer | 否 |  |  |
| 64 | cost_place | 否 |  |  |
| 65 | develop_source | 否 |  |  |
| 66 | open_type | 否 |  |  |
| 67 | open_date | 否 |  |  |
| 68 | confirm_date | 否 |  |  |
| 69 | cancel_date | 否 |  |  |
| 70 | trade_password | 否 |  |  |
| 71 | sign_flag | 否 |  |  |
| 72 | sign_date | 否 |  |  |
| 73 | client_status | 否 |  |  |
| 74 | open_business | 否 |  |  |
| 75 | contact_name | 否 |  |  |
| 76 | contact_id_kind | 否 |  |  |
| 77 | contact_id_no | 否 |  |  |
| 78 | contact_id_begindate | 否 |  |  |
| 79 | contact_id_enddate | 否 |  |  |
| 80 | contact_tel | 否 |  |  |
| 81 | contact_mobile | 否 |  |  |
| 82 | cardread_flag | 否 |  |  |
| 83 | mail_way | 否 |  |  |
| 84 | develop_net | 否 |  |  |
| 85 | partition_no | 否 |  |  |
| 86 | remark | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_client | 默认 | 是 | client_id, client_id |
| idx_uopt_client | 默认 | 是 | client_id, client_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_client | client_id, client_id |
| idx_uopt_client | client_id, client_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-10-30 20:34:40 | V3.0.3.10 | 韦子晗 | 删除物理索引中的partition_no字段 |
| 2024-05-09 09:23:06 | V3.0.3.2 | 韦子晗 | 新增partition_no字段 |
| 2024-10-30 20:34:40 | V3.0.3.10 | 韦子晗 | 删除物理索引中的partition_no字段 |
| 2024-05-09 09:23:06 | V3.0.3.2 | 韦子晗 | 新增partition_no字段 |

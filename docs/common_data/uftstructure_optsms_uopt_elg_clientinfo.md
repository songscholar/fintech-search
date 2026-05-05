# uopt_elg_clientinfo - 期权客户适当性信息表

**表对象ID**: 9606
**所属模块**: optsms
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | opt_level | 否 |  |  |
| 5 | pur_quota | 否 |  |  |
| 6 | quota_date | 否 |  |  |
| 7 | quota_end_date | 否 |  |  |
| 8 | optacct_type | 否 |  |  |
| 9 | pre_pur_quota | 否 |  |  |
| 10 | modify_date | 否 |  |  |
| 11 | partition_no | 否 |  |  |
| 12 | position_str | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | en_opt_busi | 否 |  |  |
| 15 | opt_holdlimit_model_str | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | fund_account | 否 |  |  |
| 19 | opt_level | 否 |  |  |
| 20 | pur_quota | 否 |  |  |
| 21 | quota_date | 否 |  |  |
| 22 | quota_end_date | 否 |  |  |
| 23 | optacct_type | 否 |  |  |
| 24 | pre_pur_quota | 否 |  |  |
| 25 | modify_date | 否 |  |  |
| 26 | partition_no | 否 |  |  |
| 27 | position_str | 否 |  |  |
| 28 | transaction_no | 否 |  |  |
| 29 | en_opt_busi | 否 |  |  |
| 30 | opt_holdlimit_model_str | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_elg_clientinfo_pos | 默认 | 否 | position_str, position_str |
| idx_uopt_elg_clientinfo | 默认 | 否 | exchange_type, exchange_type |
| idx_uopt_elg_clientinfo_pos | 默认 | 是 | position_str, position_str |
| idx_uopt_elg_clientinfo_temp | 默认 | 是 | exchange_type, fund_account, exchange_type, fund_account |
| idx_uopt_elg_clientinfo_pos | 默认 | 否 | position_str, position_str |
| idx_uopt_elg_clientinfo | 默认 | 否 | exchange_type, exchange_type |
| idx_uopt_elg_clientinfo_pos | 默认 | 是 | position_str, position_str |
| idx_uopt_elg_clientinfo_temp | 默认 | 是 | exchange_type, fund_account, exchange_type, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_elg_clientinfo | exchange_type, fund_account, exchange_type, fund_account |
| idx_uopt_elg_clientinfo | exchange_type, fund_account, exchange_type, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-11 09:51:05 | V3.0.2.10 | 韦子晗 | 新增临时索引支持数据二次上场 |
| 2025-09-08 19:16:51 | V3.0.2.9 | 高志强 | 所有表uopt_elg_clientinfo，添加了表字段(transaction_no);
 |
| 2025-07-25 16:37:15 | V3.0.2.1 | 汪迎 | 物理表uopt_elg_clientinfo，添加了表字段(position_str);
,物理表uopt_elg_c... |
| 2024-05-09 09:27:43 | V3.0.3.4 | 韦子晗 | 新增partition_no字段 |
| 2025-09-11 09:51:05 | V3.0.2.10 | 韦子晗 | 新增临时索引支持数据二次上场 |
| 2025-09-08 19:16:51 | V3.0.2.9 | 高志强 | 所有表uopt_elg_clientinfo，添加了表字段(transaction_no);
 |
| 2025-07-25 16:37:15 | V3.0.2.1 | 汪迎 | 物理表uopt_elg_clientinfo，添加了表字段(position_str);
,物理表uopt_elg_c... |
| 2024-05-09 09:27:43 | V3.0.3.4 | 韦子晗 | 新增partition_no字段 |

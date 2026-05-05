# ucrt_contract - 融资融券合同表

**表对象ID**: 7508
**所属模块**: crttrade
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 60 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | contract_id | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | crdtint_mode | 否 |  |  |
| 6 | crdt_fare_str | 否 |  |  |
| 7 | contract_rights | 否 |  |  |
| 8 | fin_max_quota | 否 |  |  |
| 9 | slo_max_quota | 否 |  |  |
| 10 | total_max_quota | 否 |  |  |
| 11 | papercont_id | 否 |  |  |
| 12 | compact_term | 否 |  |  |
| 13 | crdt_level | 否 |  |  |
| 14 | build_date | 否 |  |  |
| 15 | begin_date | 否 |  |  |
| 16 | end_date | 否 |  |  |
| 17 | fin_cashgroup_no | 否 |  |  |
| 18 | slo_cashgroup_no | 否 |  |  |
| 19 | contract_status | 否 |  |  |
| 20 | date_clear | 否 |  |  |
| 21 | personalization_mode | 否 |  |  |
| 22 | transaction_no | 否 |  |  |
| 23 | package_kind_str | 否 |  |  |
| 24 | package_begin_date | 否 |  |  |
| 25 | package_end_date | 否 |  |  |
| 26 | primerate_end_date | 否 |  |  |
| 27 | primerate_begin_date | 否 |  |  |
| 28 | auto_interest_type | 否 |  |  |
| 29 | auto_interest_return_flag | 否 |  |  |
| 30 | auto_interest_cycle | 否 |  |  |
| 31 | init_date | 否 |  |  |
| 32 | contract_id | 否 |  |  |
| 33 | client_id | 否 |  |  |
| 34 | fund_account | 否 |  |  |
| 35 | crdtint_mode | 否 |  |  |
| 36 | crdt_fare_str | 否 |  |  |
| 37 | contract_rights | 否 |  |  |
| 38 | fin_max_quota | 否 |  |  |
| 39 | slo_max_quota | 否 |  |  |
| 40 | total_max_quota | 否 |  |  |
| 41 | papercont_id | 否 |  |  |
| 42 | compact_term | 否 |  |  |
| 43 | crdt_level | 否 |  |  |
| 44 | build_date | 否 |  |  |
| 45 | begin_date | 否 |  |  |
| 46 | end_date | 否 |  |  |
| 47 | fin_cashgroup_no | 否 |  |  |
| 48 | slo_cashgroup_no | 否 |  |  |
| 49 | contract_status | 否 |  |  |
| 50 | date_clear | 否 |  |  |
| 51 | personalization_mode | 否 |  |  |
| 52 | transaction_no | 否 |  |  |
| 53 | package_kind_str | 否 |  |  |
| 54 | package_begin_date | 否 |  |  |
| 55 | package_end_date | 否 |  |  |
| 56 | primerate_end_date | 否 |  |  |
| 57 | primerate_begin_date | 否 |  |  |
| 58 | auto_interest_type | 否 |  |  |
| 59 | auto_interest_return_flag | 否 |  |  |
| 60 | auto_interest_cycle | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_contract | ART | 是 | fund_account, contract_id, fund_account, contract_id |
| idx_ucrt_contract_id | ART | 是 | contract_id, contract_id |
| idx_ucrt_contract_client_id | ART | 是 | client_id, client_id |
| idx_ucrt_contract | ART | 是 | fund_account, contract_id, fund_account, contract_id |
| idx_ucrt_contract_id | ART | 是 | contract_id, contract_id |
| idx_ucrt_contract_client_id | ART | 是 | client_id, client_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_contract | contract_id, contract_id |
| idx_ucrt_contract | contract_id, contract_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-02 11:11:51 | 3.0.6.1065 | 许琮擎 | 增加一个字段为client_id的索引，同时现有的两个索引的索引字段对调 |
| 2025-09-11 13:19:44 | 3.0.6.1071 | 袁文龙 | ses合入dev，版本+1 |
| 2025-08-22 09:12:34 | 3.0.6.1064 | 董瑞辉 | 所有表ucrt_contract，添加了表字段(auto_interest_type);
所有表ucrt_contra... |
| 2025-07-16 14:55:36 | 3.0.2.2013 | huangzh | 物理表ucrt_contract，添加了表字段(primerate_begin_date);
 |
| 2025-07-14 14:00:29 | 3.0.2.2010 | huangzh | 物理表ucrt_contract，添加了表字段(primerate_end_date);
 |
| 2024-12-24 14:50:21 | 3.0.6.23 | 沈勋 | 物理表ucrt_contract，添加了表字段(package_kind_str);
物理表ucrt_contract... |
| 2024-07-23 15:49:10 | 3.0.3.5 | 刘景锋 | 修复关联索引是全局索引问题 |
| 2023-08-22 13:33:32 | 0.3.3.141 | 徐志坚 | 因参数同步需要增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-09-02 11:11:51 | 3.0.6.1065 | 许琮擎 | 增加一个字段为client_id的索引，同时现有的两个索引的索引字段对调 |
| 2025-09-11 13:19:44 | 3.0.6.1071 | 袁文龙 | ses合入dev，版本+1 |
| 2025-08-22 09:12:34 | 3.0.6.1064 | 董瑞辉 | 所有表ucrt_contract，添加了表字段(auto_interest_type);
所有表ucrt_contra... |
| 2025-07-16 14:55:36 | 3.0.2.2013 | huangzh | 物理表ucrt_contract，添加了表字段(primerate_begin_date);
 |
| 2025-07-14 14:00:29 | 3.0.2.2010 | huangzh | 物理表ucrt_contract，添加了表字段(primerate_end_date);
 |
| 2024-12-24 14:50:21 | 3.0.6.23 | 沈勋 | 物理表ucrt_contract，添加了表字段(package_kind_str);
物理表ucrt_contract... |

> 共 18 条修改记录，仅显示最近15条

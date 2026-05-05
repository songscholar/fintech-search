# ucrt_fund_account - 融资融券资产账号表

**表对象ID**: 7529
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 52 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | asset_prop | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | client_group | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | client_rights | 否 |  |  |
| 6 | discount_model | 否 |  |  |
| 7 | en_entrust_way | 否 |  |  |
| 8 | fare_kind_str | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | fundacct_status | 否 |  |  |
| 11 | main_flag | 否 |  |  |
| 12 | organ_flag | 否 |  |  |
| 13 | trade_password | 否 |  |  |
| 14 | profit_flag | 否 |  |  |
| 15 | restriction | 否 |  |  |
| 16 | room_code | 否 |  |  |
| 17 | fundacct_ctrlstr | 否 |  |  |
| 18 | partition_no | 否 |  |  |
| 19 | fund_password | 否 |  |  |
| 20 | query_password | 否 |  |  |
| 21 | client_name | 否 |  |  |
| 22 | fund_card | 否 |  |  |
| 23 | risk_level | 否 |  |  |
| 24 | risk_enddate | 否 |  |  |
| 25 | product_flag | 否 |  |  |
| 26 | en_ext_rights | 否 |  |  |
| 27 | asset_prop | 否 |  |  |
| 28 | branch_no | 否 |  |  |
| 29 | client_group | 否 |  |  |
| 30 | client_id | 否 |  |  |
| 31 | client_rights | 否 |  |  |
| 32 | discount_model | 否 |  |  |
| 33 | en_entrust_way | 否 |  |  |
| 34 | fare_kind_str | 否 |  |  |
| 35 | fund_account | 否 |  |  |
| 36 | fundacct_status | 否 |  |  |
| 37 | main_flag | 否 |  |  |
| 38 | organ_flag | 否 |  |  |
| 39 | trade_password | 否 |  |  |
| 40 | profit_flag | 否 |  |  |
| 41 | restriction | 否 |  |  |
| 42 | room_code | 否 |  |  |
| 43 | fundacct_ctrlstr | 否 |  |  |
| 44 | partition_no | 否 |  |  |
| 45 | fund_password | 否 |  |  |
| 46 | query_password | 否 |  |  |
| 47 | client_name | 否 |  |  |
| 48 | fund_card | 否 |  |  |
| 49 | risk_level | 否 |  |  |
| 50 | risk_enddate | 否 |  |  |
| 51 | product_flag | 否 |  |  |
| 52 | en_ext_rights | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_fund_account_id | 默认 | 否 | client_id, client_id |
| idx_ucrt_fund_account | ART | 是 | fund_account, fund_account |
| idx_ucrt_fund_account_id | ART | 是 | client_id, client_id |
| idx_ucrt_fund_account_id | 默认 | 否 | client_id, client_id |
| idx_ucrt_fund_account | ART | 是 | fund_account, fund_account |
| idx_ucrt_fund_account_id | ART | 是 | client_id, client_id |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_fund_account | fund_account, fund_account |
| idx_ucrt_fund_account_id | client_id, client_id |
| idx_ucrt_fund_account | fund_account, fund_account |
| idx_ucrt_fund_account_id | client_id, client_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-21 19:09:24 | 3.0.6.38 | tongck54118 | 物理表ucrt_fund_account，添加了表字段(client_name);
 |
| 2025-05-16 15:04:17 | 3.0.6.54 | 牟家乐 | 物理表ucrt_fund_account，添加了表字段(fund_card);
物理表ucrt_fund_accoun... |
| 2024-11-01 14:32:30 | 3.0.6.12 | 董瑞辉 | 删除ucrt_crdt_limit_sell的关联关系 |
| 2024-10-18 09:42:38 | 3.0.6.6 | 沈勋 | 增加ucrt_bond_exemptricon表的关联关系 |
| 2024-09-04 10:32:23 | 3.0.4.2 | 沈勋 | 新增关联对象crdt_clietn_min_fare |
| 2024-07-23 15:49:39 | 3.0.3.5 | 刘景锋 | 修复关联索引是全局索引问题 |
| 2024-05-21 16:31:09 | 3.0.2.13 | 楼欣欣 | 新增关联对象crdt_client_svr_fare |
| 2023-11-27 16:28:50 | V3.0.1.22 | 沈勋 | 物理表ucrt_fund_account，增加索引(idx_ucrt_fund_account_id:[client_i... |
| 2023-08-30 10:26:57 | 0.3.3.144 | 雷玄 | 增加ucrt_compact表的关联关系 |
| 2023-08-25 16:34:28 | 0.3.3.143 | 徐志坚 | 调整事务控制方式，删除transaction_no字段 |
| 2023-08-23 18:39:36 | 0.3.3.142 | 徐志坚 | 增加transaction_no字段 |
| 2023-08-23 09:14:36 | 0.3.3.142 | 徐志坚 | 为了参数同步，调整ucrt_risk_list的关联索引；增加ucrt_ofelecagreement、ucrt_ris... |
| 2023-08-18 14:49 | 0.3.3.139 | 雷玄 | 修改idx_ucrt_fund_account_id为非唯一索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-14 14:18 | 0.3.3.132 | 程猛 | client表取消与fund_account表的关联关系 |

> 共 32 条修改记录，仅显示最近15条

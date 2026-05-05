# uopt_fund_account - 期权资产账号表

**表对象ID**: 9600
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 50 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | client_name | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | optacct_type | 否 |  |  |
| 6 | client_group | 否 |  |  |
| 7 | room_code | 否 |  |  |
| 8 | en_entrust_way | 否 |  |  |
| 9 | fundacct_status | 否 |  |  |
| 10 | fund_account_secu | 否 |  |  |
| 11 | trade_password | 否 |  |  |
| 12 | trade_check_risk_degree | 否 |  |  |
| 13 | trade_check_margin_algorithm | 否 |  |  |
| 14 | last_update_date | 否 |  |  |
| 15 | last_update_time | 否 |  |  |
| 16 | fetch_balance_ratio | 否 |  |  |
| 17 | real_limitopen_risk | 否 |  |  |
| 18 | client_prop | 否 |  |  |
| 19 | partition_no | 否 |  |  |
| 20 | profit_flag | 否 |  |  |
| 21 | position_str | 否 |  |  |
| 22 | total_asset | 否 |  |  |
| 23 | fare_kind_str | 否 |  |  |
| 24 | restriction | 否 |  |  |
| 25 | client_rights | 否 |  |  |
| 26 | branch_no | 否 |  |  |
| 27 | client_id | 否 |  |  |
| 28 | client_name | 否 |  |  |
| 29 | fund_account | 否 |  |  |
| 30 | optacct_type | 否 |  |  |
| 31 | client_group | 否 |  |  |
| 32 | room_code | 否 |  |  |
| 33 | en_entrust_way | 否 |  |  |
| 34 | fundacct_status | 否 |  |  |
| 35 | fund_account_secu | 否 |  |  |
| 36 | trade_password | 否 |  |  |
| 37 | trade_check_risk_degree | 否 |  |  |
| 38 | trade_check_margin_algorithm | 否 |  |  |
| 39 | last_update_date | 否 |  |  |
| 40 | last_update_time | 否 |  |  |
| 41 | fetch_balance_ratio | 否 |  |  |
| 42 | real_limitopen_risk | 否 |  |  |
| 43 | client_prop | 否 |  |  |
| 44 | partition_no | 否 |  |  |
| 45 | profit_flag | 否 |  |  |
| 46 | position_str | 否 |  |  |
| 47 | total_asset | 否 |  |  |
| 48 | fare_kind_str | 否 |  |  |
| 49 | restriction | 否 |  |  |
| 50 | client_rights | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_fund_account_pos | 默认 | 否 | position_str, position_str |
| idx_uopt_fund_account | 默认 | 是 | fund_account, fund_account |
| idx_uopt_fund_account_id | 默认 | 是 | client_id, client_id |
| idx_uopt_fund_account_pos | 默认 | 是 | position_str, position_str |
| idx_uopt_fund_account_pos | 默认 | 否 | position_str, position_str |
| idx_uopt_fund_account | 默认 | 是 | fund_account, fund_account |
| idx_uopt_fund_account_id | 默认 | 是 | client_id, client_id |
| idx_uopt_fund_account_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_fund_account | fund_account, fund_account |
| idx_uopt_fund_account | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 13:35:59 | V3.0.2.19 | 韦子晗 | 所有表uopt_fund_account，添加了表字段(total_asset);
 |
| 2025-09-23 13:31:46 | V3.0.2.13 | 韦子晗 | uopt_realtime表的关联关系取消关联记录为空校验 |
| 2025-07-25 16:44:25 | V3.0.2.1 | 汪迎 | 物理表uopt_fund_account，添加了表字段(position_str);
,物理表uopt_fund_ac... |
| 2025-06-04 15:11:33 | V3.0.3.15 | 张明月 | 物理表uopt_fund_account，添加了表字段(profit_flag);
 |
| 2025-12-01 13:35:59 | V3.0.2.19 | 韦子晗 | 所有表uopt_fund_account，添加了表字段(total_asset);
 |
| 2025-09-23 13:31:46 | V3.0.2.13 | 韦子晗 | uopt_realtime表的关联关系取消关联记录为空校验 |
| 2025-07-25 16:44:25 | V3.0.2.1 | 汪迎 | 物理表uopt_fund_account，添加了表字段(position_str);
,物理表uopt_fund_ac... |
| 2025-06-04 15:11:33 | V3.0.3.15 | 张明月 | 物理表uopt_fund_account，添加了表字段(profit_flag);
 |

# ucrt_acct_extend - 信用账户扩展信息表

**表对象ID**: 7501
**所属模块**: crttrade
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 46 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | riskcrdt_flag | 否 |  |  |
| 4 | payoff_flag | 否 |  |  |
| 5 | break_times | 否 |  |  |
| 6 | payoff_count | 否 |  |  |
| 7 | black_times | 否 |  |  |
| 8 | risk_restriction | 否 |  |  |
| 9 | join_acct_flag | 否 |  |  |
| 10 | crdt_score | 否 |  |  |
| 11 | cashchange_status | 否 |  |  |
| 12 | cashchange_date | 否 |  |  |
| 13 | begin_rate | 否 |  |  |
| 14 | begin_net_asset | 否 |  |  |
| 15 | extcon_cintmod_times | 否 |  |  |
| 16 | contract_postpone_flag | 否 |  |  |
| 17 | aml_risk_level | 否 |  |  |
| 18 | crdt_status | 否 |  |  |
| 19 | id_enddate | 否 |  |  |
| 20 | transaction_no | 否 |  |  |
| 21 | organ_prod_kind | 否 |  |  |
| 22 | begin_net_unfair_asset | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | client_id | 否 |  |  |
| 25 | fund_account | 否 |  |  |
| 26 | riskcrdt_flag | 否 |  |  |
| 27 | payoff_flag | 否 |  |  |
| 28 | break_times | 否 |  |  |
| 29 | payoff_count | 否 |  |  |
| 30 | black_times | 否 |  |  |
| 31 | risk_restriction | 否 |  |  |
| 32 | join_acct_flag | 否 |  |  |
| 33 | crdt_score | 否 |  |  |
| 34 | cashchange_status | 否 |  |  |
| 35 | cashchange_date | 否 |  |  |
| 36 | begin_rate | 否 |  |  |
| 37 | begin_net_asset | 否 |  |  |
| 38 | extcon_cintmod_times | 否 |  |  |
| 39 | contract_postpone_flag | 否 |  |  |
| 40 | aml_risk_level | 否 |  |  |
| 41 | crdt_status | 否 |  |  |
| 42 | id_enddate | 否 |  |  |
| 43 | transaction_no | 否 |  |  |
| 44 | organ_prod_kind | 否 |  |  |
| 45 | begin_net_unfair_asset | 否 |  |  |
| 46 | remark | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_acct_extend | ART | 是 | fund_account, fund_account |
| idx_ucrt_acct_extend | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_acct_extend | fund_account, fund_account |
| idx_ucrt_acct_extend | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-26 19:18:02 | 3.0.2.1 | 曾阳璞 | 所有表ucrt_acct_extend，添加了表字段(remark);
 |
| 2024-12-16 11:20:44 | 3.0.6.20 | 卢杰 | 物理表ucrt_acct_extend，添加了表字段(begin_net_unfair_asset);
 |
| 2023-11-08 09:25:39 | V3.0.1.17 | 吴丽丽 | 物理表ucrt_acct_extend，添加了表字段(organ_prod_kind);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-08-26 19:18:02 | 3.0.2.1 | 曾阳璞 | 所有表ucrt_acct_extend，添加了表字段(remark);
 |
| 2024-12-16 11:20:44 | 3.0.6.20 | 卢杰 | 物理表ucrt_acct_extend，添加了表字段(begin_net_unfair_asset);
 |
| 2023-11-08 09:25:39 | V3.0.1.17 | 吴丽丽 | 物理表ucrt_acct_extend，添加了表字段(organ_prod_kind);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

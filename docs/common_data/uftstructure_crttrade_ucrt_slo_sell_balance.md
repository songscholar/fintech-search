# ucrt_slo_sell_balance - 融券卖出所得表

**表对象ID**: 7511
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 50 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | slo_sell_balance | 否 |  |  |
| 5 | real_slosell_balance | 否 |  |  |
| 6 | slo_used_balance | 否 |  |  |
| 7 | real_sloused_balance | 否 |  |  |
| 8 | slo_frozen_balance | 否 |  |  |
| 9 | entrust_frozen_balance | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | remark | 否 |  |  |
| 12 | begin_slosell_balance | 否 |  |  |
| 13 | begin_sloused_balance | 否 |  |  |
| 14 | position_str | 否 |  | fund_account(18)+money_type(3) |
| 15 | tohis_date | 否 | H |  |
| 16 | client_group | 否 | H |  |
| 17 | room_code | 否 | H |  |
| 18 | asset_prop | 否 | H |  |
| 19 | limit_flag | 否 | H |  |
| 20 | risk_level | 否 | H |  |
| 21 | corp_client_group | 否 | H |  |
| 22 | corp_risk_level | 否 | H |  |
| 23 | asset_level | 否 | H |  |
| 24 | client_name | 否 | H |  |
| 25 | client_prop | 否 | H |  |
| 26 | client_id | 否 |  |  |
| 27 | fund_account | 否 |  |  |
| 28 | money_type | 否 |  |  |
| 29 | slo_sell_balance | 否 |  |  |
| 30 | real_slosell_balance | 否 |  |  |
| 31 | slo_used_balance | 否 |  |  |
| 32 | real_sloused_balance | 否 |  |  |
| 33 | slo_frozen_balance | 否 |  |  |
| 34 | entrust_frozen_balance | 否 |  |  |
| 35 | branch_no | 否 |  |  |
| 36 | remark | 否 |  |  |
| 37 | begin_slosell_balance | 否 |  |  |
| 38 | begin_sloused_balance | 否 |  |  |
| 39 | position_str | 否 |  | fund_account(18)+money_type(3) |
| 40 | tohis_date | 否 | H |  |
| 41 | client_group | 否 | H |  |
| 42 | room_code | 否 | H |  |
| 43 | asset_prop | 否 | H |  |
| 44 | limit_flag | 否 | H |  |
| 45 | risk_level | 否 | H |  |
| 46 | corp_client_group | 否 | H |  |
| 47 | corp_risk_level | 否 | H |  |
| 48 | asset_level | 否 | H |  |
| 49 | client_name | 否 | H |  |
| 50 | client_prop | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_slo_sell_balance | ART | 是 | fund_account, money_type, fund_account, money_type |
| uk_rpt_ucrtslosellbalance | ART | 是 | tohis_date, client_id, fund_account, tohis_date, client_id, fund_account |
| idx_ucrt_slo_sell_balance | ART | 是 | fund_account, money_type, fund_account, money_type |
| uk_rpt_ucrtslosellbalance | ART | 是 | tohis_date, client_id, fund_account, tohis_date, client_id, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_slo_sell_balance | fund_account, money_type, fund_account, money_type |
| idx_ucrt_slo_sell_balance | fund_account, money_type, fund_account, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-21 14:20:14 | 3.0.6.1065 |  | 物理表ucrt_slo_sell_balance，添加了表字段(branch_no);
物理表ucrt_slo_sel... |
| 2025-07-09 09:49:41 | 3.0.6.52 | 卢杰 | 物理表ucrt_slo_sell_balance，添加了表字段(branch_no);
物理表ucrt_slo_sel... |
| 2023-11-14 14:28:13 | V3.0.1.19 | huangzh | 增加关联关系idx_ucrt_slo_sell_balance_jour |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-08-21 14:20:14 | 3.0.6.1065 |  | 物理表ucrt_slo_sell_balance，添加了表字段(branch_no);
物理表ucrt_slo_sel... |
| 2025-07-09 09:49:41 | 3.0.6.52 | 卢杰 | 物理表ucrt_slo_sell_balance，添加了表字段(branch_no);
物理表ucrt_slo_sel... |
| 2023-11-14 14:28:13 | V3.0.1.19 | huangzh | 增加关联关系idx_ucrt_slo_sell_balance_jour |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

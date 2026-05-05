# ucrt_slo_sell_balance_total - 融券卖出所得汇总表

**表对象ID**: 7581
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | money_type | 否 |  |  |
| 5 | begin_slosell_balance | 否 |  |  |
| 6 | slo_sell_balance | 否 |  |  |
| 7 | real_slosell_balance | 否 |  |  |
| 8 | remark | 否 |  |  |
| 9 | position_str | 否 |  | fund_account(18) + money_type(3) |
| 10 | slo_used_balance | 否 |  |  |
| 11 | real_sloused_balance | 否 |  |  |
| 12 | begin_sloused_balance | 否 |  |  |
| 13 | slo_frozen_balance | 否 |  |  |
| 14 | entrust_frozen_balance | 否 |  |  |
| 15 | fund_account | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | money_type | 否 |  |  |
| 19 | begin_slosell_balance | 否 |  |  |
| 20 | slo_sell_balance | 否 |  |  |
| 21 | real_slosell_balance | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | position_str | 否 |  | fund_account(18) + money_type(3) |
| 24 | slo_used_balance | 否 |  |  |
| 25 | real_sloused_balance | 否 |  |  |
| 26 | begin_sloused_balance | 否 |  |  |
| 27 | slo_frozen_balance | 否 |  |  |
| 28 | entrust_frozen_balance | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_slo_sell_balance_total | ART | 是 | fund_account, money_type, fund_account, money_type |
| idx_ucrt_slo_sell_balance_total | ART | 是 | fund_account, money_type, fund_account, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_slo_sell_balance_total | fund_account, money_type, fund_account, money_type |
| idx_ucrt_slo_sell_balance_total | fund_account, money_type, fund_account, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-25 10:59:40 | V3.0.2.2001 | 曾阳璞 | 新增 |
| 2025-07-25 10:59:40 | V3.0.2.2001 | 曾阳璞 | 新增 |

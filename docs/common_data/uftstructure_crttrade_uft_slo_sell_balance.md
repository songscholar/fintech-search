# uft_slo_sell_balance - UFT融券卖出所得表

**表对象ID**: 7994
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 30 个）

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
| 9 | position_str | 否 |  |  |
| 10 | slo_used_balance | 否 |  |  |
| 11 | real_sloused_balance | 否 |  |  |
| 12 | begin_sloused_balance | 否 |  |  |
| 13 | order_no | 否 |  |  |
| 14 | slo_frozen_balance | 否 |  |  |
| 15 | entrust_frozen_balance | 否 |  |  |
| 16 | fund_account | 否 |  |  |
| 17 | client_id | 否 |  |  |
| 18 | branch_no | 否 |  |  |
| 19 | money_type | 否 |  |  |
| 20 | begin_slosell_balance | 否 |  |  |
| 21 | slo_sell_balance | 否 |  |  |
| 22 | real_slosell_balance | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | position_str | 否 |  |  |
| 25 | slo_used_balance | 否 |  |  |
| 26 | real_sloused_balance | 否 |  |  |
| 27 | begin_sloused_balance | 否 |  |  |
| 28 | order_no | 否 |  |  |
| 29 | slo_frozen_balance | 否 |  |  |
| 30 | entrust_frozen_balance | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_slo_sell_balance_acct | ART | 是 | fund_account, fund_account |
| idx_uft_slo_sell_balance_pos | ART | 是 | position_str, position_str |
| idx_uft_slo_sell_balance_acct | ART | 是 | fund_account, fund_account |
| idx_uft_slo_sell_balance_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_slo_sell_balance_pos | position_str, position_str |
| idx_uft_slo_sell_balance_pos | position_str, position_str |

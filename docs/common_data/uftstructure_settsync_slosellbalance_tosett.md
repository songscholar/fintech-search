# slosellbalance_tosett - 清算融券卖出所得表2

**表对象ID**: 3065
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 是 |  |  |
| 2 | client_id | 是 |  |  |
| 3 | branch_no | 是 |  |  |
| 4 | money_type | 是 |  |  |
| 5 | begin_slosell_balance | 是 |  |  |
| 6 | slo_sell_balance | 是 |  |  |
| 7 | real_slosell_balance | 是 |  |  |
| 8 | remark | 是 |  |  |
| 9 | position_str | 是 |  |  |
| 10 | slo_used_balance | 是 |  |  |
| 11 | real_sloused_balance | 是 |  |  |
| 12 | begin_sloused_balance | 是 |  |  |
| 13 | slo_frozen_balance | 是 |  |  |
| 14 | entrust_frozen_balance | 是 |  |  |
| 15 | fund_account | 是 |  |  |
| 16 | client_id | 是 |  |  |
| 17 | branch_no | 是 |  |  |
| 18 | money_type | 是 |  |  |
| 19 | begin_slosell_balance | 是 |  |  |
| 20 | slo_sell_balance | 是 |  |  |
| 21 | real_slosell_balance | 是 |  |  |
| 22 | remark | 是 |  |  |
| 23 | position_str | 是 |  |  |
| 24 | slo_used_balance | 是 |  |  |
| 25 | real_sloused_balance | 是 |  |  |
| 26 | begin_sloused_balance | 是 |  |  |
| 27 | slo_frozen_balance | 是 |  |  |
| 28 | entrust_frozen_balance | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_slosellbalancetosett_acct | 默认 | 是 | fund_account, fund_account |
| idx_slosellbalancetosett_acct | 默认 | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_slosellbalancetotal_pos | position_str, position_str |
| idx_slosellbalancetotal_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2018-04-26 14:12 | 8.26.1.14 | 蒋迪 | 新增 |
| 2018-04-26 14:12 | 8.26.1.14 | 蒋迪 | 新增 |

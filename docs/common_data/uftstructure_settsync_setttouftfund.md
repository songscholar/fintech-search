# setttouftfund - 清算入账资金表

**表对象ID**: 3088
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 是 |  |  |
| 2 | money_type | 是 |  |  |
| 3 | client_id | 是 |  |  |
| 4 | current_balance | 是 |  | 增量 |
| 5 | enable_balance | 是 |  | 增量 |
| 6 | frozen_balance | 是 |  | 增量 |
| 7 | unfrozen_balance | 是 |  | 增量 |
| 8 | correct_balance | 是 |  | 增量 |
| 9 | uncome_buy_balance | 是 |  | 增量 |
| 10 | uncome_sell_balance | 是 |  | 增量 |
| 11 | uncome_correct_balance | 是 |  | 增量 |
| 12 | asset_prop | 是 |  |  |
| 13 | bank_no | 是 |  |  |
| 14 | flow_count | 是 |  |  |
| 15 | foregift_balance | 是 |  |  |
| 16 | fund_account | 是 |  |  |
| 17 | money_type | 是 |  |  |
| 18 | client_id | 是 |  |  |
| 19 | current_balance | 是 |  | 增量 |
| 20 | enable_balance | 是 |  | 增量 |
| 21 | frozen_balance | 是 |  | 增量 |
| 22 | unfrozen_balance | 是 |  | 增量 |
| 23 | correct_balance | 是 |  | 增量 |
| 24 | uncome_buy_balance | 是 |  | 增量 |
| 25 | uncome_sell_balance | 是 |  | 增量 |
| 26 | uncome_correct_balance | 是 |  | 增量 |
| 27 | asset_prop | 是 |  |  |
| 28 | bank_no | 是 |  |  |
| 29 | flow_count | 是 |  |  |
| 30 | foregift_balance | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| sett_fund_idx | 默认 | 是 | flow_count, fund_account, money_type, flow_count, fund_account, money_type |
| sett_fund_idx | 默认 | 是 | flow_count, fund_account, money_type, flow_count, fund_account, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| sett_fund_idx | flow_count, fund_account, money_type, flow_count, fund_account, money_type |
| sett_fund_idx | flow_count, fund_account, money_type, flow_count, fund_account, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-07-11 10:38:05 | 1.0.0.1 | shikai | 支持清算入账 |
| 2024-07-11 10:38:05 | 1.0.0.1 | shikai | 支持清算入账 |

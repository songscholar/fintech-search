# uopt_fundreal_jour_sum - 期权交易资金流水汇总表

**表对象ID**: 9605
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 是 |  |  |
| 2 | fund_account | 是 |  |  |
| 3 | money_type | 是 |  |  |
| 4 | branch_no | 是 |  |  |
| 5 | asset_prop | 是 |  |  |
| 6 | deposit_balance | 是 |  |  |
| 7 | withdraw_balance | 是 |  |  |
| 8 | order_no | 是 |  |  |
| 9 | client_id | 是 |  |  |
| 10 | fund_account | 是 |  |  |
| 11 | money_type | 是 |  |  |
| 12 | branch_no | 是 |  |  |
| 13 | asset_prop | 是 |  |  |
| 14 | deposit_balance | 是 |  |  |
| 15 | withdraw_balance | 是 |  |  |
| 16 | order_no | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_fundreal_jour_sum | 默认 | 是 | fund_account, money_type, fund_account, money_type |
| idx_uopt_fundreal_jour_sum | 默认 | 是 | fund_account, money_type, fund_account, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_fundreal_jour_sum | fund_account, money_type, fund_account, money_type |
| idx_uopt_fundreal_jour_sum | fund_account, money_type, fund_account, money_type |

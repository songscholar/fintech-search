# uopt_entrust_sum - 期权在途订单统计表

**表对象ID**: 9622
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | option_code | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | opthold_type | 否 |  |  |
| 6 | open_frozen_amount | 否 |  |  |
| 7 | close_frozen_amount | 否 |  |  |
| 8 | exercise_frozen_amount | 否 |  |  |
| 9 | exercise_frozen_margin | 否 |  |  |
| 10 | comb_frozen_margin | 否 |  |  |
| 11 | frozen_premium | 否 |  |  |
| 12 | frozen_commission | 否 |  |  |
| 13 | uncome_put_amount | 否 |  |  |
| 14 | uncome_call_amount | 否 |  |  |
| 15 | uncome_used_pur_quota_sh | 否 |  |  |
| 16 | uncome_used_pur_quota_sz | 否 |  |  |
| 17 | order_no | 否 |  |  |
| 18 | margin_ratio | 否 |  |  |
| 19 | near_final_ratio_kind | 否 |  |  |
| 20 | option_code | 否 |  |  |
| 21 | exchange_type | 否 |  |  |
| 22 | fund_account | 否 |  |  |
| 23 | stock_account | 否 |  |  |
| 24 | opthold_type | 否 |  |  |
| 25 | open_frozen_amount | 否 |  |  |
| 26 | close_frozen_amount | 否 |  |  |
| 27 | exercise_frozen_amount | 否 |  |  |
| 28 | exercise_frozen_margin | 否 |  |  |
| 29 | comb_frozen_margin | 否 |  |  |
| 30 | frozen_premium | 否 |  |  |
| 31 | frozen_commission | 否 |  |  |
| 32 | uncome_put_amount | 否 |  |  |
| 33 | uncome_call_amount | 否 |  |  |
| 34 | uncome_used_pur_quota_sh | 否 |  |  |
| 35 | uncome_used_pur_quota_sz | 否 |  |  |
| 36 | order_no | 否 |  |  |
| 37 | margin_ratio | 否 |  |  |
| 38 | near_final_ratio_kind | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_entrust_sum | 默认 | 否 | option_code, opthold_type, option_code, opthold_type |
| idx_uopt_entrust_sum_global | 默认 | 是 | option_code, exchange_type, fund_account, opthold_type, option_code, exchange_type, fund_account, opthold_type |
| idx_uopt_entrust_sum_temp | 默认 | 是 | exchange_type, fund_account, stock_account, option_code, opthold_type, exchange_type, fund_account, stock_account, option_code, opthold_type |
| idx_uopt_entrust_sum | 默认 | 否 | option_code, opthold_type, option_code, opthold_type |
| idx_uopt_entrust_sum_global | 默认 | 是 | option_code, exchange_type, fund_account, opthold_type, option_code, exchange_type, fund_account, opthold_type |
| idx_uopt_entrust_sum_temp | 默认 | 是 | exchange_type, fund_account, stock_account, option_code, opthold_type, exchange_type, fund_account, stock_account, option_code, opthold_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_entrust_sum | exchange_type, fund_account, stock_account, option_code, opthold_type, exchange_type, fund_account, stock_account, option_code, opthold_type |
| idx_uopt_entrust_sum | exchange_type, fund_account, stock_account, option_code, opthold_type, exchange_type, fund_account, stock_account, option_code, opthold_type |

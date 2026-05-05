# setttouftcrdtlimitsell - 信用限售股份表

**表对象ID**: 3061
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 是 |  |  |
| 2 | exchange_type | 是 |  |  |
| 3 | stock_account | 是 |  |  |
| 4 | stock_code | 是 |  |  |
| 5 | client_id | 是 |  |  |
| 6 | fund_account | 是 |  |  |
| 7 | limitsell_type | 是 |  |  |
| 8 | limitsell_flag | 是 |  |  |
| 9 | limitsell_source | 是 |  |  |
| 10 | month_sell_amount | 是 |  |  |
| 11 | month_limit_ratio | 是 |  |  |
| 12 | total_sell_amount | 是 |  |  |
| 13 | total_limit_ratio | 是 |  |  |
| 14 | occur_times | 是 |  |  |
| 15 | create_date | 是 |  |  |
| 16 | remark | 是 |  |  |
| 17 | lift_date | 是 |  |  |
| 18 | branch_no | 是 |  |  |
| 19 | exchange_type | 是 |  |  |
| 20 | stock_account | 是 |  |  |
| 21 | stock_code | 是 |  |  |
| 22 | client_id | 是 |  |  |
| 23 | fund_account | 是 |  |  |
| 24 | limitsell_type | 是 |  |  |
| 25 | limitsell_flag | 是 |  |  |
| 26 | limitsell_source | 是 |  |  |
| 27 | month_sell_amount | 是 |  |  |
| 28 | month_limit_ratio | 是 |  |  |
| 29 | total_sell_amount | 是 |  |  |
| 30 | total_limit_ratio | 是 |  |  |
| 31 | occur_times | 是 |  |  |
| 32 | create_date | 是 |  |  |
| 33 | remark | 是 |  |  |
| 34 | lift_date | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdtlimitsell | 默认 | 是 | stock_account, exchange_type, stock_code, limitsell_type, client_id, limitsell_source, stock_account, exchange_type, stock_code, limitsell_type, client_id, limitsell_source |
| idx_crdtlimitsell | 默认 | 是 | stock_account, exchange_type, stock_code, limitsell_type, client_id, limitsell_source, stock_account, exchange_type, stock_code, limitsell_type, client_id, limitsell_source |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdtlimitsell | client_id, stock_code, exchange_type, limitsell_type, stock_account, limitsell_source, client_id, stock_code, exchange_type, limitsell_type, stock_account, limitsell_source |
| idx_crdtlimitsell_acct | fund_account, fund_account |
| idx_crdtlimitsell | client_id, stock_code, exchange_type, limitsell_type, stock_account, limitsell_source, client_id, stock_code, exchange_type, limitsell_type, stock_account, limitsell_source |
| idx_crdtlimitsell_acct | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2022-10-25 10:53 | 8.26.2.26 | 徐世晗 | 增加字段lift_date |
| 2021-12-22 14:40 | 8.26.2.16 | 徐世晗 | 唯一索引增加limitsell_source字段 |
| 2022-10-25 10:53 | 8.26.2.26 | 徐世晗 | 增加字段lift_date |
| 2021-12-22 14:40 | 8.26.2.16 | 徐世晗 | 唯一索引增加limitsell_source字段 |

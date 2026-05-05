# uopt_acct_holdlimit - 期权客户限仓参数表

**表对象ID**: 9607
**所属模块**: optsms
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | hedge_apply_mode | 否 |  |  |
| 2 | stock_type | 否 |  |  |
| 3 | begin_date | 否 |  |  |
| 4 | end_date | 否 |  |  |
| 5 | update_date | 否 |  |  |
| 6 | update_time | 否 |  |  |
| 7 | client_id | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | right_hold_quota | 否 |  |  |
| 12 | total_hold_quota | 否 |  |  |
| 13 | today_buy_quota | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | hedge_apply_mode | 否 |  |  |
| 16 | stock_type | 否 |  |  |
| 17 | begin_date | 否 |  |  |
| 18 | end_date | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | client_id | 否 |  |  |
| 22 | fund_account | 否 |  |  |
| 23 | exchange_type | 否 |  |  |
| 24 | stock_code | 否 |  |  |
| 25 | right_hold_quota | 否 |  |  |
| 26 | total_hold_quota | 否 |  |  |
| 27 | today_buy_quota | 否 |  |  |
| 28 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_acct_holdlimit | 默认 | 否 | exchange_type, stock_code, stock_type, exchange_type, stock_code, stock_type |
| idx_uopt_acct_holdlimit_temp | 默认 | 是 | fund_account, exchange_type, stock_code, stock_type, fund_account, exchange_type, stock_code, stock_type |
| idx_uopt_acct_holdlimit | 默认 | 否 | exchange_type, stock_code, stock_type, exchange_type, stock_code, stock_type |
| idx_uopt_acct_holdlimit_temp | 默认 | 是 | fund_account, exchange_type, stock_code, stock_type, fund_account, exchange_type, stock_code, stock_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_acct_holdlimit | stock_type, fund_account, exchange_type, stock_code, stock_type, fund_account, exchange_type, stock_code |
| idx_uopt_acct_holdlimit | stock_type, fund_account, exchange_type, stock_code, stock_type, fund_account, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-11 09:50:02 | V3.0.2.10 | 韦子晗 | 新增临时索引支持数据二次上场 |
| 2025-09-08 19:15:15 | V3.0.2.9 | 高志强 | 所有表uopt_acct_holdlimit，添加了表字段(transaction_no);
 |
| 2025-09-11 09:50:02 | V3.0.2.10 | 韦子晗 | 新增临时索引支持数据二次上场 |
| 2025-09-08 19:15:15 | V3.0.2.9 | 高志强 | 所有表uopt_acct_holdlimit，添加了表字段(transaction_no);
 |

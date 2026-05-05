# uopt_hold_limit - 期权限仓参数表

**表对象ID**: 9004
**所属模块**: optarg
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | right_hold_quota | 否 |  |  |
| 5 | total_hold_quota | 否 |  |  |
| 6 | today_buy_quota | 否 |  |  |
| 7 | optacct_type | 否 |  |  |
| 8 | model_name | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | remark | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | stock_type | 否 |  |  |
| 16 | right_hold_quota | 否 |  |  |
| 17 | total_hold_quota | 否 |  |  |
| 18 | today_buy_quota | 否 |  |  |
| 19 | optacct_type | 否 |  |  |
| 20 | model_name | 否 |  |  |
| 21 | update_date | 否 |  |  |
| 22 | update_time | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | remark | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_hold_limit | 默认 | 是 | exchange_type, stock_code, optacct_type, stock_type, exchange_type, stock_code, optacct_type, stock_type |
| idx_uopt_hold_limit | 默认 | 是 | exchange_type, stock_code, optacct_type, stock_type, exchange_type, stock_code, optacct_type, stock_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_hold_limit | exchange_type, stock_code, stock_type, optacct_type, exchange_type, stock_code, stock_type, optacct_type |
| idx_uopt_hold_limit | exchange_type, stock_code, stock_type, optacct_type, exchange_type, stock_code, stock_type, optacct_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-08 19:18:37 | V3.0.2.9 | 高志强 | 所有表uopt_hold_limit，添加了表字段(transaction_no);
 |
| 2024-12-09 16:01:54 | V3.0.3.11 | 韦子晗 | 去除idx_uopt_hold_limit_qry索引 |
| 2023-12-16 17:28:24 | 3.0.0.0 | wuxd |  |
| 2025-09-08 19:18:37 | V3.0.2.9 | 高志强 | 所有表uopt_hold_limit，添加了表字段(transaction_no);
 |
| 2024-12-09 16:01:54 | V3.0.3.11 | 韦子晗 | 去除idx_uopt_hold_limit_qry索引 |
| 2023-12-16 17:28:24 | 3.0.0.0 | wuxd |  |

# srp_fare2 - 股票质押费用表

**表对象ID**: 2620
**所属模块**: cbpsrp
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | fare_type | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_type | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | entrust_prop | 否 |  |  |
| 9 | entrust_bs | 否 |  |  |
| 10 | entrust_way | 否 |  |  |
| 11 | balance_ratio | 否 |  |  |
| 12 | par_ratio | 否 |  |  |
| 13 | min_fare | 否 |  |  |
| 14 | max_fare | 否 |  |  |
| 15 | modify_date | 否 |  |  |
| 16 | srp_kind | 否 |  |  |
| 17 | remark | 否 |  |  |
| 18 | transaction_no | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | position_str | 否 |  | fund_account(18)+srp_kind(1)+fare_type(1)+stock_type(4)+stoc |
| 22 | fund_account | 否 |  |  |
| 23 | client_id | 否 |  |  |
| 24 | branch_no | 否 |  |  |
| 25 | fare_type | 否 |  |  |
| 26 | exchange_type | 否 |  |  |
| 27 | stock_type | 否 |  |  |
| 28 | stock_code | 否 |  |  |
| 29 | entrust_prop | 否 |  |  |
| 30 | entrust_bs | 否 |  |  |
| 31 | entrust_way | 否 |  |  |
| 32 | balance_ratio | 否 |  |  |
| 33 | par_ratio | 否 |  |  |
| 34 | min_fare | 否 |  |  |
| 35 | max_fare | 否 |  |  |
| 36 | modify_date | 否 |  |  |
| 37 | srp_kind | 否 |  |  |
| 38 | remark | 否 |  |  |
| 39 | transaction_no | 否 |  |  |
| 40 | update_date | 否 |  |  |
| 41 | update_time | 否 |  |  |
| 42 | position_str | 否 |  | fund_account(18)+srp_kind(1)+fare_type(1)+stock_type(4)+stoc |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpfare2 | ART | 是 | fund_account, srp_kind, fare_type, stock_type, stock_code, entrust_prop, entrust_way, entrust_bs, exchange_type, fund_account, srp_kind, fare_type, stock_type, stock_code, entrust_prop, entrust_way, entrust_bs, exchange_type |
| idx_srpfare2 | ART | 是 | fund_account, srp_kind, fare_type, stock_type, stock_code, entrust_prop, entrust_way, entrust_bs, exchange_type, fund_account, srp_kind, fare_type, stock_type, stock_code, entrust_prop, entrust_way, entrust_bs, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpfare2 | fund_account, srp_kind, fare_type, stock_type, stock_code, entrust_prop, entrust_way, entrust_bs, exchange_type, fund_account, srp_kind, fare_type, stock_type, stock_code, entrust_prop, entrust_way, entrust_bs, exchange_type |
| idx_srpfare2 | fund_account, srp_kind, fare_type, stock_type, stock_code, entrust_prop, entrust_way, entrust_bs, exchange_type, fund_account, srp_kind, fare_type, stock_type, stock_code, entrust_prop, entrust_way, entrust_bs, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:52:29 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-02-14 10:59:24 | 3.0.3.2 |  | 物理表srp_fare2，添加了表字段(update_date);
物理表srp_fare2，添加了表字段(updat... |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:25:07 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:52:29 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-02-14 10:59:24 | 3.0.3.2 |  | 物理表srp_fare2，添加了表字段(update_date);
物理表srp_fare2，添加了表字段(updat... |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:25:07 | 3.0.3.1 | wuxd | 新增 |

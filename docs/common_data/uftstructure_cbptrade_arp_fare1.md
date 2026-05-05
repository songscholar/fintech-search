# arp_fare1 - 约定购回固定费用表

**表对象ID**: 2508
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fare_type | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | entrust_bs | 否 |  |  |
| 6 | money_type | 否 |  |  |
| 7 | balance_ratio | 否 |  |  |
| 8 | par_ratio | 否 |  |  |
| 9 | min_fare | 否 |  |  |
| 10 | max_fare | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | update_date | 否 |  |  |
| 13 | update_time | 否 |  |  |
| 14 | position_str | 否 |  | fare_type(1)+exchange_type(4)+stock_type(4)+entrust_bs(1)+st |
| 15 | fare_type | 否 |  |  |
| 16 | exchange_type | 否 |  |  |
| 17 | stock_type | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | entrust_bs | 否 |  |  |
| 20 | money_type | 否 |  |  |
| 21 | balance_ratio | 否 |  |  |
| 22 | par_ratio | 否 |  |  |
| 23 | min_fare | 否 |  |  |
| 24 | max_fare | 否 |  |  |
| 25 | transaction_no | 否 |  |  |
| 26 | update_date | 否 |  |  |
| 27 | update_time | 否 |  |  |
| 28 | position_str | 否 |  | fare_type(1)+exchange_type(4)+stock_type(4)+entrust_bs(1)+st |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arpfare1 | ART | 是 | fare_type, exchange_type, stock_type, entrust_bs, stock_code, fare_type, exchange_type, stock_type, entrust_bs, stock_code |
| idx_arpfare1 | ART | 是 | fare_type, exchange_type, stock_type, entrust_bs, stock_code, fare_type, exchange_type, stock_type, entrust_bs, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_arpfare1 | fare_type, exchange_type, stock_type, entrust_bs, stock_code, fare_type, exchange_type, stock_type, entrust_bs, stock_code |
| idx_arpfare1 | fare_type, exchange_type, stock_type, entrust_bs, stock_code, fare_type, exchange_type, stock_type, entrust_bs, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:49:55 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-14 11:03:36 | V3.0.5.1005 |  | 物理表arp_fare1，添加了表字段(update_date);
物理表arp_fare1，添加了表字段(updat... |
| 2026-03-04 15:49:55 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-14 11:03:36 | V3.0.5.1005 |  | 物理表arp_fare1，添加了表字段(update_date);
物理表arp_fare1，添加了表字段(updat... |

# arp_fare2 - 约定购回费用表

**表对象ID**: 2510
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | fare_type | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_type | 否 |  |  |
| 7 | entrust_bs | 否 |  |  |
| 8 | entrust_way | 否 |  |  |
| 9 | balance_ratio | 否 |  |  |
| 10 | par_ratio | 否 |  |  |
| 11 | min_fare | 否 |  |  |
| 12 | max_fare | 否 |  |  |
| 13 | modify_date | 否 |  |  |
| 14 | remark | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | position_str | 否 |  | fund_account(18)+branch_no(6)+fare_type(1)+stock_type(4)+ent |
| 19 | fund_account | 否 |  |  |
| 20 | client_id | 否 |  |  |
| 21 | branch_no | 否 |  |  |
| 22 | fare_type | 否 |  |  |
| 23 | exchange_type | 否 |  |  |
| 24 | stock_type | 否 |  |  |
| 25 | entrust_bs | 否 |  |  |
| 26 | entrust_way | 否 |  |  |
| 27 | balance_ratio | 否 |  |  |
| 28 | par_ratio | 否 |  |  |
| 29 | min_fare | 否 |  |  |
| 30 | max_fare | 否 |  |  |
| 31 | modify_date | 否 |  |  |
| 32 | remark | 否 |  |  |
| 33 | transaction_no | 否 |  |  |
| 34 | update_date | 否 |  |  |
| 35 | update_time | 否 |  |  |
| 36 | position_str | 否 |  | fund_account(18)+branch_no(6)+fare_type(1)+stock_type(4)+ent |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arpfare2 | ART | 是 | fund_account, branch_no, fare_type, stock_type, entrust_way, entrust_bs, exchange_type, fund_account, branch_no, fare_type, stock_type, entrust_way, entrust_bs, exchange_type |
| idx_arpfare2 | ART | 是 | fund_account, branch_no, fare_type, stock_type, entrust_way, entrust_bs, exchange_type, fund_account, branch_no, fare_type, stock_type, entrust_way, entrust_bs, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_arpfare2 | fund_account, branch_no, fare_type, stock_type, entrust_way, entrust_bs, exchange_type, fund_account, branch_no, fare_type, stock_type, entrust_way, entrust_bs, exchange_type |
| idx_arpfare2 | fund_account, branch_no, fare_type, stock_type, entrust_way, entrust_bs, exchange_type, fund_account, branch_no, fare_type, stock_type, entrust_way, entrust_bs, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:16:50 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-14 10:41:39 | V3.0.5.1004 |  | 物理表arp_fare2，添加了表字段(update_date);
物理表arp_fare2，添加了表字段(updat... |
| 2024-12-06 16:03:20 | V3.0.2.1009 | 黄积冲 | 新增表 |
| 2026-03-04 16:16:50 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-14 10:41:39 | V3.0.5.1004 |  | 物理表arp_fare2，添加了表字段(update_date);
物理表arp_fare2，添加了表字段(updat... |
| 2024-12-06 16:03:20 | V3.0.2.1009 | 黄积冲 | 新增表 |

# uft_surplus_stock - UFT余券信息表

**表对象ID**: 7568
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | cashgroup_no | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | branch_no | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_account | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | stock_type | 否 |  |  |
| 9 | money_type | 否 |  |  |
| 10 | begin_amount | 否 |  |  |
| 11 | current_amount | 否 |  |  |
| 12 | surplus_amount | 否 |  |  |
| 13 | correct_amount | 否 |  |  |
| 14 | order_no | 否 |  |  |
| 15 | position_str_long | 否 |  |  |
| 16 | cashgroup_no | 否 |  |  |
| 17 | fund_account | 否 |  |  |
| 18 | client_id | 否 |  |  |
| 19 | branch_no | 否 |  |  |
| 20 | exchange_type | 否 |  |  |
| 21 | stock_account | 否 |  |  |
| 22 | stock_code | 否 |  |  |
| 23 | stock_type | 否 |  |  |
| 24 | money_type | 否 |  |  |
| 25 | begin_amount | 否 |  |  |
| 26 | current_amount | 否 |  |  |
| 27 | surplus_amount | 否 |  |  |
| 28 | correct_amount | 否 |  |  |
| 29 | order_no | 否 |  |  |
| 30 | position_str_long | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uftsurstock | ART | 是 | position_str_long, position_str_long |
| idx_uftsurstock | ART | 是 | position_str_long, position_str_long |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uftsurstock | position_str_long, position_str_long |
| idx_uftsurstock | position_str_long, position_str_long |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-06-26 15:24:42 | 3.0.2.2006 | huangzh | 新增表 |
| 2025-06-26 15:24:42 | 3.0.2.2006 | huangzh | 新增表 |

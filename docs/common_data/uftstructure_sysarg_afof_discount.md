# afof_discount - 基金盘后业务折扣率表

**表对象ID**: 311
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | afofdiscount_kind | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | branch_no | 否 |  |  |
| 5 | entrust_way | 否 |  |  |
| 6 | business_flag | 否 |  |  |
| 7 | money_type | 否 |  |  |
| 8 | balance_step | 否 |  |  |
| 9 | discount | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | position_str | 否 |  | afofdiscount_kind(10)+exchange_type(4)+stock_code(8)+branch_ |
| 14 | afofdiscount_kind | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | entrust_way | 否 |  |  |
| 19 | business_flag | 否 |  |  |
| 20 | money_type | 否 |  |  |
| 21 | balance_step | 否 |  |  |
| 22 | discount | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | position_str | 否 |  | afofdiscount_kind(10)+exchange_type(4)+stock_code(8)+branch_ |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_afof_discount | 默认 | 否 | afofdiscount_kind, exchange_type, stock_code, branch_no, entrust_way, business_flag, balance_step, money_type, afofdiscount_kind, exchange_type, stock_code, branch_no, entrust_way, business_flag, balance_step, money_type |
| idx_afof_discount | ART | 是 | afofdiscount_kind, exchange_type, stock_code, branch_no, entrust_way, business_flag, balance_step, money_type, afofdiscount_kind, exchange_type, stock_code, branch_no, entrust_way, business_flag, balance_step, money_type |
| idx_afof_discount | 默认 | 否 | afofdiscount_kind, exchange_type, stock_code, branch_no, entrust_way, business_flag, balance_step, money_type, afofdiscount_kind, exchange_type, stock_code, branch_no, entrust_way, business_flag, balance_step, money_type |
| idx_afof_discount | ART | 是 | afofdiscount_kind, exchange_type, stock_code, branch_no, entrust_way, business_flag, balance_step, money_type, afofdiscount_kind, exchange_type, stock_code, branch_no, entrust_way, business_flag, balance_step, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_afof_discount | afofdiscount_kind, exchange_type, stock_code, branch_no, entrust_way, business_flag, balance_step, money_type, afofdiscount_kind, exchange_type, stock_code, branch_no, entrust_way, business_flag, balance_step, money_type |
| idx_afof_discount | afofdiscount_kind, exchange_type, stock_code, branch_no, entrust_way, business_flag, balance_step, money_type, afofdiscount_kind, exchange_type, stock_code, branch_no, entrust_way, business_flag, balance_step, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-14 16:22:01 | 3.0.6.37 | 李想 | 物理表afof_discount，添加了表字段(update_date);
物理表afof_discount，添加了表... |
| 2024-09-09 11:10:19 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2023-12-17 20:30:07 | 3.0.2.16 | 张训华 | 新增表，物理表增加索引 |
| 2025-02-14 16:22:01 | 3.0.6.37 | 李想 | 物理表afof_discount，添加了表字段(update_date);
物理表afof_discount，添加了表... |
| 2024-09-09 11:10:19 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2023-12-17 20:30:07 | 3.0.2.16 | 张训华 | 新增表，物理表增加索引 |

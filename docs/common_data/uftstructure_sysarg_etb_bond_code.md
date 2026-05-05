# etb_bond_code - 互联互通债券代码表

**表对象ID**: 130
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code_long | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | sub_stock_type | 否 |  |  |
| 5 | stock_name_bank | 否 |  |  |
| 6 | stock_name | 否 |  |  |
| 7 | par_value | 否 |  |  |
| 8 | issue_date | 否 |  |  |
| 9 | end_date | 否 |  |  |
| 10 | market_date | 否 |  |  |
| 11 | stock_status | 否 |  |  |
| 12 | store_unit | 否 |  |  |
| 13 | money_type | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | position_str | 否 |  | stock_code_long(32)+exchange_type(4) |
| 18 | exchange_type | 否 |  |  |
| 19 | stock_code_long | 否 |  |  |
| 20 | stock_type | 否 |  |  |
| 21 | sub_stock_type | 否 |  |  |
| 22 | stock_name_bank | 否 |  |  |
| 23 | stock_name | 否 |  |  |
| 24 | par_value | 否 |  |  |
| 25 | issue_date | 否 |  |  |
| 26 | end_date | 否 |  |  |
| 27 | market_date | 否 |  |  |
| 28 | stock_status | 否 |  |  |
| 29 | store_unit | 否 |  |  |
| 30 | money_type | 否 |  |  |
| 31 | update_date | 否 |  |  |
| 32 | update_time | 否 |  |  |
| 33 | transaction_no | 否 |  |  |
| 34 | position_str | 否 |  | stock_code_long(32)+exchange_type(4) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_etb_bond_code | 默认 | 否 |  |
| idx_etb_bond_code | ART | 是 | stock_code_long, exchange_type, stock_code_long, exchange_type |
| idx_etb_bond_code | 默认 | 否 |  |
| idx_etb_bond_code | ART | 是 | stock_code_long, exchange_type, stock_code_long, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_etb_bond_code | stock_code_long, exchange_type, stock_code_long, exchange_type |
| idx_etb_bond_code | stock_code_long, exchange_type, stock_code_long, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:39:22 | 3.0.2.103 | taocong45644 | 当前表etb_bond_code，修改了索引idx_etb_bond_code,索引字段修改为：(stock_code_... |
| 2025-02-18 17:39:44 | 3.0.6.74 | 李想 | 新增表 |
| 2025-12-01 14:39:22 | 3.0.2.103 | taocong45644 | 当前表etb_bond_code，修改了索引idx_etb_bond_code,索引字段修改为：(stock_code_... |
| 2025-02-18 17:39:44 | 3.0.6.74 | 李想 | 新增表 |

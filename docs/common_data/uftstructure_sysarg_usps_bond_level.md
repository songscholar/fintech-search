# usps_bond_level - 债券评级信息表

**表对象ID**: 88
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | bond_level | 否 |  |  |
| 6 | modify_date | 否 |  |  |
| 7 | implic_bond_level | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | position_str | 否 |  | exchange_type(4)+stock_code(8) |
| 12 | init_date | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | stock_type | 否 |  |  |
| 16 | bond_level | 否 |  |  |
| 17 | modify_date | 否 |  |  |
| 18 | implic_bond_level | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | position_str | 否 |  | exchange_type(4)+stock_code(8) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_bond_level | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_usps_bond_level | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_bond_level | exchange_type, stock_code, exchange_type, stock_code |
| idx_usps_bond_level | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-20 11:54:29 | 3.0.6.112 | 李想 | 物理表usps_bond_level，添加了表字段(update_date);
物理表usps_bond_level，... |
| 2025-02-06 16:30:01 | 3.0.2.53 | 周富安 | 物理表usps_bond_level，添加了表字段(init_date);
物理表usps_bond_level，添加... |
| 2023-11-13 14:32:11 | V3.0.1.16 | 沈勋 | 新增表，支持适当性交易匹配 |
| 2025-02-20 11:54:29 | 3.0.6.112 | 李想 | 物理表usps_bond_level，添加了表字段(update_date);
物理表usps_bond_level，... |
| 2025-02-06 16:30:01 | 3.0.2.53 | 周富安 | 物理表usps_bond_level，添加了表字段(init_date);
物理表usps_bond_level，添加... |
| 2023-11-13 14:32:11 | V3.0.1.16 | 沈勋 | 新增表，支持适当性交易匹配 |

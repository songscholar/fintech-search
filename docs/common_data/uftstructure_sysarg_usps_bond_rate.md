# usps_bond_rate - 抵押比率表

**表对象ID**: 40
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | bond_rate | 否 |  |  |
| 4 | bond_code | 否 |  |  |
| 5 | impawn_rate | 否 |  |  |
| 6 | impawn_code | 否 |  |  |
| 7 | qrp_impawn_rate | 否 |  |  |
| 8 | issue_main | 否 |  |  |
| 9 | en_impindb_flag | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | position_str | 否 |  | exchange_type(4)+stock_code(8) |
| 14 | last_impawn_rate | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | bond_rate | 否 |  |  |
| 18 | bond_code | 否 |  |  |
| 19 | impawn_rate | 否 |  |  |
| 20 | impawn_code | 否 |  |  |
| 21 | qrp_impawn_rate | 否 |  |  |
| 22 | issue_main | 否 |  |  |
| 23 | en_impindb_flag | 否 |  |  |
| 24 | transaction_no | 否 |  |  |
| 25 | update_date | 否 |  |  |
| 26 | update_time | 否 |  |  |
| 27 | position_str | 否 |  | exchange_type(4)+stock_code(8) |
| 28 | last_impawn_rate | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_bond_rate | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_usps_bond_rate | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_bond_rate | exchange_type, stock_code, exchange_type, stock_code |
| idx_usps_bond_rate | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 16:39:07 | 3.0.2.2007 | 谢宗艺 | 所有表usps_bond_rate，添加了表字段(last_impawn_rate);
 |
| 2025-02-18 17:02:44 | 3.0.6.67 | 李想 | 物理表usps_bond_rate，添加了表字段(update_date);
物理表usps_bond_rate，添加... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2026-03-09 16:39:07 | 3.0.2.2007 | 谢宗艺 | 所有表usps_bond_rate，添加了表字段(last_impawn_rate);
 |
| 2025-02-18 17:02:44 | 3.0.6.67 | 李想 | 物理表usps_bond_rate，添加了表字段(update_date);
物理表usps_bond_rate，添加... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

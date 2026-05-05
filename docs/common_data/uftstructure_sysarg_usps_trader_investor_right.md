# usps_trader_investor_right - 债券交易员权限表

**表对象ID**: 81
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | trader_id | 否 |  |  |
| 2 | bond_investor_id | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | update_date | 否 |  |  |
| 6 | update_time | 否 |  |  |
| 7 | position_str | 否 |  | trader_id(20)+bond_investor_id(32)+exchange_type(4) |
| 8 | trader_id | 否 |  |  |
| 9 | bond_investor_id | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | update_date | 否 |  |  |
| 13 | update_time | 否 |  |  |
| 14 | position_str | 否 |  | trader_id(20)+bond_investor_id(32)+exchange_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_trader_investor_right | ART | 是 | trader_id, bond_investor_id, exchange_type, trader_id, bond_investor_id, exchange_type |
| idx_usps_trader_investor_right | ART | 是 | trader_id, bond_investor_id, exchange_type, trader_id, bond_investor_id, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_trader_investor_right | trader_id, bond_investor_id, exchange_type, trader_id, bond_investor_id, exchange_type |
| idx_usps_trader_investor_right | trader_id, bond_investor_id, exchange_type, trader_id, bond_investor_id, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-19 16:36:34 | 3.0.6.103 | 李想 | 物理表usps_trader_investor_right，添加了表字段(update_date);
物理表usps_... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-07-19 18:21 | 0.0.0.14 | 徐世晗 | 新增 |
| 2025-02-19 16:36:34 | 3.0.6.103 | 李想 | 物理表usps_trader_investor_right，添加了表字段(update_date);
物理表usps_... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-07-19 18:21 | 0.0.0.14 | 徐世晗 | 新增 |

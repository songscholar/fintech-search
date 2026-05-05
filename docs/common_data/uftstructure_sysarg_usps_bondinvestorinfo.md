# usps_bondinvestorinfo - 债券交易主体信息表

**表对象ID**: 79
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | agency_no | 否 |  |  |
| 2 | bond_investor_id | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | bond_investor_type | 否 |  |  |
| 5 | bond_investor_name | 否 |  |  |
| 6 | bond_investor_name_short | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | position_str | 否 |  | agency_no(10)+exchange_type(4)+bond_investor_id(32) |
| 11 | agency_no | 否 |  |  |
| 12 | bond_investor_id | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | bond_investor_type | 否 |  |  |
| 15 | bond_investor_name | 否 |  |  |
| 16 | bond_investor_name_short | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | position_str | 否 |  | agency_no(10)+exchange_type(4)+bond_investor_id(32) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_bondinvestorinfo | ART | 是 | agency_no, exchange_type, bond_investor_id, agency_no, exchange_type, bond_investor_id |
| idx_bondinvestorinfo | ART | 是 | agency_no, exchange_type, bond_investor_id, agency_no, exchange_type, bond_investor_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_bondinvestorinfo | agency_no, exchange_type, bond_investor_id, agency_no, exchange_type, bond_investor_id |
| idx_bondinvestorinfo | agency_no, exchange_type, bond_investor_id, agency_no, exchange_type, bond_investor_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-19 16:32:22 | 3.0.6.102 | 李想 | 物理表usps_bondinvestorinfo，添加了表字段(update_date);
物理表usps_bondi... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-07-12 17:29 | 0.3.3.13 | 徐世晗 | 新增 |
| 2025-02-19 16:32:22 | 3.0.6.102 | 李想 | 物理表usps_bondinvestorinfo，添加了表字段(update_date);
物理表usps_bondi... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-07-12 17:29 | 0.3.3.13 | 徐世晗 | 新增 |

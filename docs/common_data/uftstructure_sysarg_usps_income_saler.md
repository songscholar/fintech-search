# usps_income_saler - 交易员代码表

**表对象ID**: 78
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | agency_no | 否 |  |  |
| 2 | trader_id | 否 |  |  |
| 3 | trader_name | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | default_trader_flag | 否 |  |  |
| 6 | orig_trader_id | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | position_str | 否 |  | trader_id(20)+exchange_type(4)+agency_no(10) |
| 11 | agency_no | 否 |  |  |
| 12 | trader_id | 否 |  |  |
| 13 | trader_name | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | default_trader_flag | 否 |  |  |
| 16 | orig_trader_id | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | position_str | 否 |  | trader_id(20)+exchange_type(4)+agency_no(10) |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_income_saler_trader | 默认 | 否 | agency_no, exchange_type, default_trader_flag, trader_id, agency_no, exchange_type, default_trader_flag, trader_id |
| idx_usps_income_saler | ART | 是 | trader_id, exchange_type, agency_no, trader_id, exchange_type, agency_no |
| idx_usps_income_saler_trader | ART | 是 | agency_no, exchange_type, default_trader_flag, trader_id, agency_no, exchange_type, default_trader_flag, trader_id |
| idx_usps_income_saler_trader | 默认 | 否 | agency_no, exchange_type, default_trader_flag, trader_id, agency_no, exchange_type, default_trader_flag, trader_id |
| idx_usps_income_saler | ART | 是 | trader_id, exchange_type, agency_no, trader_id, exchange_type, agency_no |
| idx_usps_income_saler_trader | ART | 是 | agency_no, exchange_type, default_trader_flag, trader_id, agency_no, exchange_type, default_trader_flag, trader_id |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_income_saler | trader_id, exchange_type, agency_no, trader_id, exchange_type, agency_no |
| idx_usps_income_saler_trader | agency_no, exchange_type, default_trader_flag, trader_id, agency_no, exchange_type, default_trader_flag, trader_id |
| idx_usps_income_saler | trader_id, exchange_type, agency_no, trader_id, exchange_type, agency_no |
| idx_usps_income_saler_trader | agency_no, exchange_type, default_trader_flag, trader_id, agency_no, exchange_type, default_trader_flag, trader_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-17 14:01:55 | 3.0.6.1016 | 常行 | 物理表usps_income_saler，增加索引(idx_usps_income_saler_trader:[agen... |
| 2025-03-22 18:20:30 | 3.0.2.2001 | 高志强 | 物理表usps_income_saler，添加了表字段(orig_trader_id);
 |
| 2025-02-15 09:33:08 | 3.0.2.55 | 洪略 | 新增orig_trader_id字段 |
| 2025-02-19 16:24:24 | 3.0.6.101 | 李想 | 物理表usps_income_saler，添加了表字段(update_date);
物理表usps_income_sa... |
| 2025-02-15 09:33:08 | 3.0.2.55 | 洪略 | 新增orig_trader_id字段 |
| 2024-09-25 15:55:34 | 3.0.2.29 | 骆鹏程 | trader_name长度从120扩展到180 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-07-12 17:29 | 0.3.3.13 | 徐世晗 | 新增 |
| 2025-07-17 14:01:55 | 3.0.6.1016 | 常行 | 物理表usps_income_saler，增加索引(idx_usps_income_saler_trader:[agen... |
| 2025-03-22 18:20:30 | 3.0.2.2001 | 高志强 | 物理表usps_income_saler，添加了表字段(orig_trader_id);
 |
| 2025-02-15 09:33:08 | 3.0.2.55 | 洪略 | 新增orig_trader_id字段 |
| 2025-02-19 16:24:24 | 3.0.6.101 | 李想 | 物理表usps_income_saler，添加了表字段(update_date);
物理表usps_income_sa... |
| 2025-02-15 09:33:08 | 3.0.2.55 | 洪略 | 新增orig_trader_id字段 |
| 2024-09-25 15:55:34 | 3.0.2.29 | 骆鹏程 | trader_name长度从120扩展到180 |

> 共 18 条修改记录，仅显示最近15条

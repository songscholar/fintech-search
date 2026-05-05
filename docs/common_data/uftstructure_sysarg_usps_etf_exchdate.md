# usps_etf_exchdate - ETF阶段控制日期表

**表对象ID**: 67
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | stage_kind | 否 |  |  |
| 4 | begin_date | 否 |  |  |
| 5 | end_date | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | update_date | 否 |  |  |
| 8 | update_time | 否 |  |  |
| 9 | position_str | 否 |  | exchange_type(4)+stock_code(8)+stage_kind(1) |
| 10 | exchange_type | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | stage_kind | 否 |  |  |
| 13 | begin_date | 否 |  |  |
| 14 | end_date | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | position_str | 否 |  | exchange_type(4)+stock_code(8)+stage_kind(1) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_etf_exchdate | ART | 是 | exchange_type, stock_code, stage_kind, exchange_type, stock_code, stage_kind |
| idx_usps_etf_exchdate | ART | 是 | exchange_type, stock_code, stage_kind, exchange_type, stock_code, stage_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_etf_exchdate | exchange_type, stock_code, stage_kind, exchange_type, stock_code, stage_kind |
| idx_usps_etf_exchdate | exchange_type, stock_code, stage_kind, exchange_type, stock_code, stage_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-19 17:02:06 | 3.0.6.107 | 李想 | 物理表usps_etf_exchdate，添加了表字段(update_date);
物理表usps_etf_exchd... |
| 2023-08-23 18:39:36 | 0.3.3.142 | 徐志坚 | 增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-02-19 17:02:06 | 3.0.6.107 | 李想 | 物理表usps_etf_exchdate，添加了表字段(update_date);
物理表usps_etf_exchd... |
| 2023-08-23 18:39:36 | 0.3.3.142 | 徐志坚 | 增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

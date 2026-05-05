# usps_witcode - 国债预发行代码表

**表对象ID**: 42
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | source_code | 否 |  |  |
| 4 | wit_type | 否 |  |  |
| 5 | ref_duration | 否 |  |  |
| 6 | bail_ratio | 否 |  |  |
| 7 | frozen_ratio | 否 |  |  |
| 8 | curr_issue_amount | 否 |  |  |
| 9 | final_trade_date | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 14 | exchange_type | 否 |  |  |
| 15 | stock_code | 否 |  |  |
| 16 | source_code | 否 |  |  |
| 17 | wit_type | 否 |  |  |
| 18 | ref_duration | 否 |  |  |
| 19 | bail_ratio | 否 |  |  |
| 20 | frozen_ratio | 否 |  |  |
| 21 | curr_issue_amount | 否 |  |  |
| 22 | final_trade_date | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | position_str | 否 |  | stock_code(8)+exchange_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_witcode | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_usps_witcode | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_witcode | stock_code, exchange_type, stock_code, exchange_type |
| idx_usps_witcode | stock_code, exchange_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 17:06:45 | 3.0.6.69 | 李想 | 物理表usps_witcode，添加了表字段(update_date);
物理表usps_witcode，添加了表字段... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-02-18 17:06:45 | 3.0.6.69 | 李想 | 物理表usps_witcode，添加了表字段(update_date);
物理表usps_witcode，添加了表字段... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

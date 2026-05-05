# usps_warrant_code - 权证代码表

**表对象ID**: 37
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | warrant_code | 否 |  |  |
| 3 | warrant_type | 否 |  |  |
| 4 | apply_code | 否 |  |  |
| 5 | source_code | 否 |  |  |
| 6 | apply_rate | 否 |  |  |
| 7 | apply_style | 否 |  |  |
| 8 | apply_price | 否 |  |  |
| 9 | settle_style | 否 |  |  |
| 10 | encash_price | 否 |  |  |
| 11 | apply_begin_date | 否 |  |  |
| 12 | apply_end_date | 否 |  |  |
| 13 | warrant_begin_date | 否 |  |  |
| 14 | warrant_end_date | 否 |  |  |
| 15 | apply_unit | 否 |  |  |
| 16 | apply_high_amount | 否 |  |  |
| 17 | use_price_limit | 否 |  |  |
| 18 | base_rate | 否 |  |  |
| 19 | total_amount | 否 |  |  |
| 20 | remain_amount | 否 |  |  |
| 21 | overflow_rate | 否 |  |  |
| 22 | apply_status | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | update_date | 否 |  | 20240223 xuzj add |
| 25 | update_time | 否 |  |  |
| 26 | warrant_name | 否 |  |  |
| 27 | position_str | 否 |  | exchange_type(4)+warrant_code(8) |
| 28 | exchange_type | 否 |  |  |
| 29 | warrant_code | 否 |  |  |
| 30 | warrant_type | 否 |  |  |
| 31 | apply_code | 否 |  |  |
| 32 | source_code | 否 |  |  |
| 33 | apply_rate | 否 |  |  |
| 34 | apply_style | 否 |  |  |
| 35 | apply_price | 否 |  |  |
| 36 | settle_style | 否 |  |  |
| 37 | encash_price | 否 |  |  |
| 38 | apply_begin_date | 否 |  |  |
| 39 | apply_end_date | 否 |  |  |
| 40 | warrant_begin_date | 否 |  |  |
| 41 | warrant_end_date | 否 |  |  |
| 42 | apply_unit | 否 |  |  |
| 43 | apply_high_amount | 否 |  |  |
| 44 | use_price_limit | 否 |  |  |
| 45 | base_rate | 否 |  |  |
| 46 | total_amount | 否 |  |  |
| 47 | remain_amount | 否 |  |  |
| 48 | overflow_rate | 否 |  |  |
| 49 | apply_status | 否 |  |  |
| 50 | transaction_no | 否 |  |  |
| 51 | update_date | 否 |  | 20240223 xuzj add |
| 52 | update_time | 否 |  |  |
| 53 | warrant_name | 否 |  |  |
| 54 | position_str | 否 |  | exchange_type(4)+warrant_code(8) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_warrant_code | ART | 是 | exchange_type, warrant_code, exchange_type, warrant_code |
| idx_warrant_code_apply | ART | 是 | exchange_type, apply_code, exchange_type, apply_code |
| idx_warrant_code | ART | 是 | exchange_type, warrant_code, exchange_type, warrant_code |
| idx_warrant_code_apply | ART | 是 | exchange_type, apply_code, exchange_type, apply_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_warrant_code | exchange_type, warrant_code, exchange_type, warrant_code |
| idx_warrant_code | exchange_type, warrant_code, exchange_type, warrant_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 18:34:53 | 3.0.6.78 | 李想 | 物理表usps_warrant_code，添加了表字段(warrant_name);
物理表usps_warrant_... |
| 2024-02-23 15:15:07 | 3.0.2.3 | 徐志坚 | 支持行情转入，增加update_date字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-02-18 18:34:53 | 3.0.6.78 | 李想 | 物理表usps_warrant_code，添加了表字段(warrant_name);
物理表usps_warrant_... |
| 2024-02-23 15:15:07 | 3.0.2.3 | 徐志坚 | 支持行情转入，增加update_date字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

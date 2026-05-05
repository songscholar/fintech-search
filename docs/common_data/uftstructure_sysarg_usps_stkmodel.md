# usps_stkmodel - 证券模板表

**表对象ID**: 41
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_type_ass | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | model_code | 否 |  |  |
| 5 | count_direction | 否 |  |  |
| 6 | start_postion | 否 |  |  |
| 7 | name_prefix | 否 |  |  |
| 8 | relative_model | 否 |  |  |
| 9 | modifiable | 否 |  |  |
| 10 | sub_stock_type | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | prefix | 否 |  |  |
| 13 | use_date | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | position_str | 否 |  | exchange_type(4)+stock_type_ass(1)+stock_type(4)+model_code( |
| 17 | exchange_type | 否 |  |  |
| 18 | stock_type_ass | 否 |  |  |
| 19 | stock_type | 否 |  |  |
| 20 | model_code | 否 |  |  |
| 21 | count_direction | 否 |  |  |
| 22 | start_postion | 否 |  |  |
| 23 | name_prefix | 否 |  |  |
| 24 | relative_model | 否 |  |  |
| 25 | modifiable | 否 |  |  |
| 26 | sub_stock_type | 否 |  |  |
| 27 | transaction_no | 否 |  |  |
| 28 | prefix | 否 |  |  |
| 29 | use_date | 否 |  |  |
| 30 | update_date | 否 |  |  |
| 31 | update_time | 否 |  |  |
| 32 | position_str | 否 |  | exchange_type(4)+stock_type_ass(1)+stock_type(4)+model_code( |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_stkmodel | ART | 是 | exchange_type, stock_type_ass, stock_type, model_code, name_prefix, exchange_type, stock_type_ass, stock_type, model_code, name_prefix |
| idx_usps_stkmodel_hq | ART | 是 | model_code, name_prefix, model_code, name_prefix |
| idx_usps_stkmodel | ART | 是 | exchange_type, stock_type_ass, stock_type, model_code, name_prefix, exchange_type, stock_type_ass, stock_type, model_code, name_prefix |
| idx_usps_stkmodel_hq | ART | 是 | model_code, name_prefix, model_code, name_prefix |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_stkmodel | exchange_type, stock_type_ass, stock_type, model_code, name_prefix, exchange_type, stock_type_ass, stock_type, model_code, name_prefix |
| idx_usps_stkmodel | exchange_type, stock_type_ass, stock_type, model_code, name_prefix, exchange_type, stock_type_ass, stock_type, model_code, name_prefix |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-14 16:58:16 | 3.0.6.12 | 常行 | 物理表usps_stkmodel，添加了表字段(prefix);
物理表usps_stkmodel，添加了表字段(us... |
| 2023-09-09 14:13:22 | V3.0.1.3 | 徐志坚 | 为了便于行情服务器处理，增加索引idx_usps_stkmodel_hq |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-02-14 16:58:16 | 3.0.6.12 | 常行 | 物理表usps_stkmodel，添加了表字段(prefix);
物理表usps_stkmodel，添加了表字段(us... |
| 2023-09-09 14:13:22 | V3.0.1.3 | 徐志坚 | 为了便于行情服务器处理，增加索引idx_usps_stkmodel_hq |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

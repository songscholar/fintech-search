# afof_quota - 基金盘后业务限额控制表

**表对象ID**: 309
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | client_group | 否 |  |  |
| 5 | room_code | 否 |  |  |
| 6 | business_flag | 否 |  |  |
| 7 | entrust_way | 否 |  |  |
| 8 | up_limited | 否 |  |  |
| 9 | current_amount | 否 |  |  |
| 10 | one_up_limited | 否 |  |  |
| 11 | date_up_limited | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | update_date | 否 |  |  |
| 14 | update_time | 否 |  |  |
| 15 | position_str | 否 |  | exchange_type(4)+stock_code(8)+branch_no(6)+client_group(4)+ |
| 16 | exchange_type | 否 |  |  |
| 17 | stock_code | 否 |  |  |
| 18 | branch_no | 否 |  |  |
| 19 | client_group | 否 |  |  |
| 20 | room_code | 否 |  |  |
| 21 | business_flag | 否 |  |  |
| 22 | entrust_way | 否 |  |  |
| 23 | up_limited | 否 |  |  |
| 24 | current_amount | 否 |  |  |
| 25 | one_up_limited | 否 |  |  |
| 26 | date_up_limited | 否 |  |  |
| 27 | transaction_no | 否 |  |  |
| 28 | update_date | 否 |  |  |
| 29 | update_time | 否 |  |  |
| 30 | position_str | 否 |  | exchange_type(4)+stock_code(8)+branch_no(6)+client_group(4)+ |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_afof_quota | 默认 | 否 | exchange_type, stock_code, branch_no, client_group, room_code, business_flag, entrust_way, exchange_type, stock_code, branch_no, client_group, room_code, business_flag, entrust_way |
| idx_afof_quota | ART | 是 | exchange_type, stock_code, branch_no, client_group, room_code, business_flag, entrust_way, exchange_type, stock_code, branch_no, client_group, room_code, business_flag, entrust_way |
| idx_afof_quota | 默认 | 否 | exchange_type, stock_code, branch_no, client_group, room_code, business_flag, entrust_way, exchange_type, stock_code, branch_no, client_group, room_code, business_flag, entrust_way |
| idx_afof_quota | ART | 是 | exchange_type, stock_code, branch_no, client_group, room_code, business_flag, entrust_way, exchange_type, stock_code, branch_no, client_group, room_code, business_flag, entrust_way |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_afof_quota | exchange_type, stock_code, branch_no, client_group, room_code, business_flag, entrust_way, exchange_type, stock_code, branch_no, client_group, room_code, business_flag, entrust_way |
| idx_afof_quota | exchange_type, stock_code, branch_no, client_group, room_code, business_flag, entrust_way, exchange_type, stock_code, branch_no, client_group, room_code, business_flag, entrust_way |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-19 16:59:54 | 3.0.6.106 | 李想 | 物理表afof_quota，添加了表字段(update_date);
物理表afof_quota，添加了表字段(upd... |
| 2024-09-09 11:09:01 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2023-12-17 20:30:07 | 3.0.2.16 | 张训华 | 新增表物理表增加索引 |
| 2025-02-19 16:59:54 | 3.0.6.106 | 李想 | 物理表afof_quota，添加了表字段(update_date);
物理表afof_quota，添加了表字段(upd... |
| 2024-09-09 11:09:01 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2023-12-17 20:30:07 | 3.0.2.16 | 张训华 | 新增表物理表增加索引 |

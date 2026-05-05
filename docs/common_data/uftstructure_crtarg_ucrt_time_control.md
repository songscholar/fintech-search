# ucrt_time_control - 融资融券交易时间控制表

**表对象ID**: 7002
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | time_kind | 否 |  |  |
| 3 | time_name | 否 |  |  |
| 4 | begin_time | 否 |  |  |
| 5 | end_time | 否 |  |  |
| 6 | entrust_type | 否 |  |  |
| 7 | entrust_bs | 否 |  |  |
| 8 | en_stock_type | 否 |  |  |
| 9 | stkres_code | 否 |  |  |
| 10 | stkres_amount | 否 |  |  |
| 11 | cash_enable_balance | 否 |  |  |
| 12 | control_flag | 否 |  |  |
| 13 | time_order | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | duration | 否 |  |  |
| 16 | withdraw | 否 |  |  |
| 17 | update_date | 否 |  |  |
| 18 | update_time | 否 |  |  |
| 19 | position_str | 否 |  | stkres_code(8)+time_kind(1)+exchange_type(4)+entrust_type(1) |
| 20 | exchange_type | 否 |  |  |
| 21 | time_kind | 否 |  |  |
| 22 | time_name | 否 |  |  |
| 23 | begin_time | 否 |  |  |
| 24 | end_time | 否 |  |  |
| 25 | entrust_type | 否 |  |  |
| 26 | entrust_bs | 否 |  |  |
| 27 | en_stock_type | 否 |  |  |
| 28 | stkres_code | 否 |  |  |
| 29 | stkres_amount | 否 |  |  |
| 30 | cash_enable_balance | 否 |  |  |
| 31 | control_flag | 否 |  |  |
| 32 | time_order | 否 |  |  |
| 33 | transaction_no | 否 |  |  |
| 34 | duration | 否 |  |  |
| 35 | withdraw | 否 |  |  |
| 36 | update_date | 否 |  |  |
| 37 | update_time | 否 |  |  |
| 38 | position_str | 否 |  | stkres_code(8)+time_kind(1)+exchange_type(4)+entrust_type(1) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_time_control | ART | 是 | stkres_code, time_kind, exchange_type, entrust_type, entrust_bs, time_order, stkres_code, time_kind, exchange_type, entrust_type, entrust_bs, time_order |
| idx_ucrt_time_control | ART | 是 | stkres_code, time_kind, exchange_type, entrust_type, entrust_bs, time_order, stkres_code, time_kind, exchange_type, entrust_type, entrust_bs, time_order |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_time_control | stkres_code, time_kind, exchange_type, entrust_type, entrust_bs, time_order, stkres_code, time_kind, exchange_type, entrust_type, entrust_bs, time_order |
| idx_ucrt_time_control | stkres_code, time_kind, exchange_type, entrust_type, entrust_bs, time_order, stkres_code, time_kind, exchange_type, entrust_type, entrust_bs, time_order |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-17 15:23:02 | 3.0.6.42 | 李想 | 物理表ucrt_time_control，添加了表字段(duration);
物理表ucrt_time_control... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:22 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no |
| 2025-02-17 15:23:02 | 3.0.6.42 | 李想 | 物理表ucrt_time_control，添加了表字段(duration);
物理表ucrt_time_control... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:22 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no |

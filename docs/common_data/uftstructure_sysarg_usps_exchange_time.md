# usps_exchange_time - 交易时间表

**表对象ID**: 9
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | begin_time | 否 |  |  |
| 2 | en_entrust_prop | 否 |  |  |
| 3 | en_stock_type | 否 |  |  |
| 4 | en_sub_stock_type | 否 |  |  |
| 5 | end_time | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | res_entrust_prop | 否 |  |  |
| 8 | res_sub_stock_type | 否 |  |  |
| 9 | time_kind | 否 |  |  |
| 10 | time_order | 否 |  |  |
| 11 | withdraw | 否 |  |  |
| 12 | res_stock_type | 否 |  |  |
| 13 | withdraw_entrust_prop | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | duration | 否 |  |  |
| 16 | time_name | 否 |  |  |
| 17 | update_date | 否 |  |  |
| 18 | update_time | 否 |  |  |
| 19 | position_str | 否 |  | time_kind(1)+time_order(10)+exchange_type(4) |
| 20 | begin_time | 否 |  |  |
| 21 | en_entrust_prop | 否 |  |  |
| 22 | en_stock_type | 否 |  |  |
| 23 | en_sub_stock_type | 否 |  |  |
| 24 | end_time | 否 |  |  |
| 25 | exchange_type | 否 |  |  |
| 26 | res_entrust_prop | 否 |  |  |
| 27 | res_sub_stock_type | 否 |  |  |
| 28 | time_kind | 否 |  |  |
| 29 | time_order | 否 |  |  |
| 30 | withdraw | 否 |  |  |
| 31 | res_stock_type | 否 |  |  |
| 32 | withdraw_entrust_prop | 否 |  |  |
| 33 | transaction_no | 否 |  |  |
| 34 | duration | 否 |  |  |
| 35 | time_name | 否 |  |  |
| 36 | update_date | 否 |  |  |
| 37 | update_time | 否 |  |  |
| 38 | position_str | 否 |  | time_kind(1)+time_order(10)+exchange_type(4) |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_exchange_time | 默认 | 否 | time_kind, time_order, exchange_type, time_kind, time_order, exchange_type |
| idx_upbs_exchange_time | 默认 | 否 |  |
| idx_usps_exchange_time | ART | 是 | exchange_type, time_kind, time_order, exchange_type, time_kind, time_order |
| idx_usps_exchange_time_kind | ART | 是 | time_kind, time_kind |
| idx_usps_exchange_time | 默认 | 否 | time_kind, time_order, exchange_type, time_kind, time_order, exchange_type |
| idx_upbs_exchange_time | 默认 | 否 |  |
| idx_usps_exchange_time | ART | 是 | exchange_type, time_kind, time_order, exchange_type, time_kind, time_order |
| idx_usps_exchange_time_kind | ART | 是 | time_kind, time_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_exchange_time | time_kind, time_order, exchange_type, time_kind, time_order, exchange_type |
| idx_usps_exchange_time | time_kind, time_order, exchange_type, time_kind, time_order, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-19 13:44:35 | 3.0.6.85 | 李想 | 物理表usps_exchange_time，添加了表字段(duration);
物理表usps_exchange_ti... |
| 2023-09-18 09:38:35 | V3.0.1.6 | 吴威 | 物理表usps_exchange_time，增加索引(idx_usps_exchange_time:[time_kind... |
| 2023-09-18 09:36:57 | V3.0.1.6 | 吴威 | 物理表usps_exchange_time，删除了表索引(idx_upbs_exchange_time);
 |
| 2023-08-16 20:58 | 0.3.3.137 | 徐世晗 | 根据内存表索引增加物理表索引 |
| 2023-06-14 21:16 | 0.0.0.9 | 吴威 | 新增transaction_no |
| 2021-07-23 15:11 | 0.0.0.1 | 毛潇俊 | 新增withdraw_entrust_prop字段 |
| 2019-02-15 11:12 | 0.0.0.1 |  | 新增res_sub_stock_type，en_sub_stock_type字段 |
| 2018-08-15 15:51 | 0.0.0.1 | 赵昌奎 | 增加res_entrust_prop字段 |
| 2014-12-29 14:17 | 0.0.0.1 |  |  |
| 2025-02-19 13:44:35 | 3.0.6.85 | 李想 | 物理表usps_exchange_time，添加了表字段(duration);
物理表usps_exchange_ti... |
| 2023-09-18 09:38:35 | V3.0.1.6 | 吴威 | 物理表usps_exchange_time，增加索引(idx_usps_exchange_time:[time_kind... |
| 2023-09-18 09:36:57 | V3.0.1.6 | 吴威 | 物理表usps_exchange_time，删除了表索引(idx_upbs_exchange_time);
 |
| 2023-08-16 20:58 | 0.3.3.137 | 徐世晗 | 根据内存表索引增加物理表索引 |
| 2023-06-14 21:16 | 0.0.0.9 | 吴威 | 新增transaction_no |
| 2021-07-23 15:11 | 0.0.0.1 | 毛潇俊 | 新增withdraw_entrust_prop字段 |

> 共 18 条修改记录，仅显示最近15条

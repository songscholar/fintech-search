# pledge_stkinfo - 质押回购代码出入库标志信息表

**表对象ID**: 312
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | en_pledgein_flag | 否 |  |  |
| 4 | en_pledgeout_flag | 否 |  |  |
| 5 | maintenan_flag | 否 |  |  |
| 6 | exch_pledgein_flag | 否 |  |  |
| 7 | exch_pledgeout_flag | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | position_str | 否 |  | exchange_type(4)+stock_code(8) |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | en_pledgein_flag | 否 |  |  |
| 15 | en_pledgeout_flag | 否 |  |  |
| 16 | maintenan_flag | 否 |  |  |
| 17 | exch_pledgein_flag | 否 |  |  |
| 18 | exch_pledgeout_flag | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | position_str | 否 |  | exchange_type(4)+stock_code(8) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_pledgestkinfo | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_pledgestkinfo | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_pledgestkinfo | exchange_type, stock_code, exchange_type, stock_code |
| idx_pledgestkinfo | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-20 14:08:53 | 3.0.6.115 | 李想 | 物理表pledge_stkinfo，添加了表字段(update_date);
物理表pledge_stkinfo，添加... |
| 2025-03-24 13:25:23 | 3.0.2.80 | 彭雪锋 | 调整表空间为HS_UFT_DATA |
| 2024-07-15 21:33:42 | 3.0.2.23 | 阮善宏 | 将表结构挪至公共参数下 |
| 2024-06-28 15:16:54 | 3.0.2.22 | 张云焘 | 新增 |
| 2025-02-20 14:08:53 | 3.0.6.115 | 李想 | 物理表pledge_stkinfo，添加了表字段(update_date);
物理表pledge_stkinfo，添加... |
| 2025-03-24 13:25:23 | 3.0.2.80 | 彭雪锋 | 调整表空间为HS_UFT_DATA |
| 2024-07-15 21:33:42 | 3.0.2.23 | 阮善宏 | 将表结构挪至公共参数下 |
| 2024-06-28 15:16:54 | 3.0.2.22 | 张云焘 | 新增 |

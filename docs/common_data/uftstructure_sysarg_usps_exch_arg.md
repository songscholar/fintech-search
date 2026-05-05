# usps_exch_arg - 交易参数表

**表对象ID**: 2
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_status | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | init_date | 否 |  |  |
| 4 | money_type | 否 |  |  |
| 5 | seat_source | 否 |  |  |
| 6 | withdraw | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | seat_prefix_len | 否 |  |  |
| 9 | exchange_name | 否 |  |  |
| 10 | account_len | 否 |  |  |
| 11 | fback_date | 否 |  |  |
| 12 | bback_date | 否 |  |  |
| 13 | count_days | 否 |  |  |
| 14 | intercept_len | 否 |  |  |
| 15 | internal_len | 否 |  |  |
| 16 | prefix | 否 |  |  |
| 17 | square_type | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | position_str | 否 |  | exchange_type |
| 21 | exchange_status | 否 |  |  |
| 22 | exchange_type | 否 |  |  |
| 23 | init_date | 否 |  |  |
| 24 | money_type | 否 |  |  |
| 25 | seat_source | 否 |  |  |
| 26 | withdraw | 否 |  |  |
| 27 | transaction_no | 否 |  |  |
| 28 | seat_prefix_len | 否 |  |  |
| 29 | exchange_name | 否 |  |  |
| 30 | account_len | 否 |  |  |
| 31 | fback_date | 否 |  |  |
| 32 | bback_date | 否 |  |  |
| 33 | count_days | 否 |  |  |
| 34 | intercept_len | 否 |  |  |
| 35 | internal_len | 否 |  |  |
| 36 | prefix | 否 |  |  |
| 37 | square_type | 否 |  |  |
| 38 | update_date | 否 |  |  |
| 39 | update_time | 否 |  |  |
| 40 | position_str | 否 |  | exchange_type |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_exch_arg | ART | 是 | exchange_type, exchange_type |
| idx_usps_exch_arg | ART | 是 | exchange_type, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_exch_arg | exchange_type, exchange_type |
| idx_usps_exch_arg | exchange_type, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-03 17:10:19 | 3.0.2.94 | 高志强 | 所有表usps_exch_arg，添加了表字段(position_str);
 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-20 16:24:09 | 3.0.6.116 | 李想 | 物理表usps_exch_arg，添加了表字段(account_len);
物理表usps_exch_arg，添加了表... |
| 2024-07-22 14:08:51 | 3.0.3.5 | 袁文龙 | 修复该全局索引被作为关联索引使用请确认是否需要修改 |
| 2023-09-18 09:39:34 | V3.0.1.6 | 吴威 | 调整索引名称 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-28 11:27 | 0.3.3.111 | 李海洋 | 内存交易需要增加接口供报盘调用获取营业部前缀长度 |
| 2023-06-06 15:59 | 0.0.0.5 | 吴威 | 新增字段transaction_no |
| 2025-09-03 17:10:19 | 3.0.2.94 | 高志强 | 所有表usps_exch_arg，添加了表字段(position_str);
 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-20 16:24:09 | 3.0.6.116 | 李想 | 物理表usps_exch_arg，添加了表字段(account_len);
物理表usps_exch_arg，添加了表... |
| 2024-07-22 14:08:51 | 3.0.3.5 | 袁文龙 | 修复该全局索引被作为关联索引使用请确认是否需要修改 |
| 2023-09-18 09:39:34 | V3.0.1.6 | 吴威 | 调整索引名称 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-28 11:27 | 0.3.3.111 | 李海洋 | 内存交易需要增加接口供报盘调用获取营业部前缀长度 |

> 共 16 条修改记录，仅显示最近15条

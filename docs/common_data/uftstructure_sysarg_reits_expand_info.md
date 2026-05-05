# reits_expand_info - 基础设施基金扩募表

**表对象ID**: 367
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_code | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | reits_expand_type | 否 |  |  |
| 4 | up_price | 否 |  |  |
| 5 | down_price | 否 |  |  |
| 6 | sub_unit | 否 |  |  |
| 7 | one_upper_rpt_quota | 否 |  |  |
| 8 | one_lower_rpt_quota | 否 |  |  |
| 9 | start_date | 否 |  |  |
| 10 | end_date | 否 |  |  |
| 11 | withdraw_flag | 否 |  |  |
| 12 | resub_flag | 否 |  |  |
| 13 | modify_date | 否 |  |  |
| 14 | update_date | 是 |  |  |
| 15 | update_time | 是 |  |  |
| 16 | position_str | 是 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | exchange_type | 否 |  |  |
| 20 | reits_expand_type | 否 |  |  |
| 21 | up_price | 否 |  |  |
| 22 | down_price | 否 |  |  |
| 23 | sub_unit | 否 |  |  |
| 24 | one_upper_rpt_quota | 否 |  |  |
| 25 | one_lower_rpt_quota | 否 |  |  |
| 26 | start_date | 否 |  |  |
| 27 | end_date | 否 |  |  |
| 28 | withdraw_flag | 否 |  |  |
| 29 | resub_flag | 否 |  |  |
| 30 | modify_date | 否 |  |  |
| 31 | update_date | 是 |  |  |
| 32 | update_time | 是 |  |  |
| 33 | position_str | 是 |  |  |
| 34 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_reits_expand_info | ART | 是 | stock_code, exchange_type, reits_expand_type, stock_code, exchange_type, reits_expand_type |
| idx_reits_expand_info | ART | 是 | stock_code, exchange_type, reits_expand_type, stock_code, exchange_type, reits_expand_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_reits_expand_info | stock_code, exchange_type, reits_expand_type, stock_code, exchange_type, reits_expand_type |
| idx_reits_expand_info | stock_code, exchange_type, reits_expand_type, stock_code, exchange_type, reits_expand_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-07 09:46:40 | 8.26.2.93 | 蒋浩宇 | 所有表reits_expand_info，添加了表字段(update_date);
所有表reits_expand_i... |
| 2025-05-10 14:09:06 | 3.0.6.1000 | 张训华 |  |
| 2025-11-07 09:46:40 | 8.26.2.93 | 蒋浩宇 | 所有表reits_expand_info，添加了表字段(update_date);
所有表reits_expand_i... |
| 2025-05-10 14:09:06 | 3.0.6.1000 | 张训华 |  |

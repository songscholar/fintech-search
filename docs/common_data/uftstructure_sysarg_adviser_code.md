# adviser_code - 投顾产品标的信息

**表对象ID**: 321
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | adproduct_id | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | transin_date | 否 |  |  |
| 6 | transout_date | 否 |  |  |
| 7 | profit_status | 否 |  |  |
| 8 | date_clear | 否 |  |  |
| 9 | position_str | 否 |  |  |
| 10 | follow_days | 否 |  |  |
| 11 | transin_time | 否 |  |  |
| 12 | transout_time | 否 |  |  |
| 13 | adviser_buy_price | 否 |  |  |
| 14 | adviser_sell_price | 否 |  |  |
| 15 | folbuy_end_date | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | remark | 否 |  |  |
| 18 | init_date | 否 |  |  |
| 19 | adproduct_id | 否 |  |  |
| 20 | exchange_type | 否 |  |  |
| 21 | stock_code | 否 |  |  |
| 22 | transin_date | 否 |  |  |
| 23 | transout_date | 否 |  |  |
| 24 | profit_status | 否 |  |  |
| 25 | date_clear | 否 |  |  |
| 26 | position_str | 否 |  |  |
| 27 | follow_days | 否 |  |  |
| 28 | transin_time | 否 |  |  |
| 29 | transout_time | 否 |  |  |
| 30 | adviser_buy_price | 否 |  |  |
| 31 | adviser_sell_price | 否 |  |  |
| 32 | folbuy_end_date | 否 |  |  |
| 33 | transaction_no | 否 |  |  |
| 34 | remark | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_advisercode_id | ART | 是 | stock_code, adproduct_id, exchange_type, transin_date, stock_code, adproduct_id, exchange_type, transin_date |
| idx_advisercode_pos | ART | 是 | position_str, position_str |
| uk_rpt_advisercode | ART | 是 | date_clear, position_str, date_clear, position_str |
| idx_advisercode_id | ART | 是 | stock_code, adproduct_id, exchange_type, transin_date, stock_code, adproduct_id, exchange_type, transin_date |
| idx_advisercode_pos | ART | 是 | position_str, position_str |
| uk_rpt_advisercode | ART | 是 | date_clear, position_str, date_clear, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_advisercode_id | stock_code, adproduct_id, exchange_type, transin_date, stock_code, adproduct_id, exchange_type, transin_date |
| idx_advisercode_pos | position_str, position_str |
| idx_advisercode_id | stock_code, adproduct_id, exchange_type, transin_date, stock_code, adproduct_id, exchange_type, transin_date |
| idx_advisercode_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-09-17 17:32:58 | 3.0.2.96 | taocong45644 | 数据存储介质修改为DB+MDB,数据表空间修改为HS_UARG |
| 2024-10-06 09:39:53 | 3.0.2.31 | 李海洋 | 变长字段顺序调整，修复插入记录乱码问题 |
| 2024-09-24 13:20:32 | 3.0.2.29 | 范文浩 | 物理表adviser_code，添加了表字段(init_date);
物理表adviser_code，添加了表字段(a... |
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-09-17 17:32:58 | 3.0.2.96 | taocong45644 | 数据存储介质修改为DB+MDB,数据表空间修改为HS_UARG |
| 2024-10-06 09:39:53 | 3.0.2.31 | 李海洋 | 变长字段顺序调整，修复插入记录乱码问题 |
| 2024-09-24 13:20:32 | 3.0.2.29 | 范文浩 | 物理表adviser_code，添加了表字段(init_date);
物理表adviser_code，添加了表字段(a... |

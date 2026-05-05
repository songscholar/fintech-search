# indexcode - 指数代码表

**表对象ID**: 7095
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | index_stock_code | 否 |  |  |
| 2 | index_stock_name | 否 |  |  |
| 3 | last_price | 否 |  |  |
| 4 | close_price | 否 |  |  |
| 5 | remark | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | tohis_date | 否 | H |  |
| 10 | index_stock_code | 否 |  |  |
| 11 | index_stock_name | 否 |  |  |
| 12 | last_price | 否 |  |  |
| 13 | close_price | 否 |  |  |
| 14 | remark | 否 |  |  |
| 15 | update_date | 否 |  |  |
| 16 | update_time | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | tohis_date | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_indexcode | ART | 是 | index_stock_code, index_stock_code |
| uk_rpt_indexcode | ART | 是 | tohis_date, index_stock_code, tohis_date, index_stock_code |
| idx_indexcode | ART | 是 | index_stock_code, index_stock_code |
| uk_rpt_indexcode | ART | 是 | tohis_date, index_stock_code, tohis_date, index_stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_indexcode | index_stock_code, index_stock_code |
| idx_indexcode | index_stock_code, index_stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-02-18 10:05:40 | 3.0.6.68 | 李想 | 新增表 |
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-02-18 10:05:40 | 3.0.6.68 | 李想 | 新增表 |

# limit_stock_price - 限售股价格信息表

**表对象ID**: 5549
**所属模块**: sestrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | money_type | 否 |  |  |
| 5 | close_price | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | update_date | 否 |  |  |
| 8 | update_time | 否 |  |  |
| 9 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 10 | init_date | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | money_type | 否 |  |  |
| 14 | close_price | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | position_str | 否 |  | stock_code(8)+exchange_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_limitstockprice | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_limitstockprice | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_limitstockprice | stock_code, exchange_type, stock_code, exchange_type |
| idx_limitstockprice | stock_code, exchange_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:02:41 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-18 16:34:55 | 3.0.6.8 | 李想 | 物理表limit_stock_price，添加了表字段(update_date);
物理表limit_stock_pr... |
| 2024-08-05 16:07:08 | 3.0.2.32 | 祝丁恺 | 物理表limit_stock_price，添加了表字段(transaction_no);
 |
| 2024-07-09 13:43:55 | 3.0.2.23 | 祝丁恺 | 新增limit_stock_price表结构 |
| 2026-03-09 14:02:41 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-18 16:34:55 | 3.0.6.8 | 李想 | 物理表limit_stock_price，添加了表字段(update_date);
物理表limit_stock_pr... |
| 2024-08-05 16:07:08 | 3.0.2.32 | 祝丁恺 | 物理表limit_stock_price，添加了表字段(transaction_no);
 |
| 2024-07-09 13:43:55 | 3.0.2.23 | 祝丁恺 | 新增limit_stock_price表结构 |

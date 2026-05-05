# income_product - 固收产品参数表

**表对象ID**: 2331
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | trade_product | 否 |  |  |
| 2 | status | 否 |  |  |
| 3 | en_entrust_prop | 否 |  |  |
| 4 | report_unit | 否 |  |  |
| 5 | min_limit_amount | 否 |  |  |
| 6 | spread_value | 否 |  |  |
| 7 | price_ratio | 否 |  |  |
| 8 | stock_type_tag | 否 |  |  |
| 9 | transaction_no | 否 |  |  |
| 10 | update_date | 否 |  |  |
| 11 | update_time | 否 |  |  |
| 12 | position_str | 否 |  | trade_product(8)+stock_type_tag(4) |
| 13 | trade_product | 否 |  |  |
| 14 | status | 否 |  |  |
| 15 | en_entrust_prop | 否 |  |  |
| 16 | report_unit | 否 |  |  |
| 17 | min_limit_amount | 否 |  |  |
| 18 | spread_value | 否 |  |  |
| 19 | price_ratio | 否 |  |  |
| 20 | stock_type_tag | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | update_date | 否 |  |  |
| 23 | update_time | 否 |  |  |
| 24 | position_str | 否 |  | trade_product(8)+stock_type_tag(4) |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_incomeproduct | 默认 | 否 |  |
| idx_incomeproduct | 默认 | 否 | stock_type_tag, stock_type_tag |
| idx_incomeproduct | ART | 是 | trade_product, stock_type_tag, trade_product, stock_type_tag |
| idx_incomeproduct | 默认 | 否 |  |
| idx_incomeproduct | 默认 | 否 | stock_type_tag, stock_type_tag |
| idx_incomeproduct | ART | 是 | trade_product, stock_type_tag, trade_product, stock_type_tag |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_incomeproduct | trade_product, stock_type_tag, trade_product, stock_type_tag |
| idx_incomeproduct | trade_product, stock_type_tag, trade_product, stock_type_tag |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:27:27 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-03-22 18:33:06 | V3.0.2.2001 | 高志强 | 修改内存索引idx_incomeproduct为部分匹配 |
| 2025-02-18 17:13:13 | V3.0.5.1009 | 李想 | 物理表income_product，增加索引字段(索引idx_incomeproduct:增加了索引字段：stock_t... |
| 2025-02-18 17:12:35 | V3.0.5.1008 | 李想 | 物理表income_product，添加了表字段(stock_type_tag);
物理表income_product... |
| 2025-02-15 09:26:04 | V3.0.2.53 | 洪略 | 增加stock_type_tag字段,同时调整索引 |
| 2024-08-06 19:25:47 | V3.0.2.1004 | 骆鹏程 | 新增 |
| 2026-03-04 15:27:27 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-03-22 18:33:06 | V3.0.2.2001 | 高志强 | 修改内存索引idx_incomeproduct为部分匹配 |
| 2025-02-18 17:13:13 | V3.0.5.1009 | 李想 | 物理表income_product，增加索引字段(索引idx_incomeproduct:增加了索引字段：stock_t... |
| 2025-02-18 17:12:35 | V3.0.5.1008 | 李想 | 物理表income_product，添加了表字段(stock_type_tag);
物理表income_product... |
| 2025-02-15 09:26:04 | V3.0.2.53 | 洪略 | 增加stock_type_tag字段,同时调整索引 |
| 2024-08-06 19:25:47 | V3.0.2.1004 | 骆鹏程 | 新增 |

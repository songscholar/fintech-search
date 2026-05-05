# ics_includefare1_model - 佣金代收费用模板表

**表对象ID**: 116
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | include_fare1_model_no | 否 |  |  |
| 2 | include_fare1_model_name | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | sub_stock_type | 否 |  |  |
| 6 | entrust_type | 否 |  |  |
| 7 | entrust_prop | 否 |  |  |
| 8 | include_fare1_str | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | position_str | 否 |  | include_fare1_model_no(10)+exchange_type(4)+stock_type(4)+su |
| 13 | include_fare1_model_no | 否 |  |  |
| 14 | include_fare1_model_name | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_type | 否 |  |  |
| 17 | sub_stock_type | 否 |  |  |
| 18 | entrust_type | 否 |  |  |
| 19 | entrust_prop | 否 |  |  |
| 20 | include_fare1_str | 否 |  |  |
| 21 | update_date | 否 |  |  |
| 22 | update_time | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | position_str | 否 |  | include_fare1_model_no(10)+exchange_type(4)+stock_type(4)+su |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ics_includefare1_model | 默认 | 否 |  |
| idx_ics_includefare1_model | ART | 是 | include_fare1_model_no, exchange_type, stock_type, sub_stock_type, entrust_type, entrust_prop, include_fare1_model_no, exchange_type, stock_type, sub_stock_type, entrust_type, entrust_prop |
| idx_ics_includefare1_model | 默认 | 否 |  |
| idx_ics_includefare1_model | ART | 是 | include_fare1_model_no, exchange_type, stock_type, sub_stock_type, entrust_type, entrust_prop, include_fare1_model_no, exchange_type, stock_type, sub_stock_type, entrust_type, entrust_prop |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ics_includefare1_model | include_fare1_model_no, exchange_type, stock_type, sub_stock_type, entrust_type, entrust_prop, include_fare1_model_no, exchange_type, stock_type, sub_stock_type, entrust_type, entrust_prop |
| idx_ics_includefare1_model | include_fare1_model_no, exchange_type, stock_type, sub_stock_type, entrust_type, entrust_prop, include_fare1_model_no, exchange_type, stock_type, sub_stock_type, entrust_type, entrust_prop |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:41:39 | 3.0.2.103 | taocong45644 | 当前表ics_includefare1_model，修改了索引idx_ics_includefare1_model,索引... |
| 2025-02-14 15:27:29 | 3.0.6.27 | 李想 | 新增表 |
| 2025-12-01 14:41:39 | 3.0.2.103 | taocong45644 | 当前表ics_includefare1_model，修改了索引idx_ics_includefare1_model,索引... |
| 2025-02-14 15:27:29 | 3.0.6.27 | 李想 | 新增表 |

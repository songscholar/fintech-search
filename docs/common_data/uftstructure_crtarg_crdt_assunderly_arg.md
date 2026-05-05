# crdt_assunderly_arg - 担保标的设置参数表

**表对象ID**: 7050
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | assunderlyarg_type | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | std_status | 否 |  |  |
| 5 | fin_ratio | 否 |  |  |
| 6 | slo_ratio | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | position_str | 否 |  | assunderlyarg_type(1)+exchange_type(4)+stock_type(4) |
| 11 | assunderlyarg_type | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_type | 否 |  |  |
| 14 | std_status | 否 |  |  |
| 15 | fin_ratio | 否 |  |  |
| 16 | slo_ratio | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | position_str | 否 |  | assunderlyarg_type(1)+exchange_type(4)+stock_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdt_assunderly_arg | ART | 是 | assunderlyarg_type, exchange_type, stock_type, assunderlyarg_type, exchange_type, stock_type |
| idx_crdt_assunderly_arg | ART | 是 | assunderlyarg_type, exchange_type, stock_type, assunderlyarg_type, exchange_type, stock_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdt_assunderly_arg | assunderlyarg_type, exchange_type, stock_type, assunderlyarg_type, exchange_type, stock_type |
| idx_crdt_assunderly_arg | assunderlyarg_type, exchange_type, stock_type, assunderlyarg_type, exchange_type, stock_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-17 19:45:02 | 3.0.6.53 | 李想 | 物理表crdt_assunderly_arg，添加了表字段(update_date);
物理表crdt_assunde... |
| 2024-10-24 15:30:32 | 3.0.6.7 | 沈勋 | 新增表结构 |
| 2025-02-17 19:45:02 | 3.0.6.53 | 李想 | 物理表crdt_assunderly_arg，添加了表字段(update_date);
物理表crdt_assunde... |
| 2024-10-24 15:30:32 | 3.0.6.7 | 沈勋 | 新增表结构 |

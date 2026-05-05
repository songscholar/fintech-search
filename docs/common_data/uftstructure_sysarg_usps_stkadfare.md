# usps_stkadfare - 证券类别冻结资金调整表

**表对象ID**: 59
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_type | 否 |  |  |
| 3 | frozen_adjustfare | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | update_date | 否 |  |  |
| 6 | update_time | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | stock_type | 否 |  |  |
| 9 | frozen_adjustfare | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_stkadfare | ART | 是 | exchange_type, stock_type, exchange_type, stock_type |
| idx_usps_stkadfare | ART | 是 | exchange_type, stock_type, exchange_type, stock_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_stkadfare | exchange_type, stock_type, exchange_type, stock_type |
| idx_usps_stkadfare | exchange_type, stock_type, exchange_type, stock_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-19 16:19:49 | 3.0.6.99 | 李想 | 物理表usps_stkadfare，添加了表字段(update_date);
物理表usps_stkadfare，添加... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-19 16:19:49 | 3.0.6.99 | 李想 | 物理表usps_stkadfare，添加了表字段(update_date);
物理表usps_stkadfare，添加... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

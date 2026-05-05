# usps_debtinterest - 国债利息表

**表对象ID**: 28
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | init_date | 否 |  |  |
| 4 | ratio | 否 |  |  |
| 5 | interest_period | 否 |  |  |
| 6 | stock_interest | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | remark | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | position_str | 否 |  | exchange_type(4)+stock_code(8) |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | init_date | 否 |  |  |
| 15 | ratio | 否 |  |  |
| 16 | interest_period | 否 |  |  |
| 17 | stock_interest | 否 |  |  |
| 18 | transaction_no | 否 |  |  |
| 19 | remark | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | position_str | 否 |  | exchange_type(4)+stock_code(8) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_debtinterest | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| uk_rpt_uspsdebtinterest | ART | 是 | init_date, exchange_type, stock_code, init_date, exchange_type, stock_code |
| idx_usps_debtinterest | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| uk_rpt_uspsdebtinterest | ART | 是 | init_date, exchange_type, stock_code, init_date, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_debtinterest | exchange_type, stock_code, exchange_type, stock_code |
| idx_usps_debtinterest | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-14 17:05:11 | 3.0.6.12 | 常行 | 物理表usps_debtinterest，添加了表字段(remark);
物理表usps_debtinterest，添... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-14 17:05:11 | 3.0.6.12 | 常行 | 物理表usps_debtinterest，添加了表字段(remark);
物理表usps_debtinterest，添... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

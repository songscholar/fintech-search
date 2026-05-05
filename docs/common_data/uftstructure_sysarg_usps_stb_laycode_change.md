# usps_stb_laycode_change - 股转分层代码变动表

**表对象ID**: 340
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stb_layer_flag | 否 |  |  |
| 5 | stb_layer_flag_old | 否 |  |  |
| 6 | bjdc_stock_type | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | position_str | 否 |  | enchange_type(4)+stock_code(8) |
| 11 | init_date | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | stb_layer_flag | 否 |  |  |
| 15 | stb_layer_flag_old | 否 |  |  |
| 16 | bjdc_stock_type | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | position_str | 否 |  | enchange_type(4)+stock_code(8) |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stblaycodechange | 默认 | 否 |  |
| idx_stblaycodechange | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| uk_rpt_uspsstblaycodechange | ART | 是 | init_date, exchange_type, stock_code, init_date, exchange_type, stock_code |
| idx_stblaycodechange | 默认 | 否 |  |
| idx_stblaycodechange | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| uk_rpt_uspsstblaycodechange | ART | 是 | init_date, exchange_type, stock_code, init_date, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stblaycodechange | exchange_type, stock_code, exchange_type, stock_code |
| idx_stblaycodechange | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-12-01 15:45:04 | 3.0.2.103 | taocong45644 | 当前表usps_stb_laycode_change，修改了索引idx_stblaycodechange,索引字段修改为... |
| 2025-04-07 11:17:31 | 3.0.6.130 | 常行 | 新增表 |
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-12-01 15:45:04 | 3.0.2.103 | taocong45644 | 当前表usps_stb_laycode_change，修改了索引idx_stblaycodechange,索引字段修改为... |
| 2025-04-07 11:17:31 | 3.0.6.130 | 常行 | 新增表 |

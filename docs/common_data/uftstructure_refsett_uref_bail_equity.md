# uref_bail_equity - 保证金权益信息表

**表对象ID**: 6155
**所属模块**: refsett
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | company_no | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | relative_code | 否 |  |  |
| 7 | equity_type | 否 |  |  |
| 8 | distribute_ratio | 否 |  |  |
| 9 | price | 否 |  |  |
| 10 | register_date | 否 |  |  |
| 11 | dr_date | 否 |  |  |
| 12 | settle_date | 否 |  |  |
| 13 | date_clear | 否 |  |  |
| 14 | remark | 否 |  |  |
| 15 | position_str | 否 |  |  |
| 16 | stock_name | 否 | H |  |
| 17 | stock_type | 否 | H |  |
| 18 | sub_stock_type | 否 | H |  |
| 19 | init_date | 否 |  |  |
| 20 | serial_no | 否 |  |  |
| 21 | company_no | 否 |  |  |
| 22 | exchange_type | 否 |  |  |
| 23 | stock_code | 否 |  |  |
| 24 | relative_code | 否 |  |  |
| 25 | equity_type | 否 |  |  |
| 26 | distribute_ratio | 否 |  |  |
| 27 | price | 否 |  |  |
| 28 | register_date | 否 |  |  |
| 29 | dr_date | 否 |  |  |
| 30 | settle_date | 否 |  |  |
| 31 | date_clear | 否 |  |  |
| 32 | remark | 否 |  |  |
| 33 | position_str | 否 |  |  |
| 34 | stock_name | 否 | H |  |
| 35 | stock_type | 否 | H |  |
| 36 | sub_stock_type | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refbailequity | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_refbailequity_pos | ART | 是 | position_str, position_str |
| idx_refbailequity | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_refbailequity_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 6 个）

| 索引名 | 字段 |
|--------|------|
| idx_refbailequity | init_date, serial_no, init_date, serial_no |
| idx_refbailequity_pos | position_str, position_str |
| uk_rpt_urefbailequity | init_date, position_str, init_date, position_str |
| idx_refbailequity | init_date, serial_no, init_date, serial_no |
| idx_refbailequity_pos | position_str, position_str |
| uk_rpt_urefbailequity | init_date, position_str, init_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-16 10:38:36 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-10-16 10:38:36 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

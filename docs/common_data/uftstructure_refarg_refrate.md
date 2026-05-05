# refrate - 转融通期限利率表

**表对象ID**: 6005
**所属模块**: refarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | ref_type | 否 |  |  |
| 3 | ref_bs | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | ref_term | 否 |  |  |
| 7 | year_rate | 否 |  |  |
| 8 | end_date | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | update_date | 否 |  |  |
| 11 | update_time | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | position_str | 否 |  | ref_type(1)+ref_bs(1)+exchange_type(4)+stock_code(8)+ref_ter |
| 14 | init_date | 否 |  |  |
| 15 | ref_type | 否 |  |  |
| 16 | ref_bs | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | ref_term | 否 |  |  |
| 20 | year_rate | 否 |  |  |
| 21 | end_date | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | update_date | 否 |  |  |
| 24 | update_time | 否 |  |  |
| 25 | transaction_no | 否 |  |  |
| 26 | position_str | 否 |  | ref_type(1)+ref_bs(1)+exchange_type(4)+stock_code(8)+ref_ter |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refrate | ART | 是 | ref_type, ref_bs, exchange_type, stock_code, ref_term, ref_type, ref_bs, exchange_type, stock_code, ref_term |
| idx_refrate_pos | ART | 是 | position_str, position_str |
| idx_refrate | ART | 是 | ref_type, ref_bs, exchange_type, stock_code, ref_term, ref_type, ref_bs, exchange_type, stock_code, ref_term |
| idx_refrate_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_refrate | ref_type, ref_bs, exchange_type, stock_code, ref_term, ref_type, ref_bs, exchange_type, stock_code, ref_term |
| idx_refrate | ref_type, ref_bs, exchange_type, stock_code, ref_term, ref_type, ref_bs, exchange_type, stock_code, ref_term |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-24 11:22:08 | V3.0.2.5 | 廖宏玮 | 调整内存表索引 |
| 2025-02-21 10:55:33 | 1.0.0.4 | 李想 | 新增表 |
| 2025-11-24 11:22:08 | V3.0.2.5 | 廖宏玮 | 调整内存表索引 |
| 2025-02-21 10:55:33 | 1.0.0.4 | 李想 | 新增表 |

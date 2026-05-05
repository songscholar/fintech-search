# usps_vote_code - 投票代码详情表

**表对象ID**: 21
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | init_date | 否 |  |  |
| 3 | last_trade_date | 否 |  |  |
| 4 | meeting_seq | 否 |  |  |
| 5 | register_date | 否 |  |  |
| 6 | sort_name | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | stock_name | 否 |  |  |
| 9 | transaction_no | 否 |  |  |
| 10 | update_date | 否 |  |  |
| 11 | update_time | 否 |  |  |
| 12 | position_str | 否 |  | meeting_seq(10)+stock_code(8)+exchange_type(4) |
| 13 | exchange_type | 否 |  |  |
| 14 | init_date | 否 |  |  |
| 15 | last_trade_date | 否 |  |  |
| 16 | meeting_seq | 否 |  |  |
| 17 | register_date | 否 |  |  |
| 18 | sort_name | 否 |  |  |
| 19 | stock_code | 否 |  |  |
| 20 | stock_name | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | update_date | 否 |  |  |
| 23 | update_time | 否 |  |  |
| 24 | position_str | 否 |  | meeting_seq(10)+stock_code(8)+exchange_type(4) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_vote_code | ART | 是 | meeting_seq, stock_code, exchange_type, meeting_seq, stock_code, exchange_type |
| uk_rpt_uspsvotecode | ART | 是 | init_date, meeting_seq, stock_code, exchange_type, init_date, meeting_seq, stock_code, exchange_type |
| idx_usps_vote_code | ART | 是 | meeting_seq, stock_code, exchange_type, meeting_seq, stock_code, exchange_type |
| uk_rpt_uspsvotecode | ART | 是 | init_date, meeting_seq, stock_code, exchange_type, init_date, meeting_seq, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_vote_code | meeting_seq, stock_code, exchange_type, meeting_seq, stock_code, exchange_type |
| idx_usps_vote_code | meeting_seq, stock_code, exchange_type, meeting_seq, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-02-18 16:59:31 | 3.0.6.66 | 李想 | 物理表usps_vote_code，添加了表字段(update_date);
物理表usps_vote_code，添加... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-29 18:44 | 0.0.0.12 | 程效 | 索引调整为分级索引 |
| 2023-06-19 17:09 | 0.0.0.9 | 吴威 | 新增transaction_no |
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-02-18 16:59:31 | 3.0.6.66 | 李想 | 物理表usps_vote_code，添加了表字段(update_date);
物理表usps_vote_code，添加... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-29 18:44 | 0.0.0.12 | 程效 | 索引调整为分级索引 |
| 2023-06-19 17:09 | 0.0.0.9 | 吴威 | 新增transaction_no |

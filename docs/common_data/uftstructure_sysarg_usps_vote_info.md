# usps_vote_info - 投票基本信息表

**表对象ID**: 19
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | begin_date | 否 |  |  |
| 2 | company_code | 否 |  |  |
| 3 | company_name | 否 |  |  |
| 4 | end_date | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | init_date | 否 |  |  |
| 7 | meeting_name | 否 |  |  |
| 8 | meeting_seq | 否 |  |  |
| 9 | meeting_type | 否 |  |  |
| 10 | company_name_long | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | update_date | 否 |  |  |
| 13 | update_time | 否 |  |  |
| 14 | position_str | 否 |  | exchange_type(4)+meeting_seq(10) |
| 15 | begin_date | 否 |  |  |
| 16 | company_code | 否 |  |  |
| 17 | company_name | 否 |  |  |
| 18 | end_date | 否 |  |  |
| 19 | exchange_type | 否 |  |  |
| 20 | init_date | 否 |  |  |
| 21 | meeting_name | 否 |  |  |
| 22 | meeting_seq | 否 |  |  |
| 23 | meeting_type | 否 |  |  |
| 24 | company_name_long | 否 |  |  |
| 25 | transaction_no | 否 |  |  |
| 26 | update_date | 否 |  |  |
| 27 | update_time | 否 |  |  |
| 28 | position_str | 否 |  | exchange_type(4)+meeting_seq(10) |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_vote_info | ART | 是 | exchange_type, meeting_seq, exchange_type, meeting_seq |
| uk_rpt_uspsvoteinfo | ART | 是 | init_date, exchange_type, meeting_seq, init_date, exchange_type, meeting_seq |
| idx_rpt_uspsvoteinfo_date | ART | 是 | begin_date, end_date, begin_date, end_date |
| idx_usps_vote_info | ART | 是 | exchange_type, meeting_seq, exchange_type, meeting_seq |
| uk_rpt_uspsvoteinfo | ART | 是 | init_date, exchange_type, meeting_seq, init_date, exchange_type, meeting_seq |
| idx_rpt_uspsvoteinfo_date | ART | 是 | begin_date, end_date, begin_date, end_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_vote_info | exchange_type, meeting_seq, exchange_type, meeting_seq |
| idx_usps_vote_info | exchange_type, meeting_seq, exchange_type, meeting_seq |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-02-18 16:54:23 | 3.0.6.64 | 李想 | 物理表usps_vote_info，添加了表字段(update_date);
物理表usps_vote_info，添加... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-19 17:10 | 0.0.0.9 | 吴威 | 新增transaction_no |
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-02-18 16:54:23 | 3.0.6.64 | 李想 | 物理表usps_vote_info，添加了表字段(update_date);
物理表usps_vote_info，添加... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-19 17:10 | 0.0.0.9 | 吴威 | 新增transaction_no |

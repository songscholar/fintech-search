# usps_vote_list - 投票议案详情表

**表对象ID**: 22
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | en_refcode | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | init_date | 否 |  |  |
| 4 | meeting_seq | 否 |  |  |
| 5 | vote_info | 否 |  |  |
| 6 | vote_motion | 否 |  |  |
| 7 | vote_numcontrol | 否 |  |  |
| 8 | vote_relation | 否 |  |  |
| 9 | vote_type | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | position_str | 否 |  | meeting_seq(10)+vote_motion(20)+exchange_type(4) |
| 14 | en_refcode | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | init_date | 否 |  |  |
| 17 | meeting_seq | 否 |  |  |
| 18 | vote_info | 否 |  |  |
| 19 | vote_motion | 否 |  |  |
| 20 | vote_numcontrol | 否 |  |  |
| 21 | vote_relation | 否 |  |  |
| 22 | vote_type | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | position_str | 否 |  | meeting_seq(10)+vote_motion(20)+exchange_type(4) |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_vote_list_uk | ART | 是 | meeting_seq, vote_motion, exchange_type, meeting_seq, vote_motion, exchange_type |
| idx_usps_vote_list | ART | 是 | meeting_seq, exchange_type, meeting_seq, exchange_type |
| idx_usps_vote_list_uk | ART | 是 | meeting_seq, vote_motion, exchange_type, meeting_seq, vote_motion, exchange_type |
| uk_rpt_uspsvotelist | ART | 是 | init_date, meeting_seq, vote_motion, exchange_type, init_date, meeting_seq, vote_motion, exchange_type |
| idx_usps_vote_list_uk | ART | 是 | meeting_seq, vote_motion, exchange_type, meeting_seq, vote_motion, exchange_type |
| idx_usps_vote_list | ART | 是 | meeting_seq, exchange_type, meeting_seq, exchange_type |
| idx_usps_vote_list_uk | ART | 是 | meeting_seq, vote_motion, exchange_type, meeting_seq, vote_motion, exchange_type |
| uk_rpt_uspsvotelist | ART | 是 | init_date, meeting_seq, vote_motion, exchange_type, init_date, meeting_seq, vote_motion, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_vote_list | meeting_seq, vote_motion, exchange_type, meeting_seq, vote_motion, exchange_type |
| idx_usps_vote_list | meeting_seq, vote_motion, exchange_type, meeting_seq, vote_motion, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-02-28 10:50:42 | 8.26.2.107 | 袁文龙 | 当前表usps_vote_list，增加索引（ idx_usps_vote_list_uk:[meeting_seq,v... |
| 2026-01-15 15:10:30 | 8.26.2.106 | 袁文龙 | 物理表usps_vote_list，增加索引(idx_usps_vote_list_vote) |
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-02-18 16:57:29 | 3.0.6.65 | 李想 | 物理表usps_vote_list，添加了表字段(update_date);
物理表usps_vote_list，添加... |
| 2024-06-19 10:57:38 | 3.0.2.14 | 杨涛 | 唯一索引去掉索引字段vote_motion，改成非唯一索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-19 17:09 | 0.0.0.9 | 吴威 | 新增transaction_no |
| 2026-02-28 10:50:42 | 8.26.2.107 | 袁文龙 | 当前表usps_vote_list，增加索引（ idx_usps_vote_list_uk:[meeting_seq,v... |
| 2026-01-15 15:10:30 | 8.26.2.106 | 袁文龙 | 物理表usps_vote_list，增加索引(idx_usps_vote_list_vote) |
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-02-18 16:57:29 | 3.0.6.65 | 李想 | 物理表usps_vote_list，添加了表字段(update_date);
物理表usps_vote_list，添加... |
| 2024-06-19 10:57:38 | 3.0.2.14 | 杨涛 | 唯一索引去掉索引字段vote_motion，改成非唯一索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-19 17:09 | 0.0.0.9 | 吴威 | 新增transaction_no |

# pre_vote_info - 资讯投票基本信息表

**表对象ID**: 360
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | company_name | 否 |  |  |
| 3 | meeting_seq | 否 |  |  |
| 4 | company_code | 否 |  |  |
| 5 | begin_date | 否 |  |  |
| 6 | end_date | 否 |  |  |
| 7 | meeting_type | 否 |  |  |
| 8 | meeting_name | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | company_name_long | 否 |  |  |
| 11 | meeting_date | 否 |  |  |
| 12 | disclosure_date | 否 |  |  |
| 13 | inner_meeting_seq | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | tohis_date | 否 |  |  |
| 16 | init_date | 否 |  |  |
| 17 | company_name | 否 |  |  |
| 18 | meeting_seq | 否 |  |  |
| 19 | company_code | 否 |  |  |
| 20 | begin_date | 否 |  |  |
| 21 | end_date | 否 |  |  |
| 22 | meeting_type | 否 |  |  |
| 23 | meeting_name | 否 |  |  |
| 24 | exchange_type | 否 |  |  |
| 25 | company_name_long | 否 |  |  |
| 26 | meeting_date | 否 |  |  |
| 27 | disclosure_date | 否 |  |  |
| 28 | inner_meeting_seq | 否 |  |  |
| 29 | transaction_no | 否 |  |  |
| 30 | tohis_date | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_pre_vote_info | ART | 是 | exchange_type, inner_meeting_seq, exchange_type, inner_meeting_seq |
| idx_rpt_pre_vote_info | ART | 是 | tohis_date, exchange_type, inner_meeting_seq, tohis_date, exchange_type, inner_meeting_seq |
| idx_pre_vote_info | ART | 是 | exchange_type, inner_meeting_seq, exchange_type, inner_meeting_seq |
| idx_rpt_pre_vote_info | ART | 是 | tohis_date, exchange_type, inner_meeting_seq, tohis_date, exchange_type, inner_meeting_seq |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_pre_vote_info | exchange_type, inner_meeting_seq, exchange_type, inner_meeting_seq |
| idx_pre_vote_info | exchange_type, inner_meeting_seq, exchange_type, inner_meeting_seq |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-04-01 10:23:16 | 3.0.2.99 | 洪略 | 表迁移至uarg |
| 2025-12-08 13:52:30 | 3.0.2.98 | 洪略 | 历史表索引增加rpt前缀 |
| 2025-11-06 15:27:14 | 3.0.2.98 | 洪略 | 新增历史 |
| 2025-08-03 09:29:47 | 3.0.2.53 | honglue | 物理表pre_vote_info，添加了表字段(tohis_date);
 |
| 2025-01-14 19:36:40 | 3.0.2.52 | 洪略 | 增加transaction_no字段 |
| 2024-12-12 13:54:14 | 3.0.2.35 | 陆良铠 | 修改对象号 |
| 2024-07-26 14:53:31 | 3.0.3.6 | 许琮擎 | 新增 |
| 2026-04-01 10:23:16 | 3.0.2.99 | 洪略 | 表迁移至uarg |
| 2025-12-08 13:52:30 | 3.0.2.98 | 洪略 | 历史表索引增加rpt前缀 |
| 2025-11-06 15:27:14 | 3.0.2.98 | 洪略 | 新增历史 |
| 2025-08-03 09:29:47 | 3.0.2.53 | honglue | 物理表pre_vote_info，添加了表字段(tohis_date);
 |
| 2025-01-14 19:36:40 | 3.0.2.52 | 洪略 | 增加transaction_no字段 |
| 2024-12-12 13:54:14 | 3.0.2.35 | 陆良铠 | 修改对象号 |
| 2024-07-26 14:53:31 | 3.0.3.6 | 许琮擎 | 新增 |

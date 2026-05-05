# settredo_pre_vote_info - 清算重做资讯投票基本信息表

**表对象ID**: 2518
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | sett_dml_type | 否 |  |  |
| 2 | sett_batch_no | 否 |  |  |
| 3 | company_name | 否 |  |  |
| 4 | meeting_type | 否 |  |  |
| 5 | meeting_name | 否 |  |  |
| 6 | begin_date | 否 |  |  |
| 7 | end_date | 否 |  |  |
| 8 | meeting_date | 否 |  |  |
| 9 | disclosure_date | 否 |  |  |
| 10 | company_name_long | 否 |  |  |
| 11 | tohis_date | 否 |  |  |
| 12 | inner_meeting_seq | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | company_code | 否 |  |  |
| 15 | sett_dml_type | 否 |  |  |
| 16 | sett_batch_no | 否 |  |  |
| 17 | company_name | 否 |  |  |
| 18 | meeting_type | 否 |  |  |
| 19 | meeting_name | 否 |  |  |
| 20 | begin_date | 否 |  |  |
| 21 | end_date | 否 |  |  |
| 22 | meeting_date | 否 |  |  |
| 23 | disclosure_date | 否 |  |  |
| 24 | company_name_long | 否 |  |  |
| 25 | tohis_date | 否 |  |  |
| 26 | inner_meeting_seq | 否 |  |  |
| 27 | exchange_type | 否 |  |  |
| 28 | company_code | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_pre_vote_info | ART | 是 | exchange_type, inner_meeting_seq, exchange_type, inner_meeting_seq |
| idx_settredo_pre_vote_info | ART | 是 | exchange_type, inner_meeting_seq, exchange_type, inner_meeting_seq |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_pre_vote_info | exchange_type, inner_meeting_seq, exchange_type, inner_meeting_seq |
| idx_settredo_pre_vote_info | exchange_type, inner_meeting_seq, exchange_type, inner_meeting_seq |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-04-01 10:10:09 | 3.0.2.99 | 洪略 | 表空间迁移至uarg |
| 2026-04-01 10:10:09 | 3.0.2.99 | 洪略 | 表空间迁移至uarg |

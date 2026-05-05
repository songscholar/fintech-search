# settredo_pre_vote_code - 清算重做资讯投票详情表

**表对象ID**: 2517
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | sett_dml_type | 否 |  |  |
| 2 | sett_batch_no | 否 |  |  |
| 3 | stock_name | 否 |  |  |
| 4 | sort_name | 否 |  |  |
| 5 | begin_date | 否 |  |  |
| 6 | end_date | 否 |  |  |
| 7 | register_date | 否 |  |  |
| 8 | meeting_seq | 否 |  |  |
| 9 | tohis_date | 否 |  |  |
| 10 | inner_meeting_seq | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | sett_dml_type | 否 |  |  |
| 14 | sett_batch_no | 否 |  |  |
| 15 | stock_name | 否 |  |  |
| 16 | sort_name | 否 |  |  |
| 17 | begin_date | 否 |  |  |
| 18 | end_date | 否 |  |  |
| 19 | register_date | 否 |  |  |
| 20 | meeting_seq | 否 |  |  |
| 21 | tohis_date | 否 |  |  |
| 22 | inner_meeting_seq | 否 |  |  |
| 23 | stock_code | 否 |  |  |
| 24 | exchange_type | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_pre_vote_code | ART | 是 | inner_meeting_seq, stock_code, exchange_type, inner_meeting_seq, stock_code, exchange_type |
| idx_settredo_pre_vote_code | ART | 是 | inner_meeting_seq, stock_code, exchange_type, inner_meeting_seq, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_pre_vote_code | inner_meeting_seq, stock_code, exchange_type, inner_meeting_seq, stock_code, exchange_type |
| idx_settredo_pre_vote_code | inner_meeting_seq, stock_code, exchange_type, inner_meeting_seq, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-04-01 10:12:20 | 8.26.2.109 | 洪略 | 表空间迁移至uarg |
| 2026-04-01 10:12:20 | 8.26.2.109 | 洪略 | 表空间迁移至uarg |

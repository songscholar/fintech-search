# pre_vote_code - 资讯投票详情表

**表对象ID**: 361
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | register_date | 否 |  |  |
| 5 | last_trade_date | 否 |  |  |
| 6 | meeting_seq | 否 |  |  |
| 7 | sort_name | 否 |  |  |
| 8 | stock_name | 否 |  |  |
| 9 | inner_meeting_seq | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | tohis_date | 否 |  |  |
| 12 | init_date | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | register_date | 否 |  |  |
| 16 | last_trade_date | 否 |  |  |
| 17 | meeting_seq | 否 |  |  |
| 18 | sort_name | 否 |  |  |
| 19 | stock_name | 否 |  |  |
| 20 | inner_meeting_seq | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | tohis_date | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_pre_vote_code | ART | 是 | inner_meeting_seq, stock_code, exchange_type, inner_meeting_seq, stock_code, exchange_type |
| idx_rpt_pre_vote_code | ART | 是 | tohis_date, inner_meeting_seq, stock_code, exchange_type, tohis_date, inner_meeting_seq, stock_code, exchange_type |
| idx_pre_vote_code | ART | 是 | inner_meeting_seq, stock_code, exchange_type, inner_meeting_seq, stock_code, exchange_type |
| idx_rpt_pre_vote_code | ART | 是 | tohis_date, inner_meeting_seq, stock_code, exchange_type, tohis_date, inner_meeting_seq, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_pre_vote_code | inner_meeting_seq, stock_code, exchange_type, inner_meeting_seq, stock_code, exchange_type |
| idx_pre_vote_code | inner_meeting_seq, stock_code, exchange_type, inner_meeting_seq, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-04-01 10:23:58 | 3.0.2.99 | 洪略 | 表迁移至uarg |
| 2025-12-08 13:53:01 | 3.0.2.98 | 洪略 | 历史表索引增加rpt前缀 |
| 2025-11-06 15:26:36 | 3.0.2.98 | 洪略 | 新增历史表 |
| 2025-08-03 09:30:58 | 3.0.2.53 | honglue | 物理表pre_vote_code，添加了表字段(tohis_date);
 |
| 2025-01-14 19:37:55 | 3.0.2.52 | 洪略 | 增加transaction_no字段 |
| 2024-12-12 14:26:26 | 3.0.2.35 | 陆良铠 | 修改对象号 |
| 2024-07-31 14:53:49 | 3.0.3.6 | 许琮擎 | 新增 |
| 2026-04-01 10:23:58 | 3.0.2.99 | 洪略 | 表迁移至uarg |
| 2025-12-08 13:53:01 | 3.0.2.98 | 洪略 | 历史表索引增加rpt前缀 |
| 2025-11-06 15:26:36 | 3.0.2.98 | 洪略 | 新增历史表 |
| 2025-08-03 09:30:58 | 3.0.2.53 | honglue | 物理表pre_vote_code，添加了表字段(tohis_date);
 |
| 2025-01-14 19:37:55 | 3.0.2.52 | 洪略 | 增加transaction_no字段 |
| 2024-12-12 14:26:26 | 3.0.2.35 | 陆良铠 | 修改对象号 |
| 2024-07-31 14:53:49 | 3.0.3.6 | 许琮擎 | 新增 |

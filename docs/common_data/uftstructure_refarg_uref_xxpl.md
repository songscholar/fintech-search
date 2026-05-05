# uref_xxpl - 转融通信息披露表

**表对象ID**: 6014
**所属模块**: refarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | disclosure_type | 否 |  |  |
| 3 | date1 | 否 |  |  |
| 4 | date2 | 否 |  |  |
| 5 | rate1 | 否 |  |  |
| 6 | rate2 | 否 |  |  |
| 7 | balance1 | 否 |  |  |
| 8 | balance2 | 否 |  |  |
| 9 | amount1 | 否 |  |  |
| 10 | amount2 | 否 |  |  |
| 11 | by1 | 否 |  |  |
| 12 | by2 | 否 |  |  |
| 13 | refcash_sh_quota | 否 | H |  |
| 14 | refcash_sz_quota | 否 | H |  |
| 15 | refmarkcash_sh_quota | 否 | H |  |
| 16 | refmarkcash_sz_quota | 否 | H |  |
| 17 | init_date | 否 |  |  |
| 18 | disclosure_type | 否 |  |  |
| 19 | date1 | 否 |  |  |
| 20 | date2 | 否 |  |  |
| 21 | rate1 | 否 |  |  |
| 22 | rate2 | 否 |  |  |
| 23 | balance1 | 否 |  |  |
| 24 | balance2 | 否 |  |  |
| 25 | amount1 | 否 |  |  |
| 26 | amount2 | 否 |  |  |
| 27 | by1 | 否 |  |  |
| 28 | by2 | 否 |  |  |
| 29 | refcash_sh_quota | 否 | H |  |
| 30 | refcash_sz_quota | 否 | H |  |
| 31 | refmarkcash_sh_quota | 否 | H |  |
| 32 | refmarkcash_sz_quota | 否 | H |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refxxpl | ART | 是 | disclosure_type, disclosure_type |
| idx_refxxpl | ART | 是 | disclosure_type, disclosure_type |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_refxxpl | disclosure_type, disclosure_type |
| rpt_uk_refxxpl | init_date, disclosure_type, init_date, disclosure_type |
| idx_refxxpl | disclosure_type, disclosure_type |
| rpt_uk_refxxpl | init_date, disclosure_type, init_date, disclosure_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-16 10:32:50 | V3.0.2.4 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-10-16 10:32:50 | V3.0.2.4 | 廖宏玮 | 增加历史表索引与字段 |

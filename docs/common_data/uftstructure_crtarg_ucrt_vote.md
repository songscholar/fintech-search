# ucrt_vote - 担保品投票议案表

**表对象ID**: 7128
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | authority_code | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | vote_motion | 否 |  |  |
| 6 | vote_type | 否 |  |  |
| 7 | vote_group | 否 |  |  |
| 8 | vote_flag | 否 |  |  |
| 9 | register_date | 否 |  |  |
| 10 | begin_date | 否 |  |  |
| 11 | end_date | 否 |  |  |
| 12 | vote_director_num | 否 |  |  |
| 13 | vote_content | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | update_date | 否 |  |  |
| 16 | update_time | 否 |  |  |
| 17 | position_str | 否 |  | stock_code(8)+exchange_type(4)+vote_motion(20) |
| 18 | init_date | 否 |  |  |
| 19 | authority_code | 否 |  |  |
| 20 | stock_code | 否 |  |  |
| 21 | exchange_type | 否 |  |  |
| 22 | vote_motion | 否 |  |  |
| 23 | vote_type | 否 |  |  |
| 24 | vote_group | 否 |  |  |
| 25 | vote_flag | 否 |  |  |
| 26 | register_date | 否 |  |  |
| 27 | begin_date | 否 |  |  |
| 28 | end_date | 否 |  |  |
| 29 | vote_director_num | 否 |  |  |
| 30 | vote_content | 否 |  |  |
| 31 | transaction_no | 否 |  |  |
| 32 | update_date | 否 |  |  |
| 33 | update_time | 否 |  |  |
| 34 | position_str | 否 |  | stock_code(8)+exchange_type(4)+vote_motion(20) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdtvote | ART | 是 | stock_code, exchange_type, vote_motion, stock_code, exchange_type, vote_motion |
| uk_rpt_crdtvote | ART | 是 | init_date, stock_code, exchange_type, vote_motion, init_date, stock_code, exchange_type, vote_motion |
| idx_crdtvote | ART | 是 | stock_code, exchange_type, vote_motion, stock_code, exchange_type, vote_motion |
| uk_rpt_crdtvote | ART | 是 | init_date, stock_code, exchange_type, vote_motion, init_date, stock_code, exchange_type, vote_motion |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdtvote | stock_code, exchange_type, vote_motion, stock_code, exchange_type, vote_motion |
| idx_crdtvote | stock_code, exchange_type, vote_motion, stock_code, exchange_type, vote_motion |

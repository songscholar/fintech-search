# setttouftvoteresult - 清算投票结果明细表

**表对象ID**: 3016
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 68 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | sett_batch_no | 是 |  |  |
| 3 | sett_id | 是 |  |  |
| 4 | company_name | 是 |  |  |
| 5 | meeting_seq | 是 |  |  |
| 6 | company_code | 是 |  |  |
| 7 | begin_date | 是 |  |  |
| 8 | end_date | 是 |  |  |
| 9 | meeting_type | 是 |  |  |
| 10 | meeting_name | 是 |  |  |
| 11 | register_date | 是 |  |  |
| 12 | last_trade_date | 是 |  |  |
| 13 | stock_name | 是 |  |  |
| 14 | vote_info | 是 |  |  |
| 15 | vote_type | 是 |  |  |
| 16 | stock_code | 是 |  |  |
| 17 | client_id | 是 |  |  |
| 18 | fund_account | 是 |  |  |
| 19 | stock_account | 是 |  |  |
| 20 | exchange_type | 是 |  |  |
| 21 | business_amount | 是 |  |  |
| 22 | business_price | 是 |  |  |
| 23 | business_date | 是 |  |  |
| 24 | business_time | 是 |  |  |
| 25 | withdraw_reason | 是 |  |  |
| 26 | spare_flag | 是 |  |  |
| 27 | placard_id | 是 |  |  |
| 28 | motion_id | 是 |  |  |
| 29 | approve_amount | 是 |  |  |
| 30 | oppose_amount | 是 |  |  |
| 31 | waive_amount | 是 |  |  |
| 32 | remark | 是 |  |  |
| 33 | rej_reason | 是 |  |  |
| 34 | position_str | 是 |  |  |
| 35 | init_date | 是 |  |  |
| 36 | sett_batch_no | 是 |  |  |
| 37 | sett_id | 是 |  |  |
| 38 | company_name | 是 |  |  |
| 39 | meeting_seq | 是 |  |  |
| 40 | company_code | 是 |  |  |
| 41 | begin_date | 是 |  |  |
| 42 | end_date | 是 |  |  |
| 43 | meeting_type | 是 |  |  |
| 44 | meeting_name | 是 |  |  |
| 45 | register_date | 是 |  |  |
| 46 | last_trade_date | 是 |  |  |
| 47 | stock_name | 是 |  |  |
| 48 | vote_info | 是 |  |  |
| 49 | vote_type | 是 |  |  |
| 50 | stock_code | 是 |  |  |
| 51 | client_id | 是 |  |  |
| 52 | fund_account | 是 |  |  |
| 53 | stock_account | 是 |  |  |
| 54 | exchange_type | 是 |  |  |
| 55 | business_amount | 是 |  |  |
| 56 | business_price | 是 |  |  |
| 57 | business_date | 是 |  |  |
| 58 | business_time | 是 |  |  |
| 59 | withdraw_reason | 是 |  |  |
| 60 | spare_flag | 是 |  |  |
| 61 | placard_id | 是 |  |  |
| 62 | motion_id | 是 |  |  |
| 63 | approve_amount | 是 |  |  |
| 64 | oppose_amount | 是 |  |  |
| 65 | waive_amount | 是 |  |  |
| 66 | remark | 是 |  |  |
| 67 | rej_reason | 是 |  |  |
| 68 | position_str | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settvoteresult | 默认 | 是 | position_str, position_str |
| idx_settvoteresult | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settvoteresult | position_str, position_str |
| idx_settvoteresult | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-05-25 15:43 | 8.26.2.51 | 丁界成 | vote_info类型从HsChar255改为HsChar2000。涉及vote_info字段、votelist表或se... |
| 2020-02-04 17:12 | 8.26.1.74 | 曾哲 | 新增rej_reason字段，调整索引 |
| 2019-02-13 17:13 | 8.26.1.55 | 彭立 | 增加字段sett_batch_no |
| 2023-05-25 15:43 | 8.26.2.51 | 丁界成 | vote_info类型从HsChar255改为HsChar2000。涉及vote_info字段、votelist表或se... |
| 2020-02-04 17:12 | 8.26.1.74 | 曾哲 | 新增rej_reason字段，调整索引 |
| 2019-02-13 17:13 | 8.26.1.55 | 彭立 | 增加字段sett_batch_no |

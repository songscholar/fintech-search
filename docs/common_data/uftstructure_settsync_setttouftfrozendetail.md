# setttouftfrozendetail - 清算冻结明细表

**表对象ID**: 3017
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | sett_batch_no | 是 |  |  |
| 3 | sett_id | 是 |  |  |
| 4 | client_id | 是 |  |  |
| 5 | fund_account | 是 |  |  |
| 6 | stock_account | 是 |  |  |
| 7 | exchange_type | 是 |  |  |
| 8 | stock_code | 是 |  |  |
| 9 | frozen_amount | 是 |  |  |
| 10 | impawn_id | 是 |  |  |
| 11 | judifrozen_id | 是 |  |  |
| 12 | report_id | 是 |  |  |
| 13 | frozen_type | 是 |  |  |
| 14 | remark | 是 |  |  |
| 15 | position_str | 是 |  |  |
| 16 | begin_date | 是 |  |  |
| 17 | end_date | 是 |  |  |
| 18 | stock_property | 是 |  |  |
| 19 | sz_frozen_organname | 是 |  |  |
| 20 | init_date | 是 |  |  |
| 21 | sett_batch_no | 是 |  |  |
| 22 | sett_id | 是 |  |  |
| 23 | client_id | 是 |  |  |
| 24 | fund_account | 是 |  |  |
| 25 | stock_account | 是 |  |  |
| 26 | exchange_type | 是 |  |  |
| 27 | stock_code | 是 |  |  |
| 28 | frozen_amount | 是 |  |  |
| 29 | impawn_id | 是 |  |  |
| 30 | judifrozen_id | 是 |  |  |
| 31 | report_id | 是 |  |  |
| 32 | frozen_type | 是 |  |  |
| 33 | remark | 是 |  |  |
| 34 | position_str | 是 |  |  |
| 35 | begin_date | 是 |  |  |
| 36 | end_date | 是 |  |  |
| 37 | stock_property | 是 |  |  |
| 38 | sz_frozen_organname | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settfrozendetail_pos | 默认 | 是 | position_str, position_str |
| idx_settfrozendetail_acct | 默认 | 是 | fund_account, fund_account |
| idx_settfrozendetail_pos | 默认 | 是 | position_str, position_str |
| idx_settfrozendetail_acct | 默认 | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settfrozendetail_pos | position_str, position_str |
| idx_settfrozendetail_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2020-06-22 11:24 | 8.26.1.84 | 曾哲 | 增加begin_date,end_date,stock_property,sz_frozen_organname字段 |
| 2019-02-13 17:14 | 8.26.1.55 | 彭立 | 增加字段sett_batch_no |
| 2020-06-22 11:24 | 8.26.1.84 | 曾哲 | 增加begin_date,end_date,stock_property,sz_frozen_organname字段 |
| 2019-02-13 17:14 | 8.26.1.55 | 彭立 | 增加字段sett_batch_no |

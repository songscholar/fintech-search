# ucrt_fund_detail_bak - 两融交易资金详细信息备份表

**表对象ID**: 7605
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 44 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | fund_enable_level | 否 |  |  |
| 6 | partition_no | 否 |  |  |
| 7 | position_str | 否 |  | fund_account(18)+money_type(3)+fund_enable_level(10)+init_da |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | begin_enable_balance | 否 |  |  |
| 11 | sett_batch_no | 否 |  |  |
| 12 | init_date | 否 |  |  |
| 13 | fund_account | 否 |  |  |
| 14 | money_type | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | fund_enable_level | 否 |  |  |
| 17 | partition_no | 否 |  |  |
| 18 | position_str | 否 |  | fund_account(18)+money_type(3)+fund_enable_level(10)+init_da |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | begin_enable_balance | 否 |  |  |
| 22 | sett_batch_no | 否 |  |  |
| 23 | init_date | 否 |  |  |
| 24 | fund_account | 否 |  |  |
| 25 | money_type | 否 |  |  |
| 26 | client_id | 否 |  |  |
| 27 | fund_enable_level | 否 |  |  |
| 28 | partition_no | 否 |  |  |
| 29 | position_str | 否 |  | fund_account(18)+money_type(3)+fund_enable_level(10)+init_da |
| 30 | update_date | 否 |  |  |
| 31 | update_time | 否 |  |  |
| 32 | begin_enable_balance | 否 |  |  |
| 33 | sett_batch_no | 否 |  |  |
| 34 | init_date | 否 |  |  |
| 35 | fund_account | 否 |  |  |
| 36 | money_type | 否 |  |  |
| 37 | client_id | 否 |  |  |
| 38 | fund_enable_level | 否 |  |  |
| 39 | partition_no | 否 |  |  |
| 40 | position_str | 否 |  | fund_account(18)+money_type(3)+fund_enable_level(10)+init_da |
| 41 | update_date | 否 |  |  |
| 42 | update_time | 否 |  |  |
| 43 | begin_enable_balance | 否 |  |  |
| 44 | sett_batch_no | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_fund_detail_bak | ART | 是 | init_date, fund_account, money_type, fund_enable_level, sett_batch_no, init_date, fund_account, money_type, fund_enable_level, sett_batch_no |
| idx_ucrt_fund_detail_bak_pos | ART | 是 | position_str, position_str |
| idx_ucrt_fund_detail_bak | ART | 是 | init_date, fund_account, money_type, fund_enable_level, sett_batch_no, init_date, fund_account, money_type, fund_enable_level, sett_batch_no |
| idx_ucrt_fund_detail_bak_pos | ART | 是 | position_str, position_str |
| idx_ucrt_fund_detail_bak | ART | 是 | init_date, fund_account, money_type, fund_enable_level, sett_batch_no, init_date, fund_account, money_type, fund_enable_level, sett_batch_no |
| idx_ucrt_fund_detail_bak_pos | ART | 是 | position_str, position_str |
| idx_ucrt_fund_detail_bak | ART | 是 | init_date, fund_account, money_type, fund_enable_level, sett_batch_no, init_date, fund_account, money_type, fund_enable_level, sett_batch_no |
| idx_ucrt_fund_detail_bak_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_fund_detail_bak | init_date, fund_account, money_type, fund_enable_level, sett_batch_no, init_date, fund_account, money_type, fund_enable_level, sett_batch_no |
| idx_ucrt_fund_detail_bak | init_date, fund_account, money_type, fund_enable_level, sett_batch_no, init_date, fund_account, money_type, fund_enable_level, sett_batch_no |
| idx_ucrt_fund_detail_bak | init_date, fund_account, money_type, fund_enable_level, sett_batch_no, init_date, fund_account, money_type, fund_enable_level, sett_batch_no |
| idx_ucrt_fund_detail_bak | init_date, fund_account, money_type, fund_enable_level, sett_batch_no, init_date, fund_account, money_type, fund_enable_level, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-02 15:01:12 | 3.0.8.13 | 沈勋 | 添加表 |
| 2026-03-02 15:01:12 | 3.0.8.13 | 沈勋 |  |
| 2026-03-02 15:01:12 | 3.0.8.13 | 沈勋 | 添加表 |
| 2026-03-02 15:01:12 | 3.0.8.13 | 沈勋 |  |

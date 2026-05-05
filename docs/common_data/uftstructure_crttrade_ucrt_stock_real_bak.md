# ucrt_stock_real_bak - 两融股份交易信息备份表

**表对象ID**: 7606
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | trustee_seat_no | 否 |  |  |
| 6 | sett_batch_no | 否 |  |  |
| 7 | begin_enable_amount | 否 |  |  |
| 8 | position_str | 否 |  | fund_account(18)+exchange_type(4) +stock_account(20) +stock_ |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | trustee_seat_no | 否 |  |  |
| 16 | sett_batch_no | 否 |  |  |
| 17 | begin_enable_amount | 否 |  |  |
| 18 | position_str | 否 |  | fund_account(18)+exchange_type(4) +stock_account(20) +stock_ |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | fund_account | 否 |  |  |
| 22 | stock_account | 否 |  |  |
| 23 | exchange_type | 否 |  |  |
| 24 | stock_code | 否 |  |  |
| 25 | trustee_seat_no | 否 |  |  |
| 26 | sett_batch_no | 否 |  |  |
| 27 | begin_enable_amount | 否 |  |  |
| 28 | position_str | 否 |  | fund_account(18)+exchange_type(4) +stock_account(20) +stock_ |
| 29 | update_date | 否 |  |  |
| 30 | update_time | 否 |  |  |
| 31 | fund_account | 否 |  |  |
| 32 | stock_account | 否 |  |  |
| 33 | exchange_type | 否 |  |  |
| 34 | stock_code | 否 |  |  |
| 35 | trustee_seat_no | 否 |  |  |
| 36 | sett_batch_no | 否 |  |  |
| 37 | begin_enable_amount | 否 |  |  |
| 38 | position_str | 否 |  | fund_account(18)+exchange_type(4) +stock_account(20) +stock_ |
| 39 | update_date | 否 |  |  |
| 40 | update_time | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_stock_real_bak | ART | 是 | fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, sett_batch_no, fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, sett_batch_no |
| idx_ucrt_stock_real_bak_pos | ART | 是 | position_str, position_str |
| idx_ucrt_stock_real_bak | ART | 是 | fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, sett_batch_no, fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, sett_batch_no |
| idx_ucrt_stock_real_bak_pos | ART | 是 | position_str, position_str |
| idx_ucrt_stock_real_bak | ART | 是 | fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, sett_batch_no, fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, sett_batch_no |
| idx_ucrt_stock_real_bak_pos | ART | 是 | position_str, position_str |
| idx_ucrt_stock_real_bak | ART | 是 | fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, sett_batch_no, fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, sett_batch_no |
| idx_ucrt_stock_real_bak_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_stock_real_bak | fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, sett_batch_no, fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, sett_batch_no |
| idx_ucrt_stock_real_bak | fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, sett_batch_no, fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, sett_batch_no |
| idx_ucrt_stock_real_bak | fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, sett_batch_no, fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, sett_batch_no |
| idx_ucrt_stock_real_bak | fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, sett_batch_no, fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-02 15:01:33 | 3.0.8.14 | 沈勋 | 添加表 |
| 2026-03-02 15:01:33 | 3.0.8.14 | 沈勋 |  |
| 2026-03-02 15:01:33 | 3.0.8.14 | 沈勋 | 添加表 |
| 2026-03-02 15:01:33 | 3.0.8.14 | 沈勋 |  |

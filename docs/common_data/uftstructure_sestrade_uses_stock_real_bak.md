# uses_stock_real_bak - 证券股份交易信息备份表

**表对象ID**: 5758
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | trustee_seat_no | 否 |  |  |
| 6 | position_str | 否 |  | branch_no(5) +fund_account(18)+exchange_type(4) +stock_accou |
| 7 | update_date | 否 |  |  |
| 8 | update_time | 否 |  |  |
| 9 | begin_enable_amount | 否 |  |  |
| 10 | sett_batch_no | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | trustee_seat_no | 否 |  |  |
| 16 | position_str | 否 |  | branch_no(5) +fund_account(18)+exchange_type(4) +stock_accou |
| 17 | update_date | 否 |  |  |
| 18 | update_time | 否 |  |  |
| 19 | begin_enable_amount | 否 |  |  |
| 20 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_stockreal_bak_unique | ART | 是 | stock_account, exchange_type, fund_account, stock_code, trustee_seat_no, sett_batch_no, stock_account, exchange_type, fund_account, stock_code, trustee_seat_no, sett_batch_no |
| idx_uses_stockreal_bak_unique | ART | 是 | stock_account, exchange_type, fund_account, stock_code, trustee_seat_no, sett_batch_no, stock_account, exchange_type, fund_account, stock_code, trustee_seat_no, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_stockreal_bak_unique | stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, sett_batch_no, stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, sett_batch_no |
| idx_uses_stockreal_bak_unique | stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, sett_batch_no, stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-02-05 21:59 | 3.0.0.1 | 杨新照 | 新增表结构 |
| 2026-02-05 21:59 | 3.0.0.1 | 杨新照 | 新增表结构 |

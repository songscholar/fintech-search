# uref_ext_stkres - 转融通外部券源信息表

**表对象ID**: 6201
**所属模块**: reffsman
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | refextstkres_id | 否 |  |  |
| 3 | refextstkres_type | 否 |  |  |
| 4 | company_no | 否 |  |  |
| 5 | company_name | 否 |  |  |
| 6 | holder_name | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | seat_no | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | stock_name | 否 |  |  |
| 12 | current_amount | 否 |  |  |
| 13 | used_amount | 否 |  |  |
| 14 | end_date | 否 |  |  |
| 15 | relation_name | 否 |  |  |
| 16 | relation_tel | 否 |  |  |
| 17 | relation_mobile | 否 |  |  |
| 18 | company_tel | 否 |  |  |
| 19 | position_str | 否 |  |  |
| 20 | stock_type | 否 | H |  |
| 21 | sub_stock_type | 否 | H |  |
| 22 | init_date | 否 |  |  |
| 23 | refextstkres_id | 否 |  |  |
| 24 | refextstkres_type | 否 |  |  |
| 25 | company_no | 否 |  |  |
| 26 | company_name | 否 |  |  |
| 27 | holder_name | 否 |  |  |
| 28 | stock_account | 否 |  |  |
| 29 | seat_no | 否 |  |  |
| 30 | exchange_type | 否 |  |  |
| 31 | stock_code | 否 |  |  |
| 32 | stock_name | 否 |  |  |
| 33 | current_amount | 否 |  |  |
| 34 | used_amount | 否 |  |  |
| 35 | end_date | 否 |  |  |
| 36 | relation_name | 否 |  |  |
| 37 | relation_tel | 否 |  |  |
| 38 | relation_mobile | 否 |  |  |
| 39 | company_tel | 否 |  |  |
| 40 | position_str | 否 |  |  |
| 41 | stock_type | 否 | H |  |
| 42 | sub_stock_type | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refextstkres | ART | 是 | refextstkres_id, refextstkres_id |
| idx_refextstkres_acct | ART | 是 | stock_code, stock_account, stock_code, stock_account |
| idx_refextstkres_pos | ART | 是 | position_str, position_str |
| idx_refextstkres | ART | 是 | refextstkres_id, refextstkres_id |
| idx_refextstkres_acct | ART | 是 | stock_code, stock_account, stock_code, stock_account |
| idx_refextstkres_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 10 个）

| 索引名 | 字段 |
|--------|------|
| idx_refextstkres | refextstkres_id, refextstkres_id |
| idx_refextstkres_acct | stock_code, stock_account, stock_code, stock_account |
| idx_refextstkres_pos | position_str, position_str |
| uk_rpt_urefextstkres | init_date, position_str, init_date, position_str |
| idx_rpt_urefextstkres_acct | stock_account, position_str, stock_account, position_str |
| idx_refextstkres | refextstkres_id, refextstkres_id |
| idx_refextstkres_acct | stock_code, stock_account, stock_code, stock_account |
| idx_refextstkres_pos | position_str, position_str |
| uk_rpt_urefextstkres | init_date, position_str, init_date, position_str |
| idx_rpt_urefextstkres_acct | stock_account, position_str, stock_account, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-16 10:33:34 | V3.0.2.1 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-10-16 10:33:34 | V3.0.2.1 | 廖宏玮 | 增加历史表索引与字段 |

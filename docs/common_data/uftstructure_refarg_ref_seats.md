# ref_seats - 转融通席位表

**表对象ID**: 6012
**所属模块**: refarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | csfc_borrow_account | 否 |  |  |
| 3 | organ_name | 否 |  |  |
| 4 | report_date | 否 |  |  |
| 5 | csdc_ref_account | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | seat_no | 否 |  |  |
| 8 | reserve_account | 否 |  |  |
| 9 | refreturn_status | 否 |  |  |
| 10 | affirm_date | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | position_str | 否 |  | seat_no(8)+exchange_type(4)+company_no(4) |
| 15 | company_no | 否 |  |  |
| 16 | csfc_borrow_account | 否 |  |  |
| 17 | organ_name | 否 |  |  |
| 18 | report_date | 否 |  |  |
| 19 | csdc_ref_account | 否 |  |  |
| 20 | exchange_type | 否 |  |  |
| 21 | seat_no | 否 |  |  |
| 22 | reserve_account | 否 |  |  |
| 23 | refreturn_status | 否 |  |  |
| 24 | affirm_date | 否 |  |  |
| 25 | update_date | 否 |  |  |
| 26 | update_time | 否 |  |  |
| 27 | transaction_no | 否 |  |  |
| 28 | position_str | 否 |  | seat_no(8)+exchange_type(4)+company_no(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ref_seats | ART | 是 | seat_no, exchange_type, company_no, seat_no, exchange_type, company_no |
| idx_ref_seats | ART | 是 | seat_no, exchange_type, company_no, seat_no, exchange_type, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ref_seats | seat_no, exchange_type, company_no, seat_no, exchange_type, company_no |
| idx_ref_seats | seat_no, exchange_type, company_no, seat_no, exchange_type, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-21 16:14:38 | 1.0.0.13 | 李想 | 新增表 |
| 2025-02-21 16:14:38 | 1.0.0.13 | 李想 | 新增表 |

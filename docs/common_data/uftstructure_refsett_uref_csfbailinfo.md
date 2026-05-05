# uref_csfbailinfo - 保证金综合信息表

**表对象ID**: 6156
**所属模块**: refsett
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 50 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | company_no | 否 |  |  |
| 3 | min_refscale_ratio | 否 |  |  |
| 4 | refscale_ratio | 否 |  |  |
| 5 | refcompact_value | 否 |  |  |
| 6 | min_ref_value | 否 |  |  |
| 7 | min_refcash_ratio | 否 |  |  |
| 8 | refcash_ratio | 否 |  |  |
| 9 | min_reffund_value | 否 |  |  |
| 10 | reffund_value | 否 |  |  |
| 11 | cash_balance | 否 |  |  |
| 12 | fin_equplus_balance | 否 |  |  |
| 13 | csfc_use_balance | 否 |  |  |
| 14 | market_value | 否 |  |  |
| 15 | refstock_value | 否 |  |  |
| 16 | ref_value | 否 |  |  |
| 17 | assure_market_value | 否 |  |  |
| 18 | csfc_refstock_value | 否 |  |  |
| 19 | correct_market_value | 否 |  |  |
| 20 | remind_reffund_value | 否 |  |  |
| 21 | remind_ref_value | 否 |  |  |
| 22 | enable_quota | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | csfc_borrow_accttype | 否 |  |  |
| 25 | position_str | 否 |  | company_no(10)+csfc_borrow_accttype(1) |
| 26 | init_date | 否 |  |  |
| 27 | company_no | 否 |  |  |
| 28 | min_refscale_ratio | 否 |  |  |
| 29 | refscale_ratio | 否 |  |  |
| 30 | refcompact_value | 否 |  |  |
| 31 | min_ref_value | 否 |  |  |
| 32 | min_refcash_ratio | 否 |  |  |
| 33 | refcash_ratio | 否 |  |  |
| 34 | min_reffund_value | 否 |  |  |
| 35 | reffund_value | 否 |  |  |
| 36 | cash_balance | 否 |  |  |
| 37 | fin_equplus_balance | 否 |  |  |
| 38 | csfc_use_balance | 否 |  |  |
| 39 | market_value | 否 |  |  |
| 40 | refstock_value | 否 |  |  |
| 41 | ref_value | 否 |  |  |
| 42 | assure_market_value | 否 |  |  |
| 43 | csfc_refstock_value | 否 |  |  |
| 44 | correct_market_value | 否 |  |  |
| 45 | remind_reffund_value | 否 |  |  |
| 46 | remind_ref_value | 否 |  |  |
| 47 | enable_quota | 否 |  |  |
| 48 | remark | 否 |  |  |
| 49 | csfc_borrow_accttype | 否 |  |  |
| 50 | position_str | 否 |  | company_no(10)+csfc_borrow_accttype(1) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refcsfbailinfo | ART | 是 | company_no, csfc_borrow_accttype, company_no, csfc_borrow_accttype |
| idx_refcsfbailinfo | ART | 是 | company_no, csfc_borrow_accttype, company_no, csfc_borrow_accttype |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_refcsfbailinfo | company_no, csfc_borrow_accttype, company_no, csfc_borrow_accttype |
| uk_rpt_urefcsfbailinfo | init_date, position_str, init_date, position_str |
| idx_refcsfbailinfo | company_no, csfc_borrow_accttype, company_no, csfc_borrow_accttype |
| uk_rpt_urefcsfbailinfo | init_date, position_str, init_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-16 10:38:52 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-10-16 10:38:52 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

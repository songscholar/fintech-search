# ref_busiarg - 转融通业务参数表

**表对象ID**: 6008
**所属模块**: refarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 80 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | csfc_borrow_account | 否 |  |  |
| 3 | csdc_ref_account | 否 |  |  |
| 4 | reserve_account_shself | 否 |  |  |
| 5 | reserve_account_szself | 否 |  |  |
| 6 | reserve_account_shcrdt | 否 |  |  |
| 7 | reserve_account_szcrdt | 否 |  |  |
| 8 | settle_account_secu | 否 |  |  |
| 9 | settle_account_fund | 否 |  |  |
| 10 | szdc_main_seat | 否 |  |  |
| 11 | credit_date | 否 |  |  |
| 12 | credit_end_date | 否 |  |  |
| 13 | credit_quota | 否 |  |  |
| 14 | crdt_used_quota | 否 |  |  |
| 15 | min_refscale_ratio | 否 |  |  |
| 16 | min_refcash_ratio | 否 |  |  |
| 17 | max_refmarket_ratio | 否 |  |  |
| 18 | refdraw_ratio | 否 |  |  |
| 19 | net_capital | 否 |  |  |
| 20 | fine_rate | 否 |  |  |
| 21 | selfund_cost_rate | 否 |  |  |
| 22 | refcash_sh_quota | 否 |  |  |
| 23 | refcash_sz_quota | 否 |  |  |
| 24 | ref_value | 否 |  |  |
| 25 | refcompact_value | 否 |  |  |
| 26 | refscale_ratio | 否 |  |  |
| 27 | refcash_ratio | 否 |  |  |
| 28 | stibpaybail_flag | 否 |  |  |
| 29 | csfc_borrow_accttype | 否 |  |  |
| 30 | refmarkcash_sh_quota | 否 |  |  |
| 31 | refmarkcash_sz_quota | 否 |  |  |
| 32 | refmarkcash_sz_quota_t1 | 否 |  |  |
| 33 | refmarkcash_sh_quota_t1 | 否 |  |  |
| 34 | fin_credit_quota | 否 |  |  |
| 35 | fin_used_quota | 否 |  |  |
| 36 | refslo_upper_limit | 否 |  |  |
| 37 | update_date | 否 |  |  |
| 38 | update_time | 否 |  |  |
| 39 | transaction_no | 否 |  |  |
| 40 | position_str | 否 |  | company_no(4)+csfc_borrow_accttype(1) |
| 41 | company_no | 否 |  |  |
| 42 | csfc_borrow_account | 否 |  |  |
| 43 | csdc_ref_account | 否 |  |  |
| 44 | reserve_account_shself | 否 |  |  |
| 45 | reserve_account_szself | 否 |  |  |
| 46 | reserve_account_shcrdt | 否 |  |  |
| 47 | reserve_account_szcrdt | 否 |  |  |
| 48 | settle_account_secu | 否 |  |  |
| 49 | settle_account_fund | 否 |  |  |
| 50 | szdc_main_seat | 否 |  |  |
| 51 | credit_date | 否 |  |  |
| 52 | credit_end_date | 否 |  |  |
| 53 | credit_quota | 否 |  |  |
| 54 | crdt_used_quota | 否 |  |  |
| 55 | min_refscale_ratio | 否 |  |  |
| 56 | min_refcash_ratio | 否 |  |  |
| 57 | max_refmarket_ratio | 否 |  |  |
| 58 | refdraw_ratio | 否 |  |  |
| 59 | net_capital | 否 |  |  |
| 60 | fine_rate | 否 |  |  |
| 61 | selfund_cost_rate | 否 |  |  |
| 62 | refcash_sh_quota | 否 |  |  |
| 63 | refcash_sz_quota | 否 |  |  |
| 64 | ref_value | 否 |  |  |
| 65 | refcompact_value | 否 |  |  |
| 66 | refscale_ratio | 否 |  |  |
| 67 | refcash_ratio | 否 |  |  |
| 68 | stibpaybail_flag | 否 |  |  |
| 69 | csfc_borrow_accttype | 否 |  |  |
| 70 | refmarkcash_sh_quota | 否 |  |  |
| 71 | refmarkcash_sz_quota | 否 |  |  |
| 72 | refmarkcash_sz_quota_t1 | 否 |  |  |
| 73 | refmarkcash_sh_quota_t1 | 否 |  |  |
| 74 | fin_credit_quota | 否 |  |  |
| 75 | fin_used_quota | 否 |  |  |
| 76 | refslo_upper_limit | 否 |  |  |
| 77 | update_date | 否 |  |  |
| 78 | update_time | 否 |  |  |
| 79 | transaction_no | 否 |  |  |
| 80 | position_str | 否 |  | company_no(4)+csfc_borrow_accttype(1) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ref_busiarg | ART | 是 | company_no, csfc_borrow_accttype, company_no, csfc_borrow_accttype |
| idx_ref_busiarg | ART | 是 | company_no, csfc_borrow_accttype, company_no, csfc_borrow_accttype |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ref_busiarg | company_no, csfc_borrow_accttype, company_no, csfc_borrow_accttype |
| idx_ref_busiarg | company_no, csfc_borrow_accttype, company_no, csfc_borrow_accttype |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-06-06 15:33:36 | 1.0.0.14 | 常行 | 表空间改为HS_UFT_DATA |
| 2025-02-21 11:03:59 | 1.0.0.7 | 李想 | 新增表 |
| 2025-06-06 15:33:36 | 1.0.0.14 | 常行 | 表空间改为HS_UFT_DATA |
| 2025-02-21 11:03:59 | 1.0.0.7 | 李想 | 新增表 |

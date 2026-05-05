# ref_return_account - 转融通资金归还账户表

**表对象ID**: 6031
**所属模块**: refacct
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | reffundrtacct_type | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | payer_bank_no | 否 |  |  |
| 4 | shdc_payer_bank_name | 否 |  |  |
| 5 | shdc_payer_account | 否 |  |  |
| 6 | shdc_payer_name | 否 |  |  |
| 7 | oppo_bank_no | 否 |  |  |
| 8 | shdc_oppo_bank_name | 否 |  |  |
| 9 | shdc_oppo_account | 否 |  |  |
| 10 | shdc_oppo_name | 否 |  |  |
| 11 | remark | 否 |  |  |
| 12 | company_no | 否 |  |  |
| 13 | csfc_borrow_accttype | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | position_str | 否 |  | exchange_type(4)+reffundrtacct_type(1)+company_no(4)+csfc_bo |
| 18 | reffundrtacct_type | 否 |  |  |
| 19 | exchange_type | 否 |  |  |
| 20 | payer_bank_no | 否 |  |  |
| 21 | shdc_payer_bank_name | 否 |  |  |
| 22 | shdc_payer_account | 否 |  |  |
| 23 | shdc_payer_name | 否 |  |  |
| 24 | oppo_bank_no | 否 |  |  |
| 25 | shdc_oppo_bank_name | 否 |  |  |
| 26 | shdc_oppo_account | 否 |  |  |
| 27 | shdc_oppo_name | 否 |  |  |
| 28 | remark | 否 |  |  |
| 29 | company_no | 否 |  |  |
| 30 | csfc_borrow_accttype | 否 |  |  |
| 31 | update_date | 否 |  |  |
| 32 | update_time | 否 |  |  |
| 33 | transaction_no | 否 |  |  |
| 34 | position_str | 否 |  | exchange_type(4)+reffundrtacct_type(1)+company_no(4)+csfc_bo |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ref_return_account | ART | 是 | exchange_type, reffundrtacct_type, company_no, csfc_borrow_accttype, exchange_type, reffundrtacct_type, company_no, csfc_borrow_accttype |
| idx_ref_return_account | ART | 是 | exchange_type, reffundrtacct_type, company_no, csfc_borrow_accttype, exchange_type, reffundrtacct_type, company_no, csfc_borrow_accttype |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ref_return_account | exchange_type, reffundrtacct_type, company_no, csfc_borrow_accttype, exchange_type, reffundrtacct_type, company_no, csfc_borrow_accttype |
| idx_ref_return_account | exchange_type, reffundrtacct_type, company_no, csfc_borrow_accttype, exchange_type, reffundrtacct_type, company_no, csfc_borrow_accttype |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-21 11:37:51 | 1.0.0.2 | 李想 | 新增表 |
| 2025-02-21 11:37:51 | 1.0.0.2 | 李想 | 新增表 |

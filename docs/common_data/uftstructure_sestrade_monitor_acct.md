# monitor_acct - 重点监控账户表

**表对象ID**: 5537
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | acode_account | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | csfc_company_no | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | risk_type_str | 否 |  |  |
| 7 | begin_date | 否 |  |  |
| 8 | end_date | 否 |  |  |
| 9 | is_list_acct | 否 |  |  |
| 10 | mark_date | 否 |  |  |
| 11 | data_check_status | 否 |  |  |
| 12 | valid_flag | 否 |  |  |
| 13 | import_flag | 否 |  |  |
| 14 | limit_begin_date | 否 |  |  |
| 15 | limit_end_date | 否 |  |  |
| 16 | en_monitorlist_type | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | acode_account | 否 |  |  |
| 19 | stock_account | 否 |  |  |
| 20 | csfc_company_no | 否 |  |  |
| 21 | fund_account | 否 |  |  |
| 22 | exchange_type | 否 |  |  |
| 23 | risk_type_str | 否 |  |  |
| 24 | begin_date | 否 |  |  |
| 25 | end_date | 否 |  |  |
| 26 | is_list_acct | 否 |  |  |
| 27 | mark_date | 否 |  |  |
| 28 | data_check_status | 否 |  |  |
| 29 | valid_flag | 否 |  |  |
| 30 | import_flag | 否 |  |  |
| 31 | limit_begin_date | 否 |  |  |
| 32 | limit_end_date | 否 |  |  |
| 33 | en_monitorlist_type | 否 |  |  |
| 34 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_monitor_acct | ART | 是 | csfc_company_no, fund_account, stock_account, exchange_type, acode_account, csfc_company_no, fund_account, stock_account, exchange_type, acode_account |
| idx_monitor_acct_acode | ART | 是 | acode_account, acode_account |
| idx_monitor_acct | ART | 是 | csfc_company_no, fund_account, stock_account, exchange_type, acode_account, csfc_company_no, fund_account, stock_account, exchange_type, acode_account |
| idx_monitor_acct_acode | ART | 是 | acode_account, acode_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_monitor_acct | acode_account, stock_account, csfc_company_no, fund_account, exchange_type, acode_account, stock_account, csfc_company_no, fund_account, exchange_type |
| idx_monitor_acct | acode_account, stock_account, csfc_company_no, fund_account, exchange_type, acode_account, stock_account, csfc_company_no, fund_account, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:52:23 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-09-25 20:08:13 | V3.0.8.5 | 陆良铠 | 所有表monitor_acct，修改了表字段类型（csfc_company_no）；
 |
| 2024-06-19 20:51:33 | 3.0.2.21 | 董乾坤 | 物理表monitor_acct，添加了表字段(acode_account);
物理表monitor_acct，添加了表... |
| 2026-03-09 13:52:23 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-09-25 20:08:13 | V3.0.8.5 | 陆良铠 | 所有表monitor_acct，修改了表字段类型（csfc_company_no）；
 |
| 2024-06-19 20:51:33 | 3.0.2.21 | 董乾坤 | 物理表monitor_acct，添加了表字段(acode_account);
物理表monitor_acct，添加了表... |

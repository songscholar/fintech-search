# ucrt_acct_busi_control - 客户个性化业务控制表

**表对象ID**: 7005
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | crdt_business_type | 否 |  |  |
| 5 | control_flag | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | stock_type | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | compact_type | 否 |  |  |
| 10 | compact_id | 否 |  |  |
| 11 | remark | 否 |  |  |
| 12 | create_date | 否 |  |  |
| 13 | end_date | 否 |  |  |
| 14 | en_crdt_busi_type | 否 |  |  |
| 15 | crdt_limit_reason | 否 |  |  |
| 16 | res_entrust_way | 否 |  |  |
| 17 | en_compact_source | 否 |  |  |
| 18 | en_crdtrisk_no | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | company_no | 否 |  |  |
| 21 | client_id | 否 |  |  |
| 22 | fund_account | 否 |  |  |
| 23 | crdt_business_type | 否 |  |  |
| 24 | control_flag | 否 |  |  |
| 25 | stock_code | 否 |  |  |
| 26 | stock_type | 否 |  |  |
| 27 | exchange_type | 否 |  |  |
| 28 | compact_type | 否 |  |  |
| 29 | compact_id | 否 |  |  |
| 30 | remark | 否 |  |  |
| 31 | create_date | 否 |  |  |
| 32 | end_date | 否 |  |  |
| 33 | en_crdt_busi_type | 否 |  |  |
| 34 | crdt_limit_reason | 否 |  |  |
| 35 | res_entrust_way | 否 |  |  |
| 36 | en_compact_source | 否 |  |  |
| 37 | en_crdtrisk_no | 否 |  |  |
| 38 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_ucrt_acct_busi_control | 默认 | 否 | compact_type, compact_type |
| idx_ucrt_acct_busi_control_unique | ART | 是 | fund_account, crdt_business_type, stock_code, exchange_type, compact_id, crdt_limit_reason, company_no, compact_type, fund_account, crdt_business_type, stock_code, exchange_type, compact_id, crdt_limit_reason, company_no, compact_type |
| uk_ucrt_acct_busi_control | 默认 | 否 | compact_type, compact_type |
| idx_ucrt_acct_busi_control_unique | ART | 是 | fund_account, crdt_business_type, stock_code, exchange_type, compact_id, crdt_limit_reason, company_no, compact_type, fund_account, crdt_business_type, stock_code, exchange_type, compact_id, crdt_limit_reason, company_no, compact_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_acct_busi_control | fund_account, crdt_business_type, stock_code, exchange_type, compact_id, crdt_limit_reason, company_no, compact_type, fund_account, crdt_business_type, stock_code, exchange_type, compact_id, crdt_limit_reason, company_no, compact_type |
| idx_ucrt_acct_busi_control | fund_account, crdt_business_type, stock_code, exchange_type, compact_id, crdt_limit_reason, company_no, compact_type, fund_account, crdt_business_type, stock_code, exchange_type, compact_id, crdt_limit_reason, company_no, compact_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-05-15 10:10:42 | 3.0.6.54 | 汪杰 | 物理表ucrt_acct_busi_control，增加索引字段(索引uk_ucrt_acct_busi_control... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:21 | 0.3.3.107 | 董瑞辉 | 新增表字段en_crdtrisk_no，transaction_no；新增索引 |
| 2025-05-15 10:10:42 | 3.0.6.54 | 汪杰 | 物理表ucrt_acct_busi_control，增加索引字段(索引uk_ucrt_acct_busi_control... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:21 | 0.3.3.107 | 董瑞辉 | 新增表字段en_crdtrisk_no，transaction_no；新增索引 |

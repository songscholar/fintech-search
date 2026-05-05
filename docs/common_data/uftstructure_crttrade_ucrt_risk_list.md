# ucrt_risk_list - 客户信用记录表

**表对象ID**: 7537
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | seat_no | 否 |  |  |
| 5 | stock_account_sh | 否 |  |  |
| 6 | stock_account_sz | 否 |  |  |
| 7 | fine_balance | 否 |  |  |
| 8 | crdtfine_type | 否 |  |  |
| 9 | crdtfine_src_type | 否 |  |  |
| 10 | crdtfine_rpt_type | 否 |  |  |
| 11 | crdtfine_no | 否 |  |  |
| 12 | create_date | 否 |  |  |
| 13 | stock_account_stb | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | company_no | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | fund_account | 否 |  |  |
| 18 | seat_no | 否 |  |  |
| 19 | stock_account_sh | 否 |  |  |
| 20 | stock_account_sz | 否 |  |  |
| 21 | fine_balance | 否 |  |  |
| 22 | crdtfine_type | 否 |  |  |
| 23 | crdtfine_src_type | 否 |  |  |
| 24 | crdtfine_rpt_type | 否 |  |  |
| 25 | crdtfine_no | 否 |  |  |
| 26 | create_date | 否 |  |  |
| 27 | stock_account_stb | 否 |  |  |
| 28 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_risk_list | ART | 是 | fund_account, crdtfine_rpt_type, create_date, crdtfine_type, crdtfine_no, fund_account, crdtfine_rpt_type, create_date, crdtfine_type, crdtfine_no |
| idx_ucrt_risk_list | ART | 是 | fund_account, crdtfine_rpt_type, create_date, crdtfine_type, crdtfine_no, fund_account, crdtfine_rpt_type, create_date, crdtfine_type, crdtfine_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_risk_list | fund_account, create_date, crdtfine_type, crdtfine_no, crdtfine_rpt_type, fund_account, create_date, crdtfine_type, crdtfine_no, crdtfine_rpt_type |
| idx_ucrt_risk_list | fund_account, create_date, crdtfine_type, crdtfine_no, crdtfine_rpt_type, fund_account, create_date, crdtfine_type, crdtfine_no, crdtfine_rpt_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-23 18:39:36 | 0.3.3.142 | 徐志坚 | 增加transaction_no字段 |
| 2023-08-23 09:12:11 | 0.3.3.142 | 徐志坚 | 为了参数同步增加transaction_no字段，并将原来索引改为分级索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-23 18:39:36 | 0.3.3.142 | 徐志坚 | 增加transaction_no字段 |
| 2023-08-23 09:12:11 | 0.3.3.142 | 徐志坚 | 为了参数同步增加transaction_no字段，并将原来索引改为分级索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

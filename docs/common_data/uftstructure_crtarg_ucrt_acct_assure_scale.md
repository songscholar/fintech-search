# ucrt_acct_assure_scale - 个人维持担保比例参数表

**表对象ID**: 7000
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | assurescale_type | 否 |  |  |
| 4 | assurescale_value | 否 |  |  |
| 5 | end_date | 否 |  |  |
| 6 | dynamic_flag | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | tohis_date | 否 | H |  |
| 9 | client_name | 否 | H |  |
| 10 | corp_client_group | 否 | H |  |
| 11 | branch_no | 否 | H |  |
| 12 | client_group | 否 | H |  |
| 13 | room_code | 否 | H |  |
| 14 | asset_prop | 否 | H |  |
| 15 | limit_flag | 否 | H |  |
| 16 | client_prop | 否 | H |  |
| 17 | asset_level | 否 | H |  |
| 18 | risk_level | 否 | H |  |
| 19 | corp_risk_level | 否 | H |  |
| 20 | client_id | 否 |  |  |
| 21 | fund_account | 否 |  |  |
| 22 | assurescale_type | 否 |  |  |
| 23 | assurescale_value | 否 |  |  |
| 24 | end_date | 否 |  |  |
| 25 | dynamic_flag | 否 |  |  |
| 26 | transaction_no | 否 |  |  |
| 27 | tohis_date | 否 | H |  |
| 28 | client_name | 否 | H |  |
| 29 | corp_client_group | 否 | H |  |
| 30 | branch_no | 否 | H |  |
| 31 | client_group | 否 | H |  |
| 32 | room_code | 否 | H |  |
| 33 | asset_prop | 否 | H |  |
| 34 | limit_flag | 否 | H |  |
| 35 | client_prop | 否 | H |  |
| 36 | asset_level | 否 | H |  |
| 37 | risk_level | 否 | H |  |
| 38 | corp_risk_level | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_acct_assure_scale_uk | ART | 是 | fund_account, assurescale_type, fund_account, assurescale_type |
| uk_ucrt_acct_assure_scale | ART | 是 | tohis_date, fund_account, assurescale_type, tohis_date, fund_account, assurescale_type |
| idx_ucrt_acct_assure_scale_uk | ART | 是 | fund_account, assurescale_type, fund_account, assurescale_type |
| uk_ucrt_acct_assure_scale | ART | 是 | tohis_date, fund_account, assurescale_type, tohis_date, fund_account, assurescale_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_acct_assure_scale_uk | fund_account, assurescale_type, fund_account, assurescale_type |
| idx_ucrt_acct_assure_scale_uk | fund_account, assurescale_type, fund_account, assurescale_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:21 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2015-04-13 11:00 | 0.0.0.1 |  | 新增期权交易时间表 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:21 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2015-04-13 11:00 | 0.0.0.1 |  | 新增期权交易时间表 |

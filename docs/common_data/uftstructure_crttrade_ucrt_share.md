# ucrt_share - 理财证券份额表

**表对象ID**: 7500
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | prodta_no | 否 |  |  |
| 4 | prod_code | 否 |  |  |
| 5 | prodcode_type | 否 |  |  |
| 6 | current_amount | 否 |  |  |
| 7 | position_str | 否 |  | fund_account(18)+prodta_no(24)+prod_code(32)+prodcode_type(1 |
| 8 | tohis_date | 否 | H |  |
| 9 | branch_no | 否 | H |  |
| 10 | client_name | 否 | H |  |
| 11 | corp_client_group | 否 | H |  |
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
| 22 | prodta_no | 否 |  |  |
| 23 | prod_code | 否 |  |  |
| 24 | prodcode_type | 否 |  |  |
| 25 | current_amount | 否 |  |  |
| 26 | position_str | 否 |  | fund_account(18)+prodta_no(24)+prod_code(32)+prodcode_type(1 |
| 27 | tohis_date | 否 | H |  |
| 28 | branch_no | 否 | H |  |
| 29 | client_name | 否 | H |  |
| 30 | corp_client_group | 否 | H |  |
| 31 | client_group | 否 | H |  |
| 32 | room_code | 否 | H |  |
| 33 | asset_prop | 否 | H |  |
| 34 | limit_flag | 否 | H |  |
| 35 | client_prop | 否 | H |  |
| 36 | asset_level | 否 | H |  |
| 37 | risk_level | 否 | H |  |
| 38 | corp_risk_level | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_share | ART | 是 | fund_account, prodta_no, prod_code, prodcode_type, fund_account, prodta_no, prod_code, prodcode_type |
| idx_ucrt_share_no | ART | 是 | fund_account, prodta_no, fund_account, prodta_no |
| idx_ucrt_share | ART | 是 | fund_account, prodta_no, prod_code, prodcode_type, fund_account, prodta_no, prod_code, prodcode_type |
| uk_rpt_ucrtshare | ART | 是 | tohis_date, position_str, tohis_date, position_str |
| idx_ucrt_share | ART | 是 | fund_account, prodta_no, prod_code, prodcode_type, fund_account, prodta_no, prod_code, prodcode_type |
| idx_ucrt_share_no | ART | 是 | fund_account, prodta_no, fund_account, prodta_no |
| idx_ucrt_share | ART | 是 | fund_account, prodta_no, prod_code, prodcode_type, fund_account, prodta_no, prod_code, prodcode_type |
| uk_rpt_ucrtshare | ART | 是 | tohis_date, position_str, tohis_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_share | fund_account, prodta_no, prod_code, prodcode_type, fund_account, prodta_no, prod_code, prodcode_type |
| idx_ucrt_share | fund_account, prodta_no, prod_code, prodcode_type, fund_account, prodta_no, prod_code, prodcode_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-15 15:18:03 | 3.0.8.12 | 袁文龙 | 物理表ucrt_share，增加索引（ idx_ucrt_share） |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-01-15 15:18:03 | 3.0.8.12 | 袁文龙 | 物理表ucrt_share，增加索引（ idx_ucrt_share） |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

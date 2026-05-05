# uarg_acct_assure_scale - 个人维持担保比例参数表2

**表对象ID**: 7112
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | assurescale_type | 否 |  |  |
| 4 | assurescale_value | 否 |  |  |
| 5 | end_date | 否 |  |  |
| 6 | dynamic_flag | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | branch_no | 否 |  |  |
| 9 | old_assurescale_value | 否 |  |  |
| 10 | source_arg | 否 |  |  |
| 11 | remark | 否 |  |  |
| 12 | update_date | 否 |  |  |
| 13 | update_time | 否 |  |  |
| 14 | position_str | 否 |  | fund_account(18)+assurescale_type(1) |
| 15 | tohis_date | 否 | H |  |
| 16 | client_id | 否 |  |  |
| 17 | fund_account | 否 |  |  |
| 18 | assurescale_type | 否 |  |  |
| 19 | assurescale_value | 否 |  |  |
| 20 | end_date | 否 |  |  |
| 21 | dynamic_flag | 否 |  |  |
| 22 | transaction_no | 否 |  |  |
| 23 | branch_no | 否 |  |  |
| 24 | old_assurescale_value | 否 |  |  |
| 25 | source_arg | 否 |  |  |
| 26 | remark | 否 |  |  |
| 27 | update_date | 否 |  |  |
| 28 | update_time | 否 |  |  |
| 29 | position_str | 否 |  | fund_account(18)+assurescale_type(1) |
| 30 | tohis_date | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_acct_assure_scale_uk | ART | 是 | fund_account, assurescale_type, fund_account, assurescale_type |
| uk_rpt_uargacctassurescale | ART | 是 | tohis_date, position_str, tohis_date, position_str |
| idx_uarg_acct_assure_scale_uk | ART | 是 | fund_account, assurescale_type, fund_account, assurescale_type |
| uk_rpt_uargacctassurescale | ART | 是 | tohis_date, position_str, tohis_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_acct_assure_scale_uk | fund_account, assurescale_type, fund_account, assurescale_type |
| idx_uarg_acct_assure_scale_uk | fund_account, assurescale_type, fund_account, assurescale_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-20 20:06:14 | 3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-03-13 14:56:09 | 3.0.6.100 | 李想 | 新增表 |
| 2025-11-20 20:06:14 | 3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-03-13 14:56:09 | 3.0.6.100 | 李想 | 新增表 |

# ucrt_spcash_fund - 客户专项头寸资金表

**表对象ID**: 8001
**所属模块**: crtspcash
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | cashgroup_no | 否 |  |  |
| 2 | money_type | 否 |  |  |
| 3 | fin_total_balance | 否 |  |  |
| 4 | fin_used_balance | 否 |  |  |
| 5 | ref_due_balance | 否 |  |  |
| 6 | frozen_balance | 否 |  |  |
| 7 | enable_balance | 否 |  |  |
| 8 | cash_interest | 否 |  |  |
| 9 | tohis_date | 否 | H |  |
| 10 | cashgroup_no | 否 |  |  |
| 11 | money_type | 否 |  |  |
| 12 | fin_total_balance | 否 |  |  |
| 13 | fin_used_balance | 否 |  |  |
| 14 | ref_due_balance | 否 |  |  |
| 15 | frozen_balance | 否 |  |  |
| 16 | enable_balance | 否 |  |  |
| 17 | cash_interest | 否 |  |  |
| 18 | tohis_date | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_spcash_fund | ART | 是 | cashgroup_no, money_type, cashgroup_no, money_type |
| uk_rpt_ucrtspcashfund | ART | 是 | tohis_date, cashgroup_no, money_type, tohis_date, cashgroup_no, money_type |
| idx_ucrt_spcash_fund | ART | 是 | cashgroup_no, money_type, cashgroup_no, money_type |
| uk_rpt_ucrtspcashfund | ART | 是 | tohis_date, cashgroup_no, money_type, tohis_date, cashgroup_no, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_spcash_fund | cashgroup_no, money_type, cashgroup_no, money_type |
| idx_ucrt_spcash_fund | cashgroup_no, money_type, cashgroup_no, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

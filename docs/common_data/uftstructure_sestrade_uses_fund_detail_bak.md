# uses_fund_detail_bak - 证券交易资金详细信息备份表

**表对象ID**: 5757
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | fund_enable_level | 否 |  |  |
| 6 | position_str | 否 |  |  |
| 7 | update_date | 否 |  |  |
| 8 | update_time | 否 |  |  |
| 9 | begin_enable_balance | 否 |  |  |
| 10 | sett_batch_no | 否 |  |  |
| 11 | init_date | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | money_type | 否 |  |  |
| 14 | client_id | 否 |  |  |
| 15 | fund_enable_level | 否 |  |  |
| 16 | position_str | 否 |  |  |
| 17 | update_date | 否 |  |  |
| 18 | update_time | 否 |  |  |
| 19 | begin_enable_balance | 否 |  |  |
| 20 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_fund_detail_bak | ART | 是 | fund_account, money_type, fund_enable_level, init_date, sett_batch_no, fund_account, money_type, fund_enable_level, init_date, sett_batch_no |
| idx_fund_detail_bak | ART | 是 | fund_account, money_type, fund_enable_level, init_date, sett_batch_no, fund_account, money_type, fund_enable_level, init_date, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_fund_detail_bak | fund_account, money_type, fund_enable_level, init_date, sett_batch_no, fund_account, money_type, fund_enable_level, init_date, sett_batch_no |
| idx_fund_detail_bak | fund_account, money_type, fund_enable_level, init_date, sett_batch_no, fund_account, money_type, fund_enable_level, init_date, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:42:36 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2026-02-05 21:59 | 3.0.0.1 | 杨新照 | 新增表结构 |
| 2026-03-09 14:42:36 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2026-02-05 21:59 | 3.0.0.1 | 杨新照 | 新增表结构 |

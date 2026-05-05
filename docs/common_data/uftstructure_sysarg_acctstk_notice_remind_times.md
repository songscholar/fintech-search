# acctstk_notice_remind_times - 账户证券提示信息提醒次数表

**表对象ID**: 366
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | stock_type | 否 |  |  |
| 7 | remind_times | 否 |  |  |
| 8 | branch_no | 否 |  |  |
| 9 | client_id | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | stock_type | 否 |  |  |
| 14 | remind_times | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_acctstknoticeremindtimes | ART | 是 | fund_account, exchange_type, stock_code, stock_type, fund_account, exchange_type, stock_code, stock_type |
| idx_acctstknoticeremindtimes | ART | 是 | fund_account, exchange_type, stock_code, stock_type, fund_account, exchange_type, stock_code, stock_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_acctstknoticeremindtimes | fund_account, exchange_type, stock_code, stock_type, fund_account, exchange_type, stock_code, stock_type |
| idx_acctstknoticeremindtimes | fund_account, exchange_type, stock_code, stock_type, fund_account, exchange_type, stock_code, stock_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-01-20 18:19:59 | 3.0.2.53 | 彭雪锋 | 新增表 |
| 2025-01-20 18:19:59 | 3.0.2.53 | 彭雪锋 | 新增表 |

# reits_alloc_quota - 基础设施基金配售额度表

**表对象ID**: 371
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | total_quota | 否 |  |  |
| 8 | used_quota | 否 |  |  |
| 9 | day_used_quota | 否 |  |  |
| 10 | date_clear | 否 |  |  |
| 11 | order_no | 否 |  |  |
| 12 | init_date | 否 |  |  |
| 13 | branch_no | 否 |  |  |
| 14 | fund_account | 否 |  |  |
| 15 | stock_account | 否 |  |  |
| 16 | exchange_type | 否 |  |  |
| 17 | stock_code | 否 |  |  |
| 18 | total_quota | 否 |  |  |
| 19 | used_quota | 否 |  |  |
| 20 | day_used_quota | 否 |  |  |
| 21 | date_clear | 否 |  |  |
| 22 | order_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_reits_alloc_quota | ART | 是 | fund_account, stock_account, exchange_type, stock_code, fund_account, stock_account, exchange_type, stock_code |
| idx_reits_alloc_quota_acc | ART | 是 | fund_account, fund_account |
| idx_reits_alloc_quota | ART | 是 | fund_account, stock_account, exchange_type, stock_code, fund_account, stock_account, exchange_type, stock_code |
| idx_reits_alloc_quota_acc | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_reits_alloc_quota | fund_account, stock_account, exchange_type, stock_code, fund_account, stock_account, exchange_type, stock_code |
| idx_reits_alloc_quota | fund_account, stock_account, exchange_type, stock_code, fund_account, stock_account, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 14:03:00 | V3.0.2.101 | zhangxh | 新增表结构 |
| 2025-11-21 14:03:00 | V3.0.2.101 | zhangxh | 新增表结构 |

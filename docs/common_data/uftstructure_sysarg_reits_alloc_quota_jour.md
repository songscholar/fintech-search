# reits_alloc_quota_jour - 基础设施基金配售额度流水表

**表对象ID**: 372
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | serial_no | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | total_quota | 否 |  |  |
| 11 | used_quota | 否 |  |  |
| 12 | day_used_quota | 否 |  |  |
| 13 | occur_quota | 否 |  |  |
| 14 | cancel_serial_no | 否 |  |  |
| 15 | position_str | 否 |  | init_date(8)+branch_no(5)+serial_no(10) |
| 16 | remark | 否 |  |  |
| 17 | init_date | 否 |  |  |
| 18 | curr_date | 否 |  |  |
| 19 | curr_time | 否 |  |  |
| 20 | serial_no | 否 |  |  |
| 21 | branch_no | 否 |  |  |
| 22 | fund_account | 否 |  |  |
| 23 | stock_account | 否 |  |  |
| 24 | exchange_type | 否 |  |  |
| 25 | stock_code | 否 |  |  |
| 26 | total_quota | 否 |  |  |
| 27 | used_quota | 否 |  |  |
| 28 | day_used_quota | 否 |  |  |
| 29 | occur_quota | 否 |  |  |
| 30 | cancel_serial_no | 否 |  |  |
| 31 | position_str | 否 |  | init_date(8)+branch_no(5)+serial_no(10) |
| 32 | remark | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_reits_alloc_quota_jour | ART | 是 | position_str, position_str |
| idx_reits_alloc_quota_jour_acc | ART | 是 | fund_account, fund_account |
| idx_rpt_reits_alloc_quota_jour2 | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_reits_alloc_quota_jour_acc2 | ART | 是 | init_date, fund_account, init_date, fund_account |
| idx_reits_alloc_quota_jour | ART | 是 | position_str, position_str |
| idx_reits_alloc_quota_jour_acc | ART | 是 | fund_account, fund_account |
| idx_rpt_reits_alloc_quota_jour2 | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_reits_alloc_quota_jour_acc2 | ART | 是 | init_date, fund_account, init_date, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_reits_alloc_quota_jour | position_str, position_str |
| idx_reits_alloc_quota_jour | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-08 13:48:43 | 8.26.2.95 | 洪略 | 历史表索引增加rpt前缀 |
| 2025-11-24 13:27:35 | V3.0.2.102 | 洪略 | 增加历史表 |
| 2025-11-21 14:03:00 | V3.0.2.101 | zhangxh | 新增表结构 |
| 2025-12-08 13:48:43 | 8.26.2.95 | 洪略 | 历史表索引增加rpt前缀 |
| 2025-11-24 13:27:35 | V3.0.2.102 | 洪略 | 增加历史表 |
| 2025-11-21 14:03:00 | V3.0.2.101 | zhangxh | 新增表结构 |

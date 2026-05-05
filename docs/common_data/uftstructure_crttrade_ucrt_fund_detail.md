# ucrt_fund_detail - 融资融交易资金详细信息表

**表对象ID**: 7534
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | business_frozen_balance | 否 |  |  |
| 6 | business_unfrozen_balance | 否 |  |  |
| 7 | fund_enable_level | 否 |  |  |
| 8 | init_date | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | money_type | 否 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | business_frozen_balance | 否 |  |  |
| 13 | business_unfrozen_balance | 否 |  |  |
| 14 | fund_enable_level | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_fund_detail | ART | 是 | fund_account, money_type, fund_enable_level, init_date, fund_account, money_type, fund_enable_level, init_date |
| idx_ucrt_fund_detail | ART | 是 | fund_account, money_type, fund_enable_level, init_date, fund_account, money_type, fund_enable_level, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_fund_detail | fund_account, money_type, fund_enable_level, init_date, fund_account, money_type, fund_enable_level, init_date |
| idx_ucrt_fund_detail | fund_account, money_type, fund_enable_level, init_date, fund_account, money_type, fund_enable_level, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-07-23 15:50:57 | 3.0.3.5 | 刘景锋 | 修复关联索引是全局索引问题 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2024-07-23 15:50:57 | 3.0.3.5 | 刘景锋 | 修复关联索引是全局索引问题 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

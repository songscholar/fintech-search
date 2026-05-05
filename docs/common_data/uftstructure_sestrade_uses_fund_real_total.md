# uses_fund_real_total - 证券交易资金汇总表

**表对象ID**: 5986
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | current_balance | 否 |  |  |
| 5 | enable_balance | 否 |  |  |
| 6 | frozen_balance | 否 |  |  |
| 7 | unfrozen_balance | 否 |  |  |
| 8 | correct_balance | 否 |  |  |
| 9 | uncome_buy_balance | 否 |  |  |
| 10 | uncome_sell_balance | 否 |  |  |
| 11 | uncome_correct_balance | 否 |  |  |
| 12 | post_enable_balance | 否 |  |  |
| 13 | post_current_balance | 否 |  |  |
| 14 | flow_count | 否 |  |  |
| 15 | foregift_balance | 否 |  |  |
| 16 | business_prop | 是 |  |  |
| 17 | init_date | 否 |  |  |
| 18 | fund_account | 否 |  |  |
| 19 | money_type | 否 |  |  |
| 20 | current_balance | 否 |  |  |
| 21 | enable_balance | 否 |  |  |
| 22 | frozen_balance | 否 |  |  |
| 23 | unfrozen_balance | 否 |  |  |
| 24 | correct_balance | 否 |  |  |
| 25 | uncome_buy_balance | 否 |  |  |
| 26 | uncome_sell_balance | 否 |  |  |
| 27 | uncome_correct_balance | 否 |  |  |
| 28 | post_enable_balance | 否 |  |  |
| 29 | post_current_balance | 否 |  |  |
| 30 | flow_count | 否 |  |  |
| 31 | foregift_balance | 否 |  |  |
| 32 | business_prop | 是 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usesfundrealtotal | 默认 | 否 |  |
| idx_usesfundrealtotal	
 | 默认 | 否 |  |
| idx_usesfundrealtotal | ART | 是 | fund_account, money_type, init_date, flow_count, fund_account, money_type, init_date, flow_count |
| idx_rpt_usesfundrealtotal	
 | ART | 是 | fund_account, money_type, init_date, flow_count, fund_account, money_type, init_date, flow_count |
| idx_usesfundrealtotal | 默认 | 否 |  |
| idx_usesfundrealtotal	
 | 默认 | 否 |  |
| idx_usesfundrealtotal | ART | 是 | fund_account, money_type, init_date, flow_count, fund_account, money_type, init_date, flow_count |
| idx_rpt_usesfundrealtotal	
 | ART | 是 | fund_account, money_type, init_date, flow_count, fund_account, money_type, init_date, flow_count |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usesfundrealtotal | fund_account, money_type, init_date, flow_count, fund_account, money_type, init_date, flow_count |
| idx_usesfundrealtotal | fund_account, money_type, init_date, flow_count, fund_account, money_type, init_date, flow_count |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:53:28 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:32:23 | V3.0.8.27 | 洪略 | 历史表索引加rpt前缀 |
| 2025-12-01 16:48:00 | 3.0.2.104 | taocong45644 | 当前表uses_fund_real_total，修改了索引idx_usesfundrealtotal,索引字段修改为：(... |
| 2025-11-07 10:13:43 | V3.0.2.103 | 洪略 | 增加历史表 |
| 2025-10-22 16:40:25 | V3.0.8.7 | 王锋 | 所有表uses_fund_real_total，添加了表字段(business_prop);
 |
| 2025-10-22 14:40:31 | 3.0.6.1020 |  | 新增字段business_prop |
| 2026-03-09 14:53:28 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:32:23 | V3.0.8.27 | 洪略 | 历史表索引加rpt前缀 |
| 2025-12-01 16:48:00 | 3.0.2.104 | taocong45644 | 当前表uses_fund_real_total，修改了索引idx_usesfundrealtotal,索引字段修改为：(... |
| 2025-11-07 10:13:43 | V3.0.2.103 | 洪略 | 增加历史表 |
| 2025-10-22 16:40:25 | V3.0.8.7 | 王锋 | 所有表uses_fund_real_total，添加了表字段(business_prop);
 |
| 2025-10-22 14:40:31 | 3.0.6.1020 |  | 新增字段business_prop |

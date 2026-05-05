# uses_fund_real_frozen_detail - 交易资金汇总表

**表对象ID**: 5580
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | money_type | 否 |  |  |
| 5 | frozen_balance | 否 |  |  |
| 6 | init_date | 否 |  |  |
| 7 | client_id | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | money_type | 否 |  |  |
| 10 | frozen_balance | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_fund_real_frozen_detail | ART | 是 | init_date, fund_account, money_type, init_date, fund_account, money_type |
| idx_rpt_fund_real_frozen_detail | ART | 是 | init_date, fund_account, money_type, init_date, fund_account, money_type |
| idx_fund_real_frozen_detail | ART | 是 | init_date, fund_account, money_type, init_date, fund_account, money_type |
| idx_rpt_fund_real_frozen_detail | ART | 是 | init_date, fund_account, money_type, init_date, fund_account, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_fund_real_frozen_detail | init_date, fund_account, money_type, init_date, fund_account, money_type |
| idx_fund_real_frozen_detail | init_date, fund_account, money_type, init_date, fund_account, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:31:08 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:27:50 | V3.0.8.17 | 洪略 | 历史表索引加rpt前缀 |
| 2025-11-07 10:50:23 | V3.0.2.103 | 洪略 | 增加历史表 |
| 2025-08-22 10:30:08 | 3.0.6.1019 | 吴威 | 新增 |
| 2026-03-09 14:31:08 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:27:50 | V3.0.8.17 | 洪略 | 历史表索引加rpt前缀 |
| 2025-11-07 10:50:23 | V3.0.2.103 | 洪略 | 增加历史表 |
| 2025-08-22 10:30:08 | 3.0.6.1019 | 吴威 | 新增 |

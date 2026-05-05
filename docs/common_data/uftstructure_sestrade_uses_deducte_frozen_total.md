# uses_deducte_frozen_total - 证券缴款冻结汇总表

**表对象ID**: 5755
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | clear_balance | 否 |  |  |
| 5 | overdraft_balance | 否 |  |  |
| 6 | sett_batch_no | 否 |  |  |
| 7 | position_str | 否 |  | init_date(10) + fund_account(18) + money_type(3) + sett_batc |
| 8 | init_date | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | money_type | 否 |  |  |
| 11 | clear_balance | 否 |  |  |
| 12 | overdraft_balance | 否 |  |  |
| 13 | sett_batch_no | 否 |  |  |
| 14 | position_str | 否 |  | init_date(10) + fund_account(18) + money_type(3) + sett_batc |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usesdeductefrozentotal | 默认 | 否 |  |
| idx_usesdeductefrozentotal_pos | 默认 | 否 |  |
| idx_usesdeductefrozentotal_pos | 默认 | 否 |  |
| idx_usesdeductefrozentotal | ART | 是 | init_date, money_type, sett_batch_no, fund_account, init_date, money_type, sett_batch_no, fund_account |
| idx_usesdeductefrozentotal_pos | ART | 是 | position_str, position_str |
| idx_rpt_usesdeductefrozentotal_pos | ART | 是 | init_date, position_str, init_date, position_str |
| idx_usesdeductefrozentotal | 默认 | 否 |  |
| idx_usesdeductefrozentotal_pos | 默认 | 否 |  |
| idx_usesdeductefrozentotal_pos | 默认 | 否 |  |
| idx_usesdeductefrozentotal | ART | 是 | init_date, money_type, sett_batch_no, fund_account, init_date, money_type, sett_batch_no, fund_account |
| idx_usesdeductefrozentotal_pos | ART | 是 | position_str, position_str |
| idx_rpt_usesdeductefrozentotal_pos | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usesdeductefrozentotal | init_date, fund_account, money_type, sett_batch_no, init_date, fund_account, money_type, sett_batch_no |
| idx_usesdeductefrozentotal | init_date, fund_account, money_type, sett_batch_no, init_date, fund_account, money_type, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:41:49 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:28:14 | V3.0.8.20 | 洪略 | 历史表索引加rpt前缀 |
| 2025-12-01 16:40:03 | 3.0.2.104 | taocong45644 | 当前表uses_deducte_frozen_total，修改了索引idx_usesdeductefrozentotal... |
| 2025-11-07 09:54:56 | V3.0.2.103 | 洪略 | 增减历史表 |
| 2025-08-21 18:58:44 | 3.0.2.1019 | yangxz |  |
| 2026-03-09 14:41:49 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:28:14 | V3.0.8.20 | 洪略 | 历史表索引加rpt前缀 |
| 2025-12-01 16:40:03 | 3.0.2.104 | taocong45644 | 当前表uses_deducte_frozen_total，修改了索引idx_usesdeductefrozentotal... |
| 2025-11-07 09:54:56 | V3.0.2.103 | 洪略 | 增减历史表 |
| 2025-08-21 18:58:44 | 3.0.2.1019 | yangxz |  |

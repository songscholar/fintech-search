# force_entrust - 强制委托表

**表对象ID**: 5733
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | entrust_no | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | entrust_type | 否 |  |  |
| 6 | entrust_prop | 否 |  |  |
| 7 | client_id | 否 | H |  |
| 8 | client_name | 否 | H |  |
| 9 | corp_client_group | 否 | H |  |
| 10 | client_group | 否 | H |  |
| 11 | room_code | 否 | H |  |
| 12 | asset_prop | 否 | H |  |
| 13 | limit_flag | 否 | H |  |
| 14 | client_prop | 否 | H |  |
| 15 | asset_level | 否 | H |  |
| 16 | risk_level | 否 | H |  |
| 17 | corp_risk_level | 否 | H |  |
| 18 | init_date | 否 |  |  |
| 19 | branch_no | 否 |  |  |
| 20 | entrust_no | 否 |  |  |
| 21 | fund_account | 否 |  |  |
| 22 | entrust_type | 否 |  |  |
| 23 | entrust_prop | 否 |  |  |
| 24 | client_id | 否 | H |  |
| 25 | client_name | 否 | H |  |
| 26 | corp_client_group | 否 | H |  |
| 27 | client_group | 否 | H |  |
| 28 | room_code | 否 | H |  |
| 29 | asset_prop | 否 | H |  |
| 30 | limit_flag | 否 | H |  |
| 31 | client_prop | 否 | H |  |
| 32 | asset_level | 否 | H |  |
| 33 | risk_level | 否 | H |  |
| 34 | corp_risk_level | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_force_entrust | ART | 是 | init_date, branch_no, entrust_no, init_date, branch_no, entrust_no |
| uk_rpt_forceentrust | ART | 是 | init_date, branch_no, entrust_no, init_date, branch_no, entrust_no |
| idx_force_entrust | ART | 是 | init_date, branch_no, entrust_no, init_date, branch_no, entrust_no |
| uk_rpt_forceentrust | ART | 是 | init_date, branch_no, entrust_no, init_date, branch_no, entrust_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_force_entrust | init_date, branch_no, entrust_no, init_date, branch_no, entrust_no |
| idx_force_entrust | init_date, branch_no, entrust_no, init_date, branch_no, entrust_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:39:26 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2026-03-09 14:39:26 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |

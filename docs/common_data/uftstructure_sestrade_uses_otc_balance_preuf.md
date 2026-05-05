# uses_otc_balance_preuf - 多金融预解冻登记表

**表对象ID**: 5582
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 52 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | register_date | 否 |  |  |
| 3 | allot_no | 否 |  |  |
| 4 | trans_account | 否 |  |  |
| 5 | prod_account | 否 |  |  |
| 6 | prod_code | 否 |  |  |
| 7 | prodta_no | 否 |  |  |
| 8 | sysnode_id_t | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | money_type | 否 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | occur_balance | 否 |  |  |
| 13 | business_flag | 否 |  |  |
| 14 | branch_no | 否 |  |  |
| 15 | deal_flag | 否 |  |  |
| 16 | umt_flag | 否 |  |  |
| 17 | client_name | 否 | H |  |
| 18 | corp_client_group | 否 | H |  |
| 19 | client_group | 否 | H |  |
| 20 | room_code | 否 | H |  |
| 21 | asset_prop | 否 | H |  |
| 22 | limit_flag | 否 | H |  |
| 23 | client_prop | 否 | H |  |
| 24 | asset_level | 否 | H |  |
| 25 | risk_level | 否 | H |  |
| 26 | corp_risk_level | 否 | H |  |
| 27 | init_date | 否 |  |  |
| 28 | register_date | 否 |  |  |
| 29 | allot_no | 否 |  |  |
| 30 | trans_account | 否 |  |  |
| 31 | prod_account | 否 |  |  |
| 32 | prod_code | 否 |  |  |
| 33 | prodta_no | 否 |  |  |
| 34 | sysnode_id_t | 否 |  |  |
| 35 | fund_account | 否 |  |  |
| 36 | money_type | 否 |  |  |
| 37 | client_id | 否 |  |  |
| 38 | occur_balance | 否 |  |  |
| 39 | business_flag | 否 |  |  |
| 40 | branch_no | 否 |  |  |
| 41 | deal_flag | 否 |  |  |
| 42 | umt_flag | 否 |  |  |
| 43 | client_name | 否 | H |  |
| 44 | corp_client_group | 否 | H |  |
| 45 | client_group | 否 | H |  |
| 46 | room_code | 否 | H |  |
| 47 | asset_prop | 否 | H |  |
| 48 | limit_flag | 否 | H |  |
| 49 | client_prop | 否 | H |  |
| 50 | asset_level | 否 | H |  |
| 51 | risk_level | 否 | H |  |
| 52 | corp_risk_level | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_otc_balance_preuf | ART | 是 | register_date, allot_no, fund_account, money_type, register_date, allot_no, fund_account, money_type |
| idx_rpt_otc_balance_preuf | ART | 是 | init_date, register_date, allot_no, fund_account, money_type, init_date, register_date, allot_no, fund_account, money_type |
| idx_otc_balance_preuf | ART | 是 | register_date, allot_no, fund_account, money_type, register_date, allot_no, fund_account, money_type |
| idx_rpt_otc_balance_preuf | ART | 是 | init_date, register_date, allot_no, fund_account, money_type, init_date, register_date, allot_no, fund_account, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_otc_balance_preuf | register_date, allot_no, fund_account, money_type, register_date, allot_no, fund_account, money_type |
| idx_otc_balance_preuf | register_date, allot_no, fund_account, money_type, register_date, allot_no, fund_account, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:31:59 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2026-01-09 16:23:03 | V3.0.2.81 | 洪略 | 增加历史表 |
| 2025-08-22 10:30:54 | 3.0.6.1019 | 吴威 | 新增 |
| 2026-03-09 14:31:59 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2026-01-09 16:23:03 | V3.0.2.81 | 洪略 | 增加历史表 |
| 2025-08-22 10:30:54 | 3.0.6.1019 | 吴威 | 新增 |

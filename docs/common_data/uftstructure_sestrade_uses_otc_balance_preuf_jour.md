# uses_otc_balance_preuf_jour - 多金融预解冻登记流水表

**表对象ID**: 5583
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | register_date | 否 |  |  |
| 4 | allot_no | 否 |  |  |
| 5 | trans_account | 否 |  |  |
| 6 | prod_account | 否 |  |  |
| 7 | prod_code | 否 |  |  |
| 8 | prodta_no | 否 |  |  |
| 9 | sysnode_id_t | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | money_type | 否 |  |  |
| 12 | client_id | 否 |  |  |
| 13 | occur_balance | 否 |  |  |
| 14 | business_flag | 否 |  |  |
| 15 | branch_no | 否 |  |  |
| 16 | deal_flag | 否 |  |  |
| 17 | umt_flag | 否 |  |  |
| 18 | client_name | 否 | H |  |
| 19 | corp_client_group | 否 | H |  |
| 20 | client_group | 否 | H |  |
| 21 | room_code | 否 | H |  |
| 22 | asset_prop | 否 | H |  |
| 23 | limit_flag | 否 | H |  |
| 24 | client_prop | 否 | H |  |
| 25 | asset_level | 否 | H |  |
| 26 | risk_level | 否 | H |  |
| 27 | corp_risk_level | 否 | H |  |
| 28 | init_date | 否 |  |  |
| 29 | serial_no | 否 |  |  |
| 30 | register_date | 否 |  |  |
| 31 | allot_no | 否 |  |  |
| 32 | trans_account | 否 |  |  |
| 33 | prod_account | 否 |  |  |
| 34 | prod_code | 否 |  |  |
| 35 | prodta_no | 否 |  |  |
| 36 | sysnode_id_t | 否 |  |  |
| 37 | fund_account | 否 |  |  |
| 38 | money_type | 否 |  |  |
| 39 | client_id | 否 |  |  |
| 40 | occur_balance | 否 |  |  |
| 41 | business_flag | 否 |  |  |
| 42 | branch_no | 否 |  |  |
| 43 | deal_flag | 否 |  |  |
| 44 | umt_flag | 否 |  |  |
| 45 | client_name | 否 | H |  |
| 46 | corp_client_group | 否 | H |  |
| 47 | client_group | 否 | H |  |
| 48 | room_code | 否 | H |  |
| 49 | asset_prop | 否 | H |  |
| 50 | limit_flag | 否 | H |  |
| 51 | client_prop | 否 | H |  |
| 52 | asset_level | 否 | H |  |
| 53 | risk_level | 否 | H |  |
| 54 | corp_risk_level | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_otc_balance_preuf_jour | 默认 | 否 | init_date, serial_no, branch_no, init_date, serial_no, branch_no |
| idx_otc_balance_preuf_jour | ART | 是 | init_date, serial_no, branch_no, init_date, serial_no, branch_no |
| idx_rpt_otc_balance_preuf_jour | ART | 是 | init_date, serial_no, branch_no, init_date, serial_no, branch_no |
| idx_otc_balance_preuf_jour | 默认 | 否 | init_date, serial_no, branch_no, init_date, serial_no, branch_no |
| idx_otc_balance_preuf_jour | ART | 是 | init_date, serial_no, branch_no, init_date, serial_no, branch_no |
| idx_rpt_otc_balance_preuf_jour | ART | 是 | init_date, serial_no, branch_no, init_date, serial_no, branch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_otc_balance_preuf_jour | init_date, serial_no, branch_no, init_date, serial_no, branch_no |
| idx_otc_balance_preuf_jour | init_date, serial_no, branch_no, init_date, serial_no, branch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:32:21 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2026-01-09 18:18:58 | V3.0.2.81 | 洪略 | 增加历史表 |
| 2025-09-24 15:41:20 | 3.0.6.1019 | 吴威 | 当前表uses_otc_balance_preuf_jour，修改了索引idx_otc_balance_preuf_jo... |
| 2025-08-22 10:31:47 | 3.0.6.1019 | 吴威 | 新增 |
| 2026-03-09 14:32:21 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2026-01-09 18:18:58 | V3.0.2.81 | 洪略 | 增加历史表 |
| 2025-09-24 15:41:20 | 3.0.6.1019 | 吴威 | 当前表uses_otc_balance_preuf_jour，修改了索引idx_otc_balance_preuf_jo... |
| 2025-08-22 10:31:47 | 3.0.6.1019 | 吴威 | 新增 |

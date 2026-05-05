# tpr_contract_ext_jour - 三方回购合约扩展流水表

**表对象ID**: 2348
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | serial_no | 否 |  |  |
| 4 | curr_date | 否 |  |  |
| 5 | curr_time | 否 |  |  |
| 6 | op_branch_no | 否 |  |  |
| 7 | operator_no | 否 |  |  |
| 8 | op_entrust_way | 否 |  |  |
| 9 | op_station | 否 |  |  |
| 10 | business_flag | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | contract_id | 否 |  |  |
| 15 | report_id | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | occur_amount | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | stock_name | 否 | H |  |
| 20 | stock_type | 否 | H |  |
| 21 | sub_stock_type | 否 | H |  |
| 22 | init_date | 否 |  |  |
| 23 | branch_no | 否 |  |  |
| 24 | serial_no | 否 |  |  |
| 25 | curr_date | 否 |  |  |
| 26 | curr_time | 否 |  |  |
| 27 | op_branch_no | 否 |  |  |
| 28 | operator_no | 否 |  |  |
| 29 | op_entrust_way | 否 |  |  |
| 30 | op_station | 否 |  |  |
| 31 | business_flag | 否 |  |  |
| 32 | fund_account | 否 |  |  |
| 33 | stock_account | 否 |  |  |
| 34 | exchange_type | 否 |  |  |
| 35 | contract_id | 否 |  |  |
| 36 | report_id | 否 |  |  |
| 37 | stock_code | 否 |  |  |
| 38 | occur_amount | 否 |  |  |
| 39 | remark | 否 |  |  |
| 40 | stock_name | 否 | H |  |
| 41 | stock_type | 否 | H |  |
| 42 | sub_stock_type | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_tprcontractextjour_id | 默认 | 否 |  |
| idx_tprcontractextjour_id | ART | 是 | init_date, serial_no, init_date, serial_no |
| uk_rpt_tprcontractextjour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_tprcontractextjour_id | 默认 | 否 |  |
| idx_tprcontractextjour_id | ART | 是 | init_date, serial_no, init_date, serial_no |
| uk_rpt_tprcontractextjour | ART | 是 | init_date, serial_no, init_date, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_tprcontractextjour_id | init_date, serial_no, init_date, serial_no |
| idx_tprcontractextjour_id | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:36:14 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-09-23 15:52:14 | V3.0.2.1007 | 张明月 | 新增 |
| 2026-03-04 15:36:14 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-09-23 15:52:14 | V3.0.2.1007 | 张明月 | 新增 |
